# Modulo and for loops

x % 2 == 0: Remainder is non present: even division

for loop test:

for i in range(1,101):
    if i < 10:
            print(i, end='  ')
    elif i % 10 == 0:
            print(i, end='\n')
    else:
            print(i, end=' ')