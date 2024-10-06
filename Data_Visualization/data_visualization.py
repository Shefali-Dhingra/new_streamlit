# General import section
import streamlit as st #streamlit backend
from visualization import Heatmap
def main(data_obj):
    """Data Visualization main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    st.header("DATA VISUALIZATION")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        st.subheader("Dataframe Head and Shape")
        st.dataframe(data_obj.df.head(10))
        st.write(data_obj.df.shape)
        
    with col2:
        st.subheader("Dataframe description")
        st.dataframe(data_obj.df.describe())
    
    with col3:
        st.subheader("Data types")
        st.dataframe(data_obj.df.dtypes.astype(str))
        
    with col4:
        st.subheader("Correlation heatmap")
        Heatmap(data_obj)

# Main
if __name__ == "__main__":
   main()
