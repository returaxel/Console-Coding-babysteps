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


## Assignment 2:

In this assignment, you are going to write your first console application.

### The goal
Write a program that is a number guessing program. Effectively, you are going to guess the number and your program will tell you if you got it right. 

## You need to know...
You need to know the following concepts first:

* if / elif / else statements

* >   <   <=   >=   =   == operands

* Difference between int() and str()

## If you get stuck
If you get stuck, Google is your friend. You can always reach me on WhatsApp if you get stuck, we'll work it through together. Remember that you need to use input() to take in values from the user, and that input() will take inputs as str(). To take input as integers, use
	
	# foo will be of datatype int()
	foo = int(input('Your guess?'))

	# bar will be of datatype str()
	bar = input('Your guess?')

## A hint
In Psuedo code, one could write something like this...

	answer is 190
	guess is input 'Guess my number!'

	if the guess is not equal to the answer,
		write 'Sorry, wrong answer.'

This example will terminate the program as soon as you either hit the right
answer OR miss it. It will also not give you any input on whether you were
too high or too low in your guess. Not very nice. Let's be more nice. 

	answer is 190
	guess is input 'Guess my number!'

	if the guess is less than answer,
		write 'Too low!'
	but the guess is higher than answer,
		write 'Too high'
	otherwise,
		write 'Correct!'

See the difference? Now, you are using your if clause to give feedback, helping the user hit the right target.