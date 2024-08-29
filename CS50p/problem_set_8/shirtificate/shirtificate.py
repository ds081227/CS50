from fpdf import FPDF, Align
class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")

    def add_header(self):
        self.set_font("helvetica" , size = 50)
        self.cell(0, 30, text = "CS50 Shirtificate", align = "C")

    def add_shirt(self):
        self.image("shirtificate.png", x = Align.C, y = 50, w = self.epw)

    def cover_text(self):
        self.name = input("Name: ")
        self.set_font("helvetica", size = 30)
        self.set_y(-180)
        self.set_text_color(r = 255, g = 255, b= 255)
        self.cell(0, 0, text = f"{self.name} took CS50", align = "C")

pdf = PDF()
pdf.add_page()
pdf.add_header()
pdf.add_shirt()
pdf.cover_text()
pdf.output("shirtificate.pdf")
