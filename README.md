# Elevate-labs
Data Analyst Internship: Cleaned and preprocessed the Netflix Movies and TV Shows dataset using Python and Pandas. Handled missing values, removed duplicates, standardized formats, and exported a clean CSV file.
# Task 1: Data Cleaning and Preprocessing

## 📁 Project Overview
This project is part of the Data Analyst Internship Task 1. It involves cleaning and preprocessing a raw dataset using Python and Pandas. The dataset used is **Netflix Movies and TV Shows**, which contains metadata about titles available on the Netflix platform.

---

## 📊 Dataset Details
- **File Name**: `netflix_titles.csv`
- **Source**: [Kaggle - Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Records**: Movies and TV Shows with details like title, director, cast, release year, rating, etc.

---

## 🧹 Cleaning Steps Performed

The script (`task 1.py`) performs the following steps:

1. **Loading the Dataset**  
   Loaded using `pandas.read_csv()` with correct handling of file paths.

2. **Handling Missing Values**
   - Replaced missing values in `director` and `country` columns with `'Unknown'`.
   - Converted `date_added` column to datetime format with `errors='coerce'`.

3. **Removing Duplicates**
   - Dropped duplicate rows using `.drop_duplicates()`.

4. **Standardizing Text Columns**
   - Standardized case for categorical values (e.g., `type`, `rating`, `country`).
   - Trimmed extra spaces from strings.

5. **Renaming Columns**
   - Renamed columns to lowercase with underscores for consistency using:
     ```python
     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
     ```

6. **Fixing Data Types**
   - Converted `release_year` to integer.
   - Ensured `date_added` is in proper datetime format.

7. **Exporting Cleaned Dataset**
   - Saved the cleaned data as `cleaned_netflix.csv`.

---

## 🧪 Tools & Libraries
- Python 3
- Pandas

---

## 🚀 How to Run

1. Ensure `netflix_titles.csv` is in the same folder as `task 1.py`.
2. Run the script using:
   ```bash
   python "task 1.py"
