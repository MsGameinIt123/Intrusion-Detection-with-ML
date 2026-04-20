from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("../models/intrusion_detection_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    data = pd.read_csv(file)
    
    scaled = scaler.transform(data)
    predictions = model.predict(scaled)
    
    data['Prediction'] = predictions
    data['Prediction'] = data['Prediction'].map({0: 'Normal', 1: 'Attack'})
    
    attack_count = (data['Prediction'] == 'Attack').sum()
    normal_count = (data['Prediction'] == 'Normal').sum()
    total = len(data)
    
    # Move Prediction column to the front
    cols = ['Prediction'] + [col for col in data.columns if col != 'Prediction']
    data = data[cols]

    # Convert to html
    table_html = data.to_html(
        classes='table table-striped',
        index = False
    )
    
    # Add coloring
    table_html = table_html.replace(
        'Attack', '<span style="color:red; font-weight:bold;">Attack</span>'
    )
    table_html = table_html.replace(
        'Normal', '<span style="color:green; font-weight:bold;">Normal</span>'
    )
    
    attack_pct = round((attack_count / total) * 100, 2)
    status = "Secure" if attack_count == 0 else "Threat Detected"
    
    alert = ""
    if attack_count > 0:
        alert = f"""
        <div style="color:white;background-color:red;padding:10px;
        margin-bottom:15px;border-radius:5px;">
            Warning: {attack_count} potential attacks detected!
        </div>
        """
    
    return f"""
    <h2>Prediction Results</h2>
    
    <div style="
        # padding:15px,
        # border:1px solid #ccc;
        # border-radius:8px;
        # margin-bottom:20px;
        # width:300px;
        padding:20px;
        border-radius:10px;
        background-color:#f8f9fa;
        box-shadow:0 2px 6px rgba(0,0,0,0.1);
        margin-bottom:20px;
    ">
        <h3>Summary</h3>
            <p><strong>Total Records:</strong> {total}</p>
            <p style="color:red;"><strong>Attacks Detected:</strong> {attack_count}</p>
            {alert}
            <p style="color:green;"><strong>Normal Traffic:</strong> {normal_count}</p>
            <p><strong>Attack Rate:</strong> {attack_pct}%</p>
        <h3>Status:
            <span style="color:red;">{status}</span>
        </h3>
    </div>
    
    <div style="overflow:auto;">
        {table_html}
    </div>
    
    <br>
    <a href="/" class="home-button" style="
        display:inline-block;
        padding:10px 15px;
        background-color:#6c757d;
        color:white;
        text-decoration:none;
        border-radius:5px;
        margin-top:15px;
    ">
    Back to Home
    </a>
    
    <hr>
    <p style="text-align:center; font-size:12px; color:gray">
        Machine Learning Cyber Defense Demo | Madison Torres
    </p>
    """

if __name__ == "__main__":
    app.run(debug=True)