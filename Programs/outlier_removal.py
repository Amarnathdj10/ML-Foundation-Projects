import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\Coding journey\ML Foundation projects\CSV files\AB_NYC_2019.csv')

upper = df['price'].quantile(0.99)
lower = df['price'].quantile(0.01)
df_no_outliers = df[df['minimum_nights']<upper]
df_no_outliers = df[(df['price'] >= lower) & (df['price'] <= upper)]

print("Original shape:", df.shape)
print("New shape:", df_no_outliers.shape)

print(df_no_outliers['price'].describe())