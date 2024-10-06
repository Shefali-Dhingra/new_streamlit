import streamlit as st
import os

def main():
    """Welcome main
    """    
    st.header("Welcome to Trend Analysis Dashboard!")
    st.warning("A Random Sample of 3001 entries is taken with random state 55043")
    st.info("""This Dashboard is Developed by Shefali Dhingra, a student of FORE School of Management PGDM-BDA""")
    st.subheader("Navigation")
    st.markdown("""
                1. **Data Preview:**  Gives a brief information about the Dataset
                2. **Data Visualization:** Shows various Visualization charts for the Dataset
                3. **Data Observations:** Provides the observations based on Visualization of the data
                4. **Managerial Insights:** Provides Managerial Insights for the Dataset based on Trade Trend Analysis
                """)
    
    st.subheader("Source code")
    st.markdown("It can be found via navigating to the menu in the top right corner and pressing 'View App Source'")
