# Coffee machine by Simon Olofsson

# Display the different options for the user. Example:
# Pick your beverage. Press the number and then enter.

# "Latte" 35 SEK
# "Cappuccino" 40 SEK
# "Moccaccino" 40 SEK
# "Black coffee" 30 SEK
# Pick your size.

# "Small" (X + 0)
# "Medium" (X + 10)
# "Large" (X + 15)
# # Your "beverage_here" is being brewed. Total amount: X SEK

bvg_choice = 0
bvg_size = 0

while bvg_choice < 1 or bvg_choice > 3:
	# Choose type of beverage
	print('Pick your beverage! Press the number and enter.', end='\n')
	print('1. Latte 35 SEK', '2. Capuccino 40 SEK', '3. Mocaccino 40 SEK', sep='\n', end='\n')
	bvg_choice = int(input('Make your choice: '))

while bvg_size < 1 or bvg_choice > 3:
	# Choose the size of beverage
	print('\n' + 'Now pick a size: ')
	print('1. Small', '2. Medium (+ 10 SEK)', '3. Large (+ 15 SEK)', sep='\n', end='\n')
	bvg_size = int(input('Make your choice: '))

# Evaluate price for the beverage.
if bvg_choice == 1:
	price = 35
elif bvg_choice == 2 or bvg_choice == 3:
	price = 40

# Evaluate price including beverage size.
if bvg_size == 2:
	price += 10
elif bvg_size == 3:
	price += 15

print('\n','Your beverage is brewing. The total amount is:','\n')
print(str(price), 'SEK')
input()