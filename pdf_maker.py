from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 
from datetime import date
import os

# help from: https://www.geeksforgeeks.org/creating-pdf-documents-with-python/

def makePDF(text):
    fileName = str(date.today())+'.pdf'
    documentTitle = str(date.today())+" Forms"
    title = 'Title'
    subTitle = 'Subtitle'
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

    # creating a pdf object 
    pdf = canvas.Canvas(fileName) 
    # setting the title of the document 
    pdf.setTitle(documentTitle) 
    # registering a external font in python 

    pdf.setFont('Arial', 36) 
    pdf.drawCentredString(300, 770, title)
    
    # creating the subtitle by setting it's font,  
    # colour and putting it on the canvas 
    pdf.setFillColorRGB(0, 0, 255) 
    pdf.setFont('Arial', 24) 
    pdf.drawCentredString(290, 720, subTitle) 
    
    # drawing a line 
    pdf.line(30, 710, 550, 710) 
    
    # creating a multiline text using 
    # textline and for loop 
    content = pdf.beginText(40, 680) 
    content.setFont('Arial', 18) 
    content.setFillColor(colors.red) 
    # print each line
    for line in text: 
        content.textLine(line) 
        
    pdf.drawText(content) 
    
    # saving the pdf 
    pdf.save()
    # Open File Explorer in the current directory
    os.startfile(os.getcwd())
    # let gui know were done here
    return True
