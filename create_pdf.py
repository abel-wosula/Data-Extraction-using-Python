from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

# PDF file name
pdf_file = "Data_Driven_Innovation_Summary.pdf"

# Create document
doc = SimpleDocTemplate(pdf_file, pagesize=A4,
                        rightMargin=40, leftMargin=40,
                        topMargin=60, bottomMargin=40)

# Get base styles
styles = getSampleStyleSheet()
story = []

# Custom style for the header
header_style = ParagraphStyle(
    'HeaderStyle',
    parent=styles['Heading1'],
    fontSize=14,
    leading=18,
    alignment=1,  # center
    spaceAfter=20,
    bold=True
)

# Add Name and Reg No at top
header_text = "<b>Name: Abel Wafula</b><br/><b>Reg No: ST61810552024@students.ouk.ac.ke</b>"
story.append(Paragraph(header_text, header_style))
story.append(Spacer(1, 20))

# Section 1: Article Summary
story.append(Paragraph("<b>1. Summary of a Data-Driven Innovation Article</b>", styles['Heading2']))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Topic:</b> Predictive Maintenance in the Manufacturing Industry", styles['Normal']))
story.append(Spacer(1, 5))
story.append(Paragraph("<b>Problem:</b> Traditional reactive or scheduled maintenance causes machine breakdowns, lost production, and high repair costs.", styles['Normal']))
story.append(Spacer(1, 5))
story.append(Paragraph("<b>Methodology:</b> IoT sensor data collection, feature engineering, and machine learning models (Random Forest, Gradient Boosting, LSTM) to predict Remaining Useful Life (RUL).", styles['Normal']))
story.append(Spacer(1, 5))
story.append(Paragraph("<b>Results:</b> Downtime reduced by 45%, maintenance costs decreased by 28%, failure detection accuracy reached 92%, ROI achieved within 10 months.", styles['Normal']))
story.append(Spacer(1, 20))

# Page break if needed
# story.append(PageBreak())

# Section 2: Microfinance Case Study
story.append(Paragraph("<b>2. Case Study: Data-Driven Innovation in Micro-Finance Institution</b>", styles['Heading2']))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Institution:</b> Equity Group Foundation Microfinance (Kenya)", styles['Normal']))
story.append(Spacer(1, 5))
story.append(Paragraph("<b>Problem:</b> Manual loan assessment, high default risk, slow approvals, and limited credit history for borrowers.", styles['Normal']))
story.append(Spacer(1, 5))
story.append(Paragraph("<b>Data-Driven Solution:</b> Developed digital credit scoring using mobile money transaction history, savings behavior, past loan repayment patterns, social network repayment behavior, and business cash flows. Integrated customer data from mobile banking, branch transactions, and community groups. Risk prediction models included Logistic Regression, Random Forest, and K-Means clustering. Automated loan approval for low-risk clients through USSD, mobile apps, and agent outlets.", styles['Normal']))
story.append(Spacer(1, 5))
story.append(Paragraph("<b>Results:</b> Loan approval time reduced to <10 minutes, default rate reduced to 7.5%, customer acquisition cost reduced by 40%, and access to rural clients expanded by 27%.", styles['Normal']))
story.append(Spacer(1, 5))
story.append(Paragraph("<b>Impact:</b> Improved financial inclusion, reduced operational costs, enhanced loan performance, and more women and youth accessed credit.", styles['Normal']))

# Build PDF
doc.build(story)

print(f"PDF successfully created: {pdf_file}")
