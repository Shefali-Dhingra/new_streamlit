import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

def Heatmap(non_cat):
    """Generates a heatmap of the correlation between numeric variables

    :param non_cat: DataFrame with non-categorical columns (Quantity, Value, Weight)
    :type non_cat: pandas.DataFrame
    """
    fig = plt.figure(figsize=(14, 10))
    sns.heatmap(non_cat.corr(), annot=True, fmt='.2f').set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
    st.pyplot(fig)

def BarGraph(data, import_export):
    """Generates a bar graph of top 10 countries by Value

    :param data: DataFrame of the original dataset
    :type data: pandas.DataFrame
    :param import_export: Filter for either Import or Export
    :type import_export: str
    """
    filtered_data = data[data['Import_Export'] == import_export]
    top_countries = filtered_data.groupby('Country')['Value'].agg(['min', 'max']).reset_index()
    top_10_countries = top_countries.sort_values(by='max', ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    top_10_countries.set_index('Country')[['min', 'max']].plot(kind='bar', ax=ax)
    ax.set_title(f'Top 10 Countries by {import_export} Value', fontsize=14)
    ax.set_xlabel('Country')
    ax.set_ylabel('Value')
    st.pyplot(fig)

def main(data_obj):
    """Data Visualization main function

    :param data_obj: DataObject instance containing the dataframe
    :type data_obj: __main__.DataObject
    """
    # Create a subset of the dataframe with only numeric columns (Quantity, Value, Weight)
    non_cat = data_obj.df[['Quantity', 'Value', 'Weight']]

    st.header("DATA VISUALIZATION")

    # Layout for the two visualizations
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Correlation Heatmap")
        Heatmap(non_cat)

    with col2:
        st.subheader("Top 10 Countries by Value")
        # Slicer for Import or Export
        import_export = st.selectbox("Select Import or Export", options=['Import', 'Export'])
        BarGraph(data_obj.df, import_export)

# Main execution block
if __name__ == "__main__":
   main()
