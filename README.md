# image-to-translated-text

Translation of foreign languages using Image Analytics and Data Extraction

This project uses: 
1. [pytesseract](https://pypi.org/project/pytesseract/)
2. [PIL](https://pillow.readthedocs.io/en/stable/reference/Image.html)
3. [googletrans](https://pypi.org/project/googletrans/)

## How to run

The image file path can be given as command line argument.
Run the following command in the terminal:

```
python main.py path/filename
```
Example:
```
python main.py images/ch1.png
```

In `img_reader.py`, `image_reader()` gets the image and converts its contents to a string. The language of the text in the image is mentioned in `image_to_string()`.

`text = pytesseract.image_to_string(Image.open(image_file), lang='chi_tra')`

In `text_translator.py`, googletrans is used to translate the obtained text.
