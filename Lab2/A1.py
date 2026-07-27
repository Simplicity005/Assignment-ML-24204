import pandas as pd
import numpy as np
df = pd.read_excel('Lab Session Data.xlsx',sheet_name='Purchase data')
df = df.iloc[:,[0,1,2,3,4]]

feature_matrix = ['Candies (#)', 'Mangoes (Kg)','Milk Packets (#)']
output_matrix = 'Payment (Rs)'
df_clean = df[feature_matrix + [output_matrix]].dropna()

rank = np.linalg.matrix_rank(feature_matrix)
print("Rank of feature matrix: ",rank)

X = df_clean[feature_matrix].to_numpy()
y = df_clean[output_matrix].to_numpy().reshape(-1, 1)


matrix_rank = np.linalg.matrix_rank(X)
print(f"Rank of the Feature Matrix (X): {matrix_rank}")

X_pinv = np.linalg.pinv(X)
c = np.dot(X_pinv, y)

print("\n--- Calculated Cost per Product ---")
print(f"Cost of 1 Candy: Rs. {c[0][0]:.2f}")
print(f"Cost of 1 Kg Mangoes: Rs. {c[1][0]:.2f}")
print(f"Cost of 1 Milk Packet: Rs. {c[2][0]:.2f}")
