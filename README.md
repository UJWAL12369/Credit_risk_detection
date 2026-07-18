# German Credit Risk Prediction using Machine Learning

## Overview

This project develops a machine learning model to predict whether a loan applicant represents a **Good Credit Risk** or **Bad Credit Risk** using the German Credit dataset. The project covers the complete machine learning workflow, including data preprocessing, exploratory data analysis, model development, hyperparameter tuning, model interpretation using SHAP, and deployment with Streamlit.

---

## Project Objectives

- Perform Exploratory Data Analysis (EDA)
- Preprocess categorical and numerical features
- Train multiple machine learning classification models
- Optimize model performance using Hyperparameter Tuning
- Interpret model predictions using SHAP
- Deploy the final model as an interactive Streamlit web application

---

## Dataset

**Dataset:** German Credit Dataset

The dataset contains demographic and financial information about loan applicants.

### Features

- Age
- Sex
- Job
- Housing
- Saving Accounts
- Checking Account
- Credit Amount
- Duration

### Target Variable

- Risk
    - Good Credit
    - Bad Credit

---

## Project Workflow

### 1. Data Preprocessing

- Removed unnecessary columns
- Checked missing values
- Label Encoding of categorical variables
- Train-Test Split
- Saved encoders using Joblib

---

### 2. Exploratory Data Analysis

Performed

- Distribution plots
- Count plots
- Box plots
- Correlation analysis
- Outlier detection

---

### 3. Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Extra Trees Classifier
- XGBoost Classifier

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

### 4. Hyperparameter Tuning

Hyperparameter tuning was performed using

- GridSearchCV

Parameters tuned included:

- n_estimators
- max_depth
- min_samples_split
- min_samples_leaf
- max_features

---

### 5. Model Explainability (SHAP)

SHAP was used to interpret the predictions made by the final model.

Generated visualizations include:

- SHAP Beeswarm Plot
- SHAP Waterfall Plot
- Global Feature Importance
- Local Prediction Explanation

Key observations:

- Duration was the most influential feature.
- Sex had a significant impact on prediction.
- Checking Account and Saving Accounts contributed considerably.
- Age and Job had comparatively lower influence.

---

## Model Deployment

The final model was deployed using **Streamlit**.

Users can enter:

- Age
- Sex
- Job
- Housing
- Saving Accounts
- Checking Account
- Credit Amount
- Duration

The application predicts whether the applicant is a Good or Bad Credit Risk.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- SHAP
- Joblib
- Streamlit

---

## Project Structure

```
German_Credit/
│
├── german_credit_data.csv
├── app.py
├── credit.py
├── extra_tress_credit_model.pkl
├── Sex_encoder.pkl
├── Housing_encoder.pkl
├── Saving accounts_encoder.pkl
├── Checking account_encoder.pkl
├── target_encoder.pkl
├── requirements.txt
├── README.md
└── notebook.ipynb
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/German-Credit-Risk-Prediction.git
```

Move into the project directory

```bash
cd German-Credit-Risk-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Streamlit App

```bash
streamlit run app.py
```

---

## Sample Prediction

Input:

- Age: 33
- Sex: Male
- Job: Skilled
- Housing: Own
- Saving Account: Little
- Checking Account: Little
- Credit Amount: 2579
- Duration: 12

Output:

```
Predicted Credit Risk: Good
```

---

## Future Improvements

- Feature Engineering
- Probability Calibration
- Cross-validation with Stratified K-Fold
- Model Monitoring
- Docker Deployment
- Cloud Deployment (Render/Streamlit Community Cloud)
- Explainability Dashboard

---

## Author

**Ujjwal Mittal**

MA Economics  
Delhi School of Economics



---

## License

This project is licensed under the MIT License.
