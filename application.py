from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle


application = Flask(__name__)

loaded_model = None
vectorizer = None

with open('basic_classifier.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

with open('count_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def predict(text):
    ttext = vectorizer.transform([text])
    return loaded_model.predict(ttext)[0]

@application.route("/")
def index():
    return "Your Flask App Works! V1.0"

# returns FAKE if fake
# returns REAL if real
@application.route("/predict", methods=['POST'])
def predict_route():
    try:
        data = request.get_json()
        if 'text' not in data:
            raise ValueError("Missing 'text' in request data")
        if not isinstance(data['text'], str):
            raise ValueError("'text' must be a string")
        text = data['text']
        prediction = predict(text)
        if prediction not in ['FAKE', 'REAL']:
            raise ValueError("Prediction must be either 'FAKE' or 'REAL'")
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    application.run(port=5000, debug=False)