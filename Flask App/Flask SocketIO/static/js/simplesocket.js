socket = io(); // io is available from the above link
socket.connect('http://127.0.0.1:5000'); // what to connect to

// add listeners
// do something when connect
socket.on('connect', function(){
    socket.send('on-connect') // send this to server
}) 	
    
// when trigger, do something
socket.on('message', function(msg){
    console.log(msg);
    socket.send('on-message');
})