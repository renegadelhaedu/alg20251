#instale o pacote antes
from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 15)

pdf.cell(200, 10, txt = "aula de algoritmos:",
         ln = 1, align = 'C')

file = open('meusatletas.txt', 'r')

linhas = file.readlines()

for i in range(len(linhas)):
    if i != 0:

        pdf.cell(200, 10, txt=linhas[i],
                 ln=i+1, align='L')

# save the pdf with name .pdf
pdf.output("meusatletas.pdf")