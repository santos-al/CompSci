"""

Suppose that you’d like to implement a CS50 “shirtificate,” 
a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, 
using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
All other details we leave to you. You’re even welcome to add borders, colors, and lines. 
Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it. 
Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) 
to share a shirtificate with your name on it in any of CS50’s communities!

"""

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering image
        self.image("./shirtificate.png", 5, 50, 200, 200)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=30)
pdf.set_text_color(255, 255, 255)
pdf.ln(80)
name = input("Name: ")
pdf.cell(0, 10, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
