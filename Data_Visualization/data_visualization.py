import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def top_countries_by_trade(data):
    trade_type = st.selectbox("Select Trade Type:", options=["Export", "Import"])
    filtered_data = data[data['Import_Export'] == trade_type]
    top_countries = filtered_data.groupby('Country')['Total_Value'].sum().nlargest(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_countries.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title(f'Top 10 Countries by {trade_type} Value', fontsize=14)
    ax.set_ylabel('Trade Value')
    ax.set_xlabel('Country')
    st.pyplot(fig)

# Plot 2: Top 10 Products by Trade - Bar Chart
def top_products_by_trade(data):
    top_export_prod = data[data['Import_Export'] == 'Export'].groupby('Product')['Total_Value'].sum().nlargest(10)
    top_import_prod = data[data['Import_Export'] == 'Import'].groupby('Product')['Total_Value'].sum().nlargest(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_export_prod.plot(kind='bar', color='orange', ax=ax, label='Exported Products', position=1, width=0.4)
    top_import_prod.plot(kind='bar', color='purple', ax=ax, label='Imported Products', position=0, width=0.4)
    ax.set_title('Top 10 Products by Trade (Export & Import)', fontsize=14)
    ax.set_ylabel('Trade Value')
    ax.legend()
    
    st.pyplot(fig)

# Plot 3: Yearly Trade Volume - Violin Plot
def yearly_trade_volume(data):
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Year'] = data['Date'].dt.year
    data = data.dropna(subset=['Year'])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='Year', y='Quantity', hue='Import_Export', data=data, split=True, ax=ax)
    ax.set_title('Yearly Trade Volume Distribution (2019-2024)', fontsize=14)
    ax.set_ylabel('Quantity')
    
    st.pyplot(fig)

# Plot 4: Shipping Costs vs Product Value - Scatter Plot
def shipping_vs_value(data, import_export):
    filtered_data = data[data['Import_Export'] == import_export]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=filtered_data, x='Total_Value', y='Weight', hue='Shipping_Method', ax=ax)
    ax.set_title(f'Shipping Costs vs Product Value ({import_export}s)', fontsize=14)
    ax.set_xlabel('Product Value')
    ax.set_ylabel('Weight (Shipping Cost Proxy)')
    
    st.pyplot(fig)

# Plot 5: Top 10 Global Suppliers by Wealth Generated - Histogram
def top_suppliers_by_exports(data):
    top_suppliers = data[data['Import_Export'] == 'Export'].groupby('Supplier')['Total_Value'].sum().nlargest(10)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    top_suppliers.plot(kind='hist', bins=5, color='green', ax=ax)
    ax.set_title('Top 10 Global Suppliers by Wealth Generated (Exports)', fontsize=14)
    ax.set_xlabel('Total Export Value')
    ax.set_ylabel('Frequency')
    
    st.pyplot(fig)

# Plot 6: Preferred Payment Methods by Countries - Pie Chart
def preferred_payment_methods(data, import_export):
    filtered_data = data[data['Import_Export'] == import_export]
    payment_methods = filtered_data['Payment_Terms'].value_counts().nlargest(5)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    payment_methods.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('Pastel1'), ax=ax)
    ax.set_title(f'Preferred Payment Methods for {import_export}s', fontsize=14)
    ax.set_ylabel('')
    
    st.pyplot(fig)

def main(data_obj):
    st.header("DATA VISUALIZATION")

    # Layout for the visualizations
    st.subheader("Top 10 Analytics Dashboard")
    
    col1, col2 = st.columns(2)
    
    # Plot 1: Top 10 Countries by Trade - Bar Plot with Slicer
    with col1:
        top_countries_by_trade(data_obj.df)
    
    # Plot 2: Top 10 Products by Trade - Bar Chart
    with col2:
        top_products_by_trade(data_obj.df)
    
    col3, col4 = st.columns(2)
    
    # Plot 3: Yearly Trade Volume - Violin Plot
    with col3:
        yearly_trade_volume(data_obj.df)
    
    # Plot 4: Shipping Costs vs Product Value - Scatter Plot (Imports)
    with col4:
        shipping_vs_value(data_obj.df, 'Import')

    col5, col6 = st.columns(2)

    # Plot 5: Top 10 Global Suppliers by Exports - Histogram
    with col5:
        top_suppliers_by_exports(data_obj.df)

    # Plot 6: Preferred Payment Methods - Pie Chart
    with col6:
        preferred_payment_methods(data_obj.df, 'Export')

# Main execution block
if __name__ == "__main__":
   main()
