import keyboard
import paho.mqtt.client as mqtt

mqtt_broker = "a71bc2131d504e6380dad83d96e8708a.s1.eu.hivemq.cloud"
mqtt_port = 1883
mqtt_topic = "topic/keyboard_event"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Kết nối thành công tới broker MQTT")
    else:
        print("Kết nối tới broker MQTT thất bại, mã lỗi:", rc)

def on_publish(client, userdata, mid):
    print("Đã gửi thông báo thành công")

def main():
    print("Nhấn phím 'a' để gửi thông báo lên server MQTT")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(mqtt_broker, mqtt_port, 60)

    keyboard.wait('a')

    client.publish(mqtt_topic, "Phím 'a' đã được nhấn")

    client.disconnect()

if __name__ == "__main__":
    main()
