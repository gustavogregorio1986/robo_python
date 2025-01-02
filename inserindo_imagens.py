from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
sheet = wb.active

img = Image("logo.png")