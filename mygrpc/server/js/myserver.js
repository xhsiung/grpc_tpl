var messages = require('./helloworld_pb');
var services = require('./helloworld_grpc_pb');

var grpc = require('grpc');

function sayHello(call, callback) {
	var reply = new messages.HelloReply();
	reply.setMessage('Hello ' + call.request.getName());
	callback(null, reply);
}

function sayHelloAgain(call, callback){
	var reply = new messages.HelloReply2();
	reply.setMessage2('Hello2 ' + call.request.getName2());
	callback(null, reply);
}

function main() {
	var server = new grpc.Server();
	server.addService(services.GreeterService, {sayHello: sayHello , sayHelloAgain: sayHelloAgain });
	server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
	server.start();
}

main();
