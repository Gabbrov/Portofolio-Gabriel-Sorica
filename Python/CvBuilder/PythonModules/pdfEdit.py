
import PyPDF2
import os

from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab import *


pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))



pdfs=[]


def find_pdfs(folder_path):#Code originally from GPT3.5

    pdf_files = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                # If it does, add its full path to the list
                pdf_files.append(file)
                
    return pdf_files


def read_file(filePath):
    
    try:
        renderer = PyPDF2.PdfReader(""+filePath)
        return(""+renderer.pages[0].extract_text())

    except:
        print("Error Reading:  "+filePath)


def write_file(fileName,font="Vera",fontSize=12,loc = 0):
    exeCode=0
    try:
        
        print("Canvasing")
        canvas = Canvas(""+fileName+".pdf")
        canvas.setFont(font,fontSize)


        
        canvas.drawString(0,0,)
        canvas.save()
        exeCode=200
    except Exception as e:
        print(e)
        exeCode=-1
    return exeCode

