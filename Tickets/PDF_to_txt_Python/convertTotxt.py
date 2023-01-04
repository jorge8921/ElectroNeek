#Eequired library
#pip install PyPDF2

import PyPDF2
import sys,json

data = sys.argv[1]
data = json.loads(data)

for i in data:
    rootPath = i['rootPath']
    fileName = i['fileName']
    pathFile = str(rootPath+"\\"+fileName)

# pathFile = r"C:\PDF Files\sample.pdf"
# fileName = "sample.pdf"

# creating a pdf file object
pdfFileObj = open(pathFile, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
pageNumbers = pdfReader.numPages
print(pdfReader.numPages)

for i in range(0, pageNumbers):
    # creating a page object
    pageObj = pdfReader.getPage(i)
    
    # extracting text from page
    print(pageObj.extractText())

    #saving results in txt file
    file1=open(r"C:\tmp\\"+fileName+".txt","a")
    file1.writelines(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()