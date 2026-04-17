from reportlab.lib.units import mm

from pathlib import Path
from pathlib import Path
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT




def  draw_speech_therapy(c, data):
    # ФИО
    c.setFont("Geologica-Bold", 26)
    x, y = 29*mm, 115*mm  
    c.drawString(x, y, data["student_name"])

    # Программа / ступень (с переносами)
    text = data["program_name"]

    style = ParagraphStyle(
        name="program",
        fontName="Geologica-Bold",
        fontSize=14,
        leading=18
        
    )

    p = Paragraph(text, style)

    x = 30*mm
    y = 80*mm
    width = 150*mm      # ширина блока
    height = 10*mm     # максимальная высота

    w, h = p.wrap(width, height)
    p.drawOn(c, x, y - h)
    
    #академ часы 
    c.setFont("Geologica-Regular", 14)
    x, y = 68*mm, 80.5*mm  
    c.drawCentredString(x, y, data["hours"])
    
    
    # Дата начала
    c.setFont("Geologica-Regular", 14)
    x, y = 107*mm, 80.5*mm  
    c.drawCentredString(x, y, data["date_start"])

    # Дата конца
    c.setFont("Geologica-Regular", 14)
    x, y = 153*mm, 80.5*mm  
    c.drawCentredString(x, y, data["date_end"])


     # ФИО педагога
    c.setFont("Geologica-Regular", 12)
    x, y = 30*mm, 37*mm  
    c.drawString(x, y, data["teacher"])



    # Год
    c.setFont("Geologica-Regular", 12)
    x, y = 115*mm, 13*mm  
    c.drawCentredString(x, y, data["year"])


