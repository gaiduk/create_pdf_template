from fpdf import FPDF
import pandas as pd


# pdf = FPDF(orientation="p", unit="mm", format="A4")
#
# pdf.add_page()
#
# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello world", align="L", ln=1, border=1)
#
# pdf.set_font(family="Times", style="I", size=15)
# pdf.cell(w=0, h=20, txt="Hello me", align="C", ln=1, border=1)
#
# pdf.output("output.pdf")
pdf = FPDF(orientation="p", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(110, 120, 90)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(11, 23, 199, 23)

pdf.output("output.pdf")
