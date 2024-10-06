import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Plot 1: Top 10 Countries by Trade (Export and Import Value) - Pie Chart
def top_countries_by_trade(data,import_export):
    filtered_data = data[data['Import_Export'] == import_export]
    top_countries = filtered_data.groupby('Country')['Value'].agg(['min', 'max']).reset_index()
    top_10_countries = top_countries.sort_values(by='max', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_10_countries.set_index('Country')[['min', 'max']].plot(kind='bar', ax=ax)
    ax.set_title(f'Top 10 Countries by {import_export} Value', fontsize=14)
    ax.set_xlabel('Country')
    ax.set_ylabel('Value')
    st.pyplot(fig)

# Plot 2: Top 10 Products by Trade - Bar Chart
def top_products_by_trade(data,import_export):
    filtered_data = data[data['Import_Export'] == import_export]
    top_countries = filtered_data.groupby('Product')['Value'].agg(['min', 'max']).reset_index()
    top_10_countries = top_countries.sort_values(by='max', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_10_countries.set_index('Product')[['min', 'max']].plot(kind='bar', ax=ax)
    ax.set_title(f'Top 10 Countries by {import_export} Value', fontsize=14)
    ax.set_xlabel('Product')
    ax.set_ylabel('Value')
    st.pyplot(fig)

# Plot 3: Yearly Trade Volume - Violin Plot
def yearly_trade_volume(data):
    # Convert Date to datetime with error handling
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Year'] = data['Date'].dt.year
    
    # Remove rows where Year is NaN
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
    sns.scatterplot(data=filtered_data, x='Value', y='Weight', hue='Shipping_Method', ax=ax)
    ax.set_title(f'Shipping Costs vs Product Value ({import_export}s)', fontsize=14)
    ax.set_xlabel('Product Value')
    ax.set_ylabel('Weight (Shipping Cost Proxy)')
    
    st.pyplot(fig)

# Plot 5: Top 10 Global Suppliers by Wealth Generated - Histogram
def top_suppliers_by_exports(data):
    top_suppliers = data[data['Import_Export'] == 'Export'].groupby('Supplier')['Value'].sum().nlargest(10)
    
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
    col1, col2 = st.columns(2)
    
    with col1:
        import_export = st.selectbox("Select Import or Export", options=['Import', 'Export'])
        top_countries_by_trade(data_obj.df,import_export)

     with col2:
        import_export = st.selectbox("Select Import or Export", options=['Import', 'Export'])
        top_products_by_trade(data_obj.df,import_export)

# Main execution block
if __name__ == "__main__":
   main()
