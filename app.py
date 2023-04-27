import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageEnhance
df=pd.read_csv(r"pub_clean.csv")


st.set_page_config(page_title="Pub App",
                   page_icon=":🍾:",
                   layout="centered")

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
    </style>pip
""", unsafe_allow_html=True)


st.title(":red[Pub App 🍾]")

st.markdown("<h5>This Application contains information about  pubs in the United Kingdom </h5>",unsafe_allow_html=True)

st.markdown("<h5>To find Nearest pubs go to page -- Find nearest pub</h5>",unsafe_allow_html=True)
st.markdown("<h5>To find the location of pubs go to page -- pub location</h5>",unsafe_allow_html=True)

