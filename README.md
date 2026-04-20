MACHINE LEARNING INTRUSION DETECTION SYSTEM
## Overview
This project implements a machine learning-based intrusion detection system (IDS) designed to identify malicious network activity using the NSL-KDD dataset. The system analyzes network traffic patterns to distinguish between normal activity and potential cyber threats.
This project was developed as part of a Computer Science capstone and demonstrates the application of machine learning techniques in cyber defense.
## Objectives
- Detect malicious network traffic using machine learning
- Compare baseline and ensemble models
- Optimize detection performance through threshold tuning
- Analyze network behavior patterns associated with intrusions
## Dataset
The project uses the NSL-KDD dataset, a refined intrusion detection dataset containing labeled network traffic records representing normal activity and multiple attack types.
Each record includes features such as:
- protocol type
- service requested
- connection duration
- byte counts
- error rates
- connection behavior metrics
## Technologies Used
Language
- Python
Libraries
- pandas
- NumPy
- scikit-learn
- matplotlib
## Methodology
Data Preparation
- Cleaned and preprocessed network traffic data
- One-hot encoded categorical features
- Standardized numerical features
- Converted labels to binary classification (normal vs attack)
Model Development
Two models were evaluated:
    1) Logistic Regression
    - Baseline performance model
    2) Random Forest Classifier
    - Captured nonlinear traffic patterns
    - Improved detection reliability
Threshold Optimization
Detection threshold tuning improved attack detection coverage while maintaining high alert precision.
## Results
Model                       Accuracy    Attack_Recall       Attack_Precision
    Logistic Regression          ~80%        Moderate            High
    Random Forest (default)      ~80%        0.68                0.97
    Random Forest (tuned)        ~89%        0.84                0.97
Key Findings
- Threshold tuning significantly improved detection coverage.
- Traffic volume metrics were strong indicators of malicious activity.
- Machine learning can effectively identify abnormal network behavior.
## Feature Importance Insights
The most influential indicators of malicious traffic included:
- src_bytes - abnormal data volume from source
- dst_bytes - irregular response volume
- same_srv_rate - repeated connections to the same service
These patterns align with real-world attack behaviors such as denial-of-service activity and automated probing.
## Visualizations
This project includes:
- Confusion matrix visualization
- Feature importance chart
- Traffic distribution graph
## Security Implications
This project demonstrates how machine learning can enhance intrusion detection by identifying abnormal traffic patterns and enabling adaptable threat detection. Threshold tuning allows detection systems to balance detection coverage and alert volume according to operational needs.
## Future Improvements
- Train on modern intrusion datasets
- Implement real-time traffic monitoring
- Explore gradient boosting and deep learning approaches
- Integrate with SIEM platforms
- Detect zero-day attack patterns
## Project Structure
- app/ -> Flask web application
- data/raw/ -> original NSL-KDD datasets
- data/processed/ -> cleaned data and test samples
- models/ -> trained ML model and scaler
- notebooks/ -> development and experimentation
- src/ -> data processing and ML pipeline scripts
- visuals/ -> charts and evaluation outputs
## Installation
1. Clone the repository or download the project files
2. Navigate to the project directory
3. Install dependencies:
    pip install -r requirements.txt
## DEMO
1. Navigate to app directory:
    cd app
2. Run the application:
    python app.py
3. Open your browser:
    http://127.0.0.1:5000
4. Upload a CSV file (e.g., data/processed/test_sample.csv)
## Screenshots/Images
- Upload interface
- Prediction results with summary
- 2 visualization outputs
## Author
Madison Torres
Computer Science Student | Cyber Defense Enthusiast
