from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # CORS制限なし

SECRET_URL = "mysecretchat"  # チャットのURLを設定

@app.route(f"/{SECRET_URL}")
def chat():
    return render_template("chat.html")

@socketio.on("message")
def handle_message(data):
    print(f"Received message: {data['user']} - {data['text']}")
    send(data, broadcast=True)  # すべての接続ユーザーにメッセージを送信

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)  # サーバーを起動
@app.route("/")
def home():
    return render_template("index.html")  # ここは適切なHTMLファイルに変更
