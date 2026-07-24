<div align="center">

# 🌍 World Happiness Report 2015 — Data Analysis & Visualization
### *Exploratory Data Analysis (EDA) of Global Happiness Factors*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"Data is the new science. Big data holds the answers to understanding human well-being and global happiness."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📊 Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **World Happiness Report 2015 Analysis** is a data science project focusing on exploratory data analysis (EDA) and visualization of happiness scores across different countries and regions. By examining variables such as GDP per capita, social support, health life expectancy, freedom, trust in government, and generosity, this project highlights key drivers of subjective well-being.

This project is designed to:
- Load, inspect, and analyze global economic and social metrics using **Pandas**.
- Identify statistical summaries, distributions, and missing values in real-world data.
- Generate high-quality statistical plots using **Matplotlib** and **Seaborn**.
- Gain actionable insights into regional happiness distributions.

---

## 🎯 Problem Statement

> **Objective:** Perform Exploratory Data Analysis (EDA) on the 2015 World Happiness Report dataset to discover key metrics influencing global happiness levels.

Understanding happiness factors allows policymakers and researchers to design better social and economic strategies. The goal is to ingest raw CSV data, perform statistical checks, handle clean datasets, and output meaningful visual patterns.

| 📂 Metric / Feature | 📄 Data Type | 🔍 Description |
|--------------------|--------------|----------------|
| Country / Region | Categorical | Geographical classifications |
| Happiness Rank/Score | Numerical | Overall happiness standing |
| Economy (GDP per Capita) | Numerical | Economic contribution to score |
| Health (Life Expectancy) | Numerical | Health and longevity metric |
| Freedom | Numerical | Perceived freedom of choice |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📂 **Data Ingestion** | Reads and parses complex CSV datasets cleanly |
| 📊 **Exploratory Data Analysis** | Comprehensive statistical summary (`describe()`, `info()`) |
| ❓ **Data Quality Check** | Evaluates missing/null values across all columns |
| 📉 **Data Visualization** | High-resolution statistical visualization with Seaborn & Matplotlib |
| 🌐 **Regional Breakdown** | Analyzes comparative metrics across distinct world regions |

---

## 🏗️ Project Structure

```text
world-happiness-analysis/
├── 📁 data/
│   └── 📄 2015.csv              # World Happiness Dataset (2015)
├── 📁 notebooks/
│   └── 📓 notebook.ipynb        # Data Analysis & Visualization Notebook
├── 📁 docs/
│   └── 🖼️ assets/              # README Images & Diagrams (Optional)
├── 📄 .gitignore                # Git ignore rules
├── 📄 LICENSE                   # MIT License
├── 📄 README.md                 # Project Documentation
└── 📄 requirements.txt          # Python dependencies
```
---

## 🔄 Project Workflow

```text
┌──────────────────────────────────────────────────────────┐
│                 📥 Load Dataset (2015.csv)               │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│                   🔍 Data Inspection                      │
│                • df.head()    • df.info()                 │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│              🧹 Missing Value & Null Check               │
│                   • df.isnull().sum()                    │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│              📊 Statistical Summarization                │
│                      • df.describe()                     │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│             📈 Data Visualization & Plots                │
│                 • Matplotlib & Seaborn                   │
└──────────────────────────────────────────────────────────┘
```
---

### 📊 Exploratory Data Analysis & Visualizations

#### 📈 Top 10 Happiest Countries (2015)

Displays the top 10 nations leading the global rankings in overall happiness and well-being.
* **Chart Type:** Horizontal Bar Plot
* **Key Metric:** `Happiness Score` (Scale: 0 – 8) aggregated by `Country`
* **Insight:** Highlights that top-ranking countries (led by Switzerland, Iceland, and Denmark) consistently maintain high happiness scores above 7.5, driven primarily by strong economic stability (GDP per Capita), social support networks, and high health/life expectancy.

#### 🛠️ Python Implementation
```python
# Sorting dataset to get top 10 happiest countries
top10 = df.sort_values(by='Happiness Score', ascending=False).head(10)

# Generating horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(top10['Country'], top10['Happiness Score'], color='#2ecc71')
plt.title('Top 10 Happiest Countries in the World (2015)', fontsize=14, fontweight='bold')
plt.xlabel('Happiness Score')
plt.ylabel('Country')
plt.xlim(0, 8)
plt.gca().invert_yaxis()  # Rank #1 ko sabse upar dikhane ke liye

# Adding data labels on bars
for index, value in enumerate(top10['Happiness Score']):
    plt.text(value + 0.1, index, f'{value:.2f}', color='black', va='center')

plt.tight_layout()
plt.show()
```
<img width="1327" height="686" alt="Screenshot 2026-07-24 212119" src="https://github.com/user-attachments/assets/a75a9bc0-72a0-40ef-b816-28ab78b42eb5" />

---
## 🛠️ Tech Stack

| Technology | Domain / Role | Purpose / Use Case |
| :--- | :--- | :--- |
| **🐍 Python 3.8+** | Core Language | Data manipulation & scripting |
| **🐼 Pandas** | Data Analysis | Dataframes, cleaning & aggregation |
| **📊 Matplotlib** | Data Visualization | Plotting graphs & customizing charts |
| **🎨 Seaborn** | Statistical Plots | Advanced visualization & themes |
| **📓 Jupyter Notebook** | IDE Environment | Interactive code execution & documentation |

---
---

## 📈 Results & Insights

* 📊 **Complete Dataset Integrity:** Initial checks confirmed structured formatting across happiness ranks.
* 💡 **Key Happiness Drivers:** High correlation was observed between GDP per Capita, Life Expectancy, and overall Happiness Score.
* 🗺️ **Regional Disparities:** Significant regional variance in happiness metrics was highlighted through graphical analysis.

---

## 🏆 Advantages

| Advantage | Detail |
| :--- | :--- |
| **🚀 Reproducible** | Fully automated through Jupyter Notebook cells |
| **🪶 Lightweight** | Requires standard Python data science packages |
| **📚 Educational** | Ideal reference for introductory EDA workflows |
| **🎨 Rich Visuals** | Utilizes Seaborn styling for clear insights |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

---

## 👤 Author

<div align="center">

### **SNEHA GUPTA**

> *"Data unveils the subtle patterns behind human behavior and societal well-being."*

[![GitHub](https://img.shields.io/badge/GitHub-isamaliya16-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

<br/>

| Profile Attribute | Details |
| :--- | :--- |
| **🎓 Role** | Junior Python Developer \| Data Science Enthusiast |
| **📍 Location** | India |
| **🛠️ Skills** | `Python` · `Pandas` · `Data Analysis` · `Visualization` · `EDA` |

</div>

---

## 🙏 Acknowledgements

* 🌍 [World Happiness Report - Kaggle](https://www.kaggle.com/datasets/unsdsn/world-happiness) — *Dataset Source*
* 📚 [Pandas Documentation](https://pandas.pydata.org/docs/)
* 🎨 [Seaborn Visualization Gallery](https://seaborn.pydata.org/)
