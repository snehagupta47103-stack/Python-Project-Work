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

#### 1. 📈 Top 10 Happiest Countries (2015)

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

#### 2. 📉 Bottom 10 Countries by Happiness Score

Displays the 10 lowest-ranking nations in global subjective well-being for 2015.
* **Chart Type:** Horizontal Bar Plot (Seaborn `barplot` with `flare` palette)
* **Key Metric:** `Happiness Score` (Scale: 0 – 5) aggregated by `Country`
* **Insight:** Highlights severe socioeconomic and governance challenges in lower-ranked nations, where happiness scores drop significantly below 3.5, showing a stark contrast to global averages.

#### 🛠️ Python Implementation
```python
# Extracting 10 countries with lowest happiness scores
bottom10 = df.nsmallest(10, 'Happiness Score')

# Generating Seaborn horizontal bar chart
plt.figure(figsize=(12, 6))
sns.barplot(
    data=bottom10, 
    x='Happiness Score', 
    y='Country', 
    hue='Country', 
    palette='flare', 
    legend=False
)

plt.title('Bottom 10 Countries by Happiness Score', fontsize=14, fontweight='bold')
plt.xlabel('Happiness Score')
plt.ylabel('Country')
plt.xlim(0, 5)

# Displaying data labels on bars
for index, value in enumerate(bottom10['Happiness Score']):
    plt.text(value + 0.1, index, f'{value:.2f}', color='black', va='center')

plt.tight_layout()
plt.show()
```
<img width="1388" height="685" alt="Screenshot 2026-07-24 212201" src="https://github.com/user-attachments/assets/a7ac3465-d3f1-4c70-bd58-7e733358245f" />

---
#### 3. 🌍 Average Happiness Score by World Region

Displays the regional comparison of overall subjective well-being across different geographic zones in 2015.
* **Chart Type:** Horizontal Bar Plot (Seaborn `barplot` with `viridis` palette)
* **Key Metric:** Mean `Happiness Score` grouped by `Region`
* **Insight:** Demonstrates clear geographic disparities, where regions like Australia/New Zealand, North America, and Western Europe lead with the highest regional averages, while Sub-Saharan Africa and Southern Asia record the lowest scores overall.

#### 🛠️ Python Implementation
```python
# Grouping data by Region and calculating average Happiness Score
region_avg = df.groupby('Region')['Happiness Score'].mean().sort_values(ascending=False).reset_index()

# Generating Seaborn horizontal bar chart
plt.figure(figsize=(12, 6))
sns.barplot(
    data=region_avg, 
    x='Happiness Score', 
    y='Region', 
    hue='Region', 
    palette='viridis', 
    legend=False
)

plt.title('Average Happiness Score by World Region', fontsize=14, fontweight='bold')
plt.xlabel('Average Happiness Score')
plt.ylabel('Region')

plt.tight_layout()
plt.show()
```
<img width="1393" height="628" alt="Screenshot 2026-07-24 212230" src="https://github.com/user-attachments/assets/68d5ac3b-da9e-4bf5-b6a9-b9aa92e39160" />

---

#### 4. 🔗 Correlation Heatmap of Happiness Factors

Displays the linear correlation between overall happiness scores and key socioeconomic indicators.
* **Chart Type:** Heatmap (Seaborn `heatmap` with `Blues` palette)
* **Key Metric:** Pearson Correlation Matrix (`corr()`) across key numeric factors
* **Insight:** Reveals a strong positive correlation between `Happiness Score`, `Economy (GDP per Capita)`, and `Health (Life Expectancy)`, indicating that economic prosperity and physical well-being are the primary drivers of global happiness.

#### 🛠️ Python Implementation
```python
# Selecting key numerical factors for correlation analysis
factors = [
    'Happiness Score', 
    'Economy (GDP per Capita)', 
    'Family', 
    'Health (Life Expectancy)', 
    'Freedom', 
    'Trust (Government Corruption)', 
    'Generosity'
]

# Computing correlation matrix
corr_matrix = df[factors].corr()

# Generating Seaborn heatmap
plt.figure(figsize=(10, 4))
sns.heatmap(
    corr_matrix, 
    annot=True, 
    cmap='Blues', 
    fmt=".2f", 
    linewidths=0.5
)

plt.title('Correlation Heatmap of Happiness Factors', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```
<img width="1357" height="719" alt="Screenshot 2026-07-24 212344" src="https://github.com/user-attachments/assets/dd4ff182-d97c-49c9-8221-ebf6bbbce576" />

---
#### 💰 Impact of Economy (GDP per Capita) on Happiness Score

Displays the relationship between economic output per person and overall happiness score, categorized by world region.
* **Chart Type:** Scatter Plot (Seaborn `scatterplot` with region-based `hue`)
* **Key Metric:** `Economy (GDP per Capita)` vs. `Happiness Score` hue-mapped by `Region`
* **Insight:** Displays a clear upward linear trend showing that countries with higher GDP per capita generally achieve higher happiness scores, with distinct regional clustering visible across different economic tiers.

#### 🛠️ Python Implementation
```python
# Generating Seaborn scatter plot
plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=df, 
    x='Economy (GDP per Capita)', 
    y='Happiness Score', 
    hue='Region', 
    s=100, 
    alpha=0.8
)

plt.title('Impact of Economy (GDP per Capita) on Happiness Score', fontsize=14, fontweight='bold')
plt.xlabel('Economy (GDP per Capita)')
plt.ylabel('Happiness Score')

# Adjusting legend position to keep visual clean
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
```
<img width="1325" height="616" alt="Screenshot 2026-07-24 212438" src="https://github.com/user-attachments/assets/332ff730-5c8c-4afb-a369-d94dccb031bb" />

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
