from flask import Flask, render_template, request, jsonify
import openai
import sqlite3  # SQLite veritabanı entegrasyonu için
from datetime import datetime  # Zaman damgası eklemek için

app = Flask(__name__)

# OpenAI API anahtarını ayarla
openai.api_key = "YOUR_OPENAI_API_KEY"

# Veritabanı bağlantısını oluştur
def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    # Mesajları ve yanıtları kaydetmek için bir tablo oluştur
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_message TEXT,
                    bot_message TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

# Veritabanına mesajları kaydet
def save_chat_to_db(user_message, bot_message):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO chat_history (user_message, bot_message) VALUES (?, ?)", (user_message, bot_message))
    conn.commit()
    conn.close()

@app.route("/")
def index():
    # Ana sayfayı kullanıcıya göster
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]

    # OpenAI API'sine istek gönder
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
    )

    bot_message = response.choices[0].message.content

    # Mesajları veritabanına kaydet
    save_chat_to_db(user_message, bot_message)

    return jsonify({"message": bot_message})

@app.route("/history")
def history():
    # Geçmiş konuşmaları kullanıcıya göster
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT user_message, bot_message, timestamp FROM chat_history ORDER BY timestamp DESC")
    chat_history = c.fetchall()
    conn.close()
    return render_template("history.html", chat_history=chat_history)

if __name__ == "__main__":
    init_db()  # Uygulama başladığında veritabanını başlat
    app.run(debug=True)
