from flask import Flask, render_to_path, request, redirect
import sqlite3

app = Flask(__name__)

# The "Database Tools" you mentioned to HR
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, title TEXT, status TEXT)')
    conn.close()

@app.route('/add_project', methods=['POST'])
def add_project():
    # Security: Using Parameterized Queries to prevent SQL Injection
    title = request.form['title']
    status = "Pending"
    
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO projects (title, status) VALUES (?, ?)", (title, status))
        conn.commit()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)