// Core
const http = require('http')
// third
const socketio = require('socket.io')
const express = require('express')
const Log = require('log')

const port = process.env.PORT || 3000
const log = new Log('debug')
const app = express()
const server = http.createServer(app)
const io = socketio(server)

// Routes
app.use(express.static(__dirname + "/public"))

app.get('/', (req, res) => {
  res.send('Hello from node:)')
})

io.sockets.on('connection', function(socket){
    socket.join('chat');

    socket.on('message', function(message){
        socket.broadcast.to('chat').emit('message',{chat:message.text});
    });
});

server.listen(port, '0.0.0.0', () => log.info(`server listening on http://localhost:${port}`))
