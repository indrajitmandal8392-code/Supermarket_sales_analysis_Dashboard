# Supermarket Sales Analysis — Data Analytics Project
### IBM SkillsBuild Academic Internship
**Lead Senior Data Analyst & Python Developer:** Indrajit Mandal  
**Domain:** Retail Analytics, Exploratory Data Analysis & Business Intelligence  
**Academic Program:** IBM SkillsBuild Academic Internship  
**Status:** Completed & Production Ready  

[![Author](https://img.shields.io/badge/Author-Indrajit%20Mandal-blue.svg)](https://github.com/)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Environment](https://img.shields.io/badge/JupyterLab-4.0%2B-orange.svg)](https://jupyter.org/)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-black.svg)](https://peps.python.org/pep-0008/)

---

## 1. Project Title & Overview

The **Supermarket Sales Analysis Project** is an end-to-end Data Analytics and Business Intelligence project developed by **Indrajit Mandal** as part of the **IBM SkillsBuild Academic Internship**. 

Modern supermarket retail chains operate in highly dynamic, competitive environments characterized by thin operating margins, fluctuating product velocity, shifting customer payment habits, and seasonal footfall variations. This project leverages historical transactional sales records from a major supermarket chain operating across three distinct metropolitan branches in Myanmar:
- **Branch A:** Yangon
- **Branch B:** Mandalay
- **Branch C:** Naypyitaw

Using Python, Pandas, Matplotlib, and Seaborn, this project implements a complete analytics pipeline from raw ingestion and automated sanity validation to multivariate exploratory analysis, KPI dashboard computation, and strategic business consulting recommendations.

---

## 2. Problem Statement & Business Objectives

### Problem Statement
Retail executives and store general managers face critical operational questions regarding resource allocation:
1. *Which supermarket branches and cities generate the highest top-line revenue and gross operating profit?*
2. *How do product categories compare in terms of sales volume, unit turnover, and profit margin contribution?*
3. *Does customer membership status (loyalty program) drive measurably larger basket sizes and transaction values compared to casual shoppers?*
4. *What are the peak sales velocity and footfall hours throughout the operating day, and how should store cashier staffing adapt?*
5. *What payment channels (E-wallets, Credit Cards, Cash) predominate across different urban branches, and are there digital payment adoption disparities?*
6. *How satisfied are customers across different product lines, and where do service or quality gaps exist?*

### Business Objectives
- **Financial Optimization:** Identify underperforming categories and evaluate gross profit margins across regional branches.
- **Operational Staffing Alignment:** Pinpoint peak operating hours and footfall surges to optimize cashier shift scheduling and minimize customer wait times.
- **Customer Loyalty Revamp:** Measure the true incremental value of the loyalty membership card program and design data-driven incentive structures.
- **Payment Infrastructure Modernization:** Align checkout POS terminal infrastructure with empirical customer payment channel preferences.
- **Service & Product Quality Assurance:** Benchmark Customer Satisfaction (CSAT) scores across retail product lines to mitigate negative customer churn.

---

## 3. Dataset Overview

The project utilizes the canonical supermarket sales dataset structured according to the following 17 attributes:

| # | Attribute | Data Type | Description | Sample Values |
|---|---|---|---|---|
| 1 | `Invoice ID` | String / Object | Unique computer-generated sales slip identifier | `581-41-7412`, `INV-1001` |
| 2 | `Branch` | Categorical / String | Branch identifier of the supermarket | `A`, `B`, `C` |
| 3 | `City` | Categorical / String | City where the supermarket branch is located | `Yangon`, `Mandalay`, `Naypyitaw` |
| 4 | `Customer type` | Categorical / String | Type of customer based on membership | `Member`, `Normal` |
| 5 | `Gender` | Categorical / String | Customer biological gender designation | `Female`, `Male` |
| 6 | `Product line` | Categorical / String | General product categorization group | `Electronic accessories`, `Food and beverages`, etc. |
| 7 | `Unit price` | Float (USD $) | Price per individual product item | `$10.00` to `$99.99` |
| 8 | `Quantity` | Integer | Total number of units purchased per invoice | `1` to `10` |
| 9 | `Tax 5%` | Float (USD $) | 5% government consumption sales tax | `5% * (Unit price * Quantity)` |
| 10 | `Total` | Float (USD $) | Total invoice amount including tax | `COGS + Tax 5%` |
| 11 | `Date` | Date / String | Date of purchase transaction (Q1 2019) | `01/15/2019` to `03/30/2019` |
| 12 | `Time` | Time / String | Time of purchase transaction (10:00 - 20:59) | `10:14`, `19:45` |
| 13 | `Payment` | Categorical / String | Payment channel utilized at point of sale | `Ewallet`, `Cash`, `Credit card` |
| 14 | `cogs` | Float (USD $) | Cost of Goods Sold | `Unit price * Quantity` |
| 15 | `gross margin percentage`| Float (%) | Theoretical operating gross margin percentage | Constant `4.761904762%` |
| 16 | `gross income` | Float (USD $) | Operating gross profit generated from invoice | `Total - COGS` (equals `Tax 5%`) |
| 17 | `Rating` | Float (1-10) | Customer satisfaction rating provided on receipt | `4.0` to `10.0` (CSAT score) |

> **Self-Contained Fallback Architecture:** If an external CSV file is not detected locally, the script/notebook automatically activates an integrated synthetic mock generator matching the schema, distributions, and accounting equations with 100% reproducibility.

---

## 4. System Requirements & Installation Instructions

### Prerequisites
- Python 3.10, 3.11, 3.12, or 3.13
- Git (optional, for version control)
- Minimum 4 GB RAM recommended for graphical rendering

### Step 1: Clone or Navigate to the Project Workspace
```bash
cd d:/project
```

### Step 2: Create and Activate a Virtual Environment (Recommended)
```bash
# On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

# On Linux / macOS:
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Production Dependencies
All required libraries are pinned in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 5. How to Run the Analysis

### Option A: Execute the Standalone Python Script
Run the automated end-to-end Python pipeline by Indrajit Mandal:
```bash
python IndrajitMandal_SupermarketSalesAnalysis.py
```

### Option B: Launch the Interactive Jupyter Notebook
Launch JupyterLab or Jupyter Notebook to interactively step through the cells, view markdown documentation, and examine inline visualizations:
```bash
jupyter lab IndrajitMandal_SupermarketSalesAnalysis.ipynb
# OR
jupyter notebook IndrajitMandal_SupermarketSalesAnalysis.ipynb
```

---

## 6. Repository Structure

```
d:/project/
│
├── requirements.txt                              # Pinned production Python dependencies
├── README.md                                     # Project documentation (Lead: Indrajit Mandal)
├── IndrajitMandal_SupermarketSalesAnalysis.py    # Modular Python analysis script by Indrajit Mandal
├── IndrajitMandal_SupermarketSalesAnalysis.ipynb # Pre-executed Jupyter Notebook with inline plots
├── IndrajitMandal_ProjectReport.docx             # Complete Microsoft Word Business Report
├── IndrajitMandal_ProjectReport.md               # Markdown source of the business report
│
├── Student_SupermarketSalesAnalysis.py           # Convenience alias
├── Student_SupermarketSalesAnalysis.ipynb        # Convenience alias
├── Student_ProjectReport.docx                   # Convenience alias
├── Student_ProjectReport.md                     # Convenience alias
│
├── [YourName]_SupermarketSalesAnalysis.py        # Template alias
├── [YourName]_SupermarketSalesAnalysis.ipynb     # Template alias
├── [YourName]_ProjectReport.docx                 # Template alias
├── [YourName]_ProjectReport.md                   # Template alias
│
├── build_notebook.py                             # Automated notebook compilation pipeline
├── generate_report.py                            # Automated python-docx report generation script
│
├── data/
│   └── supermarket_sales.csv                    # 1,000-row supermarket transaction dataset
│
└── visualizations/                               # 300-DPI publication-grade figures
    ├── plot1_branch_city_financials.png          # Figure 1: Branch & City Revenue / Profit
    ├── plot2_product_line_performance.png        # Figure 2: Product Line Sales & Gross Margin
    ├── plot3_demographic_loyalty_analysis.png     # Figure 3: Loyalty & Gender Spend Breakdown
    ├── plot4_sales_velocity_hourly.png           # Figure 4: Sales Velocity & Peak Footfall Hours
    ├── plot5_payment_method_preferences.png      # Figure 5: Payment Preferences Across Branches
    └── plot6_customer_satisfaction_ratings.png   # Figure 6: CSAT Distribution by Product Line
```

---

## 7. High-Level Summary of Findings & Strategic Recommendations

### Key Empirical Findings:
1. **Balanced Geographic Revenue:** Revenue is distributed evenly across Branch A (Yangon: ~$110.2k / 35.0%), Branch B (Mandalay: ~$109.7k / 34.8%), and Branch C (Naypyitaw: ~$95.0k / 30.2%), totaling **$314,880.46** with a **4.76%** gross profit margin ($14,994.31 gross profit).
2. **Top Product Lines:** **Sports and travel** ($60.9k) and **Food and beverages** ($53.7k) dominate top-line revenue, while **Health and beauty** ($44.8k) trails the category portfolio.
3. **Loyalty Program Inefficacy:** Normal non-member shoppers and registered Loyalty Members exhibit nearly identical Average Order Values (~$314.88) and basket unit volumes (~5.5 units). The current membership program acts as a passive registry rather than an incremental spend driver.
4. **Bimodal Footfall Surges:** Daily sales velocity peaks sharply during the late afternoon rush (**16:00 - 17:00 HRS** and **19:00 - 20:00 HRS**), accounting for over 20% of total daily transaction volume.
5. **Digital Payment Supremacy:** Digital channels (Credit Cards at 34.6% and E-wallets at 34.5%) account for nearly 70% of total receipts, while cash transactions represent 30.9%.
6. **Robust Customer Satisfaction:** Average CSAT across the supermarket chain stands at **7.00 / 10.00**, led by Fashion Accessories (7.28) and Food and Beverages (7.18), with Home & Lifestyle slightly trailing (6.71).

### Actionable Business Recommendations:
- **Operational Staffing:** Re-allocate cashier and floor replenishment personnel from morning doldrums (10:00 - 11:30) to the dual peak windows (14:00 - 17:00 and 18:30 - 20:30) to cut checkout wait times.
- **Tiered Loyalty Restructuring:** Replace flat membership cards with a tiered rewards system (Bronze, Silver, Gold) with threshold discounts (e.g., "$30 off orders above $400") to stimulate higher basket sizes.
- **Inventory & Space Allocation:** Grant prime eye-level endcap shelf space to high-velocity Food & Beverage and Sports & Travel items, and introduce cross-merchandising pairings.
- **Fintech Partnerships:** Collaborate with leading mobile wallet platforms to run exclusive co-branded promotional discounts on weekend grocery baskets.

---

## 8. Author & Academic Internship Meta
- **Lead Senior Data Analyst:** Indrajit Mandal
- **Program:** IBM SkillsBuild Academic Internship
- **Specialization:** Data Analytics & Applied Business Intelligence
- **Evaluation Status:** Complete Deliverable Package (Code, Visualizations, Notebook, Report)
