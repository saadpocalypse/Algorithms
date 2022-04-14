# Assignment 2

## Question 1
In python or C++, implement the 0/1 Knapsack problem via Dynamic Programming approach. Attach at least 3 screenshots of different test cases to verify your correct implementation. 

## Answer
```
def knapsack(weightOfItem, profitOfItem, columnChosen, rowChosen, tableArgument):
    if rowChosen == 0 or columnChosen == 0:  # This function fills the table to calculate the maximum profit.
        return 0
    if tableArgument[rowChosen][columnChosen] != -1:
        return tableArgument[rowChosen][columnChosen]

    if weightOfItem[rowChosen - 1] <= columnChosen:
        tableArgument[rowChosen][columnChosen] = max((profitOfItem[rowChosen - 1] +
                                                      knapsack(weightOfItem, profitOfItem, columnChosen -
                                                               weightOfItem[rowChosen - 1], rowChosen - 1,
                                                               tableArgument)),
                                                     knapsack(weightOfItem, profitOfItem, columnChosen,
                                                              rowChosen - 1, tableArgument))
        return tableArgument[rowChosen][columnChosen]
    elif weightOfItem[rowChosen - 1] > columnChosen:
        tableArgument[rowChosen][columnChosen] = knapsack(weightOfItem, profitOfItem, columnChosen,
                                                          rowChosen - 1, tableArgument)
        return tableArgument[rowChosen][columnChosen]


def itemsToTake(weightsList, weightOfKnapsack, numberOfItems, tableArgument, listOfItems):
    while numberOfItems > 0 and weightOfKnapsack > 0:  # This function figures out what items contribute to the profit.
        if tableArgument[numberOfItems][weightOfKnapsack] == tableArgument[numberOfItems - 1][weightOfKnapsack]:
            numberOfItems = numberOfItems - 1
        else:
            listOfItems[numberOfItems - 1].flag = True
            numberOfItems = numberOfItems - 1
            weightOfKnapsack = weightOfKnapsack - weightsList[numberOfItems]

    return listOfItems


class Item:  # All the items in my code are stored as objects of this class where the flag attribute determines
    # whether or not they are contributing to the final profit.
    def __init__(self, weight, profit, flag=False):
        self.weight = weight
        self.profit = profit
        self.flag = flag


def tableMaker(rows, columns):
    table = []  # This function generates an empty table.
    for i in range(0, rows + 1):
        table.append([])

    for element in table:
        for i in range(0, columns + 1):
            element.append(-1)

    return table


def driver(weightOfKnapsack, numberOfItems, weights, profits):
    table = tableMaker(numberOfItems, weightOfKnapsack)  # This function uses all the functions mentioned above and
    # prints the appropriate output.

    objectsList = []
    for i in range(0, numberOfItems):
        objectsList.append(Item(weights[i], profits[i]))

    for row in range(numberOfItems + 1):
        for column in range(weightOfKnapsack + 1):
            knapsack(weights, profits, column, row, table)

    for row in range(0, numberOfItems + 1):  # Here I change all the negative ones I initiated the grid with to zeros.
        for column in range(0, weightOfKnapsack + 1):  # I initiated with negative ones since I needed any
            # non-zero negative number to initiate the table with as to avoid miscalculations.
            if table[row][column] == -1:
                table[row][column] = 0

    for row in table:
        print(row)

    itemsToTake(weights, weightOfKnapsack, numberOfItems, table, objectsList)
    listTaken = []
    for element in objectsList:
        if element.flag:
            listTaken.append(1)
        else:
            listTaken.append(0)
    print(listTaken)
    print()


def main():  # This function calls the driver function with different values being passed as arguments.
    # Max weight of knapsack, number of items, list of weights, list of profits
    driver(11, 4, [4, 5, 6, 7], [2, 4, 8, 9])
    driver(10, 3, [3, 4, 5], [4, 5, 6])
    driver(10, 3, [4, 5, 6], [3, 4, 5])


main()
```
### Test case 1:

When I execute the following code:

```
driver(11, 4, [4, 5, 6, 7], [2, 4, 8, 9])
```
The output is:
```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4]
[0, 0, 0, 4, 5, 5, 5, 9, 9, 9, 9]
[0, 0, 0, 4, 5, 6, 6, 9, 10, 11, 11]
[0, 1, 1]
```
which is correct.

### Test case 2:

When I execute the following code:

```
driver(10, 3, [3, 4, 5], [4, 5, 6])
```
The output is:
```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4]
[0, 0, 0, 4, 5, 5, 5, 9, 9, 9, 9]
[0, 0, 0, 4, 5, 6, 6, 9, 10, 11, 11]
[0, 1, 1]
```
which is correct.

### Test case 3:

When I execute the following code:

```
driver(10, 3, [4, 5, 6], [3, 4, 5])

```
The output is:
```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
[0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3]
[0, 0, 0, 0, 3, 4, 4, 4, 4, 7, 7]
[0, 0, 0, 0, 3, 4, 5, 5, 5, 7, 8]
[1, 0, 1]
```
which is correct.

## Question 2
Modify the program made in the first question to display the item numbers filled in your knapsack. You need to maintain a separate list/array to keep track of the items. Test your program and perform a time analysis on it.

## Answer
In my code, a separate list of items is made where the items are stored as objects of a class.
```
class Item:  # All the items in my code are stored as objects of this class where the flag attribute determines
    # whether or not they are contributing to the final profit.
    def __init__(self, weight, profit, flag=False):
        self.weight = weight
        self.profit = profit
        self.flag = flag
```
The items in the list have an attribute, flag, which is updated if the item is contributed to the final profit. Finally, the flags of the list are printed. The function which determines whether or not the product is contributing to the final profit is:
```
def itemsToTake(weightsList, weightOfKnapsack, numberOfItems, tableArgument, listOfItems):
    while numberOfItems > 0 and weightOfKnapsack > 0:  # This function figures out what items contribute to the profit.
        if tableArgument[numberOfItems][weightOfKnapsack] == tableArgument[numberOfItems - 1][weightOfKnapsack]:
            numberOfItems = numberOfItems - 1
        else:
            listOfItems[numberOfItems - 1].flag = True
            numberOfItems = numberOfItems - 1
            weightOfKnapsack = weightOfKnapsack - weightsList[numberOfItems]

    return listOfItems
```
How the function basically works is that it takes the table that was populated by the function _**knapsack**_ and it starts with the last element of the last row of the item. The function has to determine whether or not the item this row represents is contributing to the final profit. It checks the value in the box and then it checks the value in the box above, if the value in the box above is lesser, then the current row’s item is contributing the final profit. The weight of the current object is deducted from the maximum capacity of the knapsack and the cursor moves to the previous row. If the value in the box above is the same, then the current row’s item does not contribute to the final profit and the cursor moves above without triggering the item’s flag or deducting the weight from the maximum capacity of the knapsack. In any case, it has to check every single row of the table generated, and since the number of rows generated is equal to the number of total items, if the number of total items is denoted by x, the the time complexity of the function itemsToTake is O(x), since it is a simple traversal in a while loop.


