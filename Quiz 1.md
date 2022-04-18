# Quiz 1

# Question

A group of students designed an internet upload-manager application. For each  process the application receives: 
1. Data in MB (Mega Bytes)of that process.
2. Time in millisec required to upload that process.  
<br>

The application has to filter a subset of processes to upload in total time *T* from *n* number of total processes. Use dynamic programming to fill the table given below for this scenario. **The target is to find the total data in MB(Megabytes) that the application has selected to upload in total time *T*.**

|t<sub>n</sub><br>d<sub>n</sub>| 0 | 1    | 3 | 3    | 4 | 5    | 6 | 7    | 8 | 9    | T = 10 |
| -----| --| -----| --| -----| --| -----| --| -----| --| -----| --|
|t<sub>1</sub> = 4ms<br>d<sub>1</sub> = 2 MB      |   |      |   |      |   |      |   |      |   |      |   |
|t<sub>2</sub> = 3ms<br>d<sub>2</sub> = 5 MB |   |      |   |      |   |      |   |      |   |      |   |
|t<sub>3</sub> = 5ms<br>d<sub>3</sub> = 7 MB |   |      |   |      |   |      |   |      |   |      | Target Cell  |

# Answer

|t<sub>n</sub><br>d<sub>n</sub>| 0 | 1    | 3 | 3    | 4 | 5    | 6 | 7    | 8 | 9    | T = 10 |
| -----| --| -----| --| -----| --| -----| --| -----| --| -----| --|
|t<sub>1</sub> = 4ms<br>d<sub>1</sub> = 2 MB      |  0 |  0    | 0  | 0     |  2 |   2   |  2 |   2   |  2 |   2   |  2 |
|t<sub>2</sub> = 3ms<br>d<sub>2</sub> = 5 MB |  0 |   0   | 0  |   5   | 5  |   5   | 5  |   7   |  7 |   7   |  7 |
|t<sub>3</sub> = 5ms<br>d<sub>3</sub> = 7 MB |  0 |   0   | 0  |   5   | 5  |   7   |  7 |   7   |  12 |    12  | 12  |

## Formula Used
V[i, w] = max{V[i-1, w], V[i-1, w - w[i]] + P[i]}

### Example 1
V[i, w] = max{V[i-1, w], V[i-1, w - w[i]] + P[i]} <br>
V[2, 3] = max{V[2-1, 3], V[2-1, 3 - 3[2]] + P[2]} <br> <br>
V[1, 3] = 5 <br> V[2, -2] = undefined <br>
Therefore, max = 5 <br>
V[2, 3] = 5

### Example 2
V[i, w] = max{V[i-1, w], V[i-1, w - w[i]] + P[i]} <br>
V[2, 4] = max{V[2-1, 4], V[2-1, 4 - 4[2]] + P[2]} <br> <br>
V[1, 4] = 5 <br> V[1, -1] = undefined <br>
Therefore, max = 5 <br>
V[2, 4] = 5
