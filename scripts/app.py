from flask import Flask, request, render_template, jsonify
from model import predict_customer_category
from email_templates import generate_campaign_email

## below template folder need to be replaced with actual location
app = Flask(__name__,
            template_folder='C:\\Users\\r_nra\\python\\case_study\\martech\\templates',
            static_folder='C:\\Users\\r_nra\\python\\case_study\\martech\\static')

# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to predict the category
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    age = data['age']
    transaction_history = data['transaction_history']
    location = data['location']
    interests = data['interests']
    lifestyle = data['lifestyle']

    sample_data = {
        'Age': age,
        'Transaction History': transaction_history,
        'Location': location,
        'Interests': interests,
        'Lifestyle': lifestyle
    }

    predicted_label = predict_customer_category(sample_data)

    # Convert NumPy int64 to Python int
    predicted_label = int(predicted_label)

    return jsonify({'predicted_category': predicted_label})

# Route to generate the email based on predicted category
@app.route('/generate_email', methods=['POST'])
def generate_email():
    data = request.get_json()
    target_audience = data['target_audience']
    
    email_content = generate_campaign_email(target_audience)
    
    return jsonify({'email_content': email_content})

if __name__ == '__main__':
    app.run(debug=True)
