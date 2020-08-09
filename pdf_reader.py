import PyPDF2
from PyPDF2 import PdfFileReader

pdf = open("./diveintopython.pdf", 'rb')
readerObj = PdfFileReader(pdf) # 파일 리더 객체
print("PRD Reader Obj is:\n", readerObj)