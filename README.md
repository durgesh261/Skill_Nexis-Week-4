# 📊 Week 4: Capstone Project — Financial Analytics, Machine Learning & Business Intelligence

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

Welcome to the **Week 4 Capstone Project** repository for the **Skill_Nexis Data Analyst Program**. This repository houses the complete, end-to-end commercial analytics portfolio project analyzing global financial transactions across North America and Europe using the official **Microsoft Financial Sample Dataset** (700 transactions).

---

## 📑 Table of Contents
1. [Project Overview & Curriculum Alignment](#-project-overview--curriculum-alignment)
2. [Global Executive KPIs](#-global-executive-kpis)
3. [Repository Structure](#-repository-structure)
4. [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
5. [Machine Learning Regression Modeling](#-machine-learning-regression-modeling)
6. [Power BI Dashboard & Dimensional Modeling](#-power-bi-dashboard--dimensional-modeling)
7. [Executive Stakeholder Presentation & Recommendations](#-executive-stakeholder-presentation--recommendations)
8. [Installation & Reproduction Guide](#-installation--reproduction-guide)
9. [Deliverables Checklist](#-deliverables-checklist)

---

## 🎯 Project Overview & Curriculum Alignment

This capstone project synthesizes the core competencies developed across the entire 4-week program:
- **Week 1**: Excel Modeling, Formulas, Pivot Tables & Dynamic Dashboards
- **Week 2**: Python Data Analysis & Advanced SQL Aggregations
- **Week 3**: Data Wrangling, Cleaning, Outlier Remediation & Feature Engineering
- **Week 4 (Capstone)**: End-to-End Analysis Case Study:
  1. Perform Exploratory Data Analysis (EDA) on a complex business dataset.
  2. Build a Machine Learning Regression Model to predict sales revenue.
  3. Construct an enterprise-grade Power BI dashboard with dimensional modeling & DAX.
  4. Author an executive stakeholder report detailing strategic recommendations.
  5. Package multi-format deliverables (Excel Report, Python Notebook, Power BI Assets).

---

## 📈 Global Executive KPIs

Across 700 transactions spanning September 2013 through December 2014:

| Metric | Portfolio Value | Commercial Description |
| :--- | :---: | :--- |
| **Gross Sales Revenue** | **$127,931,598.50** | Total invoiced transaction volume |
| **Total Discounts Granted** | **$9,205,248.24** | Discretionary & tier discounts applied (7.19% avg rate) |
| **Net Sales Revenue** | **$118,726,350.26** | Realized net cash revenue |
| **Cost of Goods Sold (COGS)** | **$101,832,648.00** | Direct production and inventory delivery costs |
| **Net Operating Profit** | **$16,893,702.26** | Bottom-line net income |
| **Aggregate Profit Margin** | **14.23%** | Healthy operational margin efficiency |
| **Total Units Distributed** | **1,125,806 units** | Volume sold across 6 product families |

---

## 📂 Repository Structure

```
Week-04/
├── data/
│   ├── financial_sample.xlsx              # Official raw Microsoft Financial Sample
│   └── cleaned_financial_sample.csv       # Standardized dataset with engineered ratios
├── notebooks/
│   └── Week4_Capstone_EDA_and_Regression.ipynb # Full interactive Jupyter analysis notebook
├── powerbi_dashboard/
│   ├── DAX_Measures_and_Data_Model.md     # Star Schema model & 14 production DAX measures
│   └── dashboard_preview.html             # Interactive HTML5/Chart.js Power BI simulation
├── reports/
│   ├── Week4_Financial_Analysis_Report.xlsx # Multi-tab Excel executive dashboard & pivot tables
│   └── Executive_Stakeholder_Presentation.md # Executive briefing & strategic playbook
├── scripts/
│   ├── build_excel_report.py              # Automated openpyxl Excel dashboard generator
│   ├── eda_and_regression.py              # Pipeline executing EDA, ML training, & chart export
│   ├── create_capstone_notebook.py        # Programmatic Jupyter Notebook builder
│   └── generate_powerbi_preview_image.py  # High-resolution dashboard graphic generator
├── visuals/
│   ├── eda_sales_by_country.png           # Geographic revenue & profit comparison
│   ├── eda_segment_performance.png        # Market segment breakdown
│   ├── eda_product_profitability.png      # Product family revenue & margin rankings
│   ├── eda_discount_vs_profit_margin.png  # Discount tier margin erosion boxplot
│   ├── regression_actual_vs_predicted.png # Test set prediction scatter plot
│   ├── regression_feature_importance.png  # Top 10 feature importance weights
│   └── powerbi_dashboard_preview.png      # High-res preview of the Power BI layout
├── .gitignore                             # Ignored caches & temp files
└── README.md                              # Master project documentation
```

---

## 🔍 Exploratory Data Analysis (EDA)

### 1. Geographic Performance
- Revenue is evenly balanced across North America and Europe:
  - **USA**: $25.03M Sales | $2.99M Profit (11.97% margin)
  - **Canada**: $24.89M Sales | $3.53M Profit (14.18% margin)
  - **France**: $24.31M Sales | $3.78M Profit (15.57% margin)
  - **Germany**: $23.51M Sales | $3.68M Profit (15.65% margin)
  - **Mexico**: $20.99M Sales | $2.91M Profit (13.84% margin)
- France and Germany generate the highest profit conversion rate (~15.6%).

### 2. Market Segment Analysis
- **Government**: Core profit anchor with **$52.51M in sales (44.2%)** and **$11.39M in profit (67.4%)** at a **21.70% margin**.
- **Small Business**: High volume engine (**$42.42M sales**) with solid **9.76% margin**.
- **Enterprise**: Operating at an alarming **net loss of -$622K (-3.17% margin)** due to unchecked discounting.

### 3. Product Family Profitability
- **Paseo** is the #1 volume and revenue leader ($33.01M sales, $4.80M profit).
- Followed by **VTT** ($20.51M), **Amarilla** ($19.04M), **Carretera** ($15.62M), **Montana** ($15.39M), and **Velo** ($15.17M).

### 4. Discount Margin Erosion
- **None Discount Tier**: 19.48% average margin.
- **Low Discount Tier**: 15.12% average margin.
- **Medium Discount Tier**: 12.35% average margin.
- **High Discount Tier**: Collapses to **7.81% average margin**, with 18% of transactions losing money.

---

## 🤖 Machine Learning Regression Modeling

To predict transactional sales revenue and identify key variance drivers, we implemented and compared two regression architectures using an 80/20 train/test split (560 training / 140 holdout test):

### Model Comparison Matrix

| Model Architecture | $R^2$ Score | RMSE ($ USD) | MAE ($ USD) | Assessment |
| :--- | :---: | :---: | :---: | :--- |
| **Multiple Linear Regression (OLS)** | **0.9934** | **$19,121.49** | **$13,842.10** | Unmatched accuracy for linear baseline pricing |
| **Random Forest Regressor (100 Trees)** | **0.9841** | **$29,667.59** | **$18,924.58** | Superior handling of non-linear discount elasticity |

### Key Revenue Drivers (Feature Importance)
1. **Cost of Goods Sold (COGS)** (52.4% relative importance)
2. **Units Sold** (28.1% relative importance)
3. **Discounts** (9.6% relative importance)
4. **Sale Price** (4.8% relative importance)
5. **Categorical Factors (Segment, Country, Product)** (5.1% cumulative)

---

## 📊 Power BI Dashboard & Dimensional Modeling

### Star Schema Architecture
- **Fact Table**: `FactFinancialSales`
- **Conformed Dimensions**: `DimDate`, `DimGeography`, `DimProduct`, `DimSegment`

### Core DAX Measures Implemented
- `[Total Sales]`, `[Total Profit]`, `[Total COGS]`, `[Total Units Sold]`
- `[Profit Margin %]`, `[Effective Discount %]`, `[Avg Realized Price]`
- `[Sales Prior Year]`, `[Sales YoY Growth $]`, `[Sales YoY Growth %]`, `[Sales YTD]`
- `[Margin Status Indicator]` (`🟢 Healthy`, `🟡 Moderate`, `🔴 At Risk`)

### Interactive HTML5 Simulation
Test the dashboard live in your browser:  
Open [`powerbi_dashboard/dashboard_preview.html`](powerbi_dashboard/dashboard_preview.html) to experience live slicers, real-time KPI card updates, and responsive Chart.js analytics.

---

## 💡 Executive Stakeholder Recommendations

1. **Cap Enterprise Discounts at 8%**: Restoring Enterprise contract margins from -3.17% to the corporate benchmark (14%) delivers **+$3.37M in annual net profit**.
2. **Expand Government Procurement**: Scale sales capture teams across the US and Canada to capture an additional **+$7.88M in top-line revenue**.
3. **Deploy Machine Learning Quoting**: Integrate the Random Forest pricing model into the sales quoting workflow to eradicate loss-making contracts.

---

## 🛠️ Installation & Reproduction Guide

### Prerequisites
- Python 3.9+ with `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `openpyxl`.

### 1. Clone Sub-Repository
```bash
git clone https://github.com/durgesh261/Skill_Nexis-Week-4.git
cd Skill_Nexis-Week-4
```

### 2. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

### 3. Run Analysis Pipelines
```bash
# Run EDA, Train ML Models, & Export Visuals
python scripts/eda_and_regression.py

# Generate Executive Excel Dashboard
python scripts/build_excel_report.py

# Build Jupyter Notebook
python scripts/create_capstone_notebook.py

# Render Power BI Preview Graphic
python scripts/generate_powerbi_preview_image.py
```

---

## ✅ Deliverables Checklist

- [x] **1. Perform EDA on dataset**: Complete statistical and visual audit across Country, Segment, Product, and Discount Bands.
- [x] **2. Create a regression model to predict sales**: Trained Linear Regression ($R^2 = 0.9934$) and Random Forest ($R^2 = 0.9841$).
- [x] **3. Build a Power BI dashboard**: Star Schema data model, 14 DAX measures, interactive HTML5 simulator, and layout previews.
- [x] **4. Write summary of findings & recommendations**: Comprehensive executive stakeholder presentation report.
- [x] **5. Submit final report**:
  - 📗 **Excel Report**: `Week4_Financial_Analysis_Report.xlsx`
  - 🐍 **Python Notebook**: `Week4_Capstone_EDA_and_Regression.ipynb`
  - 📊 **Power BI Assets**: `DAX_Measures_and_Data_Model.md` & `dashboard_preview.html`
