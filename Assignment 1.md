# Assignment 1 

Note: Stay Java / Python / C++ free.
## Question 1
Consider that you are given a list of odd size. You have to swap the elements in such a way that first element should be swapped with its immediate right neighbouring element, 3rd element should be swapped with its immediate right neighbouring element and so on until all the elements in the list are processed. Middle element should be fixed and should not be swapped with any other element. Design an algorithm based on Brute Force Approach and another one based on Divide & Conquer Approach to solve this problem. <br>


## Answer

### Brute Force Approach
```
counter = 0
for element in inputList:
    if counter == len(inputList) // 2:
        counter = counter + 1
    elif counter + 1 != len(inputList) and counter + 1 != len(inputList) // 2:
        nodeToSwap = inputList[counter]
        inputList[counter] = inputList[counter + 1]
        inputList[counter + 1] = nodeToSwap
        counter = counter + 2
    else:
        counter = counter + 1

```

### Divide and Conquer Approach
```
def swapTwo(inputList, start, end):
    if start + 1 == end:
        nodeToSwap = inputList[start]
        inputList[counter] = inputList[counter + 1]
        inputList[counter + 1] = nodeToSwap
    else:
        middle = (start + end) // 2
        if (start - end + 1) % 2 != 0:
            swapTwo(list, start, middle - 1)
            swapTwo(list, middle + 1, end)
        else:
            if (start + middle) % 2 != 0:
                swapTwo(list, start, middle)
                swapTwo(list, middle + 1, end)
            else:
                swapTwo(list, start, middle + 1)
                swapTwo(list, middle + 2, end)
```

## Question 2
Suppose X, Y and Z are arrays of integers of size M, N, and M + N, respectively. The numbers in array X and Y appear in ascending order. Write an algorithm to produce third array Z by merging arrays X and Y in descending order. (You cannot use the function 'sort'. Devise this logic yourself). Use brute force approach for designing your algorithm.

## Answer
### Brute Force Approach inspired by Insertion Sort Algorithm

```
indexOne = M - 1
indexTwo = N - 1
for indexThree in range(0, M + N):
    xElement = X[indexOne]
    yElement = Y[indexTwo]
    if yElement > xElement:
        z[indexThree] = yElement
        indexTwo = indexTwo - 1
    else:
        z[indexThree] = xElement
        indexOne = indexOne - 1
```
     
## Question 3
Design Divide & Conquer based algorithms for the following operations: <br> (i) multiplication  <br> (ii) subtraction Will these algorthims be logically & mathematically true?    

## Answer
### Multiplication
```
def multiplication(listInput, start, end):
    if start == end:
        return listInput[start]
    elif end - start == 1:
        return listInput[start] * listInput[end]
    if end - start == 2:
        return listInput[start] * listInput[start + 1] * listInput[end]
    else:
        floor = (start + end) // 2
        ceiling = floor * 2
        left = multiplication(listInput, start, floor)
        middle = multiplication(listInput, floor + 1, ceiling)
        right = multiplication(listInput, ceiling + 1, end)
        return left * middle * right
```

### Subtraction
```
def subtraction(listInput, start, end):
    if start == end:
        return listInput[start]
    elif end - start == 1:
        return listInput[start] - listInput[end]
    if end - start == 2:
        return listInput[start] - listInput[start + 1] - listInput[end]
    else:
        floor = (start + end) // 2
        ceiling = floor * 2
        left = subtraction(listInput, start, floor)
        middle = subtraction(listInput, floor + 1, ceiling)
        right = subtraction(listInput, ceiling + 1, end)
        return left - middle - right
```

Multiplication through divide and conquer makes logical and mathematical since due to the associative property of multiplication, which states that the mode of grouping of factors does not change the final result of the multiplication process. <br> <br>
(1 * 2) * 3 = 1 * (2 * 3) <br>(2) * 3 = 1 * (6)<br>
6 = 6 <br> <br>
This property, however, is not true for subtraction, where a different grouping of factors yields a different result. <br> <br>
(1 - 2) - 3 != 1 - (2 - 3) <br> (-1) - 3 != 1 - (-1) <br>
-4 != 2 <br> <br>
Essentially, what we are doing in a divide and conquer approach is similar to grouping of factors shown above. It makes logical and mathematical sense for multiplication but not for subtraction.
      
      
## Question 4
The following divide & conquer strategy is trying to solve a problem. Identify the problem that it is trying to solve.
```
int WHATS_GOING_ON(int[] A, int l, int r) {

if (l == r) { // l stands for left-most array index.
    return A[l];
}

mid = (l+r)/2;
Left = 0;
Right = 0;

Left = WHATS_GOING_ON (A, l, mid);
Right = WHATS_GOING_ON (A, mid+1, r);

if (Left <= Right AND Left > 0) {
    return Right;
} else return Left;
}
```
## Answer


