import streamlit as st
import requests

# Set your FastAPI endpoint
API_URL = "https://sea-turtle-app-ru5xo.ondigitalocean.app/predict"

st.title("Income Prediction App")
st.write("Predict whether an individual's income exceeds $50K based on their features.")

# Input fields for user data
age = st.number_input("Age", min_value=1, max_value=100, value=35)
workclass = st.selectbox("Workclass", ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", 
                                       "Local-gov", "State-gov", "Without-pay", "Never-worked"])
fnlwgt = st.number_input("FNLWGT", min_value=1, value=100000)
education = st.selectbox("Education Level", ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", 
                                             "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", 
                                             "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"])
educational_num = st.number_input("Years of Education", min_value=1, max_value=20, value=12)
marital_status = st.selectbox("Marital Status", ["Married", "Divorced", "Never-married", "Separated", "Widowed", 
                                                 "Married-spouse-absent", "Married-AF-spouse"])
occupation = st.selectbox("Occupation", ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial",
                                         "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical",
                                         "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv",
                                         "Armed-Forces"])
relationship = st.selectbox("Relationship", ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", 
                                             "Unmarried"])
race = st.selectbox("Race", ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"])
gender = st.selectbox("Gender", ["Male", "Female"])
capital_gain = st.number_input("Capital Gain", min_value=0, value=0)
capital_loss = st.number_input("Capital Loss", min_value=0, value=0)
hours_per_week = st.number_input("Hours Worked Per Week", min_value=1, max_value=100, value=40)
native_country = st.selectbox("Native Country", ["United-States", "Canada", "Mexico", "India", "Germany", 
                                                 "Philippines", "Other"])

# Prepare the feature dictionary
features = {
    "age": age,
    "workclass": workclass,
    "fnlwgt": fnlwgt,
    "education": education,
    "educational_num": educational_num,
    "marital_status": marital_status,
    "occupation": occupation,
    "relationship": relationship,
    "race": race,
    "gender": gender,
    "capital_gain": capital_gain,
    "capital_loss": capital_loss,
    "hours_per_week": hours_per_week,
    "native_country": native_country
}

if st.button("Predict"):
    # Make a request to the FastAPI endpoint
    response = requests.post(API_URL, json={"features": features})
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        st.error("Error occurred while making a prediction.")
