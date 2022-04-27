function WebSocketTest() {

    // 打开一个 web socket
    var ws = new WebSocket("ws://127.0.0.1:62436");

    ws.onopen = function () {
        // Web Socket 已连接上，使用 send() 方法发送数据
        var front_str = "31 31 32 32 33 33 34 34";
        ws.send(front_str);
        // alert("数据已发送");
    };

    ws.onmessage = function (evt) {
        var received_msg = evt.data;
        console.log(received_msg);
    };


}
window.onload = WebSocketTest;


