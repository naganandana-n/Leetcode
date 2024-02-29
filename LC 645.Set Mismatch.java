/*
 You have a set of integers s, which originally contains all the numbers from 1 to n. 
 Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
 which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.


Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
 */

class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] ans = new int[2];
        int fake_total = 0; // CALCULATE THE SUM OF ALL ELEMENTS IN ARRAY
        int real_total = (nums.length * (nums.length + 1)) / 2; // REAL SUM OF NO.S FROM 1 TO N
        Arrays.sort(nums); // SORT ARRAY IN ASCENDING ORDER
        for(int i = 0; i < nums.length
        ; i++){
            fake_total += nums[i];
            if (i == 0)
                continue;
            if(nums[i] == nums[i - 1])
                ans[0] = nums[i];    // COMPARE WITH THE LAST ELEMENT TO FIND DUPLICATE
        }
        fake_total -= ans[0]; // REMOVE THE DUPLICATE ELEMENT FROM THE SUM
        ans[1] = real_total - fake_total; // REAL SUM OF NO.S FROM 1 TO N - (MINUS) SUM OF ALL ELEMENTS
        return ans;                                                        // IN ARRAY WITHOUT DUPLICATE
    }
}