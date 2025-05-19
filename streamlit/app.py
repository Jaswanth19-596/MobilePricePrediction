import streamlit as st
import pandas as pd
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), 'price_prediction_pipeline.pkl')
pipeline = joblib.load(model_path)
X_train = pd.read_csv('./../data/processed/X_train.csv')

st.title("Mobile Price Prediction")




brand = st.selectbox("Select Brand", X_train['Brand'].unique())

max_resolution = st.selectbox('Select Camera Resolution', X_train['max_resolution'].unique())

selfie_camera_quality = st.selectbox("Selfie Camera Quality", X_train['selfiecamera_mp'].unique())

main_camera_quality = st.selectbox("Main Camera Quality", X_train['maincamera_mp'].unique())



battery_capacity = st.slider('Select Battery Capacity', 1, int(X_train['Battery_Capacity'].max()))


wifi_version = st.selectbox('Select Wifi Version', [1, 2, 3, 4, 5])

ram = st.selectbox("Select RAM", X_train['ram'].unique())

operating_system = st.selectbox("Select OS" ,  X_train['operating_system'].unique())



gpu_company = st.selectbox("Select GPU", X_train['GPU_company'].unique())

cpu_company = st.selectbox("Select CPU", X_train['CPU_Brand'].unique())

cpu_transistor_size = st.selectbox("Select Transistor Size", X_train['CPU_Transistor_Size'].unique())


submit_button = st.button('Submit')


if submit_button:

    df = {'Brand' : [brand],
        'max_resolution' : [max_resolution],
        'selfiecamera_mp' : [selfie_camera_quality],
        'maincamera_mp' : [main_camera_quality],
        'Battery_Capacity' : [battery_capacity],
        'latest_wifi_version' : [wifi_version],
        'ram' : [ram],
        'operating_system' : [operating_system],
        'CPU_Brand' : [cpu_company],
        'GPU_company' : [gpu_company],
        'CPU_Transistor_Size' : [cpu_transistor_size],
        }

    df = pd.DataFrame(df)

    res = pipeline.predict(df)

    # Creating a range using the Root Mean squared error.
    st.write(f'The Price of the Phone can be between {int(res[0] - 50)}  - {int(res[0] + 50)}')
    