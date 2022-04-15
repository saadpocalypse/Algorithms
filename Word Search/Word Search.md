# Word Search

## Assignment Rules
* Do not rely heavily on Python's built-in functions.
* Do not import any libraries.

## Logic

My program takes two files as input:
* Word Box.txt, which consists of a 9x9 grid of random letters.
* English Words.txt, which consists of all the words in the English language.

The program creates a 'dictionary' of all the words, splitting them into 26 different arrays, one for each letter. <br><br>
Then, the program isolates all the diagonals, columns and rows, forwards and backwards as strings. <br><br>
The program goes through these strings character by character, it runs every possible word of the chosen character through a function that checks whether or not the word exists in the particular string. <br><br>
To make the program more efficient, all the words below the legnth of 3 and greater than 9 are filtered out and no character is checked for twice in a single string. <br><br>
I created a function to create a multi-dimensional array of the _Word Box.txt_ to print for the user and at the end, all the words that are found in the Word Box are printed as well.
