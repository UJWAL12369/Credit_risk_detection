import streamlit as st
import pandas as pd
import joblib

model=joblib.load("extra_tress_credit_model.pkl")


encoders={col:joblib.load(f"{col}_encoder.pkl") for col in ["Sex","Housing","Saving accounts","Checking account"]}


st.title("Credit risk prediction app")
st.write("enter applicant information to predict if the credit risk is good or bad")


age=st.number_input("age",min_value=18,max_value=80,value=30)
sex=st.selectbox("sex",["male","female"])
job=st.number_input("job (0-3)",min_value=0,max_value=3,value=1)
housing=st.selectbox("housing",["own","rent","free"])
saving_accounts=st.selectbox("saving accounts",["little","moderate","rich","quite rich"])
checking_account=st.selectbox("checking accounts",["little","moderate","rich"])
credit_amount=st.number_input("credit amount",min_value=0,value=100)
duration=st.number_input("duration",min_value=1,value=12)


input_df = pd.DataFrame({
    'Age': [age],
    'Sex': [encoders['Sex'].transform([sex])[0]],
    'Job': [job],
    'Housing': [encoders['Housing'].transform([housing])[0]],
    'Saving accounts': [encoders['Saving accounts'].transform([saving_accounts])[0]],
    'Checking account': [encoders['Checking account'].transform([checking_account])[0]],
    'Credit amount': [credit_amount],
    'Duration': [duration]
})


if st.button("predict risk"):
    pred=model.predict(input_df)[0]


    if pred==1:
        st.success("the predicted credit risk is **good**")
    else:
        st.error("the predict risk is **bad**")

    


                       
                             
          