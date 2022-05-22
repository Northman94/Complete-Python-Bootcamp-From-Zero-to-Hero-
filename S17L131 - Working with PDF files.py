
#  PDF  = Portable Document Format  developed by Adobe in 1990s.

# Many PDFs are not machine readable via Python.

# PDF that was simply scanned is not readable.
# Images, tables, format adjustments can also be unreadable.

# Though there are many paid PDF readers & extractors.
# We will use open-source  PyPDF2 Library.


# =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =

# pip install PyPDF2
import PyPDF2


f = open('Working_Business_Proposal.pdf', 'rb') #rb = read binary

pdf_reader = PyPDF2.PdfFileReader(f)

pdf_reader.numPages
# 5

page_one = pdf_reader.getPage(0)

page_one_text = page_one.extractText()

print(page_one_text)
f.close()

# You can get an Empty string, when Page is scanned or not compatable with PyPDF2
# Try another PDF Library


# =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =


# Writing to a PDF file

# You can only create a NEW Page at the end, and write into it. Some Paid Libraries - does.

# We can not write to PDFs using Python because of the differences between the single string type of Python,
# and the variety of fonts, placements, and other parameters that a PDF could have.

# What we can do is copy pages and append pages to the end.


f = open('Working_Business_Proposal.pdf', 'rb') #rb = read binary

pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)

type(first_page)
# PyPDF2._page.PageObject

#Check above for correct type
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)


pdf_output = open('NewPDFDOC.pdf', 'wb') #wb = write binary

pdf_writer.write(pdf_output)

f.close()
pdf_output.close()



# =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =  -  =

# Grabbing All text in PDF:

f = open('Working_Business_Proposal.pdf', 'rb')  # rb = read binary

pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)

    pdf_text.append(page.extractText())


print(pdf_text)  # print(pdf_text[3])
# \n  is for a new Page

f.close()






