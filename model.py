from transformers import pipeline

emotion_model = None

def load_model():
    global emotion_model

    if emotion_model is None:
        print("Loading emotion model...")
        emotion_model = pipeline(
            "text-classification",
            model="bhadresh-savani/distilbert-base-uncased-emotion",
            device=-1
        )
        print("Model loaded successfully!")

def predict_emotion(text):
    load_model()
    result = emotion_model(text)
    return result[0]['label']