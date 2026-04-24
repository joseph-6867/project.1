import pandas as pd
import numpy as np

data = {
    "Name": ["Manoj", "Rahul", "Anu"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())


print("\nColumn (Age):")
print(df["Age"])

print("\nRow (index 0):")
print(df.loc[0])

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

df["Grade"] = ["A", "A+", "B"]
print("\nAfter adding Grade:\n", df)

df = df.drop("Grade", axis=1)
print("\nAfter deleting Grade:\n", df)

print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))
