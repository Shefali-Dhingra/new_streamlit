import streamlit as st
import os

def main():
    """Observations main
    """    
    st.header("OBSERVATIONS")
    st.markdown("""
    1. **Non-Categorical Variables Analysis**
    - Symmetry: Both Quantity and Value show a relatively symmetric distribution, with their mean and median being close.
    - Variability: There is considerable variability in all three variables, as indicated by the standard deviations and the range between minimum and maximum values.
    - Skewness: Given that the minimum values are much lower and the maximum values are quite high, these variables could be slightly positively skewed, with a few higher values pulling the mean above the median.
    - Mode values are lower than the mean and median for Value and Weight, which could indicate some common small transactions.
    - Range values confirm that the data has a very wide spread, indicating diverse transaction sizes.
    - Symmetry: All three variables have very low skewness, indicating their distributions are quite symmetric.
    - Flat Distributions: The negative kurtosis values for all three variables suggest that the distributions are flatter than normal, with fewer outliers.
    - Moderate Relative Variability: All Non-Categorical variables exhibit a moderate degree of relative variability, with CV values above 55%. This indicates that while there is variation in the data, it’s not extreme.
    - Confidence in the Mean: The narrow confidence intervals suggest that, despite the variability, the estimates for the mean of each variable are fairly precise.
    - Weight's Higher Variability: While the confidence interval for weight is wider than those for quantity and value, the overall variability in weight reflects that the traded goods may have a more diverse range of weights compared to their quantities or values.
    - The variables are largely independent, with no evidence of strong direct causal relationships based on the correlation matrix.

    2. **Trade Trend Analysis**
    - Top Importing Countries: Jamaica, Congo and New Zealand are top importing Countries based on value of Imports.
    - Top Exporting Countries: Madagascar, Kiribati and Bangladesh are among the countries exporting the highest value of goods.
    - Top Exported Products: Bad, Church and Site are the top exported products
    - Top Imported Products: Clear, Change and Value were the top imported products.
    - 2020 was the year with the maximum imported products, and 2022 had the maximum exported products. 
    - Both Imports and Exports were lowest in 2019. One probable cause could be COVID-19.
    - August 2018 was the month with the highest volume of imports.
    - Highest Valued Goods Imported in Countries: Jamaica, Congo and New Zealand
    - Highest Valued Goods Exported from Countries: Madagascar, Kiribati and Bangladesh
    - Top Suppliers: Johnson PLC and Smith PLC are the leading suppliers, contributing the most in terms of total value of exported goods.
    - Trade Balance: A positive trade balance was observed for countries that export more than they import, and vice versa for countries with a negative trade balance.
    - Average Trade Value per Transaction was $5030.32
    - Preferred Payment Terms (Imports): All Payment Methods have similar Ratios indicating that each Payment Method is equally preffered
    - Preferred Payment Terms (Exports): All Payment Methods have similar Ratios indicating that each Payment Method is equally preffered
    - Shipping Cost: The weight (shipping cost proxy) is quite spread out, with values ranging from 0 to 5000, but there is a slight increase in density around certain weight levels like 2000 to 4000.
    - Lack of Correlation: There doesn't seem to be a strong correlation between product value and shipping cost proxy. Higher product value doesn’t consistently align with higher shipping costs.
                """)
