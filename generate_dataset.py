from itertools import product

import pandas as pd
import numpy as np

np.random.seed(42)

#Define number of users and products
num_users = 1000
num_products = 500

#Generate 10000+ ratings
rows = []
for _ in range(12000):
    user_id = np.random.randint(1, num_users + 1)
    product_id = np.random.randint(1, num_products + 1)
    rating = np.random.randint(1,6)     #Rating between 1 and 5
    rows.append((user_id, product_id, rating))

#Create data frame
df = pd.DataFrame(rows, columns = ['user_id', 'item_id', 'rating'])

#Remove Duplicates
df.drop_duplicates(subset = ['user_id', 'item_id'], keep = 'last', inplace = True)

#Save to CSV
df.to_csv("ecommerce_data.csv", index = False)
print("ecommerce_data.csv created with ", len(df), " rows")