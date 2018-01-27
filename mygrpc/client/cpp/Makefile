
CC=g++
CFLAG=-std=c++11 `pkg-config --cflags protobuf grpc`

LIBS=-L. -L/usr/local/lib `pkg-config --libs protobuf grpc++ grpc`\
           -Wl,--no-as-needed -lgrpc++_reflection -Wl,--as-needed\
           -ldl
PROTOS=../..

OBJS= helloworld.pb.o helloworld.grpc.pb.o  myserver.o

MAIN=main

all: myserver

myserver: $(OBJS)
	$(CC) -o $(MAIN) $^  $(CFLAG) $(LIBS)

%.o:%.cc 
	$(CC) -c $< $(CFLAG) $(LIBS)

cpp_out:
	protoc --cpp_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` -I$(PROTOS) $(PROTOS)/helloworld.proto
	@echo "cpp_create_grpc_code"

python3_out:
	#python3 -m pip install grpcio-tools
	python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I$(PROTOS) $(PROTOS)/helloworld.proto

js_out:
	protoc --js_out=import_style=commonjs,binary:. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_node_plugin` -I$(PROTOS) $(PROTOS)/helloworld.proto
	@echo "js_create_grpc_code"	

clean:
	rm -rf `find . -name "*.o"` ; rm -rf $(MAIN)
