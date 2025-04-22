import streamlit as st
import pandas as pd
import numpy as np

class PageBackground:
# Function to display the home page
    def background(image):

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

    def form_transparency():
        st.markdown(
            """
            <style>
                div.stForm {
                    background-color: rgba(255, 255, 255, 0.4);
                    border-radius: 10px;
                    padding: 20px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )