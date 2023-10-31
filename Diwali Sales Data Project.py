#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


df = pd.read_csv(r'C:\Users\Prash\Downloads\Diwali Sales Data.csv',encoding= 'unicode_escape')
df


# In[6]:


# 2)	Find the no. of rows and columns in the dataset

df.shape


# In[7]:


# 3)	Print the first 5 rows of the said dataset.

df.head()


# In[8]:


# 4)	Print the basic information about the dataset

df.info()


# In[9]:


# 5)	Drop the irrelevant / blank columns in the dataset.

df.dropna(axis=1, how='all', inplace=True)
df


# In[10]:


# 6)	Check for null values in the column

pd.isnull(df).sum()


# In[11]:


# 7)	Drop the null values

df.dropna(inplace=True)
df


# In[12]:


# 8)	Change the data type of Amount from Float to Int

df['Amount'] = df['Amount'].astype(int)
df


# In[13]:


# 9)	Print the name of the columns

df.columns


# In[14]:


# 10)	Rename the column from Marital_Status to Shaadi

df = df.rename(columns = {'Marital_Status' : 'Shaadi'})
df


# In[15]:


# 11)	Find the statistical Analysis for Age, Order and Amount Column

df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# ## Gender

# In[16]:


# 12)	Represent no of Male & Female Customers using Bar Chart [ male & female customer count ]

import matplotlib.pyplot as plt

gender_counts = df['Gender'].value_counts()

# Create a bar chart
plt.bar(gender_counts.index, gender_counts.values)

# Add labels and title to the chart
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Number of Male and Female Customers')

# Display the chart
plt.show()


# In[17]:


# 13)	Find the total amount of purchase made by male and female customers  [ Gender wise amount purchased]

gender_amount = df.groupby('Gender')['Amount'].sum()

print(gender_amount)


# In[28]:


# 14)	Find the total amount of purchase made by male & female according to age group

gender_age_amount = df.groupby(['Gender', 'Age'])['Amount'].sum()

print(gender_age_amount)


# In[19]:


# 15)	Find the total amount of male and female count of the basis of gender

gender_count = df['Gender'].value_counts()

print(gender_count)


# In[20]:


# 16)	Perform a Chart wise analysis of  orders placed by different states


# Calculate the count of orders by state
state_orders = df['State'].value_counts()

# Create a bar chart to represent the orders by state
state_orders.plot(kind='bar')

# Add labels and title to the chart
plt.xlabel('State')
plt.ylabel('Number of Orders')
plt.title('Orders Placed by Different States')

# Adjust the layout for better visualization if needed
plt.tight_layout()

# Display the chart
plt.show()


# In[21]:


# 17)	Perform a Chart wise analysis of  amount purchased by  different states

# Group the data by 'State' and calculate the sum of 'Amount' for each state
state_amount = df.groupby(['State'],as_index = False)['Amount'].sum().sort_values(by = 'Amount',ascending = False).head(10)

# Create a bar chart to represent the amount purchased by state
state_amount.plot(kind='bar')

# Add labels and title to the chart
plt.xlabel('State')
plt.ylabel('Amount Purchased')
plt.title('Amount Purchased by Different States')

# Adjust the layout for better visualization if needed
plt.tight_layout()

# Display the chart
plt.show()


# In[22]:


# 18)	Perform a chart analysis to find the no of buyers [count ] according to marital status

# Calculate the count of buyers by marital status
marital_counts = df['Shaadi'].value_counts()

# Create a bar chart to represent the count of buyers by marital status
marital_counts.plot(kind='bar')

# Add labels and title to the chart
plt.xlabel('Marital Status')
plt.ylabel('Number of Buyers')
plt.title('Number of Buyers by Marital Status')

# Adjust the layout for better visualization if needed
plt.tight_layout()

# Display the chart
plt.show()


# In[23]:


# 19)	Perform a chart analysis to find the amount spent on purchase according to marital status


# Group the data by 'MaritalStatus' and calculate the sum of 'Amount' for each marital status
marital_amount = df.groupby('Shaadi')['Amount'].sum()


# Create a bar chart to represent the amount spent on purchases by marital status
marital_amount.plot(kind='bar')

# Add labels and title to the chart
plt.xlabel('Marital Status')
plt.ylabel('Amount Spent on Purchases')
plt.title('Amount Spent on Purchases by Marital Status')

# Adjust the layout for better visualization if needed
plt.tight_layout()

# Display the chart
plt.show()


# In[24]:


# 20)	Perform a chart analysis to find the max amount of purchase made by people on basis of occupation.

# Group the data by 'Occupation' and find the maximum purchase amount for each occupation
max_purchase = df.groupby('Occupation')['Amount'].max()

# Create a bar chart to represent the maximum purchase amount by occupation
max_purchase.plot(kind='bar')

# Add labels and title to the chart
plt.xlabel('Occupation')
plt.ylabel('Maximum Amount of Purchase')
plt.title('Maximum Amount of Purchase by Occupation')

# Adjust the layout for better visualization if needed
plt.tight_layout()

# Display the chart
plt.show()


# In[25]:


# 21)	Perform a chart analysis to show the amount of money spent of different category.

# Group the data by 'Category' and calculate the sum of 'Amount' for each category
category_amount = df.groupby('Product_Category')['Amount'].sum()

# Create a pie chart to represent the amount spent on different categories
category_amount.plot(kind='pie', autopct='%1.1f%%')

# Add a title to the chart
plt.title('Amount Spent on Different Categories')

# Adjust the layout for better visualization if needed
plt.tight_layout()

# Display the chart
plt.show()


# In[26]:


# 22)	Perform a chart analysis to show the amount of orders placed on each category

# Group the data by 'Category' and calculate the sum of 'Order' for each category
category_orders = df.groupby('Product_Category')['Orders'].sum()

# Create a bar chart to represent the amount of orders placed in each category
category_orders.plot(kind='bar')

# Add labels and title to the chart
plt.xlabel('Category')
plt.ylabel('Number of Orders')
plt.title('Number of Orders Placed in Each Category')

# Adjust the layout for better visualization if needed
plt.tight_layout()

# Display the chart
plt.show()


# In[27]:


# 23)	 Perform a chart analysis to show the top selling products.

# Group the data by 'Product' and calculate the sum of 'Quantity' for each product
product_sales = df.groupby('Product_Category')['Amount'].sum()

# Sort the products based on the quantity sold in descending order
top_selling_products = product_sales.sort_values(ascending=False).head(10)

# Create a bar chart to represent the top selling products
top_selling_products.plot(kind='bar')

# Add labels and title to the chart
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.title('Top Selling Products')

# Adjust the layout for better visualization if needed
plt.tight_layout()

# Display the chart
plt.show()


# # Conclusion:
# This EDA provides a comprehensive view of customer behavior, offering insights into how demographics, geography, and product categories influence sales during Diwali. Utilizing these insights can guide marketing strategies, inventory management, and product recommendations for future Diwali sales campaigns.
# 
# 
# 
# 
# 
