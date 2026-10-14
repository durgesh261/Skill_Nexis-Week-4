# Power BI Data Model Architecture & DAX Measures Library
**Project**: Week 4 Capstone — Enterprise Financial Analytics & Performance Dashboard  
**Dataset**: Microsoft Financial Sample (`financial_sample.xlsx` / 700 Records)  
**Author**: Durgesh (Data Analyst)

---

## 1. Dimensional Data Model Architecture (Star Schema)

To adhere to enterprise Power BI best practices, the flat financial dataset is modeled into a Star Schema with a central Fact table and supporting Dimension tables:

```
                  +-------------------+
                  |      DimDate      |
                  +-------------------+
                  | Date (PK)         |
                  | Year              |
                  | Quarter           |
                  | MonthName         |
                  | MonthNumber       |
                  +---------+---------+
                            | 1
                            |
                            | *
+-----------------+       +--+------------------------+       +-------------------+
|   DimGeography  |       |     FactFinancialSales    |       |     DimProduct    |
+-----------------+       +---------------------------+       +-------------------+
| Country (PK)    |1 --- *| SalesID (PK)              |* --- 1| Product (PK)      |
| Region          |       | Date (FK)                 |       | ProductFamily     |
| Currency        |       | Country (FK)              |       | ManufacturingPrice|
+-----------------+       | Product (FK)              |       +-------------------+
                          | Segment (FK)              |
                          | DiscountBand              |
                          | UnitsSold                 |
                          | SalePrice                 |
                          | GrossSales                |
                          | Discounts                 |
                          | Sales                     |
                          | COGS                      |
                          | Profit                    |
                          +-------------+-------------+
                                        | *
                                        |
                                        | 1
                              +---------+---------+
                              |    DimSegment     |
                              +-------------------+
                              | Segment (PK)      |
                              | SegmentCategory   |
                              +-------------------+
```

---

## 2. Core DAX Measure Calculations

### 2.1 Base Financial Measures

#### 1. Total Net Sales
```dax
Total Sales = 
SUM(FactFinancialSales[Sales])
```
*Format: Currency (`$#,##0.00`)*

#### 2. Total Net Profit
```dax
Total Profit = 
SUM(FactFinancialSales[Profit])
```
*Format: Currency (`$#,##0.00`)*

#### 3. Total Cost of Goods Sold (COGS)
```dax
Total COGS = 
SUM(FactFinancialSales[COGS])
```
*Format: Currency (`$#,##0.00`)*

#### 4. Total Discounts
```dax
Total Discounts = 
SUM(FactFinancialSales[Discounts])
```
*Format: Currency (`$#,##0.00`)*

#### 5. Total Units Sold
```dax
Total Units Sold = 
SUM(FactFinancialSales[Units Sold])
```
*Format: Whole Number (`#,##0`)*

---

### 2.2 Financial Margins & Ratio Measures

#### 6. Net Profit Margin (%)
```dax
Profit Margin % = 
DIVIDE(
    [Total Profit],
    [Total Sales],
    0
)
```
*Format: Percentage (`0.00%`)*

#### 7. Effective Discount Rate (%)
```dax
Effective Discount % = 
DIVIDE(
    [Total Discounts],
    SUM(FactFinancialSales[Gross Sales]),
    0
)
```
*Format: Percentage (`0.00%`)*

#### 8. Average Sale Price per Unit
```dax
Avg Realized Price = 
DIVIDE(
    [Total Sales],
    [Total Units Sold],
    0
)
```
*Format: Currency (`$#,##0.00`)*

---

### 2.3 Time-Intelligence Calculations (YoY & YTD)

#### 9. Sales Prior Year (PY)
```dax
Sales Prior Year = 
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(DimDate[Date])
)
```

#### 10. Year-over-Year (YoY) Sales Growth ($)
```dax
Sales YoY Growth $ = 
[Total Sales] - [Sales Prior Year]
```

#### 11. Year-over-Year (YoY) Sales Growth (%)
```dax
Sales YoY Growth % = 
DIVIDE(
    [Sales YoY Growth $],
    [Sales Prior Year],
    BLANK()
)
```
*Format: Percentage (`+0.00%;-0.00%;0.00%`)*

#### 12. Year-to-Date (YTD) Sales
```dax
Sales YTD = 
TOTALYTD(
    [Total Sales],
    DimDate[Date]
)
```

---

### 2.4 Conditional Formatting & KPI Indicators

#### 13. Profit Margin Health Status
```dax
Margin Status Indicator = 
VAR Margin = [Profit Margin %]
RETURN
    SWITCH(
        TRUE(),
        Margin >= 0.18, "🟢 Healthy (>= 18%)",
        Margin >= 0.10, "🟡 Moderate (10% - 18%)",
        "🔴 At Risk (< 10%)"
    )
```

#### 14. Top Performing Product by Sales
```dax
Top Product Name = 
TOPN(
    1,
    VALUES(FactFinancialSales[Product]),
    [Total Sales],
    DESC
)
```

---

## 3. Recommended Power BI Dashboard Layout & Visual Components

| Visual Component | Chart Type | Fields / Dimensions | Purpose |
| :--- | :--- | :--- | :--- |
| **KPI Banner 1** | Card Visual | `[Total Sales]` ($118.73M) | Global Revenue pulse |
| **KPI Banner 2** | Card Visual | `[Total Profit]` ($16.89M) | Net Profit generated |
| **KPI Banner 3** | Card Visual | `[Profit Margin %]` (14.23%) | Operational margin efficiency |
| **KPI Banner 4** | Card Visual | `[Total Units Sold]` (1.13M) | Sales volume throughput |
| **Geographic Matrix** | Clustered Column Chart | Country vs. `[Total Sales]` & `[Total Profit]` | Compare market profitability |
| **Segment Contribution** | Treemap / Donut Chart | Segment vs. `[Total Sales]` | Identify channel dependencies |
| **Product Portfolio** | Stacked Bar Chart | Product vs. `[Total Sales]` | Rank revenue by product line |
| **Discount Elasticity** | Scatter / Box Plot | Discount Band vs. `[Profit Margin %]` | Detect margin leakage |
| **Global Slicers** | Dropdown / Tiles | `Country`, `Segment`, `Year`, `Discount Band` | Interactive multidimensional filtering |

---

## 4. How to Import and Recreate in Power BI Desktop

1. Open **Power BI Desktop**.
2. Click **Get Data** > **Excel Workbook** > Select `Week-04/data/financial_sample.xlsx` or `cleaned_financial_sample.csv`.
3. In Power Query Editor, verify data types (`Sales`, `Profit`, `Discounts`, `COGS` as Currency/Decimal, `Date` as Date).
4. Create a new Table for measures: `_DAX Measures`.
5. Copy and paste each measure from Section 2 above into the formula bar.
6. Assemble the canvas according to the layout matrix in Section 3.
7. Save the dashboard as `Week4_Financial_Executive_Dashboard.pbix`.
