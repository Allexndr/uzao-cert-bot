from reportlab.lib.units import mm

from pathlib import Path
from pathlib import Path
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT




def draw_speed_reading_level_4(c, data):
    # ФИО
    c.setFont("Geologica-Bold", 26)
    x, y = 29*mm, 110*mm  
    c.drawString(x, y, data["student_name"])

    # Курс
    # Программа / ступень
    
    
    #академ часы 
    c.setFont("Geologica-Regular", 14)
    x, y = 68*mm, 77.6*mm  
    c.drawCentredString(x, y, data["hours"])
    
    
    # Дата начала
    c.setFont("Geologica-Regular", 14)
    x, y = 105*mm, 77.6*mm  
    c.drawCentredString(x, y, data["date_start"])

    # Дата конца
    c.setFont("Geologica-Regular", 14)
    x, y = 147*mm, 77.6*mm  
    c.drawCentredString(x, y, data["date_end"])


    # # ФИО педагога
    c.setFont("Geologica-Regular", 12)
    x, y = 30*mm, 37*mm  
    c.drawString(x, y, data["teacher"])



        # Год
    c.setFont("Geologica-Regular", 12)
    x, y = 115*mm, 13*mm  
    c.drawCentredString(x, y, data["year"])




def draw_speed_reading_appendix_level_4(c, data):
    # ФИО
    c.setFont("DelaGothicOne-Regular", 32)
    c.setFillColorRGB(255/255, 84/255, 31/255)
    x, y = 20*mm, 232*mm  
    c.drawString(x, y, data["student_name"])

  
    
    
    #цель 
    text = data["goal"]

    style = ParagraphStyle(
        name="goal",
        fontName="Geologica-Regular",
        fontSize=14,
        leading=18,
        alignment=TA_LEFT
    )

    p = Paragraph(text, style)

    # рамка текста
    x = 20*mm
    y = 165*mm
    width = 170*mm      # ширина блока
    height = 40*mm     # максимальная высота

    p.wrap(width, height)
    p.drawOn(c, x, y)
    
    
    # чтение до
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 115*mm, 124.3*mm  
    c.drawString(x, y, data["reading_before"])

    # чтение после
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 155*mm, 124.3*mm  
    c.drawString(x, y, data["reading_after"])

    # Мнемотехника до
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 115*mm, 112.5*mm  
    c.drawString(x, y, data["mnemo_before"])

    # Мнемотехника после
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 155*mm, 112.5*mm  
    c.drawString(x, y, data["mnemo_after"])



    # Зрительная до
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 115*mm, 100.7*mm  
    c.drawString(x, y, data["visual_before"])

    # Зрительная после
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 155*mm, 100.7*mm  
    c.drawString(x, y, data["visual_after"])


    # Наглядно до
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 115*mm, 88.9*mm  
    c.drawString(x, y, data["image_before"])

    # Наглядно после
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 155*mm, 88.9*mm  
    c.drawString(x, y, data["image_after"])


    # Динамическая до
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 115*mm, 77.1*mm  
    c.drawString(x, y, data["dynamic_before"])

    # Динамическая после
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 155*mm, 77.1*mm  
    c.drawString(x, y, data["dynamic_after"])



    # ФИО педагога
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 20*mm, 38*mm  
    c.drawString(x, y, data["teacher"])


    # Год
    c.setFont("Geologica-Regular", 14)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 20*mm, 20*mm  
    c.drawString(x, y, data["year"])




