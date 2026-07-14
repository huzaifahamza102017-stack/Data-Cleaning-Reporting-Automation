import pandas as pd

# Load cleaned data
df = pd.read_excel("../output/cleaned_data.xlsx")

# Create summary report
summary = {
    "Total Customers": len(df),
    "Average Age": round(df["Age"].mean(), 2),
    "Total Sales": df["Sales"].sum()
}

# Convert summary to dataframe
summary_df = pd.DataFrame([summary])

# City-wise sales
city_sales = df.groupby("City")["Sales"].sum().reset_index()

# Save report
with pd.ExcelWriter("../output/Automated_Report.xlsx") as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    city_sales.to_excel(writer, sheet_name="City Sales", index=False)

print("Report generated successfully!")