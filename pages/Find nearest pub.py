import streamlit as st
import numpy as np
import pandas as pd

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

#Take input latitude and longitude from user
lat=st.number_input(label="Enter Latitude Here", min_value=49.892485, max_value=60.764969)

long=st.number_input(label="Enter Longitude Here", min_value=-7.384525, max_value=1.757763)

n_pubs = st.slider('Number of nearest pubs to display:', 1, 10, 5)

def pub():
    x=np.array(df['latitude'])
    y=np.array(df['longitude'])

    df['Distance']=np.sqrt((x-lat)**2+(y-long)**2)

    data=df.sort_values(by='Distance', ascending=True)[:n_pubs].reset_index()
    st.map(data[['latitude', 'longitude']])
    st.table(data[['name','address','local_authority']])
    
st.button("Pubs Near Me" ,on_click=pub)