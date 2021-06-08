import pytesseract
from PIL import Image
import io
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def image_reader(image_file, image_text_file):

    text = pytesseract.image_to_string(Image.open(image_file), lang='chi_tra')

    d = io.open('temp.txt', 'w', encoding='utf-8')
    d.write(text)
    d.write('\n')
    d.close()

    d = io.open(image_text_file, 'w', encoding='utf-8')

    with io.open('temp.txt', encoding='utf-8') as f:
        d.write(''.join(line for line in f if not line.isspace()))

    os.remove('temp.txt')