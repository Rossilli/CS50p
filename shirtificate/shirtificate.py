from fpdf import FPDF


name = input("Enter your name: ")
pdf = FPDF(orientation = 'P', format='A4')


pdf.add_page()


pdf.set_font("helvetica", "B", size=50)
pdf.cell(200, 30, txt="CS50 Shirtificate", align="C")


pdf.image("shirtificate.png", x=5, y=50, w=0, h=0, type='', link='')


pdf.set_text_color(255, 255, 255)


pdf.set_xy(30, 150)
pdf.set_font("helvetica", size=30)
pdf.cell(0, 0, txt=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")