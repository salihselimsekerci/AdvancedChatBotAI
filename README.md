# Gelişmiş AI Chatbot

Bu proje, OpenAI'nin GPT-3.5-turbo modelini kullanarak gelişmiş bir web tabanlı AI chatbot oluşturur. Chatbot, kullanıcı mesajlarını kaydeder ve geçmiş konuşmaları görüntüler.

## Gereksinimler

- Python 3.7+
- Flask
- OpenAI API Anahtarı
- SQLite

## Kurulum

1. Gerekli bağımlılıkları yükleyin:
   ```
   pip install -r requirements.txt
   ```

2. `app.py` dosyasını çalıştırın:
   ```
   python app.py
   ```

3. Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

## Kullanım

- Kullanıcıdan gelen mesajları OpenAI API'sine gönderip yanıtlar döner.
- Kullanıcı mesajları ve bot yanıtları veritabanında kaydedilir.
- Geçmiş konuşmalar görüntülenebilir.
