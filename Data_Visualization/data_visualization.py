import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Plot 1: Top 10 Countries by Trade (Export and Import Value)
def top_countries_by_trade(data):
    top_export = data[data['Import_Export'] == 'Export'].groupby('Country')['Value'].sum().nlargest(10)
    top_import = data[data['Import_Export'] == 'Import'].groupby('Country')['Value'].sum().nlargest(10)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    top_export.plot(kind='bar', color='green', ax=ax, label='Export', position=1, width=0.4)
    top_import.plot(kind='bar', color='blue', ax=ax, label='Import', position=0, width=0.4)
    ax.set_title('Top 10 Countries by Trade (Export & Import)', fontsize=14)
    ax.set_ylabel('Total Trade Value')
    ax.legend()
    
    st.pyplot(fig)

# Plot 2: Top 10 Products by Trade (Separate for Export and Import)
def top_products_by_trade(data):
    top_export_prod = data[data['Import_Export'] == 'Export'].groupby('Product')['Value'].sum().nlargest(10)
    top_import_prod = data[data['Import_Export'] == 'Import'].groupby('Product')['Value'].sum().nlargest(10)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    top_export_prod.plot(kind='bar', color='orange', ax=ax, label='Exported Products', position=1, width=0.4)
    top_import_prod.plot(kind='bar', color='purple', ax=ax, label='Imported Products', position=0, width=0.4)
    ax.set_title('Top 10 Products by Trade (Export & Import)', fontsize=14)
    ax.set_ylabel('Total Trade Value')
    ax.legend()
    
    st.pyplot(fig)

# Plot 3: Yearly Trade Volume (2019-2024)
def yearly_trade_volume(data):
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    yearly_export = data[data['Import_Export'] == 'Export'].groupby('Year')['Quantity'].sum()
    yearly_import = data[data['Import_Export'] == 'Import'].groupby('Year')['Quantity'].sum()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    yearly_export.sort_values(ascending=False).plot(kind='bar', color='green', ax=ax, label='Export Volume')
    yearly_import.sort_values(ascending=False).plot(kind='bar', color='blue', ax=ax, label='Import Volume', alpha=0.6)
    ax.set_title('Yearly Trade Volume (Exports & Imports, 2019–2024)', fontsize=14)
    ax.set_ylabel('Total Volume')
    ax.legend()
    
    st.pyplot(fig)

# Plot 4: Shipping Costs vs Product Value (Separate for Imports and Exports)
def shipping_vs_value(data, import_export):
    filtered_data = data[data['Import_Export'] == import_export]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=filtered_data, x='Value', y='Weight', hue='Shipping_Method', ax=ax)
    ax.set_title(f'Shipping Costs vs Product Value ({import_export}s)', fontsize=14)
    ax.set_xlabel('Product Value')
    ax.set_ylabel('Weight (Shipping Cost Proxy)')
    
    st.pyplot(fig)

# Plot 5: Top 10 Global Suppliers by Wealth Generated (Exports)
def top_suppliers_by_exports(data):
    top_suppliers = data[data['Import_Export'] == 'Export'].groupby('Supplier')['Value'].sum().nlargest(10)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    top_suppliers.plot(kind='bar', color='green', ax=ax)
    ax.set_title('Top 10 Global Suppliers by Wealth Generated (Exports)', fontsize=14)
    ax.set_ylabel('Total Export Value')
    
    st.pyplot(fig)

# Plot 6: Most Preferred Payment Methods by Countries
def preferred_payment_methods(data, import_export):
    filtered_data = data[data['Import_Export'] == import_export]
    payment_methods = filtered_data['Payment_Terms'].value_counts().nlargest(5)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    payment_methods.plot(kind='bar', color='brown', ax=ax)
    ax.set_title(f'Preferred Payment Methods for {import_export}s', fontsize=14)
    ax.set_ylabel('Count of Transactions')
    
    st.pyplot(fig)

def main(data_obj):
    st.header("DATA VISUALIZATION")

    # Layout for the visualizations
    st.subheader("Top 10 Analytics Dashboard")

    # Plot 1: Top 10 Countries by Trade
    top_countries_by_trade(data_obj.df)

    # Plot 2: Top 10 Products by Trade
    top_products_by_trade(data_obj.df)

    # Plot 3: Yearly Trade Volume (2019–2024)
    yearly_trade_volume(data_obj.df)

    # Plot 4: Shipping Costs vs Product Value (Imports)
    shipping_vs_value(data_obj.df, 'Import')

    # Plot 5: Top 10 Global Suppliers by Exports
    top_suppliers_by_exports(data_obj.df)

    # Plot 6: Preferred Payment Methods for Exports
    preferred_payment_methods(data_obj.df, 'Export')

# Main execution block
if __name__ == "__main__":
   main()
