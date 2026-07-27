import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")

price_data = df.iloc[:, 3].values


def calculate_mean(data):
    total = 0.0
    for x in data:
        total += x
    return total / len(data)


def calculate_variance(data):
    mean_val = calculate_mean(data)
    total_sq_diff = 0.0
    for x in data:
        total_sq_diff += (x - mean_val) ** 2
    return total_sq_diff / len(data) 



builtin_mean = np.mean(price_data)
builtin_var = np.var(price_data)


custom_mean = calculate_mean(price_data)
custom_var = calculate_variance(price_data)

print("--- Accuracy Comparison ---")
print(f"Built-in Mean: {builtin_mean} | Custom Mean: {custom_mean}")
print(f"Built-in Variance: {builtin_var} | Custom Variance: {custom_var}")


def measure_time(func, data, runs=10):
    start = time.perf_counter()
    for _ in range(runs):
        func(data)
    end = time.perf_counter()
    return (end - start) / runs


builtin_mean_time = measure_time(np.mean, price_data)
custom_mean_time = measure_time(calculate_mean, price_data)

builtin_var_time = measure_time(np.var, price_data)
custom_var_time = measure_time(calculate_variance, price_data)

print("\n--- Computational Complexity / Execution Time (Avg over 10 runs) ---")
print(
    f"Mean Time -> Built-in: {builtin_mean_time:.8f}s | Custom: {custom_mean_time:.8f}s"
)
print(
    f"Var Time  -> Built-in: {builtin_var_time:.8f}s | Custom: {custom_var_time:.8f}s"
)


df["Date"] = pd.to_datetime(df["Date"])
df["Day_of_Week"] = df["Date"].dt.day_name()
df["Month"] = df["Date"].dt.strftime("%b")

population_mean = builtin_mean

wednesday_prices = df[df["Day_of_Week"] == "Wednesday"].iloc[:, 3]
wednesday_mean = np.mean(wednesday_prices)

print("\n--- Wednesday Price Analysis ---")
print(f"Population Mean: {population_mean:.2f}")
print(f"Wednesday Sample Mean: {wednesday_mean:.2f}")


april_prices = df[df["Month"] == "Apr"].iloc[:, 3]
april_mean = np.mean(april_prices)

print("\n--- April Price Analysis ---")
print(f"April Sample Mean: {april_mean:.2f}")


if df.iloc[:, 8].dtype == "O":
    df["Chg%_Clean"] = (
        df.iloc[:, 8].astype(str).str.rstrip("%").astype("float")
    )
else:
    df["Chg%_Clean"] = df.iloc[:, 8]


loss_count = df["Chg%_Clean"].apply(lambda x: 1 if x < 0 else 0).sum()
prob_loss = loss_count / len(df)


profit_wed_count = len(
    df[(df["Day_of_Week"] == "Wednesday") & (df["Chg%_Clean"] > 0)]
)
prob_profit_and_wednesday = profit_wed_count / len(df)


wed_count = len(df[df["Day_of_Week"] == "Wednesday"])
prob_profit_given_wednesday = (
    profit_wed_count / wed_count if wed_count > 0 else 0
)

print("\n--- Probability Analysis ---")
print(f"P(Loss overall): {prob_loss:.4f}")
print(f"P(Profit AND Wednesday): {prob_profit_and_wednesday:.4f}")
print(f"P(Profit | Wednesday): {prob_profit_given_wednesday:.4f}")


plt.figure(figsize=(10, 5))
plt.scatter(
    df["Day_of_Week"], df["Chg%_Clean"], color="skyblue", edgecolors="black"
)
plt.title("Chg% vs Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Chg%")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()