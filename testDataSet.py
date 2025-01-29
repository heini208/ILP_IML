import pandas as pd

# Load dataset
file_path = "loan_data.csv"
df = pd.read_csv(file_path)

# 🔹 Normalize column names (strip spaces, lowercase, replace spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print(df.isnull().sum())


# Proceed with the script
