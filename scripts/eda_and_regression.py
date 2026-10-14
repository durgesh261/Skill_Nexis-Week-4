"""
Week 4: Capstone Project — Exploratory Data Analysis & Machine Learning Regression Model
Dataset: Microsoft Financial Sample Dataset (financial_sample.xlsx)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def run_eda_and_regression():
    print("=" * 80)
    print("WEEK 4: CAPSTONE PROJECT — EDA & SALES REGRESSION MODELING")
    print("=" * 80)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(script_dir, "..", "data", "financial_sample.xlsx")
    cleaned_csv_path = os.path.join(script_dir, "..", "data", "cleaned_financial_sample.csv")
    visuals_dir = os.path.join(script_dir, "..", "visuals")
    os.makedirs(visuals_dir, exist_ok=True)
    
    # -------------------------------------------------------------------------
    # Step 1: Ingestion & Data Cleaning
    # -------------------------------------------------------------------------
    print("\n[Step 1] Loading and cleaning Financial Sample dataset...")
    df = pd.read_excel(raw_path)
    
    # Standardize column headers (remove leading/trailing whitespaces)
    df.columns = df.columns.str.strip()
    
    # String columns strip
    for col in ['Segment', 'Country', 'Product', 'Discount Band']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            
    # Check nulls and duplicates
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Missing Values Count: {df.isnull().sum().sum()}")
    print(f"Duplicate Rows Count: {df.duplicated().sum()}")
    
    # Feature engineering
    df['Profit_Margin_%'] = (df['Profit'] / df['Sales'] * 100).round(2)
    df['Effective_Discount_%'] = (df['Discounts'] / df['Gross Sales'] * 100).round(2)
    
    # Save cleaned CSV
    df.to_csv(cleaned_csv_path, index=False)
    print(f"-> Cleaned dataset exported to: {cleaned_csv_path}")

    # -------------------------------------------------------------------------
    # Step 2: Exploratory Data Analysis (EDA)
    # -------------------------------------------------------------------------
    print("\n[Step 2] Executing Exploratory Data Analysis (EDA)...")
    
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_units = df['Units Sold'].sum()
    overall_margin = (total_profit / total_sales) * 100
    
    print(f"• Global Net Sales Revenue : ${total_sales:,.2f}")
    print(f"• Total Net Profit          : ${total_profit:,.2f}")
    print(f"• Total Units Sold          : {total_units:,.0f} units")
    print(f"• Overall Profit Margin     : {overall_margin:.2f}%")
    
    # Styling
    sns.set_theme(style="whitegrid", palette="deep")
    plt.rcParams["font.family"] = "sans-serif"
    
    # Chart 1: Sales and Profit by Country
    print("\n[Chart 1] Generating Sales & Profit by Country bar chart...")
    country_summary = df.groupby('Country')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(country_summary))
    width = 0.35
    
    rects1 = ax.bar(x - width/2, country_summary['Sales'] / 1e6, width, label='Sales ($M)', color='#1F4E79')
    rects2 = ax.bar(x + width/2, country_summary['Profit'] / 1e6, width, label='Profit ($M)', color='#2E75B6')
    
    ax.set_ylabel('Amount in Millions USD ($M)', fontsize=11)
    ax.set_title('Financial Performance by Country (Net Sales vs. Net Profit)', fontsize=14, fontweight='bold', pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(country_summary.index, fontsize=10)
    ax.legend()
    plt.tight_layout()
    p1 = os.path.join(visuals_dir, 'eda_sales_by_country.png')
    plt.savefig(p1, dpi=300)
    plt.close()
    print(f"-> Saved: {p1}")

    # Chart 2: Segment Breakdown (Horizontal Bar)
    print("\n[Chart 2] Generating Segment Breakdown chart...")
    seg_summary = df.groupby('Segment').agg(
        Sales=('Sales', 'sum'),
        Profit=('Profit', 'sum')
    ).sort_values(by='Sales', ascending=True)
    
    plt.figure(figsize=(9, 5))
    plt.barh(seg_summary.index, seg_summary['Sales'] / 1e6, color='#2E75B6', alpha=0.9, label='Sales ($M)')
    plt.barh(seg_summary.index, seg_summary['Profit'] / 1e6, color='#5B9BD5', alpha=0.9, label='Profit ($M)')
    plt.title('Revenue & Profit Distribution Across Market Segments', fontsize=14, fontweight='bold', pad=12)
    plt.xlabel('Amount in Millions USD ($M)', fontsize=11)
    plt.legend()
    plt.tight_layout()
    p2 = os.path.join(visuals_dir, 'eda_segment_performance.png')
    plt.savefig(p2, dpi=300)
    plt.close()
    print(f"-> Saved: {p2}")

    # Chart 3: Product Profitability
    print("\n[Chart 3] Generating Product Performance chart...")
    prod_summary = df.groupby('Product')[['Gross Sales', 'Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
    plt.figure(figsize=(9, 5))
    prod_summary[['Sales', 'Profit']].div(1e6).plot(kind='bar', color=['#1F4E79', '#D9534F'], figsize=(9, 5))
    plt.title('Product Revenue and Net Profit Comparison', fontsize=14, fontweight='bold', pad=12)
    plt.ylabel('Amount in Millions USD ($M)', fontsize=11)
    plt.xlabel('Product Family', fontsize=11)
    plt.xticks(rotation=0)
    plt.tight_layout()
    p3 = os.path.join(visuals_dir, 'eda_product_profitability.png')
    plt.savefig(p3, dpi=300)
    plt.close()
    print(f"-> Saved: {p3}")

    # Chart 4: Impact of Discount Bands on Profit Margin
    print("\n[Chart 4] Generating Discount Band vs Profit Margin boxplot...")
    plt.figure(figsize=(8, 5))
    order_bands = ['None', 'Low', 'Medium', 'High']
    sns.boxplot(data=df, x='Discount Band', y='Profit_Margin_%', order=order_bands, palette='Blues_r')
    plt.axhline(0, color='red', linestyle='--', linewidth=1, label='Break-Even (0% Margin)')
    plt.title('Impact of Discount Bands on Net Profit Margin (%)', fontsize=14, fontweight='bold', pad=12)
    plt.xlabel('Discount Band Tier', fontsize=11)
    plt.ylabel('Profit Margin (%)', fontsize=11)
    plt.legend()
    plt.tight_layout()
    p4 = os.path.join(visuals_dir, 'eda_discount_vs_profit_margin.png')
    plt.savefig(p4, dpi=300)
    plt.close()
    print(f"-> Saved: {p4}")

    # -------------------------------------------------------------------------
    # Step 3: Machine Learning Regression Modeling (Predicting Sales)
    # -------------------------------------------------------------------------
    print("\n[Step 3] Building Machine Learning Regression Model to Predict Sales...")
    
    # Feature Selection
    features = ['Units Sold', 'Manufacturing Price', 'Sale Price', 'Discounts', 'COGS', 
                'Segment', 'Country', 'Product', 'Discount Band']
    target = 'Sales'
    
    X = df[features].copy()
    y = df[target].copy()
    
    # One-Hot Encoding for categorical features
    X_encoded = pd.get_dummies(X, drop_first=True)
    
    # Train / Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.20, random_state=42)
    print(f"Training Set: {X_train.shape[0]} samples | Testing Set: {X_test.shape[0]} samples")
    
    # 1. Linear Regression Model
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    
    r2_lr = r2_score(y_test, y_pred_lr)
    rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
    mae_lr = mean_absolute_error(y_test, y_pred_lr)
    
    # 2. Random Forest Regressor Model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    
    r2_rf = r2_score(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    
    print("\n================ MODEL EVALUATION METRICS ================")
    print(f"Linear Regression  -> R²: {r2_lr:.4f} | RMSE: ${rmse_lr:,.2f} | MAE: ${mae_lr:,.2f}")
    print(f"Random Forest Reg  -> R²: {r2_rf:.4f} | RMSE: ${rmse_rf:,.2f} | MAE: ${mae_rf:,.2f}")
    print("==========================================================")
    
    # Chart 5: Actual vs Predicted Sales Plot
    print("\n[Chart 5] Generating Actual vs Predicted Sales plot...")
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test / 1e3, y_pred_rf / 1e3, color='#1F4E79', alpha=0.75, edgecolors='k', s=50, label='Test Predictions')
    # 45 degree perfect prediction line
    lims = [0, max(y_test.max(), y_pred_rf.max()) / 1e3]
    plt.plot(lims, lims, color='#D9534F', linestyle='--', linewidth=2, label='Perfect Fit (Y = X)')
    plt.title(f'Sales Prediction Accuracy (Random Forest: R² = {r2_rf:.4f})', fontsize=14, fontweight='bold', pad=12)
    plt.xlabel('Actual Sales ($K USD)', fontsize=11)
    plt.ylabel('Predicted Sales ($K USD)', fontsize=11)
    plt.legend()
    plt.tight_layout()
    p5 = os.path.join(visuals_dir, 'regression_actual_vs_predicted.png')
    plt.savefig(p5, dpi=300)
    plt.close()
    print(f"-> Saved: {p5}")

    # Chart 6: Feature Importance Analysis
    print("\n[Chart 6] Generating Feature Importance plot...")
    importances = pd.Series(rf_model.feature_importances_, index=X_encoded.columns).sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(9, 5))
    importances.sort_values(ascending=True).plot(kind='barh', color='#2E75B6')
    plt.title('Top 10 Feature Importances in Predicting Sales Revenue', fontsize=14, fontweight='bold', pad=12)
    plt.xlabel('Relative Importance Weight', fontsize=11)
    plt.tight_layout()
    p6 = os.path.join(visuals_dir, 'regression_feature_importance.png')
    plt.savefig(p6, dpi=300)
    plt.close()
    print(f"-> Saved: {p6}")

    print("\n" + "=" * 80)
    print("EDA & REGRESSION MODELING PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_eda_and_regression()
