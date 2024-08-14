import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Books.csv'

data = pd.read_csv(file_path)

print(data['Price'].describe(), end='\n\n')
print(data['Availability'].value_counts(), end='\n\n')
print(data['Rating'].value_counts())


# Set a style for the plots
sns.set(style='whitegrid')

# Plotting price distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Price'], bins=20)
plt.title('Price Distribution of Books')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.show()

# Creating scatter plot for rating and price
rating_mapping = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
data['Rating'] = data['Rating'].map(rating_mapping)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Rating', y='Price')
plt.title('Rating vs. Price of Books')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.show()

