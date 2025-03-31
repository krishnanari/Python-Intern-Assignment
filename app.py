from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Helper function to connect to SQLite DB
def get_db_connection():
    conn = sqlite3.connect('apps.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the database and the app table
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS apps
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    app_name TEXT NOT NULL,
                    version TEXT NOT NULL,
                    description TEXT)''')
    conn.commit()
    conn.close()

# Task 1.1: POST /add-app
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    app_name = data.get('app_name')
    version = data.get('version')
    description = data.get('description')

    if not app_name or not version:
        return jsonify({"error": "App name and version are required!"}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO apps (app_name, version, description) VALUES (?, ?, ?)',
                 (app_name, version, description))
    conn.commit()
    conn.close()
    return jsonify({"message": "App added successfully!"}), 201

# Task 1.2: GET /get-app/{id}
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    conn = get_db_connection()
    app = conn.execute('SELECT * FROM apps WHERE id = ?', (id,)).fetchone()
    conn.close()

    if app is None:
        return jsonify({"error": "App not found!"}), 404

    return jsonify({
        "id": app['id'],
        "app_name": app['app_name'],
        "version": app['version'],
        "description": app['description']
    })

# Task 1.3: DELETE /delete-app/{id}
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    conn = get_db_connection()
    app = conn.execute('SELECT * FROM apps WHERE id = ?', (id,)).fetchone()

    if app is None:
        conn.close()
        return jsonify({"error": "App not found!"}), 404

    conn.execute('DELETE FROM apps WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "App deleted successfully!"})

if __name__ == '__main__':
    init_db()  # Initialize the DB when starting the app
    app.run(debug=True)
    