# python-project

In this project, we analyze a dataset containing information about various cars, focusing on attributes such as brand, year, price, and other relevant features. The goal was to clean, manipulate, and explore the dataset to derive insights, supported by visualizations. This report summarizes the data analysis process and key findings.

# Data loading
The dataset was loaded using pandas and basic information was extracted.

# Summary of Dataset

Columns: Brand, Model, Year, Price, Transmission, Fuel Type, Mileage, etc.
Data Types: Mix of numerical and categorical features


 # Data Cleaning
 
Handling Missing Data:
Some rows had missing values.
I decided to drop rows with missing data to ensure clean analysis.

Duplicate Removal:
I found and removed 5 duplicate rows.

Data Type Conversion:
Ensured that the year column is an integer, and the price column is a float.

 # Data Exploration
Descriptive Statistics:

The average car price is $20,000.
Cars from 2020 and later have a higher average price than older models.
Brands like BMW and Audi tend to have higher average price

# Data Visualization
 Distribution of Car Prices
The histogram  shows the price distribution.
Most cars are priced between $15,000 and $25,000.

# Scatter Plot
Observed a positive correlation between newer models and higher prices.
