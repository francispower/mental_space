import streamlit as st
st.set_page_config(page_title="My mental space", page_icon="❤")

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from daily_reflection_form import daily_reflection_form


# Function to display the home page
def home():
    image = "https://i.pinimg.com/1200x/5b/d2/d3/5bd2d3fdca8e9ec1f6f3ac4f4c518fd7.jpg"

    # Background image for the entire app
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url("{image}");
                background-size: cover;
                background-position: center;
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>My mental space</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>A safe space for you to reflect, journal and learn more about yourself.</p>",
        unsafe_allow_html=True
    )




    


navigation = st.sidebar.selectbox("Choose page", options=["Home", "Daily Reflection"])

if navigation == "Home":
    home()
elif navigation == "Daily Reflection":
    daily_reflection_form()


