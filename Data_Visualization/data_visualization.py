# General import section
import streamlit as st #streamlit backend
import seaborn as sns #for plotting
import matplotlib.pyplot as plt #to configure plots


def Heatmap(non_cat):
    """Heatmap

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    fig = plt.figure(figsize=(16, 6))
    sns.heatmap(non_cat.corr(), annot=True, fmt='.2%').set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
    st.pyplot(fig)
    
def main(data_obj):
    """Data Visualization main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    non_cat = data_obj.df.Quantity+data_obj.df.Value+data_obj.df.Weight
    st.header("DATA VISUALIZATION")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        st.subheader("Correlation heatmap")
        Heatmap(non_cat)
        
    with col2:
        st.subheader("Dataframe description")
        st.dataframe(data_obj.df.describe())
    
    with col3:
        st.subheader("Data types")
        st.dataframe(data_obj.df.dtypes.astype(str))
        
    with col4:
        st.subheader("Correlation heatmap")
        

# Main
if __name__ == "__main__":
   main()
