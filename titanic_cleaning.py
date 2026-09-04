import pandas as pd

# 1. Load the dataset
df = pd.read_csv("titanic.csv")

print("========== ORIGINAL DATASET ==========")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())


# 2. Handle missing Age values
age_median = df["Age"].median()
print("\nMedian Age:", age_median)

df["Age"] = df["Age"].fillna(age_median)


# 3. Remove Cabin column
# Cabin has too many missing values, so we remove it.
df = df.drop("Cabin", axis=1)


# 4. Handle missing Embarked values
embarked_mode = df["Embarked"].mode()[0]
print("Embarked mode:", embarked_mode)

df["Embarked"] = df["Embarked"].fillna(embarked_mode)


# 5. Check data types
print("\nData types:")
print(df.dtypes)


# 6. Standardize column names
df = df.rename(columns={
    "PassengerId": "passenger_id",
    "Survived": "survived",
    "Pclass": "pclass",
    "Name": "name",
    "Sex": "sex",
    "Age": "age",
    "SibSp": "sib_sp",
    "Parch": "parch",
    "Ticket": "ticket",
    "Fare": "fare",
    "Embarked": "embarked"
})


# 7. Final validation
print("\n========== FINAL VALIDATION ==========")

print("\nFinal shape:")
print(df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nFinal columns:")
print(df.columns.tolist())


# 8. Save the cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")