import ssl
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MQTT Configuration from .env file
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT", 8883))  # Ensure it's an integer
CLIENT_ID = os.getenv("CLIENT_ID") + "-subscriber"  # Different ID for subscriber
TOPIC = os.getenv("TOPIC")
CERT_PATH = "client.crt"
KEY_PATH = "client.key"

# Callback function when message is received
def on_message(client, userdata, msg):
    print(f"📩 Received message on {msg.topic}: {msg.payload.decode()}")

# Callback for connection
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Successfully connected to MQTT broker!")
        client.subscribe(TOPIC)  # Subscribe to the topic
        print(f"🔔 Subscribed to topic: {TOPIC}")
    else:
        print(f"❌ Connection failed with code: {rc}")

# Callback for disconnection
def on_disconnect(client, userdata, rc, properties=None):
    print(f"🔌 Disconnected from MQTT broker, reason: {rc}")

# MQTT Client Setup
client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv5)
client.tls_set(certfile=CERT_PATH, keyfile=KEY_PATH, tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Connect to broker and start listening
client.connect(BROKER, PORT, 60)
client.loop_forever()  # Keep the connection alive
