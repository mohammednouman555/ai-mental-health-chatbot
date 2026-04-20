from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import predict_emotion
from database import save_chat, get_chat_history

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]

    try:
        emotion = predict_emotion(user_message)

        responses = {
            "sadness": "I'm really sorry you're feeling this way. Would you like to talk about it?",
            "joy": "That's great to hear! What made you feel this way?",
            "anger": "I understand your frustration. Want to share what happened?",
            "fear": "That sounds difficult. I'm here for you—tell me more.",
            "love": "That's beautiful. Tell me more about it.",
            "surprise": "That sounds unexpected! What happened?"
        }

        bot_reply = responses.get(
            emotion,
            f"I understand you're feeling {emotion}. I'm here for you."
        )

        # Save chat
        save_chat(user_message, bot_reply, emotion)

        return jsonify({
            "emotion": emotion,
            "response": bot_reply
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/history", methods=["GET"])
def history():
    chats = get_chat_history()
    return jsonify(chats)


if __name__ == "__main__":
    app.run(debug=False)