import pandas as pd
import os

os.makedirs("output", exist_ok=True)

df = pd.read_csv("input/employee.csv")

# Add Annual Salary
df["AnnualSalary"] = df["Salary"] * 12

# Employee Grade
def grade(salary):
    if salary >= 60000:
        return "A"
    elif salary >= 50000:
        return "B"
    else:
        return "C"

df["Grade"] = df["Salary"].apply(grade)

# Bonus (10%)
df["Bonus"] = df["Salary"] * 0.10

# Total Package
df["TotalPackage"] = df["AnnualSalary"] + df["Bonus"]

df.to_csv("/home/azureuser/ethans-1124/output/employee_transformed.csv", index=False)

print(df)
print("Transformation completed.")
