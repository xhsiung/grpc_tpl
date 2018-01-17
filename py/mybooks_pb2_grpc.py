# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import mybooks_pb2 as mybooks__pb2


class BookServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.List = channel.unary_unary(
        '/books.BookService/List',
        request_serializer=mybooks__pb2.Empty.SerializeToString,
        response_deserializer=mybooks__pb2.BookList.FromString,
        )
    self.Get = channel.unary_unary(
        '/books.BookService/Get',
        request_serializer=mybooks__pb2.BookIdRequest.SerializeToString,
        response_deserializer=mybooks__pb2.Book.FromString,
        )
    self.Post = channel.unary_unary(
        '/books.BookService/Post',
        request_serializer=mybooks__pb2.Book.SerializeToString,
        response_deserializer=mybooks__pb2.BookList.FromString,
        )
    self.Put = channel.unary_unary(
        '/books.BookService/Put',
        request_serializer=mybooks__pb2.Book.SerializeToString,
        response_deserializer=mybooks__pb2.Empty.FromString,
        )
    self.Delete = channel.unary_unary(
        '/books.BookService/Delete',
        request_serializer=mybooks__pb2.BookIdRequest.SerializeToString,
        response_deserializer=mybooks__pb2.Empty.FromString,
        )


class BookServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def List(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Post(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Put(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BookServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=mybooks__pb2.Empty.FromString,
          response_serializer=mybooks__pb2.BookList.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=mybooks__pb2.BookIdRequest.FromString,
          response_serializer=mybooks__pb2.Book.SerializeToString,
      ),
      'Post': grpc.unary_unary_rpc_method_handler(
          servicer.Post,
          request_deserializer=mybooks__pb2.Book.FromString,
          response_serializer=mybooks__pb2.BookList.SerializeToString,
      ),
      'Put': grpc.unary_unary_rpc_method_handler(
          servicer.Put,
          request_deserializer=mybooks__pb2.Book.FromString,
          response_serializer=mybooks__pb2.Empty.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=mybooks__pb2.BookIdRequest.FromString,
          response_serializer=mybooks__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'books.BookService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
