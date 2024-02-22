/*
 You have n coins and you want to build a staircase with these coins. 
 The staircase consists of k rows where the ith row has exactly i coins. 
 The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.


Example 1:

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:
1 <= n <= 2^31 - 1

 */

 // THIS IS THE BASIC ITERATIVE SOLUTION: I DONT COMPLETELY UNDERSTAND IT
 // REDO!!
class Solution {
    public int arrangeCoins(int n) {
        int count = 1;
        while (n > 0){
            count += 1;
            n = n - count;
        }
        return count - 1;


    }
}