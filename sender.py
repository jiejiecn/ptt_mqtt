import paho.mqtt.client as mqtt
import time
import pyaudio, zlib


HOST = "192.168.10.30"#树莓的MQTT服务器
PORT = 1883#树莓的MQTT服务器端口

CHUNK = 4096
buffer = [] #语音片段缓冲区

    
def record_callback(in_data, frame_count, time_info, status):
    buffer.append(in_data)
    return b"", pyaudio.paContinue

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("ready!")

    
def on_message(client, userdata, msg):
    print("msg incoming")
    
    
if __name__ == '__main__':
    client_id = "SEND"
    client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(HOST, PORT, 60)

    p = pyaudio.PyAudio()  # 实例化对象
    stream = p.open(format=pyaudio.paInt16, #按16位音频，22kHz采样频率，单声道采集音频
                    channels=1,
                    rate=22000,
                    input=True,
                    frames_per_buffer=CHUNK,
                    stream_callback=record_callback)  
    
    stream.start_stream() #打开音频流

    while True:
        data = b"".join(buffer)
        buffer.clear()
        msg = zlib.compress(data)
        client.publish("AUD_RECV", msg)
        print("SENT: ", len(msg), "bytes")
        time.sleep(0.5)
        client.loop()