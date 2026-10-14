# Executive Stakeholder Briefing: Commercial Performance & Predictive Sales Modeling
**Capstone Project**: Skill_Nexis Data Analyst Program — Week 4  
**Presenter**: Durgesh (Lead Data Analyst)  
**Target Audience**: Executive Leadership, VP of Global Sales, Chief Commercial Officer, Regional Managing Directors  
**Dataset**: Microsoft Financial Sample (700 Transactions across North America & Europe, FY 2013–2014)

---

## 1. Executive Summary

During FY 2013–2014, global commercial operations generated **$118,726,350.26 in Net Sales** across **1,125,806 units sold**, yielding **$16,893,702.26 in Net Operating Profit** (an overall **14.23% net margin**).

While topline revenues demonstrate consistent double-digit expansion, comprehensive Exploratory Data Analysis (EDA) and Machine Learning regression modeling reveal acute operational variances across customer segments, pricing bands, and geographical territories. Most critically:
- **Government accounts represent the primary growth engine**, delivering **44.2% of total sales ($52.51M)** and **67.4% of total net profits ($11.39M)** at a stellar **21.70% margin**.
- **Enterprise contracts are currently operating at a net loss (-3.17% margin / -$622K loss)** due to aggressive unconstrained discounting combined with elevated production cost profiles.
- **High Discount bands destroy margins**: Heavy discounting compresses margins from **19.5% down to 7.8%**, without generating commensurate volume velocity.
- **Machine Learning Sales Predictor**: A Random Forest regression model was trained and validated, achieving an **$R^2$ score of 0.9841** and an MAE of **$18,924.58**, empowering commercial teams to forecast transaction revenue prior to contract execution.

---

## 2. Core Empirical Findings from Exploratory Data Analysis (EDA)

### 2.1 Geographic Distribution & Market Realization

| Country | Net Sales ($M) | Gross Sales ($M) | Discounts ($M) | Net Profit ($M) | Profit Margin (%) | Units Sold |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **United States** | **$25.03M** | $27.56M | $2.53M | **$2.99M** | 11.97% | 232,627 |
| **Canada** | **$24.89M** | $26.93M | $2.04M | **$3.53M** | 14.18% | 247,428 |
| **France** | **$24.31M** | $26.11M | $1.80M | **$3.78M** | **15.57%** | 240,931 |
| **Germany** | **$23.51M** | $25.29M | $1.78M | **$3.68M** | 15.65% | 201,489 |
| **Mexico** | **$20.99M** | $22.00M | $1.01M | **$2.91M** | 13.84% | 203,331 |
| **Total / Global** | **$118.73M** | **$127.93M** | **$9.21M** | **$16.89M** | **14.23%** | **1,125,806** |

**Key Takeaways:**
1. **Balanced Regional Footprint**: Revenue is exceptionally well distributed across all five territories (ranging between 17.7% in Mexico and 21.1% in the USA), insulating the enterprise against localized shocks.
2. **European Margin Premium**: France and Germany deliver higher margin conversion (**~15.6%**) compared to the USA (**11.97%**), driven by stronger product mix stability and lower price discounting.

---

### 2.2 Customer Segment Breakdown & The Enterprise Deficit

| Customer Segment | Units Sold | Net Sales ($M) | % Revenue | Net Profit ($M) | Margin (%) | Commercial Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Government** | 470,490 | **$52.51M** | 44.2% | **$11.39M** | **21.70%** | 🟢 Primary Profit Engine |
| **Small Business** | 184,332 | **$42.42M** | 35.7% | **$4.14M** | **9.76%** | 🟡 Volume Driver / Moderate Margin |
| **Enterprise** | 202,937 | **$19.65M** | 16.5% | **-$0.62M** | **-3.17%** | 🔴 Unprofitable Deficit Segment |
| **Midmarket** | 172,178 | **$2.38M** | 2.0% | **$0.66M** | **27.71%** | 🟢 Niche / High Margin |
| **Channel Partners** | 95,869 | **$1.77M** | 1.5% | **$1.33M** | **74.83%** | 🟢 Pure Commission Margin |

**Critical Strategic Insight:**  
The **Enterprise segment is burning cash (-$622K deficit)** despite contributing nearly $20M in top-line sales. Large corporate buyers are receiving steep enterprise discounts without committing to high-margin service attachments or volume commitments necessary to offset fixed Cost of Goods Sold.

---

### 2.3 Product Family Profitability Ranking

1. **Paseo**: Dominant flagship line with **$33.01M in Net Sales** and **$4.80M Net Profit** (14.5% margin; 338,239 units).
2. **VTT**: Second largest volume contributor with **$20.51M in Net Sales** and **$3.03M Net Profit** (14.8% margin).
3. **Amarilla**: Strong mid-tier performer with **$19.04M in Net Sales** and **$2.81M Net Profit** (14.8% margin).
4. **Carretera**: **$15.62M Net Sales** and **$2.12M Net Profit** (13.6% margin).
5. **Montana**: **$15.39M Net Sales** and **$2.11M Net Profit** (13.7% margin).
6. **Velo**: **$15.17M Net Sales** and **$2.02M Net Profit** (13.3% margin).

All six product families exhibit consistent ~13.3% to 14.8% baseline profitability, demonstrating that unit margin erosion is driven by **segment contract terms and discounting** rather than inherent manufacturing defects or raw material cost spikes.

---

### 2.4 The Risk of Unmonitored Discounting

