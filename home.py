import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a pandas DataFrame
df = pd.read_csv('data/cars.csv')

# Display basic information about the dataset
print("Basic Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Display the first 10 rows and 7 columns
df_subset = df.iloc[:10, :7]
print("\nFirst 10 rows and 7 columns:")
print(df_subset)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows with missing data
df_cleaned = df.dropna()

# Remove duplicate rows if any
df_cleaned = df_cleaned.drop_duplicates()

# Check data types of all columns
print("\nData Types (Before Conversion):")
print(df_cleaned.dtypes)

# Verify data types
print("\nData Types:")
print(df_cleaned.dtypes)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df_cleaned.describe())

# Visualize the distribution of 'price'
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned['price'], bins=20, kde=True, color='blue')
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Scatter plot between 'year' and 'price'
plt.figure(figsize=(8, 5))
plt.scatter(df_cleaned['year'], df_cleaned['price'], color='green')
plt.title(' Year vs. Price')
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()

# Group data by 'brand' and calculate average price
avg_price_by_brand = df_cleaned.groupby('brand')['price'].mean().reset_index()
print("\nAverage Price by Brand:")
print(avg_price_by_brand)

# Create a new column calculating price per year of the vehicle
df_cleaned['price_per_year'] = df_cleaned['price'] / (2024 - df_cleaned['year'])
print("\nData with Price per Year Column:")
print(df_cleaned[['brand', 'year', 'price', 'price_per_year']].head(10))
