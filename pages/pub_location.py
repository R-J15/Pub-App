import streamlit as st
import pandas as pd
from PIL import Image, ImageEnhance

df=pd.read_csv(r"pub_clean.csv")

st.markdown("""
    <style>
        body {
            background-image: url("https://media.istockphoto.com/id/538680408/photo/interior-of-pub.jpg?b=1&s=170667a&w=0&k=20&c=T3Rk0Y5LPaS__UnHJZgUzwgzl2wqXqOeqURSZ7sYyFE=");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

location_type = st.selectbox(
    "Select the location type:",
    ('Postal Code', 'Local Authority'))

if location_type == 'Postal Code':
    location = st.selectbox('Select the Postal Code:', df['postcode'].unique())
    pubs = df[df['postcode'] == location].reset_index()
else:
    location = st.selectbox('Select Local Authority:', df['local_authority'].unique())
    pubs = df[df['local_authority'] == location].reset_index()
st.write(f'We found {len(pubs)} pubs in {location}.')

st.table(pubs[['name','address']])

st.map(pubs[['latitude', 'longitude']])