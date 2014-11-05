var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io').listen(http);
var bodyParser = require('body-parser');

app.use(bodyParser.json());

var data = {};


app.get('/', function(req, res) {
    res.sendfile('index.html');
});

io.on('connection', function (socket) {
    console.log("a user connected")

    socket.on('disconnect', function(){
        console.log('user disconnected');
    });

    socket.on('message', function(msg){
        io.emit('message', msg);
    });
});

app.post('/webhook', function(req, res) {
    data = req.body;
    io.emit('message', data);
    res.send(data);
});

var server = http.listen(3000, function() {
    console.log('Listening on port %d', server.address().port);
});


