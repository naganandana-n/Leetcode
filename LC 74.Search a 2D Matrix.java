/*
You are given an m x n integer matrix matrix with the 
following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4

 */

class Solution {

// first do binary search on the rows to find which row has your answer
// then do binary search on that row alone

    public boolean searchMatrix(int[][] matrix, int target) {
        int cleft = 0; // binary search on the rows as whole
        int cright = matrix.length - 1;
        int cmid = (cleft + cright) / 2;

        int row = 0; // find the index of the row that has ur element
        
        while (cleft <= cright){
            cmid = (cleft + cright) / 2;

            if (target <= matrix[cmid][matrix[cmid].length - 1] && target >= matrix[cmid][0]){
                row = cmid;
                break;
            }
            if (target > matrix[cmid][matrix[cmid].length - 1])
                cleft = cmid + 1;
            else
                cright = cmid - 1;
        }

        int rleft = 0; // binary search in that specific row to find element.
        int rright = matrix[row].length - 1;
        int rmid = (rleft + rright) / 2;

        while (rleft <= rright){
            rmid = (rleft + rright) / 2;

            if (target == matrix[row][rmid])
                return true;
            if (target > matrix[row][rmid])
                rleft = rmid + 1;
            else
                rright = rmid - 1;
        }
        return false;
    }
}


/*
SOLUTION EXPLANATION:
Intuition

The intuition behind this approach is to first find the potential row 
where the target could be located based on the condition that the last 
element of each row is greater than or equal to the target. 
Then, once we have identified the potential row, we perform a linear 
search within that row to check if the target exists.

NOTE: THIS SOLUTION FROM ONLINE USES LINEAR SEARCH.
I IMPLEMENTED THE SAME THING WITH BINARY SEARCH.

Approach

Iterate through each row of the matrix.
Check if the last element of the current row is greater than or equal to the target.
If so, set the current row index as the potential row (r).
Perform a linear search within the potential row to find the target.
If found, return true; otherwise, return false.

 */