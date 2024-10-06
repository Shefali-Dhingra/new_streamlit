# General import section
import streamlit as st #streamlit backend
import seaborn as sns #for plotting
import matplotlib.pyplot as plt #to configure plots
# Importing specific plots
# from Visualization.visualization import Heatmap

def Heatmap(data_obj):
    """Heatmap

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    fig = plt.figure(figsize=(16, 6))
    sns.heatmap(data_obj.df.corr(), vmin=-1, vmax=1, annot=True, fmt='.2%').set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
    return st.pyplot(fig)
    
def main(data_obj):
    """Data Visualization main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    st.header("DATA VISUALIZATION")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        st.subheader("Correlation Heatmap")
        Heatmap(data_obj)
        
    with col2:
        st.subheader("Dataframe description")
        st.dataframe(data_obj.df.describe())
    
    with col3:
        st.subheader("Data types")
        st.dataframe(data_obj.df.dtypes.astype(str))
        
    with col4:
        st.subheader("Dataframe description")
        st.dataframe(data_obj.df.describe())

    # # Correlation matrix
    # st.subheader("Correlation heatmap")
    # Heatmap(data_obj)

# Main
if __name__ == "__main__":
   main()
