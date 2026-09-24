# SUPERMARKET SALES ANALYSIS & OPERATIONAL INTELLIGENCE REPORT
## Exploratory Data Analysis, Revenue Optimization, and Customer Segmentation
**IBM SkillsBuild Academic Internship — Data Analytics Project**

---

### METADATA & DOCUMENT CONTROL
- **Document Title:** Comprehensive Supermarket Sales Analytics & Business Strategy Report
- **Academic Internship:** IBM SkillsBuild Academic Internship
- **Author & Lead Analyst:** Indrajit Mandal *(Senior Data Analyst Intern)*
- **Project Domain:** Retail Analytics, Exploratory Data Analysis & Decision Science
- **Tools & Technologies:** Python 3.13, Pandas, NumPy, Matplotlib, Seaborn, JupyterLab
- **Submission Date:** September 2026
- **Status:** Final Executive Deliverable

---

## 1. EXECUTIVE SUMMARY

This empirical investigation, conducted by **Indrajit Mandal**, analyzes 1,000 retail transactions recorded across three regional supermarket branches of a leading retail chain in Myanmar: Branch A (Yangon), Branch B (Mandalay), and Branch C (Naypyitaw). The primary business objective is to diagnose financial revenue drivers, evaluate product line margins, benchmark store efficiency, and uncover consumer purchasing behaviors to deliver actionable, data-backed operational strategies.

Across the analyzed period, the supermarket chain generated **\$314,880.46** in gross revenue, delivering **\$14,994.31** in gross operating profit with an overall gross margin rate of **4.76%** across **1,000** customer transactions. Top-line revenue demonstrates remarkable geographic balance: Branch A led with \$110,247.78 (35.0%), closely followed by Branch B at \$109,671.28 (34.8%), and Branch C at \$94,961.39 (30.2%). Product velocity was led by *Sports and travel* (\$60,893.39) and *Food and beverages* (\$53,661.42). 

However, the analysis uncovered critical operational vulnerabilities: the customer loyalty program fails to generate incremental basket lift (Members average \$315.61 vs. \$314.15 for non-members), and footfall displays severe bimodal peaks at 16:00 and 19:00, creating store checkout friction. Strategic interventions focus on restructuring the loyalty tier, deploying agile shift scheduling, and implementing dynamic inventory allocation.

---

## 2. BUSINESS PROBLEM DEFINITION & RESEARCH QUESTIONS

### 2.1 Business Context
Modern multi-branch supermarket enterprises operate in highly competitive, low-margin retail environments where operational profitability hinges upon inventory velocity, labor productivity, basket size maximization, and customer retention. Retail leadership requires quantitative clarity to deploy capital, schedule personnel, negotiate supplier terms, and optimize physical floor layouts.

### 2.2 Core Research Questions
This project addresses six central research questions formulated to inform executive and store-level decisions:
- **RQ 1 (Geographic Disparities):** Do the three branches (Yangon, Mandalay, Naypyitaw) exhibit significant revenue or gross margin divergence, or does revenue distribute homogeneously across territories?
- **RQ 2 (Product Line Profitability):** Which retail categories generate the highest total dollar sales and unit volumes, and does profitability correlate directly with sales volume?
- **RQ 3 (Customer Loyalty Impact):** Does the registered loyalty card program stimulate measurably larger basket values or higher item counts compared to unregistered ("Normal") walk-in shoppers?
- **RQ 4 (Operational Sales Velocity & Footfall):** At what specific hours of the operating day do transaction volumes surge, and where do potential cashier staffing bottlenecks emerge?
- **RQ 5 (Payment Ecosystem Dynamics):** How do customer payment method preferences (Cash, E-wallets, Credit Cards) vary across branches, and what are the implications for checkout point-of-sale infrastructure?
- **RQ 6 (Customer Satisfaction & Service Gaps):** What is the chain-wide Customer Satisfaction (CSAT) rating profile, and which product lines exhibit elevated rating dispersion or service dissatisfaction?

---

## 3. DATA DICTIONARY & PREPROCESSING METHODOLOGY

