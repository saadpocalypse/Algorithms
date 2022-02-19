# This is all the data we will use in the program.
alphabets = "abcdefghijklmnopqrstuvwxyz"
englishWordsFile = open("English Words.txt", "r")
wordBoxFile = open("Word Box.txt", "r")
currentIndex = 0
wordBox = []
allStringsPossible = []  # This array will hold every horizontal line, vertical line and every diagonal.
# Both backwards and forwards.


#  This function creates a 2D array that holds all the data from the word box file.
def tableMaker(size, array):
    for iteration in range(0, size):
        array.append([])


# This function populates the 2D array.
def populateArray():
    indexChosen = 0
    while True:
        character = wordBoxFile.read(1)  # We read the file character by character.
        if not character:
            break

        elif character != "\n":
            wordBox[indexChosen].append(character.lower())
            if len(wordBox[indexChosen]) == 9:
                indexChosen = indexChosen + 1


def printBox(arrayInput):  # This function is to print the word box for the user.
    for row in range(0, 9):
        print(*arrayInput[row], sep="  ")


class ListOfDictionaries:  # This class creates an object that acts as a dictionary.
    # It creates a list that contains all the words of different alphabets stored at different indexes.
    # Exactly like a physical dictionary.
    def __init__(self, alphabetString, listOfWords=None):
        self.alphabetString = alphabetString
        if listOfWords is None:
            listOfWords = [[], [], [], [], [], [], [], [], [], [], [],
                           [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.listOfWords = listOfWords

    def addWord(self, argument):
        initialLetter = argument[0]
        letterIndex = self.alphabetString.index(initialLetter)
        self.listOfWords[letterIndex].append(argument)

    def returnList(self):
        return self.listOfWords


def englishLists():  # This function uses the class ListOfDictionaries to creat an English Dictionary.
    englishObject = ListOfDictionaries(alphabets)
    for wordChosen in englishWordsFile:
        wordChosen = wordChosen.strip("\n")
        if 3 <= len(wordChosen) <= 9:  # We ignore all the words with less than 3 letters and more than 9.
            englishObject.addWord(wordChosen)  # 9 is the maximum size of our word box.

    return englishObject.returnList()


# This function isolates every horizontal and vertical line backwards and forwards.
def concatenation(arrayInput, arrayOfStrings):
    for row in range(0, 9):
        horizontal = ""
        vertical = ""
        for column in range(0, 9):
            horizontal = horizontal + arrayInput[row][column]
            vertical = vertical + arrayInput[column][row]

        horizontalReversed = horizontal[::-1]
        horizontal = horizontal + " " + horizontalReversed
        verticalReversed = vertical[::-1]
        vertical = vertical + " " + verticalReversed
        arrayOfStrings.append(horizontal)
        arrayOfStrings.append(vertical)


# This function isolates every diagonal (except that have a size less than 3) backwards and forwards.
def diagonals(arrayInput, arrayOfStrings):
    listOfDiagonals = []
    for diagonal in range(0, 13):
        listOfDiagonals.append("")

    for row in range(0, 9):
        for column in range(0, 9):
            if row - column == 6:
                listOfDiagonals[0] = listOfDiagonals[0] + arrayInput[row][column]
            if row - column == 5:
                listOfDiagonals[1] = listOfDiagonals[1] + arrayInput[row][column]
            if row - column == 4:
                listOfDiagonals[2] = listOfDiagonals[2] + arrayInput[row][column]
            if row - column == 3:
                listOfDiagonals[3] = listOfDiagonals[3] + arrayInput[row][column]
            if row - column == 2:
                listOfDiagonals[4] = listOfDiagonals[4] + arrayInput[row][column]
            if row - column == 1:
                listOfDiagonals[5] = listOfDiagonals[5] + arrayInput[row][column]
            if row - column == 0:
                listOfDiagonals[6] = listOfDiagonals[6] + arrayInput[row][column]
            if row - column == -1:
                listOfDiagonals[7] = listOfDiagonals[7] + arrayInput[row][column]
            if row - column == -2:
                listOfDiagonals[8] = listOfDiagonals[8] + arrayInput[row][column]
            if row - column == -3:
                listOfDiagonals[9] = listOfDiagonals[9] + arrayInput[row][column]
            if row - column == -4:
                listOfDiagonals[10] = listOfDiagonals[10] + arrayInput[row][column]
            if row - column == -5:
                listOfDiagonals[11] = listOfDiagonals[11] + arrayInput[row][column]
            if row - column == -6:
                listOfDiagonals[12] = listOfDiagonals[12] + arrayInput[row][column]

    for i in range(0, len(listOfDiagonals)):
        arrayOfStrings.append(listOfDiagonals[i] + " " + listOfDiagonals[i][::-1])


# This function finds all the words that are in the word box
def findWords(dictionary):
    for element in allStringsPossible:
        wordsChecked = []  # We first create a list so we do not repeat checks for the same letter.
        for i in range(0, len(element)):
            if element[i] not in wordsChecked and element[i] != " ":
                wordsChecked.append(element[i])
                dictionaryChosen = dictionary[alphabets.index(element[i])]
                for word in dictionaryChosen:  # We go to the specific letter's dictionary.
                    if word in element:  # We do not iterate through useless letters.
                        print(word)


def main():
    try:
        tableMaker(9, wordBox)
        populateArray()
        printBox(wordBox)
        print("\nThe following words were found in the word box: ")
        diagonals(wordBox, allStringsPossible)
        concatenation(wordBox, allStringsPossible)
        englishWords = englishLists()
        findWords(englishWords)
    except:
        print("The grid entered is incorrect! The game accepts a standard 9 x 9 grid of English letters!")


main()
