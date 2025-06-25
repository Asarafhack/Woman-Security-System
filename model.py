import csv

# Load model data
def load_model_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            keyword, risk_level = row
            data[keyword.lower()] = risk_level
    return data

# Predict risk based on message
def predict_risk(message):
    model_data = load_model_data('data/model_data.csv')
    for word in message.lower().split():
        if word in model_data:
            return model_data[word]
    return "Safe"  # Default to "Safe" if no risky keywords are found
