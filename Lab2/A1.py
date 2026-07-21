import pandas as pd
import numpy as np
df = pd.read_excel('Lab Session Data.xlsx',sheet_name='Purchase data')
df = df.iloc[:,[0,1,2,3,4]]

feature_matrix = df[['Candies (#)', 'Mangoes (Kg)','Milk Packets (#)']]

output_matrix = df[['Payment (Rs)']]

rank = np.linalg.matrix_rank(feature_matrix)
print("Rank of feature matrix: ",rank)

pseudo_inv = np.linalg.pinv(output_matrix)
print("Psuedo inverse of the cost matrix: ",pseudo_inv)