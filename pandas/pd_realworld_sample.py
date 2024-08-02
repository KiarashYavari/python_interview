# Analyzing Sales Data
# Imagine we have two CSV files containing sales data for a retail store.
# One file (sales.csv) contains information about 
# individual sales transactions, and another file (products.csv) 
# contains information about the products being sold.

# solution with pandas
# what is pandas: Pandas is an open-source data manipulation and 
# analysis library for Python. It provides data structures and 
# functions needed to work with structured data seamlessly and efficiently.
import pandas as pd

# Step 1: Reading CSV files into DataFrames
sales_df = pd.read_csv('sales.csv')
products_df = pd.read_csv('products.csv')
print("sales and products dataframes: ")
print(sales_df)
print(products_df)

# Step 2: Data Selection and Filtering
# Selecting specific columns
selected_columns_df = sales_df[['TransactionID', 'ProductID', 'Quantity']]

# Filtering data where Quantity > 1
filtered_df = sales_df[sales_df['Quantity'] > 1]
print("\n Data filtering where quantity is > 1")
print(filtered_df)

# Step 3: Adding a New Column
sales_df['Total'] = sales_df['Quantity'] * sales_df['Price']
print("\nAdding Total Column")
print(sales_df)

# Step 4: Grouping and Aggregating Data
grouped_df = sales_df.groupby('ProductID').agg({'Total': 'sum'})
print("\nTotal sale for a product: ")
print(grouped_df)

# Step 5: Handling Missing Data
# Introducing a missing value for demonstration
sales_df.loc[2, 'Price'] = None
print("\nStep 5: Handling Missing Data (Before)")
print(sales_df)
# Filling missing values with the mean price
sales_df['Price'].fillna(sales_df['Price'].mean(), inplace=True)
print("\nStep 5: Handling Missing Data (After)")
print(sales_df)

# Step 6: Merging DataFrames
merged_df = pd.merge(sales_df, products_df, on='ProductID')
print("\nStep 6: Merging DataFrames")
print(merged_df)

# Step 7: Pivot Table
pivot_table = merged_df.pivot_table(values='Total', index='ProductName', columns='Date', aggfunc='sum')
print("\nTotal sale of each product in each date: ")
print(pivot_table)

# Step 8: Saving DataFrame to a CSV file
pivot_table.to_csv('analized_sales_data.csv', index=True)
print("\nStep 8: Saving DataFrame to a CSV file")
print("Data saved to 'analized_sales_data.csv'")
