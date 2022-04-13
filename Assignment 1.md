# Assignment 1 (Lexical Analyzer)

## Assignment Statement
Create a lexical analyzer without using any existing code or tool. Your code should be in C and it should support the constructs listed below.

| Keyword/Operation      | Description |
| ----------- | ----------- |
| +, -, *, /     | Adding, subtracting and multiplying floats      |
| >, >=, <, <=, !=, \|\|, &&, =, ==  | To compare two float values      |
| if     | Conditional branching      |
| while  | Conditional loop       |
| break    | Exit from a conditional loop     |
| print | Prints a float value    |
| (, )     | Start or end of an 'if' condition or a while loop       |
| {, }  | Start and end of a comparison statement      |

## Rules
1. Only float data type is supported.
2. Float values may be stored in identifiers.
3. Valid identifers start with a letter and can be followed by any combination of letters and/or numbers.
4. New line is considered the end of the line, no restrictions are to be applied for a semi-colon.

## Programming Guidelines
Your program must read the input file character by character and use the characters to fill up an input buffer. Two pointers should be used to keep track of each lexeme generated. Your major function should be a DFASimulator, which eaither accepts or rejects the lexemes as valid tokens. DFAs can be easily implemented using transition tables. Each valid token must be enlisted in a symbol table. The generated output file should contain all the tokens from the input code.

## Brute Force Approach
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

## Divide and Conquer Approach
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



                
                

       