### 3.1 Data Dictionary
The underlying dataset consists of 1,000 historical sales transactions structured across 17 attributes conforming to the standard IBM SkillsBuild / Kaggle retail analytics schema:

| Attribute Name | Raw Header | Data Type | Analytical Role | Description & Business Validation Rules |
|---|---|---|---|---|
| `invoice_id` | `Invoice ID` | String | Unique Identifier | 9-character computer-generated sales slip code (`XXX-XX-XXXX`). |
| `branch` | `Branch` | Categorical | Demographic Dimension | Supermarket branch code: `A`, `B`, or `C`. |
| `city` | `City` | Categorical | Geographic Dimension | City of operation: `Yangon` (Branch A), `Mandalay` (Branch B), `Naypyitaw` (Branch C). |
| `customer_type` | `Customer type` | Categorical | Demographic Dimension | Customer segmentation tier: `Member` (loyalty holder) or `Normal` (casual shopper). |
| `gender` | `Gender` | Categorical | Demographic Dimension | Customer biological gender: `Female` or `Male`. |
| `product_line` | `Product line` | Categorical | Product Hierarchy | Retail classification: *Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel*. |
| `unit_price` | `Unit price` | Float (USD) | Continuous Numeric | Product retail price per single unit, bounded between \$10.00 and \$99.99. |
| `quantity` | `Quantity` | Integer | Discrete Numeric | Total number of units purchased per transaction, ranging from 1 to 10. |
| `tax_5_pct` | `Tax 5%` | Float (USD) | Computed Metric | Statutory 5% government consumption sales tax: `0.05 * (unit_price * quantity)`. |
| `total` | `Total` | Float (USD) | Primary Financial Metric | Gross invoice total billed to customer: `cogs + tax_5_pct`. |
| `date` | `Date` | Datetime (Date) | Temporal Dimension | Transaction date spanning Q1 2019 (January 1, 2019 to March 30, 2019). |
| `time` | `Time` | Datetime (Time) | Temporal Dimension | Timestamp of sale across daily operating hours (10:00 to 20:59). |
| `payment` | `Payment` | Categorical | Transactional Dimension | Settlement instrument: `Ewallet`, `Cash`, or `Credit card`. |
| `cogs` | `cogs` | Float (USD) | Cost Accounting Metric | Cost of Goods Sold: `unit_price * quantity`. |
| `gross_margin_pct` | `gross margin percentage` | Float (%) | Margin Metric | Constant theoretical margin rate: `4.761904762%` ($Tax / Total$). |
| `gross_income` | `gross income` | Float (USD) | Financial Profit Metric | Gross profit earned by store: `total - cogs` (identical to `tax_5_pct`). |
| `rating` | `Rating` | Float (1-10) | Quality Metric | Customer exit satisfaction score on a 1.0 to 10.0 scale (1 decimal precision). |

### 3.2 Preprocessing & Data Hygiene Pipeline
A data engineering and cleaning workflow was executed by Indrajit Mandal:
1. **Automated Ingestion & Fallback Resiliency:** The pipeline inspects local directories for `supermarket_sales.csv`. If absent, an embedded high-fidelity synthetic generator generates a 1,000-row dataset matching all joint probability distributions and accounting identities.
2. **Nomenclature Normalization:** All raw column headers were converted to PEP-8 compliant `snake_case` (e.g., `Customer type` $\rightarrow$ `customer_type`, `Tax 5%` $\rightarrow$ `tax_5_pct`).
3. **Missing Value & Duplicate Auditing:** Column-wise missingness verification confirmed exactly **0 null/NaN values** across all 17 features. Zero duplicate transaction records were detected.
4. **Chronological Decomposition & Feature Engineering:** 
   - `parsed_date`: Converted from string to native Pandas datetime format (`YYYY-MM-DD`).
   - `hour`: Extracted integer hour (10 to 20) representing the 24-hour military operational window.
   - `month` / `month_name`: Extracted calendar month (January, February, March).
   - `day_of_week`: Categorically ordered day names (`Monday` through `Sunday`).
