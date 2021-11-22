# Sudoku solver
Python program to solve sudoku with colors and numbers
This program uses BackTrack algorithm with MRV(Minimum Remaining Value) and Degree heuristics. 

Input: 
- line 1: numbers of colors, size of table
- line 2: colors
- line 3 n + 2: rows of the table

Output: a solved sudoku

## Example
This a sample input:
- line 1: 5 , 3
- line 2: r, g, b, y, p
- line 3: 1# *b , *#
- line 4: *#, 3r, *#
- line 5: *g, 1#, *#

![image](https://user-images.githubusercontent.com/47606879/142888852-2e7c1737-c709-4c1a-83e1-fcda3b463a29.png)


This is the result output:

![image](https://user-images.githubusercontent.com/47606879/142888899-540d4be1-eecc-46db-bdbc-a90e9481b905.png)



## Problem Formulation

The variable for this problem are the colors and the numbers that are unknown.
The domain of each number variable would be 1, 2, 3, ..., n and n is the length of the sudoku table.
The domain of each color variable would be a set of colors which the user enters.
For instance, in the aforementioned example, color domain = {r, g, b, y, p} and the number domain = {1, 2, 3}
Rules for numbers are as the same as the regular sudoku. The rule for colors is that adjacent cell should not have the same colors.
Based on these rules, I reduced the domains for the variables. 

I defined a class named "sudoku" which contains all the information of the table. In the program, I created an object of this class and applied functions to solve the sudoku.

#### I also added a dictionary of colors to show colors more beautiful, like a cell with colored blue with "2", rather than just "2b".
![image](https://user-images.githubusercontent.com/47606879/142894521-2c4d106f-524d-412e-aab4-bde5c288757a.png)

Vs. "2b"






