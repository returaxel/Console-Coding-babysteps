
def main():
	print('''
1. Convert digit to binary
2. Convert text to binary
3. Convert binary to numbers 
4. Convert binary to words
5. Lame, exit \n ''')

	sel = int(input('Select one and press enter: '))
	if sel and sel < 5:
		raw = input('Enter what you wish to convert: ')
		print()
		if sel == 1: 
			raw = int(raw)
			get_bin_from_int(raw)
		elif sel == 2:
			get_bin_from_word(raw)
		elif sel == 3:
			get_int_from_bin(raw)
		elif sel == 4:
			get_chr_from_bin(raw)
		print()
		main()
	else:
		exit()

def get_bin_from_int(raw):
	if type(raw) == str:
		print(raw,'is not a digit!')
		main()
	print(format(raw, "08b"), sep = ' ', end = ' ')


def get_bin_from_word(raw):
	if type(raw) == int:
		print(raw,'is not a word!')
		main()
	for i in raw:
			i = ord(i)
			print(format(i, "08b"), sep = ' ', end = ' ')


def get_int_from_bin(raw):
	raw = str(raw)
	print(int(raw, 2), sep = ' ', end = ' ')


def get_chr_from_bin(raw):
	raw = raw.split()
	for i in raw:
		char = int(i, 2)
		char = chr(char)
		print(char, sep = '', end = '')
		

if __name__ == '__main__':
	main()