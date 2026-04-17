from reportlab.lib.units import mm

from pathlib import Path
from pathlib import Path
from reportlab.lib import colors




def draw_chemistry_level_4(c, data):
    # ФИО
    c.setFont("Geologica-Bold", 36)
    c.setFillColorRGB(227/255, 54/255, 89/255)
    x, y = 25*mm, 114*mm  
    c.drawString(x, y, data["student_name"])

    # Курс
    # Программа / ступень
    
    
    #академ часы 
    
    
    
    # Дата начала
    

    # Дата конца
   


    # ФИО педагога
    c.setFont("Georgia-Bold", 18)
    c.setFillColorRGB(58/255, 86/255, 156/255)
    x, y = 85*mm, 40*mm  
    c.drawString(x, y, data["teacher"])



    # Год
    c.setFont("Georgia-Regular", 16)
    c.setFillColorRGB(58/255, 86/255, 156/255)
    x, y = 163*mm, 22.8*mm  
    c.drawCentredString(x, y, data["year"])



