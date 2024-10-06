import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def top_countries_by_trade(data, trade_type):
    filtered_data = data[data['Import_Export'] == trade_type]
    top_countries = filtered_data.groupby('Country')['Total_Value'].sum().nlargest(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_countries.plot(kind='bar', color='#2977B7', ax=ax)
    ax.set_title(f'Top 10 Countries by {trade_type} Value', fontsize=14)
    ax.set_ylabel('Total Value of Trade')
    ax.set_xlabel('Country')
    st.pyplot(fig)

def top_products_by_trade(data, trade_type):
    filtered_data = data[data['Import_Export'] == trade_type]
    top_products = filtered_data.groupby('Product')['Total_Value'].sum().nlargest(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_products.plot(kind='bar', color='#EDA946', ax=ax)
    ax.set_title(f'Top 10 Products by {trade_type} Value', fontsize=14)
    ax.set_ylabel('Total Value of Trade')
    ax.set_xlabel('Products')
    st.pyplot(fig)

def yearly_trade_volume(data):
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Year'] = data['Date'].dt.year
    data = data.dropna(subset=['Year'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='Year', y='Quantity', hue='Import_Export', data=data, split=True, ax=ax)
    ax.set_title('Yearly Trade Volume Distribution (2019-2024)', fontsize=14)
    ax.set_ylabel('Quantity')
    st.pyplot(fig)

def shipping_vs_value(data, trade_type):
    filtered_data = data[data['Import_Export'] == trade_type]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=filtered_data, x='Total_Value', y='Weight', hue='Shipping_Method', ax=ax)
    ax.set_title(f'Shipping Costs vs Product Value', fontsize=14)
    ax.set_xlabel('Product Value')
    ax.set_ylabel('Weight (Shipping Cost Proxy)')
    st.pyplot(fig)

def top_suppliers_by_exports(data, trade_type):
    filtered_data = data[data['Import_Export'] == trade_type]
    if filtered_data.empty:
        st.warning(f"No data available for {trade_type}.")
        return
    
    top_suppliers = filtered_data.groupby('Supplier')['Total_Value'].sum().nlargest(10)
    if top_suppliers.empty:
        st.warning(f"No suppliers found for {trade_type}.")
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    top_suppliers.plot(kind='bar', color='#ADD8E6', ax=ax) 
    ax.set_title(f'Top 10 Global Suppliers by {trade_type} Wealth', fontsize=14)
    ax.set_ylabel('Total Value of Trade')
    ax.set_xlabel('Supplier')
    st.pyplot(fig)

def preferred_payment_methods(data, trade_type):
    filtered_data = data[data['Import_Export'] == trade_type]
    payment_methods = filtered_data['Payment_Terms'].value_counts().nlargest(5)
    fig, ax = plt.subplots(figsize=(6, 6))
    payment_methods.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('Pastel1'), ax=ax)
    ax.set_title(f'Preferred Payment Methods for {trade_type}', fontsize=14)
    ax.set_ylabel('')
    st.pyplot(fig)

def main(data_obj):
    st.header("DATA VISUALIZATION")
    st.subheader("Top 10 Analytics Dashboard")
    trade_type = st.selectbox("Select Trade Type:", options=["Export", "Import"])
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    
    with col1:
        top_countries_by_trade(data_obj.df, trade_type)
    with col2:
        top_products_by_trade(data_obj.df, trade_type)
    with col3:
        yearly_trade_volume(data_obj.df)
    with col4:
        shipping_vs_value(data_obj.df, trade_type)
    with col5:
        top_suppliers_by_exports(data_obj.df, trade_type)
    with col6:
        preferred_payment_methods(data_obj.df, trade_type)

# Main execution block
if __name__ == "__main__":
   main()
