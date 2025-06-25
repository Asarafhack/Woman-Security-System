from flask import Flask, render_template, request, jsonify
import csv
from model import predict_risk

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Chat page
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.json.get("message")
        prediction = predict_risk(user_message)
        
        # Save chat to CSV
        with open('data/chats.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_message, prediction])
        
        return jsonify({"prediction": prediction})
    return render_template("chat.html")

# Profile page
@app.route("/profile")
def profile():
    chats = []
    with open('data/chats.csv', 'r') as file:
        reader = csv.reader(file)
        chats = [row for row in reader]
    return render_template("profile.html", chats=chats)

if __name__ == "__main__":
    app.run(debug=True)
