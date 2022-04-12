# Question 1: [4 marks] 
Consider that you are given a list of odd size. You have to swap the elements in such a way that first element should be swapped with its immediate right neighbouring element, 3rd element should be swapped with its immediate right neighbouring element and so on until all the elements in the list are processed. Middle element should be fixed and should not be swapped with any other element. Design an algorithm based on Brute Force and another one based on Divide & Conquer Approach to solve this problem. <br>
Note: Stay Java/Python/C++ free.


## Answer
### Brute Force:
counter = 0 <br>
for element in inputList:<br>
  if counter == len(inputList) // 2: <br>
    counter = counter + 1<br>
  elif counter + 1 != len(inputList) and counter + 1 != len(inputList) // 2: <br>
    nodeToSwap = inputList[counter]<br>
    inputList[counter] = inputList[counter + 1]<br>
    inputList[counter + 1] = nodeToSwap<br>
    counter = counter + 2 <br>
  else:<br>
    counter = counter + 1<br>