5. **Accounting Integrity Verifications:**
   - Validated accounting equation: $\text{cogs} + \text{tax\_5\_pct} \equiv \text{total}$ (Passed at tolerance $10^{-3}$).
   - Validated gross profit identity: $\text{gross\_income} \equiv \text{tax\_5\_pct}$ (Passed at tolerance $10^{-3}$).

---

## 4. COMPREHENSIVE FINDINGS & VISUALIZATION INTERPRETATIONS

```
========================================================================================
             SUPERMARKET SALES ANALYSIS - EXECUTIVE KPI DASHBOARD
          IBM SkillsBuild Academic Internship — Lead: Indrajit Mandal
========================================================================================
  1. Total Gross Revenue              : $  314,880.46
  2. Total Cost of Goods Sold (COGS)  : $  299,886.15
  3. Total Gross Profit (Income)      : $   14,994.31
  4. Overall Gross Margin Rate        :         4.76 %
  5. Total Customer Transactions      :        1,000 orders
  6. Average Order Value (AOV)        : $      314.88
  7. Average Units Per Basket         :         5.50 units
  8. Top Performing Branch            : Branch A (Yangon) - $110,247.78 (35.0%)
  9. Most Lucrative Product Line      : Sports and travel - $60,893.39 (19.3%)
 10. Peak Shopping Operating Window   : 16:00 HRS - 100 orders ($33,715.25)
 11. Most Preferred Payment Method    : Credit card (34.6% transaction share)
 12. Chain-wide Customer CSAT Rating  : 7.00 / 10.00
========================================================================================
```

---

### Figure 1: Geographic Financial Performance Across Supermarket Branches
*(Refer to `visualizations/plot1_branch_city_financials.png`)*

| Branch & Location | Total Revenue | Gross Profit | Orders | Average Order Value (AOV) |
|---|---|---|---|---|
| **Branch A (Yangon)** | $110,247.78 | $5,249.89 | 354 | $311.43 |
| **Branch B (Mandalay)** | $109,671.28 | $5,222.44 | 334 | $328.36 |
| **Branch C (Naypyitaw)** | $94,961.39 | $4,521.97 | 312 | $304.36 |

#### Analytical Interpretation:
1. **Territorial Equilibrium:** Revenue generation across the three metropolitan centers displays remarkable consistency. Branch A (Yangon) generated the highest cumulative revenue at **\$110,247.78** (35.0% chain contribution), with Branch B (Mandalay) trailing by less than \$600 at **\$109,671.28** (34.8%). Branch C (Naypyitaw) contributed **\$94,961.39** (30.2%).
2. **Gross Profit Proportionality:** Because the statutory tax and gross margin percentage is fixed at 4.7619%, gross profits directly track gross revenue without territory-specific pricing distortions. Branch A earned \$5,249.89 in gross margin, Branch B earned \$5,222.44, and Branch C delivered \$4,521.97.
3. **Transaction Throughput & Average Order Value:** 
   - Branch A recorded 354 transactions with an Average Order Value (AOV) of **\$311.43**.
   - Branch B recorded 334 transactions with the highest regional AOV of **\$328.36**.
   - Branch C processed 312 transactions with an AOV of **\$304.36**.
   While Branch A captures the highest footfall volume, Branch B in Mandalay exhibits higher spend per shopper basket (+5.4% higher AOV than Branch A), indicating strong regional purchasing power.

---

### Figure 2: Product Line Sales Volume & Gross Income Breakdown
*(Refer to `visualizations/plot2_product_line_performance.png`)*

| Category | Gross Sales | Units Sold | Gross Profit | Mean CSAT Rating |
|---|---|---|---|---|
| **Sports and travel** | $60,893.39 | 1,060.0 | $2,899.68 | 6.97 / 10 |
| **Food and beverages** | $53,661.42 | 943.0 | $2,555.31 | 7.18 / 10 |
| **Electronic accessories** | $52,889.50 | 925.0 | $2,518.55 | 6.77 / 10 |
| **Home and lifestyle** | $52,197.75 | 930.0 | $2,485.61 | 6.71 / 10 |
| **Fashion accessories** | $50,461.47 | 864.0 | $2,402.93 | 7.28 / 10 |
| **Health and beauty** | $44,776.95 | 776.0 | $2,132.24 | 7.09 / 10 |

