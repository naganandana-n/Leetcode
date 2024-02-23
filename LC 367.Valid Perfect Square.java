/*

SAME QUESTION AS 69.SQRT(X)

 Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. 
In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.


Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

Constraints:

1 <= num <= 2^31 - 1

 */

class Solution {
    public boolean isPerfectSquare(int num) {
        if (num  == 1)
            return true;
        else{
        int left = 0;
        int right = num - 1;
        int mid = 0;
        while (left <= right){
            mid = left + (right - left) / 2;
            if (mid * mid == num)
                return true;
            if ((long) mid * mid >  (long) num) // SAME MISTAKE I MADE HERE AGAIN
                right = mid - 1;                // HAVE TO USE LONG TO MAKE SURE WHOLE VALUE GETS 
            else                                // RETAINED.
                left = mid + 1;
    }
    return false;
}
    }
}