from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=0, h=15, txt=row["Topic"], ln=1, align="L")
    y = 25

    for i in range(15):
        pdf.line(10, y, 200, y)
        y = y + 18


pdf.output("output_lines.pdf")