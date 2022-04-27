function WebSocketTest() {

    // 打开一个 web socket
    var ws = new WebSocket("ws://localhost:5679");

    ws.onopen = function () {
        // Web Socket 已连接上，使用 send() 方法发送数据
        ws.send("前端页面发来的数据");
        alert("数据已发送");
    };

    ws.onmessage = function (evt) {
        var received_msg = evt.data;
        alert(received_msg);
        var text1=document.getElementById("text1");
        var text2=document.getElementById("text2");
        if(received_msg=="25")
            text1.value=received_msg
        else
            text2.value=received_msg
    };

    // ws.onclose = function () {
    //     // 关闭 websocket
    //     alert("连接已关闭...");
    // };

}

window.onload = WebSocketTest