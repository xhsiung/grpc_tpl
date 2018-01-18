var grpc = require("grpc");
var booksProto = grpc.load("mybooks.proto");

var events = require("events");
var bookStream = new events.EventEmitter();

var books = [{  
    id: 123,
    title: 'A Tale of Two Cities',
    author: 'Charles Dickens'
}];

var server = new grpc.Server();

server.addService(booksProto.books.BookService.service, {
    list: function( call , callback){
        callback( null , books );
    },

    get: function(call , callback){
        for (var i=0; i < books.length ; i++)        {
            if (books[i].id == call.request.id ){
                return callback(null , books[i]);
            }
        }

        //error response
        callback({
            code:grpc.status.NOT_FOUND,
            details: 'Not Found'
        });
    },

    post: function(call , callback){
        var book = call.request;
        
        for (var k=0; k < books.length ; k++){
            if (books[ k ].id == book.id ){
                //remove k location , one item delete
                books.splice( k ,1) ;
            }
        }

        //insert
        books.push( book );
        
        //emit event
        bookStream.emit( 'new_book' ,book );
        return callback( null, { success: true } );
    },

    put: function(call , callback){
        var book = call.request;

        for (var k=0; k < books.length ; k++){
            if (books[ k ].id == book.id ){
                //remove k location , one item delete
                books[k].title = book.title;
                books[k].author = book.author;
                return callback( null, { success: true }  );
            }
        }
    
        //error response
        callback({
            code:grpc.status.NOT_FOUND,
            details: 'Not Found'
        });
    },

    delete: function( call , callback ){
        var id = call.request.id;

        for (var k=0; k < books.length ; k++){
            if (books[ k ].id == id ){
                //remove k location , one item delete
                books.splice( k ,1) ;
                return callback( null, { success: true } );
            }
        }
        
        //error response
        callback({
            code:grpc.status.NOT_FOUND,
            details: 'Not Found'
        });
    },

    watch: function( call ){
        console.log( "watch ~~");

        //recieve client data
        call.on('data', function(result){
            console.log( result );
        }).on('end', function(){
            console.log('end');
	});
        
        //recieve emit event
        bookStream.on("new_book" , function(book){
            //send client data
            call.write( book );
        });
    }

});

server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
server.start();
