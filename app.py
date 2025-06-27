from flask import Flask, render_template, request, jsonify 
import pickle
tf = pickle.load(open("vectorizer.pkl", "rb"))


model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get("message", "")


    transformed_message = tf.transform([message])
    prediction = model.predict(transformed_message)

    result = "Spam" if prediction[0] == 1 else "Not Spam"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860)