Across 700 transactions:
- **None Discount Tier**: Average Net Profit Margin is **19.48%**.
- **Low Discount Tier**: Average Net Profit Margin is **15.12%**.
- **Medium Discount Tier**: Average Net Profit Margin is **12.35%**.
- **High Discount Tier**: Average Net Profit Margin drops to **7.81%** (with over 18% of individual transactions posting outright net losses).

---

## 3. Machine Learning Predictive Sales Modeling

### 3.1 Model Formulation & Objective
To prevent margin leakage and enable dynamic sales quota setting, we developed a supervised regression model predicting transactional **`Sales`** revenue using operational drivers:
- **Numerical Inputs**: `Units Sold`, `Manufacturing Price`, `Sale Price`, `Discounts`, `COGS`.
- **Categorical Factors (One-Hot Encoded)**: `Segment`, `Country`, `Product`, `Discount Band`.
- **Validation Protocol**: 80% Training Set (560 transactions), 20% Out-of-Sample Holdout Test Set (140 transactions).

### 3.2 Model Evaluation Matrix

| Architecture | $R^2$ Score (Test) | Root Mean Squared Error (RMSE) | Mean Absolute Error (MAE) | Commercial Assessment |
| :--- | :---: | :---: | :---: | :--- |
| **Multiple Linear Regression (OLS)** | **0.9934** | **$19,121.49** | **$13,842.10** | Highly accurate for baseline pricing formulas |
| **Random Forest Regressor (100 Trees)** | **0.9841** | **$29,667.59** | **$18,924.58** | Exceptional resilience against non-linear discount thresholds |

### 3.3 Feature Importance Hierarchy
According to Random Forest Gini impurity reduction:
1. **Cost of Goods Sold (COGS)** (52.4% relative importance) — Direct scale proxy.
2. **Units Sold** (28.1% relative importance) — Fundamental volume driver.
3. **Discounts** (9.6% relative importance) — Primary price adjustment mechanism.
4. **Sale Price** (4.8% relative importance) — Unit list price tier.
5. **Product Family & Segment** (5.1% cumulative importance).

---

## 4. Power BI Performance Dashboard & Dimensional Modeling

An executive business intelligence dashboard was designed and built to monitor these dynamics continuously:
- **Interactive Slicers**: Multi-dimensional filtering by Country, Customer Segment, Operating Year, and Discount Band.
- **Enterprise Star Schema**: Implemented using a central fact table (`FactFinancialSales`) linked to conformable dimensions (`DimDate`, `DimGeography`, `DimProduct`, `DimSegment`).
- **DAX Calculations**: Standardized measures including `[Total Sales]`, `[Total Profit]`, `[Profit Margin %]`, `[Sales YoY Growth %]`, and automated conditional margin health alerting (`🟢`, `🟡`, `🔴`).
- **Interactive Simulation**: Accessible via `Week-04/powerbi_dashboard/dashboard_preview.html`.

---

## 5. Strategic Recommendations & Action Plan

### Recommendation 1: Institute an Immediate Moratorium on Deep Enterprise Discounting
- **The Problem**: Enterprise sales are generating a -$622K cumulative operating loss due to uncapped discounts.
- **The Action**: Enforce an executive approval gate for any enterprise contract exceeding an 8% discount. Require multi-year commitments or bundled maintenance tiers to protect gross margins.
- **Projected Impact**: Restoring Enterprise margins to the corporate average (14%) will add **+$3.37M in net profit** annually.

### Recommendation 2: Double Down on the Government Growth Flywheel
- **The Problem**: While Government delivers 67% of profits, sales are concentrated in standard RFP renewals.
- **The Action**: Establish dedicated federal and municipal procurement capture teams in the US and Canada. Build targeted Paseo and VTT multi-year hardware/service packages.
- **Projected Impact**: A 15% expansion in public sector sales yields **+$7.88M top-line revenue** and **+$1.71M incremental profit**.

### Recommendation 3: Embed the Regression Pricing Tool into CRM / CPQ
- **The Problem**: Sales reps currently guess discount impacts during contract negotiation.
- **The Action**: Embed the trained regression scoring model into the sales configure-price-quote (CPQ) workflow to show reps real-time predicted revenue and expected net profit before quotes are sent to prospects.
- **Projected Impact**: Elimination of negative-margin deals across all international territories.

---

## 6. Project Artifact & Deliverables Index

All source code, data pipelines, visual artifacts, and interactive models have been structured into the `Skill_Nexis-Week-4` repository:

| Deliverable | File Path | Description |
| :--- | :--- | :--- |
| **Cleaned Dataset** | [`cleaned_financial_sample.csv`](../data/cleaned_financial_sample.csv) | Standardized 700-row dataset with engineered margin ratios |
| **Excel Report** | [`Week4_Financial_Analysis_Report.xlsx`](../reports/Week4_Financial_Analysis_Report.xlsx) | Executive dashboard with Pivot Tables, KPIs, and charts |
| **Jupyter Notebook** | [`Week4_Capstone_EDA_and_Regression.ipynb`](../notebooks/Week4_Capstone_EDA_and_Regression.ipynb) | Complete end-to-end Python EDA, modeling, and evaluation |
| **Power BI DAX Specs** | [`DAX_Measures_and_Data_Model.md`](../powerbi_dashboard/DAX_Measures_and_Data_Model.md) | Star Schema data model and 14 production DAX measures |
| **Interactive BI App** | [`dashboard_preview.html`](../powerbi_dashboard/dashboard_preview.html) | Live HTML5/Chart.js simulation of Power BI dashboard |
| **Visual Gallery** | [`visuals/`](../visuals/) | 7 high-res charts (EDA, regression diagnostics, dashboard preview) |
