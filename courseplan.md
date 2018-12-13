
## Konsolkunskap

	* cli vs. gui
	* navigera (cd, ls, tree)
	* starta program från PS
	* stäng av program från PS
	* miljövariabler och variabler
	* skapa, döp, flytta, kopiera och radera mappar och filer
	* skriv data till fil

	# uppgifter:

	* skapa en mapp på ditt skrivbord
	* skriv ditt namn och dagens datum till en fil i mappen
	* kopiera filen i mappen till skrivbordet
	* radera mappen med filen inuti

## Tillfälle 1: introduktion till programmering
	
	* Installera miljön
	* Börja med print()
		- print('Hello world')
	
	* Vad är en variabel? 
		- = vs ==
		- input()
		- string concatenation, var = 3. var += 1
		- type(foo)

	* datatyper
		- str
		- int
		- list
		- tuple
		- float
		- dict
		- set

	# uppgifter:

	DEMO: skapa ett program som frågar ditt för och efternamn och skriver ut det på skärmen.
	DEMO: skapa ett program som ger dig en e-post adress baserat på namn, efternamn och domän.

	Uppgift: skapa ett program som ger dig ordinalen för bokstäver du skriver till programmet
	Uppgift: skapa ett program som ger dig bokstaven för ordinalen du skriver till programmet


## Tillfälle 2: logiskt control flow

	* logical operators
		- logical operators:
			and, or, not, xor, <, >, <=, >=, ==, !=, %
	
	* if / elif / else
		- if 1 == 0 (do something)
		- if foo == bar or foo == foofoo
		- if foo != bar and bar != 0


	# uppgifter:
	
	DEMO: skapa ett program som skriver ut om ett tal är ett primtal eller ej
	DEMO: skapa ett lotteriprogram 
	
	Uppgift: skapa ett program som förstår om du skriver på engelska eller inte.
	(isalpha && ord >= && <= 97 122)



## Tillfälle 3:

	* loopar
	- for loops
	- while loops

	* Boolean statements

	# uppgifter:
	* skapa ett program som räknar sekunder i en halv minut

	DEMO:
		* skapa ett program som frågar efter 10 tal. Programmet ska ha en meny med följande val:
		
		1 Mata in 10 tal
		2 Visa alla tal
		3 Visa det minsta talet
		4 Visa det största talet
		5 Avsluta

		* programmet skriver du med hjälp av följande tekniker:
		 - Initiera en meny med print() och ta in valen från användaren
		 - med en for loop, bygg upp alternativ 1 där inmatningen läggs till i en array
		 - med din array full, kalla på print() metoden för alla i listan.
		 - med din array full, kalla på min() och max() metoden.


## Tillfälle 5: binär matematik i programmering

	- bitwise operators och binära tal
		| & 
		- 128 64 32 16 4 2 (visa bild)
		- konvertera sträng till ordinal
		- räkna ut vad ordinalen av a är i binärt tal 

	# uppgift:
	* skapa ett program som konverterar en mening till binära tal.
		programmet ska ha en meny
		programmet ska kunna konvertera tillbaka det till text
		programmet ska kunna fortsätta i oändlighet, och gå att avsluta i menyn