from flask import Flask, request, jsonify
from api.model.predict import get_notification_prediction

app = Flask(__name__)

@app.route('/predict_notification', methods=['POST'])
def predict():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    notification_type = get_notification_prediction(data)
    return jsonify({"notification_type": notification_type})

if __name__ == '__main__':
    app.run(debug=True)
