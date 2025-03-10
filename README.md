# SimpleMessageTool

## 📌 Overview
SimpleMessageTool is a Python-based MQTT client that connects to an **Azure Event Grid MQTT broker** and publishes temperature readings every 5 minutes.

## ⚙️ Configuration
Before running the script, configure the environment variables in a **`.env`** file:

```
BROKER=ip-adress of broker
PORT= Your port
CLIENT_ID=Client-id
TOPIC=sensor/temperature
CERT_PATH=client.crt
KEY_PATH=client.key
```

## 🛠 Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/ThiboL-Skyline/SimpleMessageTool.git
   cd SimpleMessageTool
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Running the Script
To start the MQTT client and publish messages:
```sh
python MessageSend.py
```
This will send a random temperature reading **between 5°C and 31°C** to the MQTT broker every 5 minutes.

## 🔧 Troubleshooting
- If you get **certificate errors**, ensure that the **client.crt** and **client.key** files are valid.
- If the connection fails, check your **Azure Event Grid MQTT permissions**.
- Use `git branch` and `git push -u origin main` if you have trouble pushing to GitHub.

## 📜 License
This project is licensed under the MIT License.

