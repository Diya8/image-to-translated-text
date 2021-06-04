import img_reader
import text_translator

def main():
	image_file = 'images/ch1.png'
	image_text_file = 'img_txt.txt'
	output_file = 'output.txt'
	img_reader.image_reader(image_file, image_text_file)
	print('Obtained text from image!')
	text_translator.translate_text(image_text_file, output_file)
	print('Translated text saved in ' + output_file + ' successfully!')
if __name__ == '__main__':
	main()