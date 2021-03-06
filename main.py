import img_reader, text_translator, sys

def main():
	
	if len(sys.argv) > 1:
		image_file = sys.argv[1]
	else:
		image_file = 'images/ch1.png'
	image_text_file = 'img_txt.txt'
	output_file = 'output.txt'
	img_reader.image_reader(image_file, image_text_file)
	print('Obtained text from image!')
	text_translator.translate_text(image_text_file, output_file)

if __name__ == '__main__':
	main()