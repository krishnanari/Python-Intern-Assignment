**# Python Intern Assignment

This repository contains the code for the Python Intern Assignment, which includes backend development, database management, virtual Android system simulation, and basic networking tasks.

## Table of Contents

1. [Task 1: Backend Development](#task-1-backend-development)
2. [Task 2: Database Management](#task-2-database-management)
3. [Task 3: Virtual Android System Simulation](#task-3-virtual-android-system-simulation)
4. [Task 4: Basic Networking](#task-4-basic-networking)
5. [Installation & Setup](#installation-setup)

---

## Task 1: Backend Development

**API Code:**

A Flask-based API to manage app details in a database. The following endpoints are available:

1. **POST /add-app**: Add app details to the database (fields: `app_name`, `version`, `description`).
2. **GET /get-app/{id}**: Retrieve app details by ID.
3. **DELETE /delete-app/{id}**: Remove an app by ID.

### Instructions:
1. Clone the repository and navigate to the folder containing the `networking_script.py` and API code.
2. Install required dependencies by running:
3. Start the Flask server by running:
4. The API will be available on `http://127.0.0.1:5000`.

---

## Task 2: Database Management

**Database:**

SQLite is used to store app details (app_name, version, description). The schema and integration with the Flask API are included in `app.py`.

### Instructions:

1. The database is created automatically when the Flask app is started by running `python app.py`.
2. The database schema is initialized inside the `init_db()` function in the code.
3. Sample data can be added using the `POST /add-app` endpoint or via any HTTP client (e.g., Postman or CURL).

---

## Task 3: Virtual Android System Simulation

**Virtual Android System:**

This task involves simulating a virtual Android system capable of running basic tasks such as creating a virtual Android environment, installing apps, and logging system information.

### Instructions:

1. **Required Tools**:
- Install **QEMU** or an Android Emulator plugin on your system.
- Ensure that the necessary Android SDK tools are installed.

2. **Setup**:
- The Python script for setting up and managing the virtual Android system is available as `android_simulation.py`.

3. **Running the script**:
- Run the script using:

  ```
  python android_simulation.py
  ```

4. The script will:
- Set up the virtual Android environment.
- Launch the system interface (terminal or GUI).
- Install a sample APK file into the virtual system.
- Log system information (OS version, device model, available memory).

---

## Task 4: Basic Networking

**Networking Script:**

This Python script connects the virtual Android system to the backend server (created in Task 1). It performs the following:

1. Establishes a **TCP/HTTP connection** with the backend server.
2. Sends mock data (e.g., device ID, system info) to the backend API.
3. Receives and logs the server's response.

### Instructions:

1. **Setup**:
- Ensure the Flask server (from Task 1) is running.
- The script for networking is available as `networking_script.py`.

2. **Running the script**:
- Run the script using:

  ```
  python networking_script.py
  ```

3. The script will:
- Wait for an ADB connection (virtual Android system).
- Send mock data to the `/add-app` endpoint of the Flask server.
- Log the server's response (such as a success message).

---

## Installation & Setup

### Prerequisites:

1. **Python 3.7+** is required. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install dependencies**: In the root directory of the project, run the following command to install required libraries:


### Running the Application:

1. **Task 1 & 2: Flask API**:
- To start the Flask server, run:

  ```
  python app.py
  ```

- The server will run at `http://127.0.0.1:5000`.

2. **Task 3: Virtual Android System**:
- Ensure you have QEMU or Android Emulator set up.
- Run the script to simulate the virtual Android system:

  ```
  python android_simulation.py
  ```

3. **Task 4: Networking**:
- Make sure the Flask API server is running.
- Run the networking script to send data to the server:

  ```
  python networking_script.py
  ```

---

### Sample Data:

- You can test the API using **Postman** or **CURL** by sending requests to the following endpoints:
- **POST /add-app**: 

 ```json
 {
   "app_name": "Sample App",
   "version": "1.0.0",
   "description": "This is a sample app."
 }
 ```

- **GET /get-app/{id}**: Retrieve app details by ID.
- **DELETE /delete-app/{id}**: Delete an app by ID.

---

## Conclusion

This project demonstrates your skills in backend development with Flask, database management with SQLite, virtual Android system simulation, and networking concepts in Python. 

The implementation allows you to interact with a virtual Android system, integrate it with a backend server, and manage app details in a database.
