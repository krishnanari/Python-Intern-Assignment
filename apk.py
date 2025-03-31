import subprocess
import time

# Paths
emulator_path = r"C:\Users\USER\AppData\Local\Android\Sdk\emulator\emulator.exe"
device_name = "Pixel_6"
adb_path = r"C:\Users\USER\AppData\Local\Android\Sdk\platform-tools\adb.exe"
apk_path = r"C:\Users\USER\Downloads\livio.rssreader_111.apk"

# Start the emulator
print("Starting the emulator...")
subprocess.Popen([emulator_path, "-avd", device_name])

# Wait for the emulator to fully boot
print("Waiting for the emulator to start...")
time.sleep(30)  # Adjust time as needed

# Ensure ADB is ready
print("Checking for ADB devices...")
subprocess.run([adb_path, "wait-for-device"])

# Install APK
print("Installing APK...")
subprocess.run([adb_path, "install", apk_path])

# Retrieve system information
print("Fetching system information...")

# Get OS version
os_version = subprocess.run([adb_path, "shell", "getprop ro.build.version.release"], capture_output=True, text=True).stdout.strip()
print(f"Android OS Version: {os_version}")

# Get Device Model
device_model = subprocess.run([adb_path, "shell", "getprop ro.product.model"], capture_output=True, text=True).stdout.strip()
print(f"Device Model: {device_model}")

# Get Available Memory
memory_info = subprocess.run([adb_path, "shell", "dumpsys meminfo | grep 'Free RAM'"], capture_output=True, text=True).stdout.strip()
print(f"Memory Info: {memory_info}")

# Log system information
with open("android_system_log.txt", "w") as log_file:
    log_file.write(f"Android OS Version: {os_version}\n")
    log_file.write(f"Device Model: {device_model}\n")
    log_file.write(f"Memory Info: {memory_info}\n")

print("System information logged successfully!")
