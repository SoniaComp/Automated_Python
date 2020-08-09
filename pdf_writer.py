from PyPDF2 import PdfFileReader, PdfFileWriter
infile = PdfFileReader(open('./diveintopython.pdf', 'rb')) 
outfile = PdfFileWriter()

outfile.addBlankPage(612, 792) # 기본 단위
p = infile.getPage(0) # 첫번째 페이지...
outfile.addPage(p) # 두번째로 데려옴

with open('./myPdf.pdf', 'wb') as f:
  outfile.write(f)

f.close()