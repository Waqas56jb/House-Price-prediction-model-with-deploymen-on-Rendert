from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Load Trained Model
with open('models/house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])

        # Prediction
        prediction = model.predict([[area, bedrooms, bathrooms]])[0]
        return jsonify({'prediction': f"${prediction:,.2f}"})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
