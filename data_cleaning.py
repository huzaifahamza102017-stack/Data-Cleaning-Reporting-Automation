import pandas as pd

# Load the raw Excel file
df = pd.read_excel("../data/raw_data.xlsx")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age values with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Sales values with 0
df["Sales"] = df["Sales"].fillna(0)

# Fix inconsistent city names
df["City"] = df["City"].str.title()

# Save the cleaned data
df.to_excel("../output/cleaned_data.xlsx", index=False)

print("Data cleaning completed successfully!")