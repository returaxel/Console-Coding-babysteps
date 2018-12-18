## Assignment 1:

Write a program that asks for your firstname, lastname and phone number. 
The program will then print it out on the screen. 

Example output:

	>>> What's your name? Bruce
	>>> What's your lastname? Wayne
	>>> What's your phone number? 0701111222
	Your name is Bruce Wayne and your phone number is 0701111222.

# TIP!
## Use input() to ask user for values. 
Remember to declare a variable to store the input in. Example:

	var = input('Your prompt for the user goes here! ') 
whatever the user types is stored in 'var'.

# String concatenation. 
Keep in mind that you can't do math with strings and integers. 
They're not friends like that. If you want to input a digit as a string, input() simply
does this for you. If you want to take in the numbers as integers however, you need to say so.

	var = int(input('What is 1+1? )) 
In this case, the input will be stored in var and the type will be int().
String + string is True! To add content to a string, simply do:

	foo = 'Hakuna '
	foo += 'Matata'
	print(foo)
	>>> Hakuna Matata
the '+=' operand is equal to saying:

	foo = 'Hakuna '
	foo = foo + 'Matata'
We just discard the 'foo = foo +...' way of doing it.

# Keep it simple
	You need to break down the problem:
	Ask for firstname, store it in a variable.
	Ask for lastname, and store it in a separate (or add it to the previous..?) variable.
	Ask for phone number, and store it in a variable. Or... add everything to one variable, as you go!

