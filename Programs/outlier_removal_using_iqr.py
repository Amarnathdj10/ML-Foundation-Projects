import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\Coding journey\ML Foundation projects\CSV files\weight-height.csv')

plt.hist(df.Height,bins=20)
plt.xlabel('Height')
plt.ylabel('Count')
plt.show()
plt.hist(df.Weight,bins=20)
plt.xlabel('Weight')
plt.ylabel('Count')
plt.show()

q1h = df.Height.quantile(0.25)
q3h = df.Height.quantile(0.75)

iqrh = q3h-q1h

lower_limit_h = q1h-1.5*iqrh
upper_limit_h = q3h+1.5*iqrh

print(df.shape)
df = df[(df.Height>lower_limit_h) & (df.Height<upper_limit_h)]
print(df.shape)

q1w = df.Weight.quantile(0.25)
q3w = df.Weight.quantile(0.75)

iqrw = q3w-q1w

lower_limit_w = q1w-1.5*iqrw
upper_limit_w = q3w+1.5*iqrw

df = df[(df.Weight>lower_limit_w) & (df.Weight<upper_limit_w)]
print(df.shape)
