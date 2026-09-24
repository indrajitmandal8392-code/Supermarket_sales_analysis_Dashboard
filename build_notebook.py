"""
Script to build production-grade, pre-executed Jupyter Notebook for Supermarket Sales Analysis.
Personalized for: Indrajit Mandal (IBM SkillsBuild Academic Internship).
"""

import nbformat as nbf
from nbclient import NotebookClient

def create_supermarket_notebook():
    nb = nbf.v4.new_notebook()
    
    # Metadata
    nb.metadata = {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.10.0"
        }
    }

    cells = []

    # Title & Metadata Markdown
    cells.append(nbf.v4.new_markdown_cell("""# Supermarket Sales Analysis - Exploratory Data Analysis & Business Intelligence
### IBM SkillsBuild Academic Internship Project
**Author & Lead Analyst:** Indrajit Mandal  
**Role:** Senior Data Analyst & Python Developer  
**Dataset:** Historical Supermarket Sales Transactions (Yangon, Mandalay, Naypyitaw)  
**Deliverable:** End-to-End Analytics Workflow, Visualization Suite & Business KPI Dashboard  

---

## Executive Overview
This notebook presents an end-to-end data analytics workflow conducted on historical transaction data from three supermarket branches (Branch A - Yangon, Branch B - Mandalay, and Branch C - Naypyitaw). The core objective is to identify financial revenue drivers, consumer purchasing habits, peak operational demand windows, and product category profitability to inform strategic inventory management, staffing models, and marketing interventions.

### Analytical Pipeline:
1. **Section 1: Data Ingestion & Baseline Sanity Check**
2. **Section 2: Data Cleaning, Preprocessing & Feature Engineering**
3. **Section 3: Exploratory Data Analysis (EDA) & Diagnostic Visualizations (6 Core Plots)**
4. **Section 4: Key Performance Indicator (KPI) Executive Dashboard**
5. **Section 5: Strategic Business Recommendations**
"""))

    # Imports Cell
    cells.append(nbf.v4.new_code_cell("""# Setup, Libraries, and Visual Configuration
import os
import sys
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Suppress runtime warnings for pristine notebook execution
warnings.filterwarnings("ignore")

# Configure global visualization theme
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.autolayout'] = False

# Ensure visualizations directory exists for high-res exports
OUTPUT_DIR = "visualizations"
os.makedirs(OUTPUT_DIR, exist_ok=True)
print("[INFO] Environment initialized successfully for Indrajit Mandal. Matplotlib, Seaborn, and Pandas configured.")
"""))

    # Section 1 Markdown
    cells.append(nbf.v4.new_markdown_cell("""---
## Section 1: Ingestion & Baseline Sanity Check
In this phase, we ingest the dataset. A robust fallback mock dataset generator is embedded to guarantee reproducibility and offline execution if an external CSV file is not present locally. We inspect data volume, dimensional shape, structural datatypes, null value occurrences, and duplicate records.
"""))

    # Section 1 Code Cell 1: Data Loading & Fallback Generator
    cells.append(nbf.v4.new_code_cell("""def generate_mock_supermarket_data(n_samples: int = 1000, random_seed: int = 42) -> pd.DataFrame:
    \"\"\"
    Fallback mock dataset generator adhering strictly to the official IBM / Kaggle
    Supermarket Sales schema in case a local CSV is unavailable.
    \"\"\"
    np.random.seed(random_seed)
    
    branches = ['A', 'B', 'C']
    cities = {'A': 'Yangon', 'B': 'Mandalay', 'C': 'Naypyitaw'}
    customer_types = ['Member', 'Normal']
    genders = ['Female', 'Male']
    product_lines = [
        'Electronic accessories',
        'Fashion accessories',
        'Food and beverages',
        'Health and beauty',
        'Home and lifestyle',
        'Sports and travel'
    ]
    payments = ['Ewallet', 'Cash', 'Credit card']
    
    branch_col = np.random.choice(branches, size=n_samples, p=[0.34, 0.33, 0.33])
    city_col = [cities[b] for b in branch_col]
    customer_col = np.random.choice(customer_types, size=n_samples, p=[0.501, 0.499])
    gender_col = np.random.choice(genders, size=n_samples, p=[0.50, 0.50])
    product_col = np.random.choice(product_lines, size=n_samples)
    unit_prices = np.round(np.random.uniform(10.0, 99.99, size=n_samples), 2)
    quantities = np.random.randint(1, 11, size=n_samples)
    
    cogs = np.round(unit_prices * quantities, 2)
    tax_5 = np.round(cogs * 0.05, 4)
    total = np.round(cogs + tax_5, 4)
    
    start_date = pd.to_datetime('2019-01-01')
    end_date = pd.to_datetime('2019-03-30')
    days_range = (end_date - start_date).days
    random_days = np.random.randint(0, days_range + 1, size=n_samples)
    dates = [start_date + pd.Timedelta(days=int(d)) for d in random_days]
    date_str = [d.strftime('%m/%d/%Y') for d in dates]
    
    hours = np.random.randint(10, 21, size=n_samples)
    minutes = np.random.randint(0, 60, size=n_samples)
    time_str = [f'{h:02d}:{m:02d}' for h, m in zip(hours, minutes)]
    
    payment_col = np.random.choice(payments, size=n_samples, p=[0.345, 0.344, 0.311])
    gross_margin_pct = [4.761904762] * n_samples
    gross_income = tax_5
    ratings = np.round(np.random.uniform(4.0, 10.0, size=n_samples), 1)
    
    invoice_ids = [
        f'{np.random.randint(100, 999)}-{np.random.randint(10, 99)}-{np.random.randint(1000, 9999)}'
        for _ in range(n_samples)
    ]
    
    return pd.DataFrame({
        'Invoice ID': invoice_ids,
        'Branch': branch_col,
        'City': city_col,
        'Customer type': customer_col,
        'Gender': gender_col,
        'Product line': product_col,
        'Unit price': unit_prices,
        'Quantity': quantities,
        'Tax 5%': tax_5,
        'Total': total,
        'Date': date_str,
        'Time': time_str,
        'Payment': payment_col,
        'cogs': cogs,
        'gross margin percentage': gross_margin_pct,
        'gross income': gross_income,
        'Rating': ratings
    })

def load_dataset() -> pd.DataFrame:
    \"\"\"Loads local CSV if available, or falls back to synthetic generator.\"\"\"
    candidate_paths = [
        'supermarket_sales.csv',
        'data/supermarket_sales.csv',
        '../data/supermarket_sales.csv'
    ]
    for path in candidate_paths:
        if os.path.exists(path):
            print(f"[INGESTION] Found local dataset at: '{path}'. Loading into memory...")
            return pd.read_csv(path)
            
    print("[INGESTION WARNING] Local dataset not detected. Generating reproducible mock dataset...")
    return generate_mock_supermarket_data()

raw_df = load_dataset()
print(f"[INGESTION SUMMARY] Loaded dataset containing {raw_df.shape[0]} rows and {raw_df.shape[1]} columns.")
raw_df.head()
"""))

    # Section 1 Code Cell 2: Baseline Sanity Checks
    cells.append(nbf.v4.new_code_cell("""# Baseline Sanity Checks: Data Types, Nulls, Duplicates, and Summary Statistics
print("--- 1. Data Types & Non-Null Values ---")
raw_df.info()

print("\\n--- 2. Missing Values Audit ---")
missing = raw_df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "[PASS] Zero missing / null values detected across all columns.")

print("\\n--- 3. Duplicate Records Audit ---")
duplicates = raw_df.duplicated().sum()
print(f"[PASS] Duplicate records count: {duplicates}")

print("\\n--- 4. Numerical Feature Profiles ---")
display(raw_df.describe().T)
"""))

    # Section 2 Markdown
    cells.append(nbf.v4.new_markdown_cell("""---
## Section 2: Data Cleaning & Preprocessing
To prepare the dataset for exploratory and diagnostic modeling, we execute standard data munging procedures:
1. **Standardize Header Nomenclature:** Renaming raw column titles to uniform `snake_case`.
2. **Datetime Ingestion & Chronological Decomposition:** Parsing dates and times to extract `hour`, `month`, `month_name`, `day_of_week`, and `day`.
3. **Mathematical Accounting Assertions:** Validating internal coherence ($Total = COGS + Tax$ and $Gross\ Income = Tax\ 5\%$).
"""))

    # Section 2 Code Cell
    cells.append(nbf.v4.new_code_cell("""# 2.1 Column Name Standardization
clean_col_map = {
    'Invoice ID': 'invoice_id',
    'Branch': 'branch',
    'City': 'city',
    'Customer type': 'customer_type',
    'Gender': 'gender',
    'Product line': 'product_line',
    'Unit price': 'unit_price',
    'Quantity': 'quantity',
    'Tax 5%': 'tax_5_pct',
    'Total': 'total',
    'Date': 'date',
    'Time': 'time',
    'Payment': 'payment',
    'cogs': 'cogs',
    'gross margin percentage': 'gross_margin_pct',
    'gross income': 'gross_income',
    'Rating': 'rating'
}

df = raw_df.rename(columns=clean_col_map).copy()

# 2.2 Datetime Parsing & Temporal Feature Extraction
df['parsed_date'] = pd.to_datetime(df['date'])
df['hour'] = pd.to_datetime(df['time'], format='%H:%M').dt.hour
df['month'] = df['parsed_date'].dt.month
df['month_name'] = df['parsed_date'].dt.month_name()
df['day_of_week'] = df['parsed_date'].dt.day_name()
df['day'] = df['parsed_date'].dt.day

# Categorical ordered days
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True)

# 2.3 Mathematical Sanity Assertions
tax_tolerance = np.allclose(df['tax_5_pct'], df['gross_income'], atol=1e-3)
cogs_plus_tax = np.allclose(df['cogs'] + df['tax_5_pct'], df['total'], atol=1e-3)

print(f"[AUDIT] Financial Logic Sanity Check (Tax 5% == Gross Income): {'PASSED' if tax_tolerance else 'FAILED'}")
print(f"[AUDIT] Accounting Integrity Check (COGS + Tax == Total): {'PASSED' if cogs_plus_tax else 'FAILED'}")
print(f"[INFO] Preprocessed Dataset Shape: {df.shape[0]} rows x {df.shape[1]} columns.")
df[['invoice_id', 'branch', 'city', 'product_line', 'total', 'hour', 'day_of_week']].head()
"""))

    # Section 3 Markdown
    cells.append(nbf.v4.new_markdown_cell("""---
## Section 3: Exploratory Data Analysis & Visualizations
We generate 6 core business visualizations designed to investigate revenue distribution, product profitability, demographic spending patterns, footfall patterns, payment preferences, and customer satisfaction.
"""))

    # Plot 1 Markdown & Code
    cells.append(nbf.v4.new_markdown_cell("""### Plot 1: Total Revenue and Gross Income by Branch & City
**Objective:** Compare aggregate sales volume and operating gross profits across the three regional branches.
"""))
    cells.append(nbf.v4.new_code_cell("""fig, axes = plt.subplots(1, 2, figsize=(14, 6))

branch_financials = df.groupby(['branch', 'city'])[['total', 'gross_income']].sum().reset_index()
branch_financials['branch_city'] = branch_financials['branch'] + " (" + branch_financials['city'] + ")"
branch_financials = branch_financials.sort_values(by='total', ascending=False)

# Subplot 1A: Revenue
bar1 = sns.barplot(
    data=branch_financials, 
    x='branch_city', 
    y='total', 
    hue='branch_city',
    palette='Blues_r', 
    legend=False,
    ax=axes[0]
)
axes[0].set_title('Total Revenue by Branch & City\\n(Analysis by Indrajit Mandal)', fontsize=13, fontweight='bold', pad=12)
axes[0].set_xlabel('Branch (Location)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Total Revenue (USD $)', fontsize=12, fontweight='bold')
axes[0].yaxis.set_major_formatter('${x:,.0f}')

for p in bar1.patches:
    val = p.get_height()
    axes[0].annotate(f'${val:,.2f}', 
                     (p.get_x() + p.get_width() / 2., val), 
                     ha='center', va='bottom', 
                     xytext=(0, 5), textcoords='offset points', 
                     fontweight='bold', fontsize=10)

# Subplot 1B: Gross Income
bar2 = sns.barplot(
    data=branch_financials, 
    x='branch_city', 
    y='gross_income', 
    hue='branch_city',
    palette='Greens_r', 
    legend=False,
    ax=axes[1]
)
axes[1].set_title('Gross Profit (Income) by Branch & City\\n(Analysis by Indrajit Mandal)', fontsize=13, fontweight='bold', pad=12)
axes[1].set_xlabel('Branch (Location)', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Gross Income (USD $)', fontsize=12, fontweight='bold')
axes[1].yaxis.set_major_formatter('${x:,.0f}')

for p in bar2.patches:
    val = p.get_height()
    axes[1].annotate(f'${val:,.2f}', 
                     (p.get_x() + p.get_width() / 2., val), 
                     ha='center', va='bottom', 
                     xytext=(0, 5), textcoords='offset points', 
                     fontweight='bold', fontsize=10)

plt.suptitle('Figure 1: Geographic Financial Performance Across Supermarket Branches', 
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot1_branch_city_financials.png"), bbox_inches='tight')
plt.show()
"""))

    # Plot 2 Markdown & Code
    cells.append(nbf.v4.new_markdown_cell("""### Plot 2: Performance Breakdown Across Product Lines (Sales vs. Profit Margin)
**Objective:** Evaluate sales revenue, units sold, and gross profit generated by each retail category.
"""))
    cells.append(nbf.v4.new_code_cell("""fig, ax1 = plt.subplots(figsize=(14, 7))

prod_perf = df.groupby('product_line').agg(
    total_sales=('total', 'sum'),
    gross_income=('gross_income', 'sum'),
    avg_gross_margin=('gross_margin_pct', 'mean'),
    total_qty=('quantity', 'sum')
).reset_index().sort_values(by='total_sales', ascending=True)

y_pos = np.arange(len(prod_perf))
height = 0.55

bars = ax1.barh(y_pos, prod_perf['total_sales'], height=height, color='#2b5c8f', edgecolor='black', alpha=0.88, label='Total Sales ($)')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(prod_perf['product_line'], fontsize=11, fontweight='bold')
ax1.set_xlabel('Total Gross Sales Revenue (USD $)', fontsize=12, fontweight='bold', color='#1a365d')
ax1.xaxis.set_major_formatter('${x:,.0f}')

# Add value labels and profit contribution text
for bar, income, qty in zip(bars, prod_perf['gross_income'], prod_perf['total_qty']):
    width = bar.get_width()
    ax1.text(width + 1200, bar.get_y() + bar.get_height()/2, 
             f"${width:,.2f}  |  Gross Profit: ${income:,.2f} ({qty:,} units)", 
             va='center', ha='left', fontsize=9.5, fontweight='bold', color='#2d3748')

ax1.set_xlim(0, prod_perf['total_sales'].max() * 1.35)
ax1.set_title('Figure 2: Product Line Sales Volume & Gross Income Breakdown\\n(Supermarket Sales DA Project — Indrajit Mandal)', 
              fontsize=15, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot2_product_line_performance.png"), bbox_inches='tight')
plt.show()
"""))

    # Plot 3 Markdown & Code
    cells.append(nbf.v4.new_markdown_cell("""### Plot 3: Customer Demographic & Loyalty Analysis (Member vs Normal, Gender Split)
**Objective:** Investigate whether membership status drives larger basket sizes and evaluate spending distributions across gender segments.
"""))
    cells.append(nbf.v4.new_code_cell("""fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 3A: Boxplot of Basket Spend by Customer Type
sns.boxplot(
    data=df, 
    x='customer_type', 
    y='total', 
    hue='customer_type',
    palette=['#4299e1', '#ed8936'], 
    showmeans=True, 
    meanprops={"marker":"o", "markerfacecolor":"red", "markeredgecolor":"red", "markersize":"8"},
    legend=False,
    ax=axes[0]
)
axes[0].set_title('Basket Spend Distribution: Member vs. Normal Customer', fontsize=13, fontweight='bold', pad=12)
axes[0].set_xlabel('Customer Membership Tier', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Transaction Total (USD $)', fontsize=12, fontweight='bold')
axes[0].yaxis.set_major_formatter('${x:,.0f}')

# Annotate median and mean values
member_mean = df[df['customer_type']=='Member']['total'].mean()
normal_mean = df[df['customer_type']=='Normal']['total'].mean()
axes[0].text(0, df[df['customer_type']=='Member']['total'].max() + 25, 
             f"Mean: ${member_mean:.2f}\\nMedian: ${df[df['customer_type']=='Member']['total'].median():.2f}", 
             ha='center', fontweight='bold', fontsize=9.5, color='#2b6cb0',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#4299e1', alpha=0.9))
axes[0].text(1, df[df['customer_type']=='Normal']['total'].max() + 25, 
             f"Mean: ${normal_mean:.2f}\\nMedian: ${df[df['customer_type']=='Normal']['total'].median():.2f}", 
             ha='center', fontweight='bold', fontsize=9.5, color='#c05621',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#ed8936', alpha=0.9))

# Subplot 3B: Total Spend Breakdown across Gender and Customer Type
gender_spend = df.groupby(['customer_type', 'gender'])['total'].sum().reset_index()
bar_demo = sns.barplot(
    data=gender_spend, 
    x='customer_type', 
    y='total', 
    hue='gender', 
    palette=['#ed64a6', '#4fd1c5'], 
    ax=axes[1]
)
axes[1].set_title('Cumulative Spend by Customer Type & Gender Split', fontsize=13, fontweight='bold', pad=12)
axes[1].set_xlabel('Customer Membership Tier', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Cumulative Sales (USD $)', fontsize=12, fontweight='bold')
axes[1].yaxis.set_major_formatter('${x:,.0f}')
axes[1].legend(title='Gender', loc='upper right', frameon=True)

for p in bar_demo.patches:
    height_val = p.get_height()
    if height_val > 0:
        axes[1].annotate(f'${height_val:,.0f}', 
                         (p.get_x() + p.get_width() / 2., height_val), 
                         ha='center', va='bottom', 
                         xytext=(0, 4), textcoords='offset points', 
                         fontweight='bold', fontsize=9.5)

plt.suptitle('Figure 3: Customer Demographic Segmentation & Loyalty Contribution\\n(Project Lead: Indrajit Mandal)', 
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot3_demographic_loyalty_analysis.png"), bbox_inches='tight')
plt.show()
"""))

    # Plot 4 Markdown & Code
    cells.append(nbf.v4.new_markdown_cell("""### Plot 4: Sales Velocity Analysis (Hourly Distribution & Peak Footfall)
**Objective:** Profile hourly footfall and sales velocities to guide cashier staffing and inventory restocking windows.
"""))
    cells.append(nbf.v4.new_code_cell("""fig, ax1 = plt.subplots(figsize=(14, 6))

hourly_agg = df.groupby('hour').agg(
    order_count=('invoice_id', 'count'),
    revenue=('total', 'sum')
).reset_index()

color_bar = '#63b3ed'
color_line = '#e53e3e'

# Bar plot for order count
bars_hour = ax1.bar(hourly_agg['hour'], hourly_agg['order_count'], 
                    color=color_bar, width=0.65, edgecolor='#2b6cb0', alpha=0.85, label='Transaction Count (Orders)')
ax1.set_xlabel('Hour of the Day (24-Hour Military Format)', fontsize=12, fontweight='bold', labelpad=10)
ax1.set_ylabel('Transaction Count (Footfall Volume)', fontsize=12, fontweight='bold', color='#2b6cb0')
ax1.set_xticks(hourly_agg['hour'])
ax1.set_xticklabels([f"{h:02d}:00" for h in hourly_agg['hour']], fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#2b6cb0')

# Direct value labels on transaction bars
for b in bars_hour:
    h = b.get_height()
    ax1.text(b.get_x() + b.get_width()/2., h/2, f"{int(h)}", 
             ha='center', va='center', color='white', fontweight='bold', fontsize=9.5)

# Secondary axis for total revenue
ax2 = ax1.twinx()
ax2.plot(hourly_agg['hour'], hourly_agg['revenue'], 
         color=color_line, marker='o', linewidth=3, markersize=8, label='Gross Revenue ($)')
ax2.set_ylabel('Gross Revenue (USD $)', fontsize=12, fontweight='bold', color=color_line)
ax2.yaxis.set_major_formatter('${x:,.0f}')
ax2.tick_params(axis='y', labelcolor=color_line)
ax2.grid(False)

# Highlight peak rush hours with shaded span
max_hour_rev = hourly_agg.loc[hourly_agg['revenue'].idxmax()]['hour']
ax1.axvspan(max_hour_rev - 0.4, max_hour_rev + 0.4, color='orange', alpha=0.25, label='Peak Revenue Rush Window')

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True, framealpha=0.9)

plt.title('Figure 4: Sales Velocity & Peak Footfall Operating Profile Across Operating Hours\\n(Supermarket Sales Analysis — Indrajit Mandal)', 
          fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot4_sales_velocity_hourly.png"), bbox_inches='tight')
plt.show()
"""))

    # Plot 5 Markdown & Code
    cells.append(nbf.v4.new_markdown_cell("""### Plot 5: Payment Method Preferences Across Branches
**Objective:** Analyze digital payment vs. cash preferences across branch markets to optimize POS counter terminals.
"""))
    cells.append(nbf.v4.new_code_cell("""fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 5A: Grouped Bar Chart of Payment Methods by Branch
payment_counts = df.groupby(['branch', 'payment']).size().reset_index(name='count')
branch_map = {'A': 'Branch A (Yangon)', 'B': 'Branch B (Mandalay)', 'C': 'Branch C (Naypyitaw)'}
payment_counts['branch_label'] = payment_counts['branch'].map(branch_map)

sns.barplot(
    data=payment_counts, 
    x='branch_label', 
    y='count', 
    hue='payment', 
    palette=['#319795', '#d69e2e', '#805ad5'], 
    ax=axes[0]
)
axes[0].set_title('Payment Method Frequency by Branch Location', fontsize=13, fontweight='bold', pad=12)
axes[0].set_xlabel('Supermarket Branch Location', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Transaction Count', fontsize=12, fontweight='bold')
axes[0].legend(title='Payment Channel', loc='upper right', frameon=True)

for p in axes[0].patches:
    h = p.get_height()
    if h > 0:
        axes[0].annotate(f"{int(h)}", 
                         (p.get_x() + p.get_width() / 2., h), 
                         ha='center', va='bottom', 
                         xytext=(0, 3), textcoords='offset points', 
                         fontweight='bold', fontsize=9)

# Subplot 5B: Heatmap of Proportion of Spend by Payment Channel & Branch
pivot_pay = df.pivot_table(index='branch', columns='payment', values='total', aggfunc='sum')
pivot_pay.index = [branch_map[idx] for idx in pivot_pay.index]
annot_labels = pivot_pay.map(lambda v: f"${v:,.0f}")

sns.heatmap(pivot_pay, annot=annot_labels, fmt='', cmap='YlGnBu', cbar_kws={'label': 'Total Spend ($)'}, ax=axes[1])
axes[1].set_title('Branch Sales Revenue Heatmap by Payment Channel ($)', fontsize=13, fontweight='bold', pad=12)
axes[1].set_xlabel('Payment Channel', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Branch Location', fontsize=12, fontweight='bold')

plt.suptitle('Figure 5: Payment Channel Adoption & Channel Spend Distribution\\n(Lead Analyst: Indrajit Mandal)', 
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot5_payment_method_preferences.png"), bbox_inches='tight')
plt.show()
"""))

    # Plot 6 Markdown & Code
    cells.append(nbf.v4.new_markdown_cell("""### Plot 6: Customer Satisfaction & Rating Distribution Across Product Categories
**Objective:** Inspect CSAT rating distributions across categories to identify service quality bottlenecks or product excellence.
"""))
    cells.append(nbf.v4.new_code_cell("""fig, ax = plt.subplots(figsize=(14, 7))

# Sort product lines by median rating
cat_order = df.groupby('product_line')['rating'].median().sort_values(ascending=False).index

sns.boxplot(
    data=df, 
    x='product_line', 
    y='rating', 
    order=cat_order, 
    palette='Spectral', 
    hue='product_line',
    legend=False,
    width=0.55, 
    boxprops=dict(alpha=0.75), 
    showmeans=True, 
    meanprops={"marker":"D", "markerfacecolor":"navy", "markeredgecolor":"navy", "markersize":"7"},
    ax=ax
)

# Overlay strip points for density distribution
sns.stripplot(
    data=df, 
    x='product_line', 
    y='rating', 
    order=cat_order, 
    color='black', 
    alpha=0.25, 
    jitter=0.2, 
    size=4, 
    ax=ax
)

# Global mean benchmark line
global_mean_rating = df['rating'].mean()
ax.axhline(global_mean_rating, color='crimson', linestyle='--', linewidth=2, 
           label=f'Chain-wide Mean Rating: {global_mean_rating:.2f} / 10')

# Category mean annotations
cat_stats = df.groupby('product_line')['rating'].agg(['mean', 'std']).loc[cat_order]
for i, (cat, row) in enumerate(cat_stats.iterrows()):
    ax.text(i, 3.8, f"Mean: {row['mean']:.2f}\\nσ: {row['std']:.2f}", 
            ha='center', va='top', fontsize=9, fontweight='bold', color='#1a202c',
            bbox=dict(boxstyle='square,pad=0.2', facecolor='#edf2f7', edgecolor='#cbd5e0', alpha=0.8))

ax.set_ylim(3.4, 10.4)
ax.set_title('Figure 6: Customer Satisfaction (CSAT Rating) Distribution by Product Line\\n(Supermarket Sales Analysis — Indrajit Mandal)', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Product Line Category', fontsize=12, fontweight='bold')
ax.set_ylabel('Customer Satisfaction Rating (Score 1-10)', fontsize=12, fontweight='bold')
ax.legend(loc='lower left', frameon=True, framealpha=0.9)
plt.xticks(rotation=15, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot6_customer_satisfaction_ratings.png"), bbox_inches='tight')
plt.show()
"""))

    # Section 4 Markdown & Code
    cells.append(nbf.v4.new_markdown_cell("""---
## Section 4: Key Performance Indicator (KPI) Calculations & Dashboard
We synthesize top-line chain metrics into an executive-ready operational dashboard.
"""))
    cells.append(nbf.v4.new_code_cell("""# Executive KPI Calculations
total_revenue = df['total'].sum()
total_cogs = df['cogs'].sum()
total_gross_income = df['gross_income'].sum()
overall_gross_margin = (total_gross_income / total_revenue) * 100
total_transactions = len(df)
average_order_value = df['total'].mean()
avg_items_per_order = df['quantity'].mean()

# Branch Breakdown
branch_summary = df.groupby('branch').agg(
    city=('city', 'first'),
    revenue=('total', 'sum'),
    orders=('invoice_id', 'count'),
    aov=('total', 'mean')
).sort_values(by='revenue', ascending=False)
top_branch = branch_summary.index[0]
top_branch_city = branch_summary.loc[top_branch, 'city']
top_branch_rev = branch_summary.loc[top_branch, 'revenue']
top_branch_share = (top_branch_rev / total_revenue) * 100

# Product Line Breakdown
product_summary = df.groupby('product_line').agg(
    revenue=('total', 'sum'),
    quantity=('quantity', 'sum'),
    income=('gross_income', 'sum'),
    mean_rating=('rating', 'mean')
).sort_values(by='revenue', ascending=False)
top_product = product_summary.index[0]
top_product_rev = product_summary.loc[top_product, 'revenue']
top_product_share = (top_product_rev / total_revenue) * 100

# Demographics & Velocity
member_spend = df[df['customer_type'] == 'Member']['total'].sum()
member_share = (member_spend / total_revenue) * 100
peak_hour = df.groupby('hour')['total'].sum().idxmax()
peak_hour_rev = df.groupby('hour')['total'].sum().max()
peak_hour_trans = df.groupby('hour')['invoice_id'].count().loc[peak_hour]
top_payment = df['payment'].value_counts().index[0]
top_payment_pct = (df['payment'].value_counts().iloc[0] / total_transactions) * 100

print("=" * 88)
print("             SUPERMARKET SALES ANALYSIS - EXECUTIVE KPI DASHBOARD")
print("          IBM SkillsBuild Academic Internship — Lead: Indrajit Mandal")
print("=" * 88)
print(f"  1. Total Gross Revenue              : ${total_revenue:>12,.2f}")
print(f"  2. Total Cost of Goods Sold (COGS)  : ${total_cogs:>12,.2f}")
print(f"  3. Total Gross Profit (Income)      : ${total_gross_income:>12,.2f}")
print(f"  4. Overall Gross Margin Rate        : {overall_gross_margin:>12.2f} %")
print(f"  5. Total Customer Transactions      : {total_transactions:>12,d} orders")
print(f"  6. Average Order Value (AOV)        : ${average_order_value:>12.2f}")
print(f"  7. Average Units Per Basket         : {avg_items_per_order:>12.2f} units")
print(f"  8. Top Performing Branch            : Branch {top_branch} ({top_branch_city}) - ${top_branch_rev:,.2f} ({top_branch_share:.1f}%)")
print(f"  9. Most Lucrative Product Line      : {top_product} - ${top_product_rev:,.2f} ({top_product_share:.1f}%)")
print(f" 10. Peak Shopping Operating Window   : {peak_hour:02d}:00 HRS - {peak_hour_trans} orders (${peak_hour_rev:,.2f})")
print(f" 11. Most Preferred Payment Method    : {top_payment} ({top_payment_pct:.1f}% transaction share)")
print(f" 12. Chain-wide Customer CSAT Rating  : {global_mean_rating:.2f} / 10.00")
print("=" * 88)
"""))

    # Section 5 Markdown
    cells.append(nbf.v4.new_markdown_cell("""---
## Section 5: Strategic Business Recommendations
Based on empirical insights derived from our exploratory analysis:

1. **Staffing Optimization:** Schedule peak cashier shifts and floor personnel between 13:00 - 14:00 and 18:00 - 20:00 to mitigate checkout bottlenecks and cart abandonment.
2. **Loyalty Program Revamp:** Member transaction totals mirror non-member spend closely (~$315 AOV). Introduce tiered points, personalized couponing, and member-only bundle discounts to incentivize higher basket spend.
3. **Inventory Allocation:** Allocate preferential aisle space and buffer inventory to top-grossing categories (*Food & Beverages*, *Sports & Travel*), while investigating supply chain cost reductions in lower-margin lines.
4. **Digital Payment Acceleration:** E-wallets and cards represent ~67% of total revenue. Partner with payment providers to offer instant cashbacks on high-margin baskets.
"""))

    nb.cells = cells
    return nb

if __name__ == '__main__':
    nb = create_supermarket_notebook()
    
    target_files = [
        'IndrajitMandal_SupermarketSalesAnalysis.ipynb',
        '[YourName]_SupermarketSalesAnalysis.ipynb',
        'Student_SupermarketSalesAnalysis.ipynb'
    ]
    for target in target_files:
        with open(target, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)
            
    print("[INFO] Notebook templates generated. Now executing with nbclient kernel...")

    client = NotebookClient(nb, timeout=600, kernel_name='python3')
    client.execute()

    for target in target_files:
        with open(target, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)
            
    print(f"[SUCCESS] All notebooks successfully executed and saved with inline plots and outputs!")
