import paho.mqtt.client as mqtt
import pyaudio, zlib

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=22000, output=True)


HOST = "192.168.10.30"#树莓的MQTT服务器
PORT = 1883#树莓的MQTT服务器端口

def client_loop():
    client_id = "RECV"
    client = mqtt.Client(client_id)    
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(HOST, PORT, 30)
    client.loop_forever()
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("AUD_RECV")#订阅语音频道
    print("ready!")
 
def on_message(client, userdata, msg):
    print("RECV:", len(msg.payload), "bytes")

    data = zlib.decompress(msg.payload)     #解压数据并填入播放音频流
    stream.write(data)
    
 
if __name__ == '__main__':
    client_loop()