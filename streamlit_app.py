import streamlit as st
#st.set_page_config(page_title="My mental space", page_icon="❤", layout="wide")

import pandas as pd
import numpy as np
import datetime
import html
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

    # Custom CSS for frosted glass effect
    custom_css = """
    <style>
        .tile-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 50px;
            flex-wrap: wrap;
            row-gap: 20px;
            width: 100%;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }

        .tile {
            width: 350px;
            height: 200px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            color: black;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
            text-decoration: none;
            position: relative;
            padding-bottom: 140px;
            margin-bottom: 20px;
        }

        .tile:hover {
            transform: scale(1.05);
            box-shadow: 0px 0px 15px rgba(255, 165, 0, 0.6);
        }
    </style>
    """

    st.markdown(custom_css, unsafe_allow_html=True)


    pages = [
        {"title": "Mood"},
        {"title": "People gratitude"},
        {"title": "Sleep"},
        {"title": "Stress triggers"},
    ]

    tile_html = "<div class='tile-container'>"

    for page in pages:
        safe_title = html.escape(page['title'])
        tile_html += f"<div class='tile'>{safe_title}</div>"

    tile_html += "</div>"

    st.markdown(tile_html, unsafe_allow_html=True)


navigation = st.sidebar.selectbox("Choose page", options=["Home", "Daily Reflection"])

if navigation == "Home":
    home()
elif navigation == "Daily Reflection":
    daily_reflection_form()


