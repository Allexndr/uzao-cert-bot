from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

FONTS_DIR = os.path.join(BASE_DIR, "pdf", "fonts")

pdfmetrics.registerFont(
    TTFont("Geologica-Regular", os.path.join(FONTS_DIR, "Geologica-Regular.ttf"))
)
pdfmetrics.registerFont(
    TTFont("Georgia-Regular", os.path.join(FONTS_DIR, "georgia.ttf"))
)
pdfmetrics.registerFont(
    TTFont("Georgia-Bold", os.path.join(FONTS_DIR, "georgiab.ttf"))
)
pdfmetrics.registerFont(
    TTFont("Geologica-Bold", os.path.join(FONTS_DIR, "Geologica-Bold.ttf"))
)
pdfmetrics.registerFont(
    TTFont("DelaGothicOne-Regular", os.path.join(FONTS_DIR, "DelaGothicOne-Regular.ttf"))
)

pdfmetrics.registerFont(
    TTFont("Nunito-Black", os.path.join(FONTS_DIR, "Nunito-Black.ttf"))
)
pdfmetrics.registerFont(
    TTFont("Arial", os.path.join(FONTS_DIR, "Arial.ttf"))
)
pdfmetrics.registerFont(
    TTFont("Arialb", os.path.join(FONTS_DIR, "Arialb.ttf"))
)

def generate_certificate_from_template(
    template_path: str,
    output_path: str,
    draw_func,     # ⬅️ ВАЖНО
    data: dict
):
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)

    # ⬇️ ВСЯ ОТРИСОВКА уходит наружу
    
    draw_func(c, data)

    c.save()
    packet.seek(0)

    template = PdfReader(template_path)
    overlay = PdfReader(packet)

    page = template.pages[0]
    page.merge_page(overlay.pages[0])

    writer = PdfWriter()
    writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)