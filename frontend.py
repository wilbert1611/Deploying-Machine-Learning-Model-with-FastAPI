import streamlit as st
import requests
import json

#URL backend API FastAPI yang sudah berjalan
backend_url = "http://127.0.0.1:8000/predict"

#Kategori hasil prediksi
categories = ['Insufficient_Weight', 'Normal_Weight', 'Overweight_Level_I', 'Overweight_Level_II', 
              'Obesity_Type_I', 'Obesity_Type_II', 'Obesity_Type_III']

#Membuat form input untuk menerima data dari pengguna
st.title('Obesity Prediction App')
st.markdown("## Dibuat oleh: Wilbert Suwanto - 2702369756")
st.markdown("""
    **Selamat datang di aplikasi prediksi obesitas!**  
    Masukkan data yang diperlukan di bawah ini untuk mengetahui prediksi apakah seseorang berisiko obesitas atau tidak.
""")
st.markdown("---") 

with st.form(key='obesity_form'):
    st.subheader('Masukkan Data Pengguna:')
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", min_value=0, max_value=100, value=25)
    Height = st.number_input("Height (in meters)", min_value=0.5, max_value=2.5, value=1.7)
    Weight = st.number_input("Weight (in kg)", min_value=30.0, max_value=200.0, value=70.0)
    family_history_with_overweight = st.selectbox("Family History with Overweight", ["yes", "no"])
    FAVC = st.selectbox("FAVC (Frequent Consumption of High-Calorie Food)", ["yes", "no"])
    FCVC = st.number_input("FCVC (Food Consumption Frequency)", min_value=1.0, max_value=3.0, value=2.0)
    NCP = st.number_input("NCP (Number of main meals per day)", min_value=1.0, max_value=5.0, value=3.0)
    CAEC = st.selectbox("CAEC (Consumption of Alcohol)", ["no", "Sometimes", "Frequently", "Always"])
    SMOKE = st.selectbox("SMOKE (Smoking)", ["yes", "no"])
    CH2O = st.number_input("CH2O (Water Consumption in liters)", min_value=1.0, max_value=5.0, value=2.0)
    SCC = st.selectbox("SCC (Sleep Condition)", ["yes", "no"])
    FAF = st.number_input("FAF (Physical Activity)", min_value=0.0, max_value=5.0, value=2.0)
    TUE = st.number_input("TUE (Time on exercise)", min_value=0.0, max_value=5.0, value=1.0, format="%.3f")
    CALC = st.selectbox("CALC (Consumption of Soft Drinks)", ["no", "Sometimes", "Frequently", "Always"])
    MTRANS = st.selectbox("MTRANS (Transportation Mode)", ["Public_Transportation", "Automobile", "Walking", "Motorbike", "Bike"])

    #Submit button
    submit_button = st.form_submit_button("Submit")

if submit_button:
    #Menyusun data input untuk dikirim ke backend API
    input_data = {
        "Gender": Gender,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": FAVC,
        "FCVC": FCVC,
        "NCP": NCP,
        "CAEC": CAEC,
        "SMOKE": SMOKE,
        "CH2O": CH2O,
        "SCC": SCC,
        "FAF": FAF,
        "TUE": TUE,
        "CALC": CALC,
        "MTRANS": MTRANS
    }

    response = requests.post(backend_url, json=input_data)

    if response.status_code == 200:
        prediction = response.json()["prediction"]

        #Mengonversi prediksi menjadi kategori yang lebih mudah dipahami
        predicted_category = categories[prediction]
        
        #Menampilkan hasil prediksi di frontend
        st.subheader("Hasil Prediksi")
        st.success(f"Prediksi Kategori: {predicted_category}")
