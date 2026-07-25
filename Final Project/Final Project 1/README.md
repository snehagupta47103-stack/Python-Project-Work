# 🦠 COVID-19 Data Analysis & Visualization

## Exploratory Data Analysis (EDA) of COVID-19 Global Dataset

<p align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)

</p>

<p align="center">

*"Data helps us understand the spread of diseases and supports informed public health decisions."*

</p>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📊 Exploratory Data Analysis & Visualizations](#-exploratory-data-analysis--visualizations)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **COVID-19 Data Analysis & Global Tracker** is an exploratory time-series analysis project designed to examine, analyze, and visualize the global spread of the COVID-19 pandemic using official **World Health Organization (WHO)** Situation Report data.

By unpivoting raw time-series data from wide to long format, this project computes critical public health metrics, tracks cumulative growth curves, identifies primary epicenters, and summarizes regional impacts across WHO geographic divisions.

This project is designed to:
- Process and clean raw WHO time-series epidemiological datasets.
- Demonstrate wide-to-long dataset reshaping using `pd.melt()`.
- Compute global, regional, and national cumulative case totals.
- Produce clean, publication-ready statistical visualizations using `Matplotlib` and `Seaborn`.

---

## 🎯 Problem Statement

> **Objective:** Build an exploratory data analysis pipeline to transform wide WHO time-series data into structured insights and visual reports.

During pandemic outbreaks, public health organizations require continuous monitoring of infection trajectories to allocate medical resources efficiently. Raw time-series reporting often spreads daily counts across hundreds of columns, making direct analysis difficult without structured unpivoting and data cleaning.

| 📂 Module | 📄 Feature Type | 🔍 Description |
|------------|---------|----------------|
| Data Reshaping | Data Processing | Converts wide date-wise columns into long relational rows |
| Global Trajectory | Line Plot | Plots global cumulative confirmed cases over time |
| Top 5 Epicenters | Bar Chart | Identifies nations with the highest cumulative infections |
| Regional Impact | Bar Chart | Categorizes total cases across official WHO regions |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Automated Reshaping** | Unpivots wide WHO date columns into structured, datetime-indexed Pandas rows |
| 📉 **Global Growth Tracking** | Aggregates and tracks daily global cumulative confirmed case totals |
| 🏆 **Top Epicenter Identification** | Dynamically calculates and plots the top 5 most affected nations |
| 🌍 **WHO Regional Breakdown** | Summarizes cumulative pandemic distribution across official WHO regions |
| 🛡️ **Boundary Date Validation** | Filters non-zero date limits to avoid blank chart rendering |
| 📊 **Summary Statistics** | Computes descriptive numeric statistics on global case distribution |

---

## 🏗️ Project Structure

```text
FINAL PROJECT/
└── 01_COVID19_Analysis/
    ├── COVID19_Analysis.ipynb
    ├── who_covid_19_sit_rep_time_series.csv
    └── README.md

```
---

🔄 Project Workflow

```text

+-------------------------------------------------------+
|                 Start Project                         |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|  Load WHO CSV Dataset (Read time-series raw data)     |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|  Reshape Wide to Long Format (Apply pd.melt())        |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|  Parse Dates & Clean Data (Datetime & fillna)          |
+-------------------------------------------------------+
                           |
            +--------------+--------------+
            |                             |
            v                             v
+-----------------------+     +-------------------------+
| Global Trajectory     |     | Regional & Top Country  |
| Analysis              |     | Aggregations            |
+-----------------------+     +-------------------------+
            |                             |
            +--------------+--------------+
                           |
                           v
+-------------------------------------------------------+
|  Generate Line & Bar Plots (Matplotlib & Seaborn)     |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|              Print Findings & Insights                |
+-------------------------------------------------------+

```

---


## 📊 Exploratory Data Analysis & Visualizations

### 📈 1. Global Cumulative Case Growth
> Displays the overall global trajectory of confirmed COVID-19 cases over time.

- **Chart Type:** Line Plot (Red)
- **Insight:** Highlights exponential growth during the early acceleration phases of the pandemic outbreak.

<img width="1228" height="619" alt="Screenshot 2026-07-24 151520" src="https://github.com/user-attachments/assets/aa9c95cc-e479-4e82-b159-11b0ac83c959" />

---

### 🏛️ 2. Top 5 Most Affected Countries
> Compares cumulative confirmed case counts across the top 5 global epicenters as of peak reporting.

- **Chart Type:** Vertical Bar Chart (Purple)
- **Insight:** Pinpoints primary outbreak centers led by initial transmission epicenters.

<img width="1262" height="730" alt="Screenshot 2026-07-24 151600" src="https://github.com/user-attachments/assets/9426a278-51c6-42cb-ace2-de5ac7af4857" />

---

### 🌍 3. WHO Region-Wise Distribution
> Analyzes cumulative case distribution across official WHO geographic territories.

- **Chart Type:** Vertical Bar Chart (Orange)
- **Insight:** Highlights severe outbreak burdens across specific continental divisions.

<img width="1171" height="721" alt="Screenshot 2026-07-24 151827" src="https://github.com/user-attachments/assets/7c82d6ba-9326-4162-a8ee-cba5ceaf09c1" />

---

## 🛠️ Tech Stack

| Tool / Library | Version | Purpose |
|----------------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming platform |
| 🐼 **Pandas** | Latest | Data cleaning, unpivoting (`melt`), and aggregations |
| 🔢 **NumPy** | Latest | Numerical transformations and array management |
| 📊 **Matplotlib** | Latest | Base charting and figure plotting |
| 🎨 **Seaborn** | Latest | Statistical styling and color palettes |
| 📓 **Jupyter Notebook** | Interactive | Step-by-step code execution environment |

---

## 📈 Results & Insights

- 📉 **Exponential Curve:** Global cumulative cases exhibited steep exponential growth during the early pandemic phase.
- 🌍 **Regional Concentration:** The **Western Pacific Region (WPRO)** and **European Region (EURO)** recorded major early infection totals.
- 📍 **Primary Epicenters:** China, Italy, and the Republic of Korea represented the earliest high-burden transmission epicenters.
- 🧹 **Structured Pipeline:** Successfully unpivoted 200+ date columns into a relational structure for analytics.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner & Reviewer Friendly** | Sequential cell-by-cell Jupyter Notebook execution |
| 🔄 **High Reusability** | Pipeline easily adapts to new WHO time-series dataset updates |
| 📊 **Publication Ready Visuals** | Clear, high-contrast visual charts with clear labels |
| ⚡ **Zero External Heavy Setup** | Runs lightweight with pure Python data science libraries |
| 📖 **Clean Readable Code** | Straightforward Pandas operations without overly complex abstractions |
| 🛡️ **Boundary Safety** | Zero-value filtering prevents generating empty or blank graphs |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

MIT License — Free to use, modify, and distribute with attribution.


---

## 👤 Author

<div align="center">

### SNEHA GUPTA

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

> *"Turning raw health data into actionable visual insights."*

**🎓 Role:** Data Analyst / Python Developer \
**📍 Location:** India \
**🛠️ Skills:** Python · Pandas · Data Analysis · Exploratory Data Analysis · Data Visualization

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities:

- 🏥 [World Health Organization (WHO)](https://www.who.int/) — Source for official COVID-19 Situation Reports
- 🐼 [Pandas Official Documentation](https://pandas.pydata.org/docs/) — Data manipulation and reshaping guides
- 📊 [Matplotlib Plotting Guide](https://matplotlib.org/stable/contents.html) — Visualization documentation
- 🎨 [Seaborn Statistical Data Visualization](https://seaborn.pydata.org/) — Palettes and chart styling reference

---

<div align="center">

---

*Made with ❤️ and Python — Last updated: July, 2026*
