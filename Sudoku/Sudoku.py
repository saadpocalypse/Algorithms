def sudokuGridGenerator(variation, gridArgument):  # This function generates a sudokuGrid
    for i in range(0, 9):                          # It takes difficulty level and an empty array as an argument
        gridArgument.append([" ", " ", " ", " ", " ", " ", " ", " ", " "])

    if variation == 1:  # This is one of the difficulties.
        gridArgument[0][0] = 9
        gridArgument[0][4] = 7
        gridArgument[0][8] = 3  # Some values are hardcoded into the board
        gridArgument[1][3] = 9
        gridArgument[2][2] = 8
        gridArgument[2][6] = 6
        gridArgument[3][7] = 1
        gridArgument[4][0] = 5
        gridArgument[4][4] = 6
        gridArgument[4][8] = 9
        gridArgument[5][1] = 7
        gridArgument[6][2] = 3
        gridArgument[6][6] = 1
        gridArgument[7][5] = 1
        gridArgument[8][0] = 8
        gridArgument[8][4] = 9
        gridArgument[8][8] = 7
        hardCodedValues = [gridArgument[0][0], gridArgument[0][4], gridArgument[0][8], gridArgument[1][3],
                           gridArgument[2][2],
                           gridArgument[2][6], gridArgument[3][7], gridArgument[4][0], gridArgument[4][4],
                           gridArgument[4][8],
                           gridArgument[5][1], gridArgument[6][2], gridArgument[6][6], gridArgument[7][5],
                           gridArgument[8][0],
                           gridArgument[8][4], gridArgument[8][8]]

    elif variation == 2:  # The hardcoded values are returned to make sure user does not overwrite them.
        gridArgument[4][0] = 4
        gridArgument[5][1] = 1
        gridArgument[7][3] = 2
        gridArgument[7][5] = 8
        gridArgument[8][4] = 4
        gridArgument[4][8] = 1
        gridArgument[5][7] = 2
        hardCodedValues = [gridArgument[4][0], gridArgument[5][1], gridArgument[7][3], gridArgument[7][5],
                           gridArgument[8][4], gridArgument[4][8], gridArgument[5][7]]

    else:
        gridArgument[2][2] = 9
        gridArgument[6][6] = 9
        hardCodedValues = [gridArgument[2][2], gridArgument[6][6]]

    return hardCodedValues


def sudokuBoardPrinter(gridArgument):  # This function prints the sudoku board.
    print("_" * 37)
    for column, row in enumerate(gridArgument):
        print(("|" + " {}   {}   {} |" * 3).format(*[node for node in row]))
        if column == 8:
            print("-" * 37)
        elif column % 3 == 2:
            print("|" + "---+" * 8 + "---|")
        else:
            print("|" + "   +" * 8 + "   |")

    print()


