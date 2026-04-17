from reportlab.lib.units import mm

from pathlib import Path
from pathlib import Path
from reportlab.lib import colors




def draw_chemistry_level_1(c, data):
    # ФИО
    c.setFont("Geologica-Bold", 36)
    c.setFillColorRGB(227/255, 54/255, 89/255)
    x, y = 25*mm, 115*mm  
    c.drawString(x, y, data["student_name"])

    # Курс
    # Программа / ступень
    
    
    #академ часы 
    
    
    
    # Дата начала
    

    # Дата конца
   


    # ФИО педагога
    c.setFont("Georgia-Bold", 18)
    c.setFillColorRGB(58/255, 86/255, 156/255)
    x, y = 80*mm, 38*mm  
    c.drawString(x, y, data["teacher"])



    # Год
    c.setFont("Georgia-Regular", 16)
    c.setFillColorRGB(58/255, 86/255, 156/255)
    x, y = 166*mm, 19.2*mm  
    c.drawCentredString(x, y, data["year"])



