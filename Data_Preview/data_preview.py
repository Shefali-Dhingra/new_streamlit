# General import section
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

def Heatmap(non_cat):
    """Generates a heatmap of the correlation between numeric variables

    :param non_cat: DataFrame with non-categorical columns (Quantity, Value, Weight)
    :type non_cat: pandas.DataFrame
    """
    fig = plt.figure(figsize=(15, 10))
    sns.heatmap(non_cat.corr(), annot=True, fmt='.2f').set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
    st.pyplot(fig)
    
def main(data_obj):
    """Data Preview main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    non_cat = data_obj.df[['Quantity', 'Value', 'Weight']]
    st.header("DATA INFORMATION")
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
        st.subheader("Correlation Heatmap")
        Heatmap(non_cat)
        
    with col4:
        st.subheader("Catagorical and Non-Categorical Variables")
        st.markdown("""
                1. **Index Variables:**  Transaction ID and Invoice Number
                2. **Nominal Variables:** Country,Product,Import Export, Category,Port,Shipping_Method,Supplier,Customer and Customs Code
                3. **Ordinal Variables:** Payment Terms
                4. **Non-Categorical Variables:** Quantity, Value and Weight
                """)

# Main
if __name__ == "__main__":
   main()
