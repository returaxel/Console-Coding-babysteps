# Initiera variablerna som används direkt i looparna.
bvg_choice = 0
size_choice = 0
payment = 0

# Skapa listor med priser och dryckerna
price_list = [20, 30, 35, 50]
bvg_list = [
	'Mocaccino', 'Capuccino',
	'Latte', 'Coffee with milk',
	'Coffee', 'Chocolate'
]

# Huvud loop: programmet hålls vid liv i oändlighet 
while True:
	
	# Loop som hålls igång så länge användaren inte valt dryck, eller väljer fel
	while bvg_choice < 1 or bvg_choice > 6:	
		print(
			'*	 The best coffee in the world	*','\n',
			'*	   Pick a beverage and size 	*',
			sep = '', end = '\n\n'
		)	
		print(
			'1. Mocaccino			2. Capuccino','\n',
			'3. Latte			4. Coffee with milk','\n',
			'5. Coffee 			6. Chocolate','\n\n',
			'* Please make a selection and press Enter.',
			sep = '', end = '\n\n'
		)	

		bvg_choice = int(input(' -> '))
	
	# Loop som hålls igång så länge användaren inte valt storlek, eller väljer fel
	while size_choice < 1 or size_choice > 4:
		print(
			'1. Small 20 SEK		2. Medium 30 SEK','\n',
			'3. Large 35 SEK		4. Huge 50 SEK','\n\n',
			'* Pick the size for your ', bvg_list[bvg_choice - 1],		
			sep = '', end = '\n\n'
		)
		# Ta inmatning på dryckesvalet från användaren
		size_choice = int(input(' -> '))
	
	# Sätt priset för beställningen lika med dryckens plats i listan minus ett från menyvalet
	price = (price_list[size_choice - 1])

	# Loop som hålls igång så länge användaren inte betalat rätt belopp
	while payment != price:
		print(
			'* Please pay in the slot below.','\n\n',
			'Total: ', str(price), ' SEK',
			sep = '', end = '\n\n'
		)
		# Ta inmatning på deras betalning
		payment = int(input(' -> '))
		# Säkerställ att de betalat rätt. För lite, gör om. För mycket, ge växel och fortsätt.
		if payment < price:
			print('Sorry, you didnt pay enough.')
		elif payment > price:
			print(
				'You paid ', str(payment),'.','\n',
				'Change: ', str(payment - price), ' SEK',
				sep = '', end = '\n\n'
			)
			payment = price

	print(
		'Your',(str(bvg_list[bvg_choice - 1])), 'is brewing. Thank you for your order!',
		end = '\n\n'
	)
	# Nolla variablerna för första loopen så att allt börjar om igen.
	bvg_choice = 0
	size_choice = 0