from __future__ import print_function

import grpc

import mybooks_pb2
import mybooks_pb2_grpc

'''
python3 -m pip install --upgrade pip
python3 -m pip install grpcio
python3 -m pip install grpcio-tools
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./mybooks.proto 
'''

channel = grpc.insecure_channel('localhost:50051')
stub = mybooks_pb2_grpc.BookServiceStub(channel)


def listBooks():
    global stub
    result = stub.List( mybooks_pb2.BookIdRequest() )
    print( result )

def getBookId(xid):
    global stub
    try:
        result = stub.Get( mybooks_pb2.Book( id=xid ))
        print( result )
    except Exception as err :
        print( err )
    
def postBook( xid, xtitle, xauthor ):
    global stub
    try:
        result = stub.Post( mybooks_pb2.Book(id=xid, title=xtitle , author=xauthor) )
        #print( result )
    except Exception as err:
        print(err)

def delBook( xid ):
    global stub
    try:
        result = stub.Delete( mybooks_pb2.BookIdRequest( id=xid))
    except Exception as err:
        print( err)


def sendBookStream():
    #send server data
    yield mybooks_pb2.Book( id=333, title="mytitle" , author="alex")
    
def watchBook():
    global stub
    it = stub.Watch( sendBookStream() )
    
    #recieve server data
    try:
        for book in it:
            print( book )
    except grpc._channel._Rendezvous as err:
        print(err)


if __name__ == '__main__':
    #getBookId( 123 )
    #postBook( 222, "test02" , "alex")
    #delBook( 123 )
    #getBookId(123)
    listBooks()

    #will lock
    #watchBook()
    
