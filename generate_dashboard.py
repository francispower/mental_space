import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt


def generate_dashboard():
    st.title("Daily Reflection Dashboard")
    st.write("This is the dashboard page.")

    try:
        df = pd.read_csv("daily_reflection.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.write("No data available yet. Please submit your daily reflections first.")

    plt.plot(df["Date"], df["Feelings"])
    plt.xlabel("Date")
    plt.ylabel("Feelings")
    plt.title("Feelings Over Time")
    st.pyplot(plt)