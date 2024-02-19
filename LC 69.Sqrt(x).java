/* 

Given a non-negative integer x, 
return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., 
and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1

*/

class Solution {
    public int mySqrt(int x) {
        if ( x == 0 || x == 1)
            return x;
        else{
            int left = 1;
            int right = x;
            int mid;
            while (left <= right){
                mid = left + (right - left) / 2;
                if(mid * mid == x)
                    return mid;
                if ((long) mid * mid > (long) x) // here (long) type casting is 
                    right = mid - 1;             // done to save time (explained below)
                else
                    left = mid + 1;
            }
            return Math.round(right);
        }
}
}

/*
 
The reason why casting to long resolves the time limit exceeded issue 
in your code is related to how integer overflow affects the binary 
search algorithm you're using.

In Java, arithmetic operations on int values can result in integer overflow 
if the result exceeds the maximum value that can be represented by an int. 
When integer overflow occurs, it leads to unexpected behavior, which can affect 
the correctness and performance of your algorithm.

In your binary search loop, you're performing the operation mid * mid. 
If mid is sufficiently large, mid * mid might exceed the maximum value of int, 
resulting in an integer overflow. This could lead to incorrect comparisons and 
potentially infinite loops.

By casting mid and x to long before performing the multiplication, you're ensuring 
that the multiplication is done with long integers, which have a much larger range 
than int. This prevents integer overflow and ensures that the comparisons are done correctly.

However, it's worth noting that using long comes with a trade-off in terms of memory usage, 
as long requires more memory than int. Therefore, while casting to long may resolve the 
time limit exceeded issue, it may also increase memory usage. Depending on the constraints
of the problem, this trade-off may or may not be acceptable.

In general, when dealing with large numbers or potentially large intermediate results, 
it's a good practice to use larger data types such as long to avoid 
integer overflow issues. However, it's essential to consider the trade-offs in terms 
of memory usage and ensure that the chosen approach is within the problem constraints.

 */