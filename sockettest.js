function WebSocketTest() {

    // 打开一个 web socket
    var ws = new WebSocket("ws://localhost:62436");

    ws.onopen = function () {
        // Web Socket 已连接上，使用 send() 方法发送数据
        var front_str = "hello";
        ws.send("前端页面发来的数据: " + front_str);
        // alert("数据已发送");
    };

    ws.onmessage = function (evt) {
        var received_msg = evt.data;
        var temperature=document.getElementById("temperature");
        var humidity=document.getElementById("humidity")
        var set_temperature=document.getElementById("temperature_design");
        var set_humidity=document.getElementById("humidity_design");
        var received_json = JSON.parse(received_msg);
        temperature.value=received_json.temperature;
        humidity.value=received_json.humidity;
        set_temperature.value=received_json.set_temperature;
        set_humidity.value = received_json.set_humidity;

    };

    // ws.onclose = function () {
    //     // 关闭 websocket
    //     alert("连接已关闭...");
    // };

}



window.onload = WebSocketTest;
