import streamlit as st
#st.set_page_config(page_title="My mental space", page_icon="❤", layout="wide")

import pandas as pd
import numpy as np
import datetime
import html
import matplotlib.pyplot as plt
from daily_reflection_form import save_to_csv


def mood_graph(title, x, y):
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(x, y, marker='o', linestyle='-', color='orange')
    ax.set_title(title)
    plt.xticks(rotation=45)
    return fig

def load_data():
    """Load the daily reflection data from CSV file."""
    try:
        df = pd.read_csv("daily_reflection.csv")
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Mood", "Sleep", "Feelings", "Good", "Could Be Better", "Looking Forward", "Stress Triggers", "People Shoutout"])


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


    cols = st.columns(1)

    df = load_data()

    if not df.empty:
        with cols[0]:
            st.markdown("<h2 style='text-align: center;'>Mood over time</h2>", unsafe_allow_html=True)

            try:
                df['Date'] = pd.to_datetime(df['Date'])
                df.sort_values('Date', inplace=True)
                fig = mood_graph("Mood Over Time", df['Date'], df['Mood'])
                st.pyplot(fig)
            except FileNotFoundError:
                st.warning("No data available yet. Please fill out the daily reflection form.")
    else:
        with cols[0]:
            st.warning("Please fill out the daily reflection form to see your mood over time.")


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


