import pandas as pd
import numpy as np
import pickle

# Load the model and encoders
with open('model_new.pkl', 'rb') as model_file:
    model_new = pickle.load(model_file)
with open('label_encoders_new.pkl', 'rb') as le_file:
    label_encoders_new = pickle.load(le_file)
with open('scaler_new.pkl', 'rb') as scaler_file:
    scaler_new = pickle.load(scaler_file)
    
# Function to handle unseen labels
def safe_transform(encoder, value):
    try:
        return encoder.transform([value])[0]
    except ValueError:
        return np.median(encoder.transform(encoder.classes_))

# Function to predict customer category using new features
def predict_customer_category(data):
    encoded_data = {}
    for column, le in label_encoders_new.items():
        if column in data:
            encoded_data[column] = safe_transform(le, data[column])
    print(f"Encoded data: {encoded_data}")

    features = pd.DataFrame([[
        data['Age'],
        data['Transaction History'],
        encoded_data.get('Location', data['Location']),
        encoded_data.get('Interests', data['Interests']),
        encoded_data.get('Lifestyle', data['Lifestyle'])
    ]], columns=['Age', 'Transaction History', 'Location', 'Interests', 'Lifestyle'])

    print(f"Features before scaling: {features}")
    features = scaler_new.transform(features)
    print(f"Features after scaling: {features}")

    prediction_numeric = model_new.predict(features)[0]
    prediction_label = label_encoders_new['Target'].inverse_transform([prediction_numeric])[0]
    print(f"Decoded Prediction: {prediction_label}")
    return prediction_label
