# bits-2023-DS
BITS DS Assignment

You want to walk in a forest but you can only walk the paths where the sum is your lucky number (given). You start at a fixed point forming a tree of paths. Don’t worry atleast one valid path will always be there.

Requirements
1. Implement the above problem statement as a DFS.
2. Analyze the time complexity of your algorithm.
3. Implement the above problem statement using Python 3.7.
4. Make sure proper exception handling is written for the code.

Sample Input
Input should be taken in through a file called “inputPS10.txt” which has the fixed format as below (can have multiple trees across multiple lines):
tree1::lucky number
tree2::lucky number
tree3:lucky number
  
Example:
5,4,8,11,null,9,4,-7,2,null,null,5,1::22 1,4,3,null,null,-10,null,10,2::5 1,2,3,4,5,null,-4,1::0
Note that the input/output data shown here is only for understanding and testing, the actual file used for evaluation will be different.

Sample Output
All possible paths separated by semicolon(;), please make sure the output is in the exact format shown
5,4,11,2;5,8,9;5,8,4,5 1,4;1,3,-10,11
1,3,-4
Note that the input/output data shown here is only for understanding and testing, the actual file used for evaluation will be different.

Display the output in outputPS10.txt.
