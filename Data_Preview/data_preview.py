# General import section
import streamlit as st #streamlit backend

def main(data_obj):
    """Data Preview main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
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
        st.subheader("Data types")
        st.dataframe(data_obj.df.dtypes.astype(str))
        
    with col4:
        st.subheader("Data Info")
        st.markdown("""
                1. **Index Variables:**  Transaction ID and Invoice Number
                2. **Nominal Variables:** Country,Product,Import Export, Category,Port,Shipping_Method,Supplier,Customer and Customs Code
                3. **Ordinal Variables:** Payment Terms
                4. **Non-Categorical Variables:** Quantity, Value and Weight
                """)

# Main
if __name__ == "__main__":
   main()
