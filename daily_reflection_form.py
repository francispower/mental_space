import streamlit as st
import pandas as pd
import numpy as np
import datetime

from background import PageBackground

def get_user_input():
    """Helper function to get inputs from the user in the form."""
    mood_score = st.slider("How was your mood today?", min_value=1, max_value=100, value=69, step=1)
    sleep_score = st.slider("How was your sleep last night?", min_value=1, max_value=100, value=69, step=1)
    category_feelings = st.multiselect("How are you feeling today?", options=["Happy", "Sad", "Angry", "Excited", "Bored", "Nervous", "Tired", "Hungover", "Stressed", "Relaxed"])
    good_feelings_text = st.text_input("What went well today?")
    could_be_better_text = st.text_input("What could have gone better today?")
    looking_forward = st.multiselect("What are you looking forward to tomorrow?", options=["Work", "Family", "Friends", "Food", "Exercise", "Sleep", "Hobbies", "Travel", "Learning", "Relaxation"])
    stress_triggers = st.text_input("Did anything stress you out today?")
    people_shoutout = st.multiselect("Did anyone make your day special today?", options=["Pia", "Mum", "Dad", "Ed", "Will", "Luke", "Lucy", "Jack W", "Amy", "Kyran", "Sara", "Alex", "Finlay", "Steve"])

    return {
        "Mood": mood_score,
        "Sleep": sleep_score,
        "Feelings": category_feelings,
        "Good": good_feelings_text,
        "Could Be Better": could_be_better_text,
        "Looking Forward": looking_forward,
        "Stress Triggers": stress_triggers,
        "People Shoutout": people_shoutout,
        "Date": datetime.date.today().strftime("%Y-%m-%d"),
    }


def save_to_csv(data):
    """Helper function to load, append and save data to a CSV file."""
    try:
        df = pd.read_csv("daily_reflection.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Date", "Mood", "Sleep", "Feelings", "Good", "Could Be Better", "Looking Forward", "Stress Triggers", "People Shoutout"])

    new_df = pd.DataFrame([data])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv("daily_reflection.csv", index=False)
    
    return df


def daily_reflection_form():
    # Background settings
    PageBackground.form_transparency()
    PageBackground.background("https://i.pinimg.com/1200x/5b/d2/d3/5bd2d3fdca8e9ec1f6f3ac4f4c518fd7.jpg")

    st.markdown("<h1 style='text-align: center;'>My mental space</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Reflect on your day below</p>", unsafe_allow_html=True)


    with st.form(key="daily_reflection_form"):

        data = get_user_input()

        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            # Save the data to a CSV file
            try:
                df = save_to_csv(data)
                st.success("Well done for taking the time to reflect on your day!")
            except Exception as e:
                st.error(f"An error occurred while saving your data: {e}")

    return df
        