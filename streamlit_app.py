# General import section
import pandas as pd #to work with dataframes
import streamlit as st #streamlit backend
from io import StringIO #to read data files as .csv correctly
import os #to work with files
import seaborn as sns #for plotting
import matplotlib.pyplot as plt #to configure plots

# Streamlit main page configuration
st.set_page_config(page_title="DEVP Dashboard",
                    page_icon=None,
                    layout="wide",
                    initial_sidebar_state="expanded",
                    menu_items=None)

# App import
import Welcome_Page
import Data_Preview
import Data_Visualization

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
      dt_obj.data = pd.read_csv("Imports_Exports_Dataset.csv")
      # Data Sampling
      dt_obj.df = pd.DataFrame.sample(dt_obj.data, n=3001, random_state=55043)
      dt_obj.filesize = dt_obj.df.size
      dt_obj.Non_Categorical_Variables=dt_obj.df.Quantity+dt_obj.df.Value+dt_obj.df.Weight
      def show_heat_map(dt_obj.df):
        st.title('Heat Map of Trade Data')
        
        # Compute correlation matrix
        corr = self.dt_obj.df.corr()
        
        # Display the correlation matrix using Seaborn heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
        
        # Show the plot in Streamlit
        st.pyplot(fig)
        # Side bar navigation menu with a select box
      menu = ['Welcome Page','Data Preview','Data Visualization']
      navigation = st.sidebar.selectbox(label="Select menu", options=menu)

        # Runs 'Data Preview' app
      if navigation == 'Data Preview':
        with st.container():
         Data_Preview.data_preview(dt_obj)

      elif navigation == 'Data Visualization':
        with st.container():
          show_heat_map(dt_obj.df)
          
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