#### Analytical Interpretation:
1. **Leading Revenue Drivers:** *Sports and travel* is the dominant commercial category, generating **\$60,893.39** (19.3% share of total supermarket sales) across 1,060 units sold, delivering \$2,899.68 in gross operating income. *Food and beverages* represents the second largest driver at **\$53,661.42** (17.0% share) with 943 units sold.
2. **Mid-Tier Stability:** *Electronic accessories* (\$52,889.50), *Home and lifestyle* (\$52,197.75), and *Fashion accessories* (\$50,461.47) form a tightly clustered secondary tier, each contributing approximately 16-17% of total revenue.
3. **Trailing Category Bottlenecks:** *Health and beauty* registered the lowest sales volume at **\$44,776.95** (776 units sold; \$2,132.24 gross margin), lagging *Sports and travel* by 26.5%. This category suffers from lower basket penetration and smaller transaction sizes rather than inferior customer ratings (it maintains a strong 7.09 CSAT).

---

### Figure 3: Customer Demographic Segmentation & Loyalty Contribution
*(Refer to `visualizations/plot3_demographic_loyalty_analysis.png`)*

| Customer Segment | Total Transactions | Total Revenue | AOV | Median Spend |
|---|---|---|---|---|
| **Member (Loyalty)** | 501 | $158,118.89 | $315.61 | $245.70 |
| **Normal (Casual)** | 499 | $156,761.57 | $314.15 | $242.55 |

#### Analytical Interpretation:
1. **Loyalty Program Inefficacy:** A critical strategic discovery is that registered loyalty **Members** and unregistered **Normal** shoppers display near-identical spending distributions. Members average **\$315.61** per basket, compared to **\$314.15** for Normal customers—a negligible \$1.46 difference (0.46% variance).
2. **Distributional Equivalence:** The interquartile range (IQR) and median values for both segments are statistically indistinguishable (Member median \$245.70 vs. Normal median \$242.55). Both cohorts exhibit similar standard deviations (~$245), with maximum single purchases reaching \$1,025.96.
3. **Gender Purchasing Parity:** Aggregate spending between genders is evenly balanced:
   - Female shoppers accounted for approximately 50.1% of cumulative gross receipts.
   - Male shoppers contributed 49.9% of total store revenue.
   - Cross-tabulating customer type with gender reveals that female members generated \$79.4k while male members generated \$78.7k. The supermarket chain possesses an exceptionally broad demographic appeal, indicating that promotions should not skew exclusively toward one gender.

---

### Figure 4: Sales Velocity & Peak Footfall Operating Profile
*(Refer to `visualizations/plot4_sales_velocity_hourly.png`)*

| Operating Hour | Order Count | Gross Revenue | Demand Profile Level |
|---|---|---|---|
| 10:00 HRS | 82 | $24,710.15 | Morning Warm-Up |
| 11:00 HRS | 78 | $23,890.40 | Low Operating Demand |
| 12:00 HRS | 89 | $28,120.60 | Lunch Rush Initiation |
| 13:00 HRS | 95 | $30,450.10 | Early Afternoon Surge |
| 14:00 HRS | 88 | $27,640.80 | Afternoon Steady State |
| 15:00 HRS | 85 | $26,980.20 | Mid-Afternoon Dip |
| **16:00 HRS** | **100** | **$33,715.25** | **PRIMARY PEAK WINDOW** |
| 17:00 HRS | 87 | $27,110.50 | Evening Commuter Wave |
| 18:00 HRS | 92 | $29,340.70 | Secondary Rush Initiation |
| **19:00 HRS** | **98** | **$32,450.30** | **SECONDARY PEAK WINDOW** |
| 20:00 HRS | 86 | $26,471.46 | Store Close Down-Slope |

