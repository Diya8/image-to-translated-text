from googletrans import Translator
import io, os

def translate_text(image_text_file, output_file):
	translator = Translator(service_urls = ['translate.googleapis.com'])

	f = io.open(image_text_file, 'r', encoding='utf-8')
	t = io.open(output_file, 'w', encoding='utf-8')
	lines = f.readlines()

	results = translator.translate(lines)

	print("\nTranslated text:\n")
	for r in results:
		t.write(r.text+'\n')
		print(r.text)
	f.close()
	t.close()
	os.remove(image_text_file)
	os.remove(output_file)
	print()