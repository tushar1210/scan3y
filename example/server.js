var express = require('express');
var app = express();

var PORT = 50 ;

app.get('/',(req,res)=>{
    res.sendFile(__dirname+'/index.html') ;
});

app.listen(PORT,()=>{
    console.log('listening '+PORT);
});