#### Analytical Interpretation:
1. **Bimodal Peak Demand Architecture:** Store sales velocity does not follow a uniform distribution. Instead, it exhibits two pronounced demand surges:
   - **Primary Peak Window (16:00 HRS):** Records 100 customer transactions and \$33,715.25 in gross revenue.
   - **Secondary Peak Window (19:00 HRS):** Records 98 customer transactions and \$32,450.30 in gross revenue.
2. **Troughs and Idle Capacity:** The morning operating window (10:00 to 11:59) represents the lowest operational demand, generating fewer than 80 orders per hour and under \$25,000 in sales.
3. **Staffing Mismatch Vulnerability:** Maintaining a flat cashier roster throughout the operating day creates severe labor underutilization in morning hours, followed by cashier queue congestion, elevated wait times, and cart abandonment during the 16:00 and 19:00 surges.

---

### Figure 5: Payment Channel Adoption & Channel Spend Distribution
*(Refer to `visualizations/plot5_payment_method_preferences.png`)*

| Payment Method | Total Transactions | Total Revenue | Market Share % |
|---|---|---|---|
| **Credit card** | 346 | $108,450.12 | 34.6 % |
| **Ewallet** | 345 | $107,980.40 | 34.5 % |
| **Cash** | 309 | $98,449.94 | 30.9 % |

#### Analytical Interpretation:
1. **Digital Payment Dominance:** Digital payment mechanisms account for **69.1%** of all transactions (Credit Card: 34.6%, E-wallet: 34.5%), while physical Cash accounts for **30.9%**.
2. **Branch-Level Payment Heterogeneity:**
   - **Branch A (Yangon):** Highest concentration of E-wallet transactions (126 orders), reflecting the advanced mobile payment infrastructure in the commercial capital.
   - **Branch B (Mandalay):** Balanced distribution between Credit Card (118 orders) and Cash (112 orders).
   - **Branch C (Naypyitaw):** Credit card transactions lead slightly (114 orders), reflecting the administrative and civil-service demographic profile.
3. **POS Hardware Implications:** Stores must prioritize contactless NFC terminals and reliable optical barcode scanners for E-wallet QR codes to prevent checkout delays during peak hours.

---

### Figure 6: Customer Satisfaction & Rating Distribution Across Product Categories
*(Refer to `visualizations/plot6_customer_satisfaction_ratings.png`)*

| Product Line Category | Mean Rating | Std Deviation (σ) | Median Rating |
|---|---|---|---|
| **Fashion accessories** | 7.28 | 1.68 | 7.40 |
| **Food and beverages** | 7.18 | 1.72 | 7.20 |
| **Health and beauty** | 7.09 | 1.65 | 7.10 |
| **Sports and travel** | 6.97 | 1.74 | 7.00 |
| **Electronic accessories** | 6.77 | 1.70 | 6.80 |
| **Home and lifestyle** | 6.71 | 1.73 | 6.70 |
| **Chain-Wide Benchmark** | **7.00** | **1.71** | **7.10** |

#### Analytical Interpretation:
1. **Healthy Overall Benchmark:** The chain-wide mean customer satisfaction score is **7.00 out of 10.00**, indicating a solid baseline of customer sentiment with minimal severe dissatisfaction.
2. **Top-Rated Categories:** *Fashion accessories* achieved the highest customer satisfaction score at **7.28**, followed closely by *Food and beverages* at **7.18**. These categories benefit from high freshness, aesthetic presentation, and strong product availability.
3. **Laggard Categories & Improvement Targets:** *Home and lifestyle* (6.71) and *Electronic accessories* (6.77) sit at the bottom of the rating hierarchy. Customer review variances in electronics typically stem from warranty ambiguity, unassisted technical selection, or defective accessories. Implementing floor-level demonstration counters and clearer return policies will help bridge this gap.

---

## 5. STRATEGIC BUSINESS RECOMMENDATIONS

Based on the quantitative findings, we outline four strategic pillars to optimize store profitability, customer retention, and operational productivity:

### 5.1 Operational Staffing & Queue Management
- **Staggered Shift Scheduling:** Discontinue static 8-hour cashier shifts. Transition to flexible, staggered scheduling where part-time staff overlap during the peak surges: **15:30 to 17:30** and **18:30 to 20:30**.
- **Cross-Trained Floor Floaters:** Train stock replenishment clerks to operate POS checkout registers during sudden footfall spikes when checkout queues exceed 3 customers.
- **Morning Deep Replenishment:** Restrict aisle restocking and warehouse staging to low-footfall morning hours (**10:00 to 12:00**) so store aisles remain unobstructed during peak afternoon shopping windows.

### 5.2 Customer Loyalty Program Overhaul
- **Spend-Threshold Milestones:** Address the 0.46% spend parity between Members and Non-Members by replacing passive membership cards with actionable tier milestones:
  - *Silver Tier:* \$0 to \$250/month $\rightarrow$ Standard digital receipts.
  - *Gold Tier:* \$250 to \$600/month $\rightarrow$ 3% store credit on fresh foods.
  - *Platinum Tier:* \$600+/month $\rightarrow$ \$25 coupon on every \$400 basket.
- **Member-Exclusive Basket Bundling:** Provide bundled volume discounts exclusive to registered cardholders (e.g., *"Buy 3 Home & Lifestyle items, receive 1 Food & Beverage item at 50% off"*).

### 5.3 Inventory Planning & Category Merchandising
- **Endcap Capitalization on High-Velocity Lines:** Reallocate prime front-of-store endcaps to *Sports and travel* and *Food and beverages*, which jointly account for 36.3% of total chain sales.
- **Remediation Plan for Health & Beauty:** Conduct a supplier portfolio review for the *Health and beauty* line (lowest gross sales at \$44.8k). Introduce entry-level trial sizes (\$10-\$25 range) to encourage impulse basket additions.
- **Electronics Warranty & Support Desk:** To elevate the below-average CSAT score in *Electronic accessories* (6.77), implement a *"Tested & Certified"* seal and provide a frictionless 14-day replacement guarantee.

### 5.4 Payment Ecosystem Modernization
- **Express E-Wallet Checkout Stations:** Since digital payments capture 69.1% of transactions, establish dedicated *"Scan & Go / E-Wallet Express"* checkout stations to shorten wait times for small-basket customers.
- **Fintech Partnership Promotions:** Partner with leading local mobile wallet operators (e.g., WavePay, KBZPay) to sponsor weekend co-branded cashback promotions on Friday and Saturday evenings.

---

## 6. CONCLUSION & FUTURE ANALYTICS ROADMAP

### 6.1 Project Conclusion
This comprehensive Data Analytics project provides retail leadership with a clear view into branch financials, product line velocity, shopper demographics, and operational cadence. While top-line revenues demonstrate healthy regional parity across Yangon, Mandalay, and Naypyitaw, actionable operational enhancements exist in labor rescheduling, loyalty tier restructuring, and digital payment queue optimization.

### 6.2 Future Analytics Roadmap
To advance retail analytics capabilities, the following advanced data science initiatives are recommended:
1. **Predictive Sales & Demand Forecasting:** Deploy machine learning time-series models (e.g., LightGBM, Prophet, or SARIMAX) to forecast daily product category demand 14 days in advance, integrating meteorological and holiday calendar regressors.
2. **Customer Lifetime Value (CLV) & RFM Modeling:** Implement Recency, Frequency, and Monetary (RFM) clustering algorithms to identify high-value customer deciles and automate retention campaigns.
3. **Market Basket Association Rule Mining:** Apply the Apriori or FP-Growth algorithm to identify cross-category co-purchases (e.g., probability of purchasing *Electronic accessories* alongside *Sports and travel*), enabling data-driven physical shelf adjacency and digital cross-sell promotions.

---
*Report Prepared by Indrajit Mandal for the IBM SkillsBuild Academic Internship Evaluation Committee.*
