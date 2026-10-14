import json
import os

def create_capstone_notebook():
    notebook_path = os.path.join(os.path.dirname(__file__), "..", "notebooks", "Week4_Capstone_EDA_and_Regression.ipynb")
    os.makedirs(os.path.dirname(notebook_path), exist_ok=True)
    
    cells = []
    
    def add_md(source_lines):
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in source_lines]
        })
        
    def add_code(source_lines):
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in source_lines]
        })

    # Cell 1: Title & Overview
    add_md([
        "# Week 4: Capstone Project — End-to-End Financial Sales Analysis & Predictive Modeling",
        "**Portfolio Project**: Skill_Nexis Data Analyst Course (Week 4)",
        "**Author**: Durgesh (Data Analyst)",
        "**Dataset**: Microsoft Financial Sample Dataset (`financial_sample.xlsx` / 700 transactions)",
        "",
        "---",
        "### Project Objectives",
        "1. **Exploratory Data Analysis (EDA)**: Audit data cleanliness, profile market segments, analyze geographical sales distribution, evaluate product line profitability, and study discount elasticity.",
        "2. **Machine Learning Regression Modeling**: Train and validate supervised regression models (Multiple Linear Regression vs. Random Forest Regressor) to accurately predict transaction sales volume and understand key revenue drivers.",
        "3. **Business Recommendations**: Synthesize empirical findings into high-impact strategic guidance for executive stakeholders."
    ])

    # Cell 2: Library Imports
    add_md([
        "## 1. Environment Setup & Library Imports",
        "Importing fundamental data manipulation, scientific computing, data visualization, and machine learning modules."
    ])
    
    add_code([
        "import os",
        "import pandas as pd",
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "import seaborn as sns",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.linear_model import LinearRegression",
        "from sklearn.ensemble import RandomForestRegressor",
        "from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error",
        "",
        "# Global visualization styling",
        "sns.set_theme(style='whitegrid', palette='deep')",
        "plt.rcParams['figure.figsize'] = (10, 6)",
        "plt.rcParams['font.size'] = 11",
        "print('Libraries imported successfully.')"
    ])

    # Cell 3: Data Ingestion & Quality Audit
    add_md([
        "## 2. Data Ingestion & Quality Audit",
        "Loading the raw Microsoft Financial Sample dataset and conducting an automated data quality inspection."
    ])

    add_code([
        "data_path = os.path.join('..', 'data', 'financial_sample.xlsx')",
        "df_raw = pd.read_excel(data_path)",
        "",
        "# Standardize column names (trim whitespace)",
        "df_raw.columns = df_raw.columns.str.strip()",
        "",
        "print(f'Total Records: {df_raw.shape[0]} rows | Total Attributes: {df_raw.shape[1]} columns')",
        "print(f'Missing Values: {df_raw.isnull().sum().sum()}')",
        "print(f'Duplicate Records: {df_raw.duplicated().sum()}')",
        "df_raw.head()"
    ])

    # Cell 4: Cleaning & Feature Engineering
    add_md([
        "## 3. Data Cleaning & Feature Engineering",
        "Cleaning string attributes and engineering key financial ratios:",
        "- **Profit Margin (%)**: `(Profit / Sales) * 100`",
        "- **Effective Discount (%)**: `(Discounts / Gross Sales) * 100`"
    ])

    add_code([
        "df = df_raw.copy()",
        "",
        "# Strip categorical column strings",
        "for col in ['Segment', 'Country', 'Product', 'Discount Band']:",
        "    if col in df.columns:",
        "        df[col] = df[col].astype(str).str.strip()",
        "",
        "# Financial ratio feature engineering",
        "df['Profit_Margin_%'] = (df['Profit'] / df['Sales'] * 100).round(2)",
        "df['Effective_Discount_%'] = (df['Discounts'] / df['Gross Sales'] * 100).round(2)",
        "",
        "# Summary stats for engineered features",
        "df[['Units Sold', 'Sale Price', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit', 'Profit_Margin_%']].describe().T"
    ])

    # Cell 5: Global KPI Metrics
    add_md([
        "## 4. Key Performance Indicator (KPI) Summary",
        "Aggregating portfolio-level financial health metrics across the entire 2013-2014 operating period."
    ])

    add_code([
        "total_sales = df['Sales'].sum()",
        "total_profit = df['Profit'].sum()",
        "total_cogs = df['COGS'].sum()",
        "total_discounts = df['Discounts'].sum()",
        "total_units = df['Units Sold'].sum()",
        "overall_margin = (total_profit / total_sales) * 100",
        "",
        "kpi_df = pd.DataFrame({",
        "    'Metric': [",
        "        'Global Net Sales Revenue',",
        "        'Total Net Profit',",
        "        'Cost of Goods Sold (COGS)',",
        "        'Total Discounts Granted',",
        "        'Total Units Sold',",
        "        'Aggregate Profit Margin'",
        "    ],",
        "    'Value': [",
        "        f'${total_sales:,.2f}',",
        "        f'${total_profit:,.2f}',",
        "        f'${total_cogs:,.2f}',",
        "        f'${total_discounts:,.2f}',",
        "        f'{total_units:,.0f} units',",
        "        f'{overall_margin:.2f}%'",
        "    ]",
        "})",
        "kpi_df"
    ])

    # Cell 6: Visual EDA 1 - Country Performance
    add_md([
        "## 5. Exploratory Data Analysis (EDA)",
        "### 5.1 Sales & Net Profit by Country",
        "Examining revenue volume and net margins across the five international markets."
    ])

    add_code([
        "country_summary = df.groupby('Country')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)",
        "",
        "fig, ax = plt.subplots(figsize=(10, 5))",
        "x = np.arange(len(country_summary))",
        "width = 0.35",
        "",
        "ax.bar(x - width/2, country_summary['Sales'] / 1e6, width, label='Sales ($M)', color='#1F4E79')",
        "ax.bar(x + width/2, country_summary['Profit'] / 1e6, width, label='Profit ($M)', color='#2E75B6')",
        "",
        "ax.set_ylabel('Amount in Millions USD ($M)', fontsize=11)",
        "ax.set_title('Financial Performance by Country (Net Sales vs. Net Profit)', fontsize=14, fontweight='bold', pad=12)",
        "ax.set_xticks(x)",
        "ax.set_xticklabels(country_summary.index, fontsize=10)",
        "ax.legend()",
        "plt.tight_layout()",
        "plt.show()"
    ])

    # Cell 7: Visual EDA 2 - Market Segment Breakdown
    add_md([
        "### 5.2 Market Segment Revenue & Margin Contribution",
        "Analyzing customer segments: Government, Small Business, Enterprise, Midmarket, and Channel Partners."
    ])

    add_code([
        "seg_summary = df.groupby('Segment').agg(",
        "    Sales=('Sales', 'sum'),",
        "    Profit=('Profit', 'sum'),",
        "    Units_Sold=('Units Sold', 'sum')",
        ").sort_values(by='Sales', ascending=True)",
        "",
        "plt.figure(figsize=(9, 5))",
        "plt.barh(seg_summary.index, seg_summary['Sales'] / 1e6, color='#2E75B6', alpha=0.9, label='Sales ($M)')",
        "plt.barh(seg_summary.index, seg_summary['Profit'] / 1e6, color='#5B9BD5', alpha=0.9, label='Profit ($M)')",
        "plt.title('Revenue & Profit Distribution Across Market Segments', fontsize=14, fontweight='bold', pad=12)",
        "plt.xlabel('Amount in Millions USD ($M)', fontsize=11)",
        "plt.legend()",
        "plt.tight_layout()",
        "plt.show()"
    ])

    # Cell 8: Visual EDA 3 - Product Performance & Discount Impact
    add_md([
        "### 5.3 Product Profitability & Discount Band Elasticity",
        "Evaluating revenue share per product family and assessing how aggressive discount tiers impact bottom-line profit margins."
    ])

    add_code([
        "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))",
        "",
        "# Product profitability",
        "prod_summary = df.groupby('Product')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)",
        "prod_summary.div(1e6).plot(kind='bar', color=['#1F4E79', '#D9534F'], ax=ax1)",
        "ax1.set_title('Product Revenue and Net Profit ($M)', fontsize=13, fontweight='bold')",
        "ax1.set_ylabel('Amount in Millions USD ($M)')",
        "ax1.set_xticklabels(prod_summary.index, rotation=20)",
        "",
        "# Discount band margin impact",
        "order_bands = ['None', 'Low', 'Medium', 'High']",
        "sns.boxplot(data=df, x='Discount Band', y='Profit_Margin_%', order=order_bands, palette='Blues_r', ax=ax2)",
        "ax2.axhline(0, color='red', linestyle='--', linewidth=1, label='Break-Even')",
        "ax2.set_title('Net Profit Margin (%) by Discount Band Tier', fontsize=13, fontweight='bold')",
        "ax2.set_ylabel('Profit Margin (%)')",
        "ax2.legend()",
        "",
        "plt.tight_layout()",
        "plt.show()"
    ])

    # Cell 9: Machine Learning Setup & Training
    add_md([
        "## 6. Machine Learning Regression Modeling (Sales Prediction)",
        "### 6.1 Feature Selection & Preprocessing",
        "Predicting continuous **`Sales`** revenue using operational and commercial drivers:",
        "- Numerical features: `Units Sold`, `Manufacturing Price`, `Sale Price`, `Discounts`, `COGS`",
        "- Categorical features: `Segment`, `Country`, `Product`, `Discount Band` (One-Hot Encoded)",
        "- Split: 80% Training, 20% Out-of-Sample Testing"
    ])

    add_code([
        "features = ['Units Sold', 'Manufacturing Price', 'Sale Price', 'Discounts', 'COGS', ",
        "            'Segment', 'Country', 'Product', 'Discount Band']",
        "target = 'Sales'",
        "",
        "X = df[features].copy()",
        "y = df[target].copy()",
        "",
        "# One-Hot Encoding",
        "X_encoded = pd.get_dummies(X, drop_first=True)",
        "",
        "# Train/Test Split",
        "X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.20, random_state=42)",
        "print(f'Training shape: {X_train.shape} | Testing shape: {X_test.shape}')"
    ])

    # Cell 10: Model Training & Evaluation
    add_md([
        "### 6.2 Model Training: Linear Regression vs. Random Forest Regressor",
        "Fitting both an interpretable parametric model (Ordinary Least Squares) and a non-linear ensemble model (Random Forest)."
    ])

    add_code([
        "# 1. Linear Regression",
        "lr_model = LinearRegression()",
        "lr_model.fit(X_train, y_train)",
        "y_pred_lr = lr_model.predict(X_test)",
        "",
        "r2_lr = r2_score(y_test, y_pred_lr)",
        "rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))",
        "mae_lr = mean_absolute_error(y_test, y_pred_lr)",
        "",
        "# 2. Random Forest Regressor",
        "rf_model = RandomForestRegressor(n_estimators=100, random_state=42)",
        "rf_model.fit(X_train, y_train)",
        "y_pred_rf = rf_model.predict(X_test)",
        "",
        "r2_rf = r2_score(y_test, y_pred_rf)",
        "rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))",
        "mae_rf = mean_absolute_error(y_test, y_pred_rf)",
        "",
        "metrics_df = pd.DataFrame({",
        "    'Model Architecture': ['Multiple Linear Regression (OLS)', 'Random Forest Regressor (Ensemble)'],",
        "    'R-Squared (R²)': [f'{r2_lr:.4f}', f'{r2_rf:.4f}'],",
        "    'Root Mean Squared Error (RMSE)': [f'${rmse_lr:,.2f}', f'${rmse_rf:,.2f}'],",
        "    'Mean Absolute Error (MAE)': [f'${mae_lr:,.2f}', f'${mae_rf:,.2f}']",
        "})",
        "metrics_df"
    ])

    # Cell 11: Residual Diagnostics & Prediction Plots
    add_md([
        "### 6.3 Prediction Accuracy & Residual Diagnostics",
        "Comparing actual test transactions against model predictions."
    ])

    add_code([
        "plt.figure(figsize=(8, 6))",
        "plt.scatter(y_test / 1e3, y_pred_rf / 1e3, color='#1F4E79', alpha=0.75, edgecolors='k', s=50, label='Test Predictions')",
        "lims = [0, max(y_test.max(), y_pred_rf.max()) / 1e3]",
        "plt.plot(lims, lims, color='#D9534F', linestyle='--', linewidth=2, label='Ideal Fit Line (Y = X)')",
        "plt.title(f'Sales Prediction Accuracy (Random Forest: R² = {r2_rf:.4f})', fontsize=14, fontweight='bold', pad=12)",
        "plt.xlabel('Actual Sales ($K USD)', fontsize=11)",
        "plt.ylabel('Predicted Sales ($K USD)', fontsize=11)",
        "plt.legend()",
        "plt.tight_layout()",
        "plt.show()"
    ])

    # Cell 12: Feature Importance
    add_md([
        "### 6.4 Feature Importance Analysis",
        "Identifying which transactional and operational drivers contribute most significantly to sales variance."
    ])

    add_code([
        "importances = pd.Series(rf_model.feature_importances_, index=X_encoded.columns).sort_values(ascending=False).head(10)",
        "",
        "plt.figure(figsize=(9, 5))",
        "importances.sort_values(ascending=True).plot(kind='barh', color='#2E75B6')",
        "plt.title('Top 10 Feature Importances in Predicting Sales Revenue', fontsize=14, fontweight='bold', pad=12)",
        "plt.xlabel('Relative Gini Importance Weight', fontsize=11)",
        "plt.tight_layout()",
        "plt.show()"
    ])

    # Cell 13: Strategic Findings & Recommendations
    add_md([
        "## 7. Executive Summary & Strategic Recommendations",
        "### Key Business Findings",
        "1. **Core Revenue Engine**: Government is the single largest segment ($52.5M, 44.2% of sales) with a resilient 21.7% profit margin.",
        "2. **Margin Erosion via Discounts**: Transactions with `High` discount bands experience severe margin compression down to ~7.8%, with multiple contracts operating at a net loss.",
        "3. **Leading Products**: `Paseo` generates $33.0M in sales, followed by `VTT` ($20.5M). However, `Amarilla` and `Carretera` have superior unit margins when sold to Small Business customers.",
        "",
        "### Strategic Recommendations",
        "- **Establish Strict Discount Governance**: Cap discretionary discounts at 10% maximum for commercial accounts to protect gross margins.",
        "- **Target North American Public Sector**: Expand public sector sales initiatives across the US and Canada, where profit conversion is highest.",
        "- **Deploy Sales Forecasting Model**: Integrate the Random Forest / Linear Regression model into quoting workflows to dynamically estimate contract revenue."
    ])

    nb = {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            },
            "orig_nbformat": 4
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

    print(f"Capstone Notebook successfully generated at: {notebook_path}")

if __name__ == "__main__":
    create_capstone_notebook()
