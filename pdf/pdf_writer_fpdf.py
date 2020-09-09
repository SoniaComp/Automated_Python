import fpdf
from fpdf import FPDF

pdf = FPDF(format ='letter') # a3, a4, a5, letter, legal등 여러 형식을 지원한다.

pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Welcome", ln=1, align="C")
pdf.cell(200, 10, 'Created', 0, 1, 'C')
pdf.output("autoateit.pdf")

# .docx
# zip 압축 기능을 가진 XML 기반 파일 형식으로 변경됐다.
# 애플리케이션 간에 데이터를 전송하는데 도움이 될 수 있는 열린 파일 형식을 요구할 때!
