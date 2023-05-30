var socket = new WebSocket('ws://localhost:8000/ws/chat/');

socket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    // Add message to chat
};

socket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    socket }
