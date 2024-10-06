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
                1. **Index Variables:**  You can have a look at your dataset in general and spot some correlations between the features
                2. **Data Preparation:** Drop and/or rename single/multiple columns, don't forget to submit changes
                3. **Smoothing and Filtering:** Use a multitude of tools to trim or adjust your data to increase its quality. Don't forget to save and finalize the results! Even if you didn't change anything :)
                4. **Classification:** You can perform several classification methods (e.g. Random Forest) and get results as visualization and datasheet.  
                5. **Regression:** Predict the next data points using Neural Networks, Random Forest and other algorithms
                """)
        

# Main
if __name__ == "__main__":
   main()
