from flask import Flask, request, jsonify, render_template_string
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
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Not Fake News Co.</title>
            <style>
              .container {
                display: flex;
                justify-content: center;
                align-items: flex-start;
                height: 100vh;
                text-align: center;
              }
              .form-group {
                width: 100%;
              }
              #textInput {
                width: 100%;
                height: 200px;
                max-height: 1000px;
                resize: vertical;
              }
              .content {
                width: 100%;
                max-width: 800px;
              }
            </style>
          </head>
          <body>
            <div class="container">
              <div class="content">
                <h1>Fake News Detector</h1>
                <form id="predictForm">
                  <div class="form-group">
                    <textarea class="form-control" id="textInput" name="text"></textarea>
                  </div>
                  <button type="submit" class="btn btn-primary">Is this real?</button>
                </form>
                <div id="result"></div>
              </div>
            </div>
            <script>
              document.getElementById('predictForm').addEventListener('submit', function(event) {
                event.preventDefault();
                var text = document.getElementById('textInput').value;
                fetch('/predict', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({ text: text })
                })
                .then(response => response.json())
                .then(data => {
                  document.getElementById('result').innerText = 'Prediction: ' + data.prediction;
                })
                .catch(error => {
                  document.getElementById('result').innerText = 'Error: ' + error;
                });
              });
            </script>
          </body>
        </html>
    ''')

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