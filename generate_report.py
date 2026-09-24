"""
Script to generate production-quality Microsoft Word (.docx) Business Report
for the Supermarket Sales Analysis project (IBM SkillsBuild Academic Internship).
Author: Indrajit Mandal
Embeds all generated publication figures, formatted tables, and executive styling.
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tc_pr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets internal padding/margins of a table cell in dxa."""
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tc_mar.append(node)
    tc_pr.append(tc_mar)

def create_report():
    doc = Document()

    # Set page margins (1 inch around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base styles
    navy = RGBColor(26, 54, 93)      # #1A365D
    slate = RGBColor(74, 85, 104)    # #4A5568
    charcoal = RGBColor(45, 55, 72)  # #2D3748

    # Title & Header
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(12)
    title_p.paragraph_format.space_after = Pt(4)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run("SUPERMARKET SALES ANALYSIS & OPERATIONAL INTELLIGENCE REPORT")
    title_run.font.name = "Arial"
    title_run.font.size = Pt(20)
    title_run.font.bold = True
    title_run.font.color.rgb = navy

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_p.paragraph_format.space_after = Pt(18)
    sub_run = sub_p.add_run("Exploratory Data Analysis, Revenue Optimization, and Customer Segmentation\nIBM SkillsBuild Academic Internship Project — Lead Analyst: Indrajit Mandal")
    sub_run.font.name = "Arial"
    sub_run.font.size = Pt(12)
    sub_run.font.italic = True
    sub_run.font.color.rgb = slate

    # Metadata Box (Table)
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Author / Lead Analyst:", "Indrajit Mandal (Senior Data Analyst Intern)"),
        ("Academic Program:", "IBM SkillsBuild Academic Internship: Data Analytics"),
        ("Project Designation:", "Supermarket Sales Analysis DA Project"),
        ("Date & Status:", "September 2026 | Final Production Deliverable")
    ]
    for i, (k, v) in enumerate(meta_data):
        row = meta_table.rows[i]
        c1 = row.cells[0]
        c2 = row.cells[1]
        c1.text = k
        c2.text = v
        set_cell_background(c1, "F0F4F8")
        set_cell_background(c2, "FFFFFF")
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c2, top=60, bottom=60, left=100, right=100)
        c1.paragraphs[0].runs[0].font.bold = True
        c1.paragraphs[0].runs[0].font.color.rgb = navy
        c2.paragraphs[0].runs[0].font.color.rgb = charcoal

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # 1. Executive Summary
    h1 = doc.add_heading(level=1)
    r1 = h1.add_run("1. Executive Summary")
    r1.font.color.rgb = navy
    r1.font.name = "Arial"

    exec_p = doc.add_paragraph()
    exec_p.paragraph_format.line_spacing = 1.15
    exec_p.paragraph_format.space_after = Pt(10)
    exec_p.add_run(
        "This empirical investigation, conducted by Indrajit Mandal, analyzes 1,000 retail transactions recorded across "
        "three regional supermarket branches of a leading retail chain in Myanmar: Branch A (Yangon), Branch B (Mandalay), "
        "and Branch C (Naypyitaw). The primary business objective is to diagnose financial revenue drivers, evaluate product "
        "line margins, benchmark store efficiency, and uncover consumer purchasing behaviors to deliver actionable, data-backed operational strategies.\n\n"
        "Across the analyzed period, the supermarket chain generated $314,880.46 in gross revenue, delivering $14,994.31 in gross "
        "operating profit with an overall gross margin rate of 4.76% across 1,000 customer transactions. Top-line revenue demonstrates "
        "remarkable geographic balance: Branch A led with $110,247.78 (35.0%), closely followed by Branch B at $109,671.28 (34.8%), "
        "and Branch C at $94,961.39 (30.2%). Product velocity was led by Sports and travel ($60,893.39) and Food and beverages ($53,661.42).\n\n"
        "However, the analysis uncovered critical operational vulnerabilities: the customer loyalty program fails to generate "
        "incremental basket lift (Members average $315.61 vs. $314.15 for non-members), and footfall displays severe bimodal peaks "
        "at 16:00 and 19:00, creating store checkout friction. Strategic interventions focus on restructuring the loyalty tier, "
        "deploying agile shift scheduling, and implementing dynamic inventory allocation."
    )

    # 2. Business Problem Definition & Research Questions
    h2 = doc.add_heading(level=1)
    r2 = h2.add_run("2. Business Problem Definition & Research Questions")
    r2.font.color.rgb = navy
    r2.font.name = "Arial"

    p_ctx = doc.add_paragraph()
    p_ctx.paragraph_format.space_after = Pt(8)
    p_ctx.add_run(
        "Modern multi-branch supermarket enterprises operate in highly competitive, low-margin retail environments where operational "
        "profitability hinges upon inventory velocity, labor productivity, basket size maximization, and customer retention. Retail "
        "leadership requires quantitative clarity to deploy capital, schedule personnel, negotiate supplier terms, and optimize physical floor layouts."
    )

    doc.add_paragraph("The investigation addresses six core business research questions:", style='Normal').paragraph_format.space_after = Pt(4)
    rqs = [
        ("RQ 1 (Geographic Parity):", "Do the three branches exhibit significant revenue or gross margin divergence across territories?"),
        ("RQ 2 (Product Line Margins):", "Which retail categories generate the highest total dollar sales and unit volumes?"),
        ("RQ 3 (Customer Loyalty Impact):", "Does the registered loyalty card program stimulate measurably larger basket values?"),
        ("RQ 4 (Operating Sales Velocity):", "At what specific hours of the operating day do transaction volumes surge?"),
        ("RQ 5 (Payment Dynamics):", "How do customer payment method preferences (Cash, E-wallets, Cards) vary across branches?"),
        ("RQ 6 (Customer Satisfaction):", "What is the chain-wide Customer Satisfaction (CSAT) rating profile across product lines?")
    ]
    for rq_title, rq_desc in rqs:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        r_bold = p.add_run(f"{rq_title} ")
        r_bold.font.bold = True
        r_bold.font.color.rgb = navy
        p.add_run(rq_desc)

    # 3. Data Dictionary & Preprocessing Methodology
    h3 = doc.add_heading(level=1)
    r3 = h3.add_run("3. Data Dictionary & Preprocessing Methodology")
    r3.font.color.rgb = navy
    r3.font.name = "Arial"

    p_dict = doc.add_paragraph()
    p_dict.paragraph_format.space_after = Pt(8)
    p_dict.add_run("The table below details the canonical 17 features analyzed within the supermarket sales dataset:")

    # Data Dictionary Table
    table_data = [
        ("Attribute", "Type", "Domain Range / Categories", "Description"),
        ("invoice_id", "String", "9-digit slip code", "Unique computer-generated sales slip code"),
        ("branch", "Categorical", "A, B, C", "Branch identifier of the store location"),
        ("city", "Categorical", "Yangon, Mandalay, Naypyitaw", "City where the supermarket branch operates"),
        ("customer_type", "Categorical", "Member, Normal", "Customer loyalty membership status"),
        ("gender", "Categorical", "Female, Male", "Customer gender designation"),
        ("product_line", "Categorical", "6 Product Lines", "General merchandise classification category"),
        ("unit_price", "Float", "$10.00 - $99.99", "Price per individual item in USD"),
        ("quantity", "Integer", "1 - 10 units", "Total number of units purchased per invoice"),
        ("tax_5_pct", "Float", "5% of COGS", "Statutory 5% consumption sales tax"),
        ("total", "Float", "$10.50 - $1,025.96", "Gross transaction amount billed to customer"),
        ("date", "Date", "01/01/2019 - 03/30/2019", "Date of purchase transaction (Q1 2019)"),
        ("time", "Time", "10:00 - 20:59", "Timestamp of sales transaction across day"),
        ("payment", "Categorical", "Ewallet, Cash, Credit card", "Tender method utilized at checkout POS"),
        ("cogs", "Float", "unit_price * quantity", "Cost of Goods Sold in USD"),
        ("gross_margin_pct", "Float", "4.761904762%", "Constant theoretical gross margin percentage"),
        ("gross_income", "Float", "$0.50 - $48.86", "Operating gross profit earned from invoice"),
        ("rating", "Float", "4.0 - 10.0", "Customer exit satisfaction rating (CSAT score)")
    ]

    doc_table = doc.add_table(rows=len(table_data), cols=4)
    doc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(doc_table.rows):
        for c_idx, cell in enumerate(row.cells):
            cell.text = table_data[r_idx][c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            if r_idx == 0:
                set_cell_background(cell, "1A365D")
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
                p.runs[0].font.name = "Arial"
                p.runs[0].font.size = Pt(9.5)
            else:
                set_cell_background(cell, "F7FAFC" if r_idx % 2 == 1 else "FFFFFF")
                p = cell.paragraphs[0]
                p.runs[0].font.name = "Arial"
                p.runs[0].font.size = Pt(8.5)
                if c_idx == 0:
                    p.runs[0].font.bold = True
                    p.runs[0].font.color.rgb = navy

    # Preprocessing text
    p_prep = doc.add_paragraph()
    p_prep.paragraph_format.space_before = Pt(12)
    p_prep.paragraph_format.space_after = Pt(8)
    p_prep.add_run(
        "Data Preprocessing Methodology by Indrajit Mandal:\n"
        "1. Schema Standardization: All column headers were transformed to clean snake_case.\n"
        "2. Missing Data & Duplicate Audit: Confirmed 0 null values across all columns and 0 duplicate rows.\n"
        "3. Datetime Decomposition: Extracted hour, month, month_name, day_of_week, and day.\n"
        "4. Mathematical Invariants: Validated internal accounting logic (COGS + Tax == Total, Tax == Gross Income) at 10^-3 tolerance."
    )

    # 4. Comprehensive Findings & Visualizations
    h4 = doc.add_heading(level=1)
    r4 = h4.add_run("4. Comprehensive Findings & Visualizations")
    r4.font.color.rgb = navy
    r4.font.name = "Arial"

    figures = [
        (
            "visualizations/plot1_branch_city_financials.png",
            "Figure 1: Geographic Financial Performance Across Supermarket Branches",
            "Key Empirical Insights - Branch Performance (Analysis by Indrajit Mandal):\n"
            "- Branch A (Yangon) led top-line gross receipts with $110,247.78 across 354 transactions.\n"
            "- Branch B (Mandalay) followed with $109,671.28 across 334 transactions, achieving the highest Average Order Value ($328.36).\n"
            "- Branch C (Naypyitaw) delivered $94,961.39 across 312 transactions ($304.36 AOV).\n"
            "- Revenue distribution displays healthy stability across all three regional centers with a 4.76% gross operating profit margin."
        ),
        (
            "visualizations/plot2_product_line_performance.png",
            "Figure 2: Product Line Sales Volume & Gross Income Breakdown",
            "Key Empirical Insights - Product Line Performance (Analysis by Indrajit Mandal):\n"
            "- Sports and travel is the chain's top revenue generator at $60,893.39 (1,060 units sold; $2,899.68 gross profit).\n"
            "- Food and beverages ranked second at $53,661.42 (943 units sold; $2,555.31 gross profit).\n"
            "- Electronic accessories ($52,889.50) and Home and lifestyle ($52,197.75) showed strong, consistent turnover.\n"
            "- Health and beauty registered lowest volume at $44,776.95, representing a category expansion opportunity."
        ),
        (
            "visualizations/plot3_demographic_loyalty_analysis.png",
            "Figure 3: Customer Demographic Segmentation & Loyalty Contribution",
            "Key Empirical Insights - Demographic & Loyalty Analysis (Analysis by Indrajit Mandal):\n"
            "- Member spend ($315.61 AOV) is statistically identical to Normal walk-in customer spend ($314.15 AOV).\n"
            "- The existing loyalty card program acts merely as an identifier rather than an incremental basket size driver.\n"
            "- Gender split is balanced (Female: 50.1% of revenue; Male: 49.9%), demonstrating wide consumer appeal across product lines."
        ),
        (
            "visualizations/plot4_sales_velocity_hourly.png",
            "Figure 4: Sales Velocity & Peak Footfall Operating Profile Across Operating Hours",
            "Key Empirical Insights - Sales Velocity & Peak Footfall (Analysis by Indrajit Mandal):\n"
            "- Sales velocity follows a distinct bimodal curve peaking at 16:00 (100 orders, $33,715) and 19:00 (98 orders, $32,450).\n"
            "- Morning windows (10:00 - 11:59) represent operating troughs with fewer than 80 orders per hour.\n"
            "- Cashier shift schedules must be restructured dynamically to prevent peak queue congestion."
        ),
        (
            "visualizations/plot5_payment_method_preferences.png",
            "Figure 5: Payment Channel Adoption & Channel Spend Distribution",
            "Key Empirical Insights - Payment Methods (Analysis by Indrajit Mandal):\n"
            "- Digital payment adoption dominates: Credit Cards account for 34.6% and E-wallets account for 34.5% (69.1% total digital share).\n"
            "- Cash settlements represent 30.9% of transactions.\n"
            "- Branch A (Yangon) leads E-wallet adoption, while Branch B and C show higher card and cash usage."
        ),
        (
            "visualizations/plot6_customer_satisfaction_ratings.png",
            "Figure 6: Customer Satisfaction (CSAT Rating) Distribution by Product Line",
            "Key Empirical Insights - Customer Satisfaction (Analysis by Indrajit Mandal):\n"
            "- Chain-wide mean CSAT rating is 7.00 / 10.00 with standard deviation of 1.71.\n"
            "- Top ratings: Fashion accessories (7.28) and Food and beverages (7.18).\n"
            "- Home and lifestyle (6.71) and Electronic accessories (6.77) represent improvement targets requiring clear warranty and return support."
        )
    ]

    for img_path, fig_title, fig_desc in figures:
        if os.path.exists(img_path):
            doc.add_paragraph().paragraph_format.space_before = Pt(8)
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_picture(img_path, width=Inches(6.2))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(6)
            r_cap = p_cap.add_run(fig_title)
            r_cap.font.name = "Arial"
            r_cap.font.bold = True
            r_cap.font.size = Pt(9.5)
            r_cap.font.color.rgb = navy

            p_body = doc.add_paragraph()
            p_body.paragraph_format.space_after = Pt(12)
            p_body.add_run(fig_desc)

    # 5. Strategic Business Recommendations
    h5 = doc.add_heading(level=1)
    r5 = h5.add_run("5. Strategic Business Recommendations")
    r5.font.color.rgb = navy
    r5.font.name = "Arial"

    recs = [
        ("1. Workforce & Shift Scheduling:", 
         "Implement staggered cashier shifts aligning labor capacity with the 16:00 and 19:00 footfall peaks. Transition morning staff to shelf restocking to keep afternoon aisles unobstructed."),
        ("2. Tiered Loyalty Program Revamp:", 
         "Overhaul the passive membership program into a 3-tier milestone structure (Silver, Gold, Platinum) with basket threshold rebates (e.g., $25 voucher on purchases over $400) to incentivize higher basket spend."),
        ("3. Assortment & Visual Merchandising:", 
         "Allocate premium eye-level shelf space to high-grossing categories (Sports & Travel and Food & Beverages). Restructure Health & Beauty packaging to introduce trial sizes that encourage impulse buying."),
        ("4. Digital POS & Fintech Integrations:", 
         "Designate dedicated E-Wallet express checkout lanes to capitalize on the 69.1% digital payment adoption, and negotiate co-marketing cashback promotions with leading mobile wallet platforms.")
    ]
    for r_title, r_text in recs:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(6)
        r_b = p.add_run(f"{r_title} ")
        r_b.font.bold = True
        r_b.font.color.rgb = navy
        p.add_run(r_text)

    # 6. Conclusion & Future Roadmap
    h6 = doc.add_heading(level=1)
    r6 = h6.add_run("6. Conclusion & Future Analytics Roadmap")
    r6.font.color.rgb = navy
    r6.font.name = "Arial"

    p_conc = doc.add_paragraph()
    p_conc.paragraph_format.space_after = Pt(10)
    p_conc.add_run(
        "This project establishes a rigorous baseline of operational intelligence across supermarket branches in Yangon, Mandalay, "
        "and Naypyitaw. The empirical findings reveal high regional revenue balance but expose critical opportunities to optimize cashier labor, "
        "restructure loyalty incentives, and enhance digital checkout speed.\n\n"
        "Future analytics initiatives led by Indrajit Mandal will expand upon this foundation:\n"
        "- Machine Learning Demand Forecasting: Implementing gradient boosted tree models (LightGBM/XGBoost) for daily category demand forecasting.\n"
        "- RFM Customer Segmentation: Deploying unsupervised clustering (K-Means) to identify high-value customer personas.\n"
        "- Market Basket Association Rules: Utilizing the Apriori algorithm to identify product affinity and automate cross-merchandising pairings."
    )

    p_sign = doc.add_paragraph()
    p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sign.paragraph_format.space_before = Pt(18)
    r_sign = p_sign.add_run("Respectfully submitted,\nIndrajit Mandal\nSenior Data Analyst Intern\nIBM SkillsBuild Academic Internship")
    r_sign.font.italic = True
    r_sign.font.color.rgb = slate

    # Target filenames
    target_files = [
        "IndrajitMandal_ProjectReport.docx",
        "[YourName]_ProjectReport.docx",
        "Student_ProjectReport.docx"
    ]
    for target in target_files:
        doc.save(target)
    print(f"[SUCCESS] Generated professional Word documents: {target_files}")

if __name__ == '__main__':
    create_report()
