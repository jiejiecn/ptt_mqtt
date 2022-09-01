# PTT(Push to Talk) over MQTT
Python audio stream over MQTT protocol


<br>

### 

Sender      发送端

Receiver    接收端

接收端启动后持续监听消息频道，（默认Topic：RECV）
发送端启动后会持续录音并切片发送

音频发送过程中采用zlib做简单压缩以节省带宽和流量，降低转发延迟  


<br>

#### ToDo

增加“延迟”指标统计


