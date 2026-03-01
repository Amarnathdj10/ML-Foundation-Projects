import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

df = pd.read_csv(r'D:\Coding journey\ML Foundation projects\CSV files\bhp.csv')
print(df.describe())

upper = df.price_per_sqft.quantile(0.999)
lower = df.price_per_sqft.quantile(0.001)
df1 = df[(df['price_per_sqft']>lower) & (df['price_per_sqft']<upper)]
print(df.shape)
print(df1.shape)

upper_limit = df1.price_per_sqft.mean() + 4*df1.price_per_sqft.std()
lower_limit = df1.price_per_sqft.mean() - 4*df1.price_per_sqft.std()

df2 = df1[(df['price_per_sqft']>lower_limit) & (df['price_per_sqft']<upper_limit)]
print(df2.shape)

plt.hist(df2.price_per_sqft, bins=20, rwidth=0.8, density=True)
plt.xlabel('Price per sqft')
plt.ylabel('Density')
rng = np.arange(df2.price_per_sqft.min(), df2.price_per_sqft.max(), 0.1)
plt.plot(rng, norm.pdf(rng, df2.price_per_sqft.mean(),df2.price_per_sqft.std()))
plt.show()

df2['z_score'] = (df2.price_per_sqft-df2.price_per_sqft.mean())//df2.price_per_sqft.std()
df2 = df2[(df2.z_score>-4) & (df2.z_score<4)]

print(df2.shape)