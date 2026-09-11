import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

styles = getSampleStyleSheet()
title_style = ParagraphStyle("DocTitle", parent=styles["Heading1"], fontSize=18, textColor=colors.HexColor("#1A365D"), spaceAfter=10)
heading_style = ParagraphStyle("DocSubTitle", parent=styles["Heading2"], fontSize=13, textColor=colors.HexColor("#2B6CB0"), spaceAfter=6, spaceBefore=10)
body_style = ParagraphStyle("DocBody", parent=styles["Normal"], fontSize=9, leading=13, spaceAfter=6)

# ---------------------------------------------------------
# 1. Company Overview (3 Pages)
# ---------------------------------------------------------
doc1_path = os.path.join(OUTPUT_DIR, "1_Company_Overview.pdf")
doc1 = SimpleDocTemplate(doc1_path, pagesize=letter)
story1 = [
    Paragraph("AeroEstate Realty — Corporate Overview & Strategic Vision", title_style),
    Paragraph("<b>Document Reference:</b> CORP-DOC-2026-V2 | <b>Effective Date:</b> January 15, 2026", body_style),
    Spacer(1, 8),
    Paragraph("<b>Page 1 — Corporate History & Core Objectives</b>", heading_style),
    Paragraph("AeroEstate Realty was established in 2018 in Islamabad, Pakistan, as a full-service commercial and residential real estate advisory firm. Built on the core principle of modernizing property transactions through technology, transparency, and data-driven market analysis, the firm serves institutional investors, high-net-worth individuals, and first-time homebuyers across Pakistan.", body_style),
    Paragraph("Our technology-first approach incorporates digital title verification systems, automated property management dashboards, and AI-assisted portfolio evaluation tools. Over the past eight years, AeroEstate Realty has facilitated over $120 Million in private and commercial property transactions across major urban centers including Islamabad, Rawalpindi, Lahore, and Karachi.", body_style),
    Paragraph("<b>Key Market Focus:</b> High-density commercial developments, executive luxury residential villas, planned gated communities, and retail arcade leasing.", body_style),
    
    PageBreak(),
    Paragraph("<b>Page 2 — Executive Leadership & Organizational Structure</b>", heading_style),
    Paragraph("<b>Chief Executive Officer (CEO):</b> Sarah Jenkins — Former Vice President of Commercial Real Estate at Global Properties Group. Sarah holds an MBA from London Business School and brings over 18 years of international asset management expertise.", body_style),
    Paragraph("<b>Lead Commercial Broker & Senior Partner:</b> Tariq Mahmood — Specializes in urban commercial zoning and high-value acquisitions. Tariq has managed commercial development sales in Blue Area and Sector F-11 for over 15 years.", body_style),
    Paragraph("<b>Head of Legal & Title Verification:</b> Barrister Salman Chaudhry — Expert in CDA (Capital Development Authority) regulatory frameworks, land acquisition disputes, and municipal tax compliance.", body_style),
    Paragraph("<b>Head of Client Relations:</b> Ayesha Khan — Directs customer support operations, tenant dispute resolution, and digital onboarding platforms.", body_style),

    PageBreak(),
    Paragraph("<b>Page 3 — Operational Milestones & Certifications</b>", heading_style),
    Paragraph("AeroEstate Realty operates in strict accordance with the Real Estate Regulatory Authority (RERA) guidelines and holds official accreditation from the Islamabad Chamber of Commerce and Industry (ICCI).", body_style),
    Paragraph("<b>Key Milestones:</b>", body_style),
    Paragraph("• <b>2020:</b> Launched the first automated online title verification index for Islamabad Sector developments.<br/>"
              "• <b>2023:</b> Expanded commercial leasing division, managing over 250,000 sq. ft. of prime office space.<br/>"
              "• <b>2025:</b> Introduced escrow-protected buyer deposit security protocols to guarantee 100% money-back safety on unverified land titles.", body_style)
]
doc1.build(story1)

