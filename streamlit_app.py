# General import section
import pandas as pd #to work with dataframes
import streamlit as st #streamlit backend
from io import StringIO #to read data files as .csv correctly
import os #to work with files

# Streamlit main page configuration
st.set_page_config(page_title="DEVP Dashboard",
                    page_icon=None,
                    layout="wide",
                    initial_sidebar_state="expanded",
                    menu_items=None)

# App import
import Welcome_Page
import Data_Preview

# Data object class
class DataObject():
    """
    Data object class holds a dataframe and its byte size.
    """


# Interface class        
class Interface():
    
    def side_bar(cls, dt_obj):
      """Sidebar configuration and file picker

      :param dt_obj: pandas dataframe object
      :type dt_obj: pandas.core.frame.DataFrame
      """
      dt_obj.data = pd.read_csv("Imports_Exports_Dataset.csv", sep=';', decimal=',', index_col = False)
      # Data Sampling
      dt_obj.df = pd.DataFrame.sample(dt_obj.data, n=3001, random_state=55043)
      dt_obj.filesize = dt_obj.df.size
      
        # Side bar navigation menu with a select box
      menu = ['Welcome Page','Data Preview']
      navigation = st.sidebar.selectbox(label="Select menu", options=menu)

        # Apps

        # Landing page
      if navigation == 'Welcome Page':
        with st.container():
         Welcome_Page.welcome()

        # Runs 'Data Preview' app
      if navigation == 'Data Preview':
        with st.container():
         Data_Preview.data_preview(dt_obj)

        # Runs 'Data Preparation' app
        # if navigation == 'Data Preparation':
        #   with st.container():
        #    Data_Preparation.data_prep(dt_obj)
      
      # Initial welcome page when there is no file selected
      else:
        Welcome_Page.welcome()
        
def main():
  """
  Main and its Streamlit configuration
  """

  # Creating an instance of the original dataframe data object                   
  data_main = DataObject()
  # Creating an instance of the main interface
  interface = Interface()
  interface.side_bar(data_main)


# Run Main
if __name__ == '__main__':
  main()
