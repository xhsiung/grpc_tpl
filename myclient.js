
var grpc = require('grpc');
var booksProto = grpc.load('mybooks.proto');
var client = new booksProto.books.BookService('0.0.0.0:50051', grpc.credentials.createInsecure());

function listBooks() {
    client.list({}, function(error, result) {
        console.log("listBook-->");
        if (error){
            console.log( 'Error:', error);
        }else{            
            console.log( result) ;
        }
    });
}

function getBookId( obj ){

    client.get(  {id: parseInt( obj.id) } , function( error , result){
        console.log("getBookId-->");
        if ( error ){
            console.log( 'Error:' , error );
        }else{
            console.log( result )
        }
   });
}

function postBook(obj){
    var book = {  
        id: obj.id,
        title: obj.title,
        author: obj.author
    };
    
    client.post( book , function( error , result){
        console.log("postBook-->");
        if (error){
            console.log( 'Error:' , error);
        }else{
            console.log( result );
        }
    });
}

function putBook( obj ){
    var book = {  
        id: obj.id,
        title: obj.title,
        author: obj.author
    };
    
    client.put( book , function(error , result){
        console.log("putBook-->");
        if (error){
            console.log( 'Error:' , error);
        }else{
            console.log( result );
        }
    });
}

function delBook( obj ){
    client.delete( { id: obj.id } , function(error , result){
        console.log("delBook-->");
        if (error){
            console.log( 'Error:' , error);
        }else{
            console.log( result );
        }
    });
}

//listBooks
//listBooks();

//Get 
//getBookId( {id:123} );

//Post
postBook( { id:222 , title:'hello' , author:"alex"});

//Put
//putBook( { id: 123 , title:'hello' , author:"alex"});

//Delete
//delBook( {id:123} );

listBooks();
