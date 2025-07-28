from flask import Flask, render_template, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    complaint = data.get("complaint", "")
    
    if complaint:
        with open("complaints.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), complaint])
        return jsonify({"message": "✅ Complaint submitted successfully!"})
    
    return jsonify({"message": "⚠️ Complaint is empty!"})

if __name__ == "__main__":
    app.run(debug=True)
