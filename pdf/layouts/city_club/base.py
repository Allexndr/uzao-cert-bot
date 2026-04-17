from reportlab.lib.units import mm

from pathlib import Path
from pathlib import Path





def  draw_city_club(c, data):
    # ФИО
    c.setFont("Geologica-Bold", 26)
    x, y = 27.6*mm, 137*mm  
    c.drawString(x, y, data["student_name"])

    
  
    
   
    
    
    # Дата начала
    c.setFont("Geologica-Regular", 14)
    x, y = 86*mm, 111.5*mm  
    c.drawCentredString(x, y, data["date_start"])

    # Дата конца
    c.setFont("Geologica-Regular", 14)
    x, y = 132*mm, 111.5*mm  
    c.drawCentredString(x, y, data["date_end"])


    
    c.setFont("Geologica-Bold", 14)
    x, y = 27.6*mm, 97*mm  
    c.drawString(x, y, data["program_name"])
 



    # Год
    c.setFont("Geologica-Regular", 12)
    x, y = 115*mm, 13*mm  
    c.drawCentredString(x, y, data["year"])



