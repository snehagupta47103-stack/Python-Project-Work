# 📚 E-Library Dashboard

A data-driven **E-Library Dashboard** built with Python that analyzes library transaction data and provides meaningful insights through statistics, filtering options, and interactive visualizations.

This project helps librarians and administrators understand borrowing patterns, popular books, user activity, and genre trends using data analysis techniques.

---

## 🚀 Project Overview

The **E-Library Dashboard** is a Python-based data analytics application designed to manage and analyze library transaction records.

The system loads library transaction data from a CSV file, cleans the dataset, performs statistical analysis, and generates visual reports using different visualization techniques.

It provides an easy-to-use menu-driven interface for exploring library activities.

---

## ✨ Features

### 📊 Data Management
- Load library transaction data from CSV files
- Validate required dataset columns
- Remove duplicate records
- Handle missing values
- Convert date fields into proper datetime format

### 📈 Statistical Analysis
The dashboard provides:

- Average borrowing duration
- Standard deviation of borrowing duration
- Most borrowed book
- Busiest borrowing day

### 🔍 Transaction Filtering
Users can filter records based on:

- 📚 Book Genre
- ⏳ Minimum borrowing duration

### 📊 Data Visualization

The project generates multiple analytical charts:

#### 📌 Bar Chart
- Displays number of borrowed books according to genre

#### 📈 Line Graph
- Shows daily borrowing trends

#### 🥧 Pie Chart
- Represents genre distribution percentage

#### 🔥 Heatmap
- Displays relationship between genre and borrowing duration

### 📑 Library Report

Generates a detailed summary containing:

- Total transactions
- Total users
- Total unique books
- Top 5 borrowed books
- Genre-wise borrowing count

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Pandas | Data Processing & Analysis |
| NumPy | Numerical Calculations |
| Matplotlib | Data Visualization |
| Seaborn | Advanced Visualization |

---

# 📂 Project Structure

```
E-Library-Dashboard/
│
├── main.py
├── library_transactions.csv
├── README.md
│
└── requirements.txt
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/E-Library-Dashboard.git
```

## 2. Navigate to Project Folder

```bash
cd E-Library-Dashboard
```

## 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

or

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run the Python file:

```bash
python main.py
```

Make sure your CSV file name is:

```
library_transactions.csv
```

and it is placed in the same directory.

---

# 📄 Dataset Requirements

The CSV file should contain the following columns:

| Column Name | Description |
|-------------|-------------|
| Transaction ID | Unique transaction identifier |
| Date | Borrowing transaction date |
| User ID | Library user identifier |
| Book Title | Name of borrowed book |
| Genre | Book category |
| Borrowing Duration (Days) | Number of borrowing days |

Example:

| Transaction ID | Date | User ID | Book Title | Genre | Borrowing Duration |
|---|---|---|---|---|---|
| T001 | 12-01-2025 | U101 | Python Basics | Programming | 7 |

---

# 🖥️ Dashboard Menu

```
========== E-LIBRARY DASHBOARD ==========

1. Show Statistics
2. Filter Transactions
3. Bar Chart
4. Line Graph
5. Pie Chart
6. Heatmap
7. Report
8. Exit

```

---

# 📸 Screenshots

<img width="1370" height="722" alt="Screenshot 2026-07-18 151825" src="https://github.com/user-attachments/assets/0c32879f-3b2a-441f-bae4-d8db5e3db835" />
<img width="1316" height="726" alt="Screenshot 2026-07-18 151856" src="https://github.com/user-attachments/assets/284989c2-a155-40df-870a-31bf7aa0aada" />
<img width="1116" height="630" alt="Screenshot 2026-07-18 151919" src="https://github.com/user-attachments/assets/3a082e5f-6980-41f6-8c92-c9d544ee11f6" />
<img width="1462" height="635" alt="Screenshot 2026-07-18 151950" src="https://github.com/user-attachments/assets/dacf9597-ccb5-4f56-8779-c83b9e8e1aa3" />
<img width="1093" height="222" alt="Screenshot 2026-07-18 152010" src="https://github.com/user-attachments/assets/37d191aa-af1c-4c90-beec-1399ff5a637b" />
<img width="1331" height="645" alt="Screenshot 2026-07-18 152029" src="https://github.com/user-attachments/assets/f484829d-4f2c-40e7-8415-f887aba62928" />
<img width="1265" height="834" alt="Screenshot 2026-07-18 152114" src="https://github.com/user-attachments/assets/470bdaea-a643-4815-a622-4957dd16b221" />
<img width="1137" height="233" alt="Screenshot 2026-07-18 152133" src="https://github.com/user-attachments/assets/6eceeb8e-124a-40be-ba4e-abc6552d465d" />
<img width="1384" height="778" alt="Screenshot 2026-07-18 152153" src="https://github.com/user-attachments/assets/866a523f-0fc1-40da-b853-54bdf8fb20b2" />
<img width="1189" height="682" alt="Screenshot 2026-07-18 152219" src="https://github.com/user-attachments/assets/5c60ec5b-31ef-4a6d-8069-eed83b9c361c" />


---

# 🎯 Project Objectives

- Analyze library borrowing behavior
- Identify popular books and genres
- Understand user activity patterns
- Visualize library performance data
- Practice data analysis using Python

---

# 🔮 Future Improvements

Possible enhancements:

- Add graphical user interface using Tkinter/PyQt
- Connect with SQL database
- Add user login system
- Generate automated PDF reports
- Create real-time dashboard using Streamlit
- Add advanced recommendation system for books

---

# 🤝 Contribution

Contributions are welcome!

Steps:

1. Fork this repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 📜 License

This project is created for educational and learning purposes.

---

# 👨‍💻 Author

**GUPTA SNEHA**

⭐ If you like this project, consider giving it a star!
