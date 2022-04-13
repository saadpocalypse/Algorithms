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



                
                

       
