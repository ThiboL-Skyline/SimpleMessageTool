import ssl
import time
import random
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MQTT Configuration from .env file
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT", 8883))
CLIENT_ID = os.getenv("CLIENT_ID")
TOPIC = os.getenv("TOPIC")
CERT_PATH = "client.crt"
KEY_PATH = "client.key"

# Callback functions
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Successfully connected to MQTT broker!")
    else:
        print(f"❌ Connection failed with code: {rc}")

def on_publish(client, userdata, mid, properties=None):
    print(f"📡 Message published: {mid}")

def on_disconnect(client, userdata, rc, properties=None):
    print(f"🔌 Disconnected from MQTT broker, reason: {rc}")

# MQTT Client Setup
client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv5)
client.tls_set(certfile=CERT_PATH, keyfile=KEY_PATH, tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Connect to broker
client.connect(BROKER, PORT, 60)

# Start event loop
client.loop_start()

try:
    while True:
        temperature = round(random.uniform(5, 31), 1)
        payload = f'{{"temperature": {temperature}}}'
        client.publish(TOPIC, payload, qos=1)
        print(f"📤 Sent message to topic {TOPIC}: {payload}")
        time.sleep(300)
except KeyboardInterrupt:
    print("🔴 Shutting down...")
    client.loop_stop()
    client.disconnect()