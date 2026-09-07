# Titanic Data Cleaning & Preprocessing

## 📌 Project Overview

This project is part of the **Synent Technologies Data Science Internship – Task 1**.
The objective of this task is to clean and preprocess the Titanic dataset using **Python and Pandas**. The dataset contains information about passengers aboard the Titanic, including their age, gender, passenger class, fare, cabin, and survival status.
Data cleaning is an important step in the data science workflow because it helps improve data quality and prepares the dataset for further analysis and machine learning.

---

## 🎯 Objectives

The main objectives of this project are:

- Load and inspect the Titanic dataset.
- Identify missing values.
- Handle missing values appropriately.
- Remove unnecessary columns.
- Check for duplicate records.
- Standardize column names.
- Create a clean and analysis-ready dataset.
- Save the cleaned dataset as a new CSV file.

---
## 📊 Dataset
The dataset contains information about passengers aboard the RMS Titanic, including passenger details, class, ticket information, fare, and survival status.

Original records: 891
Original columns: 12

### Dataset Source: Kaggle — Titanic Dataset

---
| File | Description |
|------|-------------|
| `titanic.csv` | Original Titanic dataset |
| `titanic_cleaned.csv` | Cleaned and preprocessed dataset |
| `titanic_cleaning.py` | Python script used for data cleaning |
| `README.md` | Project documentation |

---

## Data cleaning and preprocessing
| Issue | Action |
|---|---|
| **Age — 177 missing values** | Filled with median (**28.0**) |
| **Cabin — 687 missing values** | Removed due to excessive missing data |
| **Embarked — 2 missing values** | Filled with mode (**S**) |
| **Duplicate rows** | None found |
| **Column names** | Standardized to lowercase **snake_case** |
| **Data types** | Inspected and validated |

The **Age** column was kept as `float64` because the dataset contains valid fractional ages.

---

## 📊 Results table
| Check | Result |
|---|---|
| **Original dataset** | 891 rows × 12 columns |
| **Final dataset** | 891 rows × 11 columns |
| **Missing values** | 0 |
| **Duplicate rows** | 0 |
| **Removed column** | `Cabin` |

The cleaned dataset was successfully exported as `titanic_cleaned.csv`.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **VS Code**
- **Git**
- **GitHub**

---


## 📂 Project Structure

```text
synent_task1_datacleaning/
│
├── titanic.csv
├── titanic_cleaned.csv
├── titanic_cleaning.py
└── README.md