def winChecker(gridArgument):  # This function is used to check if the user has won.
    gridOne = [gridArgument[0][0], gridArgument[0][1], gridArgument[0][2], gridArgument[1][0], gridArgument[0][1],
               gridArgument[1][2], gridArgument[2][0], gridArgument[2][1], gridArgument[2][2]]
    gridTwo = [gridArgument[0][3], gridArgument[0][4], gridArgument[0][5], gridArgument[1][3], gridArgument[1][4],
               gridArgument[1][5], gridArgument[2][3], gridArgument[2][4], gridArgument[2][5]]
    gridThree = [gridArgument[0][6], gridArgument[0][7], gridArgument[0][8], gridArgument[1][6], gridArgument[1][7],
                 gridArgument[1][8], gridArgument[2][6], gridArgument[2][7], gridArgument[2][8]]
    gridFour = [gridArgument[3][0], gridArgument[3][1], gridArgument[3][2], gridArgument[4][0], gridArgument[4][1],
                gridArgument[4][2], gridArgument[5][0], gridArgument[5][1], gridArgument[5][2]]
    gridFive = [gridArgument[3][3], gridArgument[3][4], gridArgument[3][5], gridArgument[4][3], gridArgument[4][4],
                gridArgument[4][5], gridArgument[5][3], gridArgument[5][4], gridArgument[5][5]]
    gridSix = [gridArgument[3][6], gridArgument[3][7], gridArgument[3][8], gridArgument[4][6], gridArgument[4][7],
               gridArgument[4][8], gridArgument[5][6], gridArgument[5][7], gridArgument[5][8]]
    gridSeven = [gridArgument[6][0], gridArgument[6][1], gridArgument[6][2], gridArgument[7][0], gridArgument[7][1],
                 gridArgument[7][2], gridArgument[8][0], gridArgument[8][1], gridArgument[8][2]]
    gridEight = [gridArgument[6][3], gridArgument[6][4], gridArgument[6][5], gridArgument[7][3], gridArgument[7][4],
                 gridArgument[7][5], gridArgument[8][3], gridArgument[8][4], gridArgument[8][5]]
    gridNine = [gridArgument[6][6], gridArgument[6][7], gridArgument[6][8], gridArgument[7][6], gridArgument[7][7],
                gridArgument[7][8], gridArgument[8][6], gridArgument[8][7], gridArgument[8][8]]
    # All the grids have been individually isolated.

    grids = [gridOne, gridTwo, gridThree, gridFour, gridFive, gridSix, gridSeven, gridEight, gridNine]

    horizontals = [[], [], [], [], [], [], [], [], []]
    verticals = [[], [], [], [], [], [], [], [], []]

    horizontalErrors = []  # These arrays hold the lines at which errors exist.
    verticalErrors = []

    for row in range(0, 9):  # All the horizontal and vertical lines are isolated here.
        for column in range(0, 9):
            rowElement = gridArgument[row][column]
            columnElement = gridArgument[column][row]

            if rowElement == " ":
                rowElement = 0

            if columnElement == " ":
                columnElement = 0

            horizontals[row].append(rowElement)
            verticals[row].append(columnElement)

    gridErrors = []  # This array holds the grids at which errors exist.

    for box in range(0, 9):  # The errors are added to error arrays here.
        if " " in grids[box]:
            gridErrors.append(box + 1)

    for rowChosen in range(0, len(horizontals)):
        if 0 in horizontals[rowChosen]:
            horizontalErrors.append(rowChosen + 1)

    for columnChosen in range(0, len(verticals)):
        if 0 in verticals[columnChosen]:
            verticalErrors.append(columnChosen + 1)

    if len(gridErrors) == 0 and len(horizontalErrors) == 0 and len(verticalErrors) == 0:
        return True  # If there are no errors, the user wins.

    else:
        for i in range(0, len(gridErrors)):
            print("You have an error in grid number {0}!".format(gridErrors[i]))
        print()
        for i in range(0, len(horizontalErrors)):
            print("You have an error in row number {0}!".format(horizontalErrors[i]))
        print()
        for i in range(0, len(verticalErrors)):
            print("You have an error in column number {0}!".format(verticalErrors[i]))
        return False  # Otherwise, just the errors are printed.


def main():  # This is the main driver function.
    quittingFlag = False  # The flag is used to determine whether to end the program or not.
    while True:  # All the while loops make sure the mis-input is repeated, not the whole function.
        if not quittingFlag:
            while True:
                difficulty = int(input("What difficulty do you want to play at?\n1) Easy\n2) Medium\n3) Hard\n"))
                if difficulty < 1 or difficulty > 3:
                    print("Please select a difficulty level between 1 and 3!")
                else:
                    break
            sudokuGrid = []
            fixedValues = sudokuGridGenerator(difficulty, sudokuGrid)  # The grid is generated here.
            sudokuBoardPrinter(sudokuGrid)
        else:
            break

        while True:
            choiceInput = int(input("\nWhat do you want to do?\n1) Enter a number\n2) Check if you have won\n"
                                    "3) Restart\n4) Quit game\n"))

            if choiceInput == 1:
                while True:
                    rowInput = int(input("Enter number of row (1 - 9): \n"))
                    rowInput = rowInput - 1
                    columnInput = int(input("Enter number of column (1 - 9): \n"))
                    columnInput = columnInput - 1

                    if rowInput > 8 or rowInput < 0 or columnInput > 8 or columnInput < 0:
                        print("Wrong input, try again! Pick numbers between 1 and 9!\n")

                    elif sudokuGrid[rowInput][columnInput] in fixedValues:
                        print("Sorry, that box is hardcoded, try again!\n")

                    else:
                        break

                while True:
                    numberInput = int(input("Enter a number between 1 and 9: \n"))
                    if numberInput < 1 or numberInput > 9:
                        print("Incorrect input, try again! Pick a number between 1 and 9!\n")
                    else:
                        sudokuGrid[rowInput][columnInput] = numberInput
                        sudokuBoardPrinter(sudokuGrid)
                        break

            elif choiceInput == 2:
                result = winChecker(sudokuGrid)
                if result:
                    print("Congratulations, you won!")
                    quittingFlag = True
                    break

            elif choiceInput == 3:
                break

            elif choiceInput == 4:
                quittingFlag = True
                break


main()