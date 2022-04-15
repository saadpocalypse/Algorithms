# Word Search

## Assignment Rules
* Do not rely heavily on Python's built-in functions.
* Do not import any libraries.

## Logic

My program takes two files as input:
* Word Box.txt, which consists of a 9x9 grid of random letters.
* English Words.txt, which consists of all the words in the English language.

The program creates a 'dictionary' of all the words, splitting them into 26 different arrays, one for each letter. <br>
Then, the program isolates all the diagonals, columns and rows, forwards and backwards as strings. <br>
The program goes through these strings character by character, it runs every possible word of the chosen character through a function that checks whether or not the word exists in the particular string. <br>
To make the program more efficient, all the words below the legnth of 3 and greater than 9 are filtered out. <br>
