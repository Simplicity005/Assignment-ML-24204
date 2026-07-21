import pandas as pd
import numpy as np


def average_Data(price_data):
    sum = 0
    for row in price_data:
        sum += row
    return float(sum/len(price_data))


def variance(price_data,mean):
    var = 0
    for row in price_data:
        var += ((row - mean)**2)/len(price_data)
    return var

df = pd.read_excel('Lab Session Data.xlsx',sheet_name='IRCTC Stock Price')
price_data = df['Price'].astype('float')
print(price_data)

print("Using numpy: ",np.average(price_data))
print("The result after using custom function :",average_Data(price_data))

print("Using numpy variance: ",np.var(price_data))
print("Using custom function for variance: ",variance(price_data,np.average(price_data)))

# Filter price data for wednesdays
row_indices = np.where(df['Day'] == 'Wed')
filtered_Days = df.iloc[row_indices]
filtered_Days = filtered_Days['Price']
print("Average for wed: ",np.average(filtered_Days))

