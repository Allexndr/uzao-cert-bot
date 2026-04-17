from reportlab.lib.units import mm

from pathlib import Path
from pathlib import Path
from reportlab.lib import colors

from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth



    
def draw_english_level_2(c, data):

    LEVEL_LABELS = {
        "pre_a1": "Pre-A1",
        "a1": "A1",
        "a2": "A2",
        "b1": "B1",
        "b2": "B2",
        "c1": "C1",
        "c2": "C2",
    }
    level = LEVEL_LABELS.get(data["base_level"], data["base_level"])
    # Настройки шрифта и цвета
    font_name = "Nunito-Black"
    font_size = 48
    c.setFont(font_name, font_size)
    c.setFillColorRGB(227/255, 27/255, 64/255)

    # Координаты и ширина для текста
    x, y = 19.7*mm, 135*mm
    max_width = 160*mm
    line_height = 1.2  # множитель высоты строки

    # Разделяем фамилию и остальные слова
    parts = data["student_name"].split()
    if len(parts) == 0:
        return
    last_name = parts[0]  # первая часть — фамилия
    rest_name = " ".join(parts[1:])  # остальные слова — имя и отчество

    # Рисуем фамилию (на одной строке)
    c.drawString(x, y, last_name)
    y -= font_size * line_height

    # Рисуем оставшиеся слова с переносом
    line = ""
    words = rest_name.split()
    for word in words:
        test_line = line + (" " if line else "") + word
        if stringWidth(test_line, font_name, font_size) <= max_width:
            line = test_line
        else:
            c.drawString(x, y, line)
            y -= font_size * line_height
            line = word
    if line:
        c.drawString(x, y, line)
    
    
    # уровнь 
    c.setFont("Arialb", 12)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 116.5*mm, 99*mm  
    c.drawString(x, y, level)


    # баллы набрано 
    c.setFont("Arialb", 22)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 18.7*mm, 76.1*mm  
    c.drawString(x, y, data["eng_score"])

    # баллы всего 
    c.setFont("Arial", 11)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 24*mm, 66.5*mm  
    c.drawString(x, y, data["eng_total"])


    # ФИО педагога
    c.setFont("Arial", 12)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 64.4*mm, 18.9*mm  
    c.drawString(x, y, data["teacher"])



    # Год
    c.setFont("Arial", 11)
    c.setFillColorRGB(0/255, 0/255, 0/255)
    x, y = 35*mm, 99*mm  
    c.drawCentredString(x, y, data["year"])



