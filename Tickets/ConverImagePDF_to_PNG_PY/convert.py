import sys
from pdf2jpg import pdf2jpg
inputpath = sys.argv[1] #aqui se lee la variable filePath
outputpath = r"C:\tmp" #esta es la ruta donde se va a guardar la imagen
result = pdf2jpg.convert_pdf2jpg(inputpath,outputpath, pages="ALL") #aqui se procesa la conversion. 

#Para usar este archivo es necesario tener el interpreter de python instalado. 