import streamlit as st
import os

def main():
    """Observations main
    """    
    st.header("OBSERVATIONS")
    st.subheader("Non-Categorical Variables Analysis")
    
    st.markdown("""
    - Symmetry: Both Quantity and Value show a relatively symmetric distribution, with their mean and median being close.
    - Variability: There is considerable variability in all three variables, as indicated by the standard deviations and the range between minimum and maximum values.
    - Skewness: Given that the minimum values are much lower and the maximum values are quite high, these variables could be slightly positively skewed, with a few higher values pulling the mean above the median.
    - Mode values are lower than the mean and median for Value and Weight, which could indicate some common small transactions.
    - Range values confirm that the data has a very wide spread, indicating diverse transaction sizes.
    - Symmetry: All three variables have very low skewness, indicating their distributions are quite symmetric.
    - Flat Distributions: The negative kurtosis values for all three variables suggest that the distributions are flatter than normal, with fewer outliers.
    - Moderate Relative Variability: All Non-Categorical variables exhibit a moderate degree of relative variability, with CV values **above 55%**. This indicates that while there is variation in the data, it’s not extreme.
    - Confidence in the Mean: The narrow confidence intervals suggest that, despite the variability, the estimates for the mean of each variable are fairly precise.
    - Weight's Higher Variability: While the confidence interval for weight is wider than those for quantity and value, the overall variability in weight reflects that the traded goods may have a more diverse range of weights compared to their quantities or values.
    - The variables are largely independent, with no evidence of strong direct causal relationships based on the correlation matrix.

    """)
    
   st.subheader("Trade Trend Analysis")

   st.markdown("""
    - Top Importing Countries: Jamaica, Congo and New Zealand are top importing Countries
    - Top Exporting Countries: India, Congo, and Maldives are among the countries exporting the highest value of goods.
    - Top Exported Products: Onto, Now, and Mr are the top exported products. Although Onto generates the most wealth for its suppliers, Now is not among the top 10 wealth-generating products for the country, and Mr is ranked 8th.
    - Top Imported Products: Explain, Strong, and Focus were the top imported products.
    - 2021 was the year with the maximum imported products, and 2019 had the minimum exported products. One probable cause could be COVID-19.
    - August 2018 was the month with the highest volume of imports.
    - Highest Valued Goods Imported in Countries: Bahrain, Brazil, and Belarus.
    - Highest Valued Goods Exported from Countries: India, Congo, and Maldives.
    - Top Suppliers: Wright Group and Brown PLC are the leading suppliers, contributing the most in terms of total value of exported goods.
    - Trade Balance: A positive trade balance was observed for countries that export more than they import, and vice versa for countries with a negative trade balance. Bahrain has the largest trade balance gap, indicating a focus on exports.
    - Average Trade Value per Transaction was **$5057.81**.
    - Maximum Average value per product is for the product **need**
    - Preferred Payment Terms: Cash on Delivery is the most preferred payment term in Bahrain, while countries like India favor Net 30 terms.
    - Time Between Orders: The average time between orders is approximately 1.85 days for exports and 1.80 days for imports, indicating similar purchasing patterns.
    
                """)
