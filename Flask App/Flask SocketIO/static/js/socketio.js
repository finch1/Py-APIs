document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect('http://' + document.domain + ':' + location.port); // how to connect to the socketio server

    // Predefined events
    // When the socket connects...event is trigered
    socket.on('connect', () =>{
        socket.send("I am connected"); // the message event will receive this on the server
    });

    // When the server sends message to this event bucket
    socket.on('message', data => {        
        const p = document.createElement('p');
        const br = document.createElement('br');
        p.innerHTML = data;
        document.querySelector('#display-message-section').append(p);
        console.log(`Message received: ${data}`)
    });

    // custom bucket name
    socket.on('some-event', data => {
        console.log(data)
    });

    document.querySelector('#send_message').onclick = () => {
        socket.send(document.querySelector('#user_message').value);

    }
})