# image-to-translated-text

Translation of foreign languages using Image Analytics and Data Extraction

This project uses: 
1. [pytesseract](https://pypi.org/project/pytesseract/)
2. [io](https://docs.python.org/3/library/io.html)
3. [PIL](https://pillow.readthedocs.io/en/stable/reference/Image.html)
4. [googletrans](https://pypi.org/project/googletrans/)

The image file should be initialized into `image_file` in `main.py`.

In `img_reader.py`, `image_reader()` gets the image and converts its contents to a string. The language of the text in the image is mentioned in `image_to_string()`.

`text = pytesseract.image_to_string(Image.open(image_file), lang='chi_tra')`

In `text_translator.py`, we use googletrans to translate the obtained text.

## How to run

Run the following command in the terminal:

```
python main.py
```