# ---------------------------------------------------------
# 2. Property Listings (3 Pages)
# ---------------------------------------------------------
doc2_path = os.path.join(OUTPUT_DIR, "2_Property_Listings.pdf")
doc2 = SimpleDocTemplate(doc2_path, pagesize=letter)
story2 = [
    Paragraph("AeroEstate Realty — Exclusive Property Catalog", title_style),
    Paragraph("<b>Catalog Edition:</b> Q3/Q4 2026 | <b>Updated:</b> August 2026", body_style),
    Spacer(1, 8),
    Paragraph("<b>Page 1 — Premium Residential Properties</b>", heading_style),
    Paragraph("<b>Property Code: RES-101 — Skyline Heights Luxury Penthouse</b><br/>"
              "<b>Location:</b> Sector F-11/1, Islamabad (Corner plot facing Margalla Hills)<br/>"
              "<b>Asking Price:</b> $350,000 (PKR 98,000,000 approx.)<br/>"
              "<b>Covered Area:</b> 2,800 sq. ft. | <b>Bedrooms:</b> 3 | <b>Bathrooms:</b> 4<br/>"
              "<b>Description:</b> Brand-new high-rise penthouse featuring imported Italian floor tiles, fully equipped smart-home automation system, double-glazed soundproof windows, and 2 dedicated basement parking slots. Building amenities include a heated rooftop swimming pool, 24/7 dual-backup diesel generators, and 3-tier biometric security.", body_style),
    Spacer(1, 6),
    Paragraph("<b>Property Code: RES-102 — Pine Villa Executive Residence</b><br/>"
              "<b>Location:</b> Bahria Town Phase 8, Sector C, Rawalpindi<br/>"
              "<b>Asking Price:</b> $480,000 (PKR 134,000,000 approx.)<br/>"
              "<b>Covered Area:</b> 4,500 sq. ft. | <b>Bedrooms:</b> 5 | <b>Bathrooms:</b> 6<br/>"
              "<b>Description:</b> Custom-built double-story villa featuring solid teak woodwork, servant quarters with private access, solar panel array (15kW system included), and landscaped front lawn.", body_style),

    PageBreak(),
    Paragraph("<b>Page 2 — Commercial & Office Spaces</b>", heading_style),
    Paragraph("<b>Property Code: COM-201 — Blue Area Prime Corporate Floor</b><br/>"
              "<b>Location:</b> Jinnah Avenue, Blue Area, Islamabad<br/>"
              "<b>Asking Price (Purchase):</b> $750,000<br/>"
              "<b>Lease Rate:</b> $4,500 / month (1-year advance required)<br/>"
              "<b>Covered Area:</b> 3,800 sq. ft. (Floor 7)<br/>"
              "<b>Description:</b> Fully furnished corporate floor with open-plan workstation layout, 2 executive boardrooms equipped with conference displays, central HVAC, dedicated fiber-optic internet trunk line, and 4 assigned underground parking spaces.", body_style),
    Spacer(1, 6),
    Paragraph("<b>Property Code: COM-202 — Gulberg Greens Commercial Retail Hub</b><br/>"
              "<b>Location:</b> Main Executive Block, Gulberg Residencia, Islamabad<br/>"
              "<b>Asking Price:</b> $220,000<br/>"
              "<b>Covered Area:</b> 1,100 sq. ft. Ground Floor Shop<br/>"
              "<b>Description:</b> High foot-traffic corner commercial shop suitable for retail franchises or pharmacy chains.", body_style),

    PageBreak(),
    Paragraph("<b>Page 3 — Agricultural & Investment Plots</b>", heading_style),
    Paragraph("<b>Property Code: LND-301 — Chak Shahzad Farmhouse Land</b><br/>"
              "<b>Location:</b> Park Road, Chak Shahzad, Islamabad<br/>"
              "<b>Asking Price:</b> $1,200,000<br/>"
              "<b>Plot Size:</b> 4 Kanal (21,780 sq. ft.)<br/>"
              "<b>Description:</b> CDA-approved residential farmhouse plot with existing tube well connection, boundary wall, gas meter sanction, and direct asphalt road access.", body_style)
]
doc2.build(story2)

# ---------------------------------------------------------
# 3. Services and Fees (3 Pages)
# ---------------------------------------------------------
doc3_path = os.path.join(OUTPUT_DIR, "3_Services_and_Fees.pdf")
doc3 = SimpleDocTemplate(doc3_path, pagesize=letter)
story3 = [
    Paragraph("AeroEstate Realty — Comprehensive Fee Structure & Services Schedule", title_style),
    Paragraph("<b>Document ID:</b> FEE-SCHED-2026 | <b>Applicability:</b> All Active Contracts", body_style),
    Spacer(1, 8),
    Paragraph("<b>Page 1 — Real Estate Brokerage Commissions</b>", heading_style),
    Paragraph("AeroEstate Realty maintains a transparent commission schedule for all buyer, seller, and landlord representation services.", body_style),
    
    # Table of fees
    Table([
        ["Service Category", "Residential Properties", "Commercial Properties"],
        ["Seller Representation Fee", "2.5% of Final Agreed Sale Price", "3.0% of Final Agreed Sale Price"],
        ["Buyer Administrative Fee", "1.0% at Closing", "1.5% at Closing"],
        ["Tenant Placement Fee", "1 Month Equivalent Rent", "1.5 Month Equivalent Rent"],
        ["Property Management Fee", "8.0% Monthly Rent Collected", "10.0% Monthly Rent Collected"]
    ], colWidths=[150, 180, 180], style=TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ])),
    Spacer(1, 10),
    Paragraph("<i>Note: All commission payments are processed exclusively through official bank transfers or crossed cheques payable to 'AeroEstate Realty (Pvt) Ltd'. Cash payments to individual brokers are strictly prohibited.</i>", body_style),

    PageBreak(),
    Paragraph("<b>Page 2 — Advisory, Valuation & Legal Verification Rates</b>", heading_style),
    Paragraph("<b>Legal Title Search & Verification Service ($500 flat fee):</b> Involves complete examination of allotment letters, revenue record extracts (Fard-e-Malkiat), non-encumbrance certificates (NEC), and municipal lien verifications.", body_style),
    Paragraph("<b>Certified Property Appraisal ($300 Residential / $750 Commercial):</b> Detailed physical inspection and market comparison report delivered within 72 hours by certified valuation engineers.", body_style),
    Paragraph("<b>NOC & CDA Transfer Coordination ($400 flat fee):</b> Processing of transfer documents with local authorities including CDA, RDA, Bahria Town, and DHA offices.", body_style),

    PageBreak(),
    Paragraph("<b>Page 3 — Full Property Management Scope</b>", heading_style),
    Paragraph("Our 8% monthly Property Management agreement includes the following integrated services:", body_style),
    Paragraph("1. Monthly rent collection and automated electronic ledger reporting.<br/>"
              "2. Quarterly physical building inspections with photo documentation.<br/>"
              "3. On-demand emergency plumbing, electrical, and structural maintenance dispatch (contractor costs billed separately after landlord approval).<br/>"
              "4. Lease renewal negotiations and annual rent escalation indexing (standard 10% annual rent increase clause).", body_style)
]
doc3.build(story3)

# ---------------------------------------------------------
# 4. Frequently Asked Questions (2 Pages)
# ---------------------------------------------------------
doc4_path = os.path.join(OUTPUT_DIR, "4_Frequently_Asked_Questions.pdf")
doc4 = SimpleDocTemplate(doc4_path, pagesize=letter)
story4 = [
    Paragraph("AeroEstate Realty — Frequently Asked Questions & Client Handbook", title_style),
    Paragraph("<b>Document Reference:</b> FAQ-2026-V1", body_style),
    Spacer(1, 8),
    Paragraph("<b>Page 1 — General Purchasing & Legal Queries</b>", heading_style),
    Paragraph("<b>Q1: How long does a standard residential property purchase closing take?</b><br/>"
              "<b>A:</b> The typical closing window takes between 14 to 30 business days. This includes title verification (3-5 days), buyer deposit escrow lock (2 days), NOC issuance from relevant housing authorities (7-10 days), and final registration at the Sub-Registrar office.", body_style),
    Paragraph("<b>Q2: Can foreign nationals or overseas Pakistanis purchase real estate through AeroEstate?</b><br/>"
              "<b>A:</b> Yes. Overseas Pakistanis holding a valid NICOP (National Identity Card for Overseas Pakistanis) or POC (Pakistan Origin Card) possess full legal rights to acquire residential and commercial properties. Transactions can be completed remotely using a registered Power of Attorney (POA) attested by the relevant Pakistan Embassy or High Commission.", body_style),
    Paragraph("<b>Q3: What taxes apply to property buyers during closing?</b><br/>"
              "<b>A:</b> Buyers are subject to Advance Tax under Section 236K of the Income Tax Ordinance (3% for tax Filers, 12% for Non-Filers), Stamp Duty (2% of DC value), and Municipal Registration fees (1%).", body_style),

    PageBreak(),
    Paragraph("<b>Page 2 — Dispute Resolution & Cancellation FAQ</b>", heading_style),
    Paragraph("<b>Q4: How can a landlord cancel a Property Management Agreement with AeroEstate?</b><br/>"
              "<b>A:</b> Landlords can terminate their agreement by submitting a written 30-day notice via registered email to <i>clientservices@aeroestate.com</i> or official letter. Any outstanding tenant security deposits must be reconciled before final contract offboarding.", body_style),
    Paragraph("<b>Q5: What happens if a buyer defaults on an agreed payment schedule?</b><br/>"
              "<b>A:</b> If a buyer fails to pay the balance within 15 days of the stipulated due date without formal written extension, a grace period notice is issued. Continued default beyond 30 days results in forfeiture of 10% of the initial earnest token deposit as per standard sale agreements.", body_style)
]
doc4.build(story4)

# ---------------------------------------------------------
# 5. Terms and Policies (2 Pages)
# ---------------------------------------------------------
doc5_path = os.path.join(OUTPUT_DIR, "5_Terms_and_Policies.pdf")
doc5 = SimpleDocTemplate(doc5_path, pagesize=letter)
story5 = [
    Paragraph("AeroEstate Realty — Standard Terms, Conditions & Policy Framework", title_style),
    Paragraph("<b>Document Reference:</b> POL-TERMS-2026", body_style),
    Spacer(1, 8),
    Paragraph("<b>Page 1 — Escrow Deposit & Refund Policies</b>", heading_style),
    Paragraph("<b>Section 1.1 — Escrow Deposit Protection:</b> All initial earnest token money deposits (minimum 5% of the total negotiated agreement price) collected from buyers are deposited into a dedicated AeroEstate Escrow Account managed at Bank AL Habib Limited. Funds are held securely and are only disbursed to the seller upon successful receipt of the Non-Encumbrance Certificate (NEC) and formal transfer approval.", body_style),
    Paragraph("<b>Section 1.2 — Full Refund Guarantee:</b> If a property title search fails legal verification, or if undisclosed municipal liens/encumbrances are discovered during our 5-day due diligence window, 100% of the token deposit is refunded back to the buyer within 5 business days without any deduction.", body_style),
    Paragraph("<b>Section 1.3 — Buyer-Initiated Withdrawal:</b> If a buyer voluntarily withdraws from a purchase agreement after successful legal title clearance for reasons unrelated to title defects, the token deposit is subject to a 20% administrative retention fee.", body_style),

    PageBreak(),
    Paragraph("<b>Page 2 — Data Compliance, Anti-Money Laundering (AML) & Privacy</b>", heading_style),
    Paragraph("<b>Section 2.1 — AML & Know Your Customer (KYC) Protocols:</b> In compliance with Financial Action Task Force (FATF) and national AML regulations, all clients must provide verified CNIC/Passport copies, proof of income/source of funds, and bank account verifications prior to final deed execution.", body_style),
    Paragraph("<b>Section 2.2 — Digital Data Privacy:</b> All personal records, financial statements, and property ownership documents uploaded to the AeroEstate client portal or RAG information system are encrypted using AES-256 standard and stored on secure local servers.", body_style)
]
doc5.build(story5)

print("✓ Successfully regenerated 5 extended, highly detailed PDF files in 'data/raw/'")