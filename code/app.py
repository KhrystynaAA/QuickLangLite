from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_phrases():
    conn = sqlite3.connect('phrases.db')
    cursor = conn.cursor()
    cursor.execute('SELECT category, phrase, translation FROM phrases')
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    phrases = get_phrases()
    return render_template('index.html', phrases=phrases)

if __name__ == '__main__':
    app.run(debug=True)
