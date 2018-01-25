
#include <iostream>
#include <memory>
#include <string>
#include <thread>

#include <grpc++/grpc++.h>
#include <grpc/support/log.h>

#include "helloworld.grpc.pb.h"

using grpc::Server;
using grpc::ServerAsyncResponseWriter;
using grpc::ServerBuilder;
using grpc::ServerCompletionQueue;
using grpc::ServerContext;
using grpc::Status;
using helloworld::Greeter;
using helloworld::HelloReply;
using helloworld::HelloRequest;

class CallData {
private:
    Greeter::AsyncService* service_;
    ServerCompletionQueue* cq_;
    ServerContext ctx_;
    HelloRequest request_;
    HelloReply reply_;
    ServerAsyncResponseWriter<HelloReply> responder_;
    
    enum CallStatus { CREATE, PROCESS, FINISH };
    CallStatus status_;  // The current serving state.

 public:
    CallData(Greeter::AsyncService* service, ServerCompletionQueue* cq) 
        : service_(service), cq_(cq), responder_(&ctx_), status_(CREATE) {
            
        Proceed();
    }

    void Proceed() {
        if (status_ == CREATE) {
            status_ = PROCESS;
            service_->RequestSayHello(&ctx_, &request_, &responder_, cq_, cq_, this);
            std::cout << "CREATE--->"  << std::endl;
            
        } else if (status_ == PROCESS) {
            new CallData(service_, cq_);

            std::string prefix("Hello ");
            reply_.set_message(prefix + request_.name());

            status_ = FINISH;
            responder_.Finish(reply_, Status::OK, this);
            std::cout << "PROCESS--->"  << std::endl;
        } else {
            GPR_ASSERT(status_ == FINISH);
            delete this;
            std::cout << "what else--->"  << std::endl;
        }
    }
};


class ServerImpl final {
private:
    std::unique_ptr<ServerCompletionQueue> cq_;
    Greeter::AsyncService service_;
    std::unique_ptr<Server> server_;

public:
    ~ServerImpl() {
        server_->Shutdown();
        cq_->Shutdown();
    }

    void Run() {
        std::string server_address("0.0.0.0:50051");

        ServerBuilder builder;
        builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());

        builder.RegisterService(&service_);

        cq_ = builder.AddCompletionQueue();

        server_ = builder.BuildAndStart();
        std::cout << "Server listening on " << server_address << std::endl;

        HandleRpcs();
    }

    void HandleRpcs() {
        new CallData(&service_, cq_.get());
        void* tag;  
        bool ok;
        while (true) {
            GPR_ASSERT(cq_->Next(&tag, &ok));
            GPR_ASSERT(ok);
            static_cast<CallData*>(tag)->Proceed();
        }
    }
};


int main(int argc, char** argv) {
  ServerImpl server;
  std::cout << "run aysnc server" << std::endl;
  server.Run();

  return 0;
}
