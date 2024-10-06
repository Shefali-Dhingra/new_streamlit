# General import section
import streamlit as st #streamlit backend
import seaborn as sns #for plotting
import matplotlib.pyplot as plt #to configure plots

def Heatmap(data_obj):
    """Heatmap

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    fig = plt.figure(figsize=(16, 6))
    sns.heatmap(data_obj.df.corr(), vmin=-1, vmax=1, annot=True, fmt='.2%').set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
    return st.pyplot(fig)
    
    # height=300
    return heatmap
    
def main(data_obj):
    """Data Visualization main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    st.header("DATA VISUALIZATION")

    # Correlation matrix
    st.subheader("Correlation heatmap")
    Heatmap(data_obj)

# Main
if __name__ == "__main__":
   main()
