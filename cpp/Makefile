
CC=g++
CFLAG=-std=c++11 `pkg-config --cflags protobuf grpc`

LIBS=-L. -L/usr/local/lib `pkg-config --libs protobuf grpc++ grpc`\
           -Wl,--no-as-needed -lgrpc++_reflection -Wl,--as-needed\
           -ldl

OBJS= helloworld.pb.o helloworld.grpc.pb.o  myasyncserver.o

MAIN=main

all: myasyncserver

myasyncserver: $(OBJS)
	$(CC) -o $(MAIN) $^  $(CFLAG) $(LIBS)

%.o:%.cc 
	$(CC) -c $< $(CFLAG) $(LIBS)

grpc:
	protoc --cpp_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` -I. helloworld.proto
	@echo "cpp_create_grpc_code"


clean:
	rm -rf `find . -name "*.o"` ; rm -rf $(MAIN)

