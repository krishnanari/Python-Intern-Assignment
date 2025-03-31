import subprocess
import requests
import json

# Define ADB path
adb_path = r"C:\Users\USER\AppData\Local\Android\Sdk\platform-tools\adb.exe"

# Backend API URL (Correct route for adding an app)
server_url = "http://127.0.0.1:5000/add-app"  # Flask API running locally

# Ensure ADB is connected
print("Waiting for ADB connection...")
subprocess.run([adb_path, "wait-for-device"])

# Fetch system details from Android emulator
device_id = subprocess.run([adb_path, "shell", "settings get secure android_id"], capture_output=True, text=True).stdout.strip()
os_version = subprocess.run([adb_path, "shell", "getprop ro.build.version.release"], capture_output=True, text=True).stdout.strip()
device_model = subprocess.run([adb_path, "shell", "getprop ro.product.model"], capture_output=True, text=True).stdout.strip()
memory_info = subprocess.run([adb_path, "shell", "dumpsys meminfo | grep 'Free RAM'"], capture_output=True, text=True).stdout.strip()

# Prepare data payload
data = {
    "app_name": "Sample App",  # You can replace this with dynamic data if needed
    "version": "1.0.0",  # Replace with the version you're working with
    "description": "A sample app for testing"
}

# Send data to the backend API
print("Sending data to server...")
response = requests.post(server_url, json=data)

# Log the server response
if response.status_code == 201:  # 201 means resource created successfully
    print("Server Response:", response.json())
else:
    print("Failed to send data. Status Code:", response.status_code)

# Save response to a log file
with open("network_log.txt", "w") as log_file:
    log_file.write(f"Sent Data: {json.dumps(data, indent=4)}\n")
    log_file.write(f"Server Response: {response.text}\n")

print("Data logged successfully!")
