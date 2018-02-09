
CC=g++
CFLAG=-std=c++11 `pkg-config --cflags protobuf grpc`

LIBS=-L. -L/usr/local/lib `pkg-config --libs protobuf grpc++ grpc`\
           -Wl,--no-as-needed -lgrpc++_reflection -Wl,--as-needed\
           -ldl

PROTOS_FILE=helloworld.proto
PROTOS_DIR=..

OBJS= helloworld.pb.o helloworld.grpc.pb.o  myserver.o

MAIN=main

all: myserver

myserver: $(OBJS)
	$(CC) -o $(MAIN) $^  $(CFLAG) $(LIBS)

%.o:%.cc 
	$(CC) -c $< $(CFLAG) $(LIBS)

cpp_out:
	protoc --cpp_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` -I$(PROTOS_DIR) $(PROTOS_DIR)/$(PROTOS_FILE)
	@echo "cpp_create_grpc_code"

csharp_out:
	protoc --csharp_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_csharp_plugin` -I$(PROTOS_DIR) $(PROTOS_DIR)/$(PROTOS_FILE)
	@echo "csharp_create_grpc_code"

python3_out:
	#python3 -m pip install grpcio-tools
	python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I$(PROTOS_DIR) $(PROTOS_DIR)/$(PROTOS_FILE)

js_out:
	protoc --js_out=import_style=commonjs,binary:. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_node_plugin` -I$(PROTOS_DIR) $(PROTOS_DIR)/$(PROTOS_FILE)
	@echo "js_create_grpc_code"	


clean:
	rm -rf `find . -name "*.o"` ; rm -rf $(MAIN)
