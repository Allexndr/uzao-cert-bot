from reportlab.lib.units import mm

from pathlib import Path
from pathlib import Path





def draw_mental_level_1(c, data):
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
    x, y = 107*mm, 77.6*mm  
    c.drawCentredString(x, y, data["date_start"])

    # Дата конца
    c.setFont("Geologica-Regular", 14)
    x, y = 151*mm, 77.6*mm  
    c.drawCentredString(x, y, data["date_end"])


     # ФИО педагога
    c.setFont("Geologica-Regular", 12)
    x, y = 30*mm, 37*mm  
    c.drawString(x, y, data["teacher"])



        # Год
    c.setFont("Geologica-Regular", 12)
    x, y = 115*mm, 13*mm  
    c.drawCentredString(x, y, data["year"])



