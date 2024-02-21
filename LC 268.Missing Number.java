/* 
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length; // length of array
        Arrays.sort(nums);

        //[2, 0, 1], n = 3
        //[0, 1, 2]
        // using linear search doesn't fit time constraints

        
        for (int i = 0; i < n; i++){
            if (i != nums[i])
                return i;
        }
        return n; 
        }
    }

TRIED A DIFF SOLUTION TO MAKE THE LINEAR SEARCH A LIL MORE FASTER:

class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length; // length of array
        Arrays.sort(nums);

        //[2, 0, 1], n = 3
        //[0, 1, 2]
        // using linear search doesn't fit time constraints

        if (nums[n - 1] == n - 1) // ONLY STARTS LINEAR SEARCH WHEN LAST ELEMENT ISN'T CORRECT
            return n;
        else{
            for (int i = 0; i < n; i++){
            if (i != nums[i])
                return i;
        }
        }
        return -1;
        }
    }

IN ORDER TO GET IT TO RUN FASTER, I GOTTA FIND A WAY TO IMPLEMENT BINARY SEARCH:

* looks like binary search wasn't used... problem was just labelled wrongly
* all the solutions are O(n)

LETS TRY TO GET THE BEST RUNTIME:

BEST SOLUTION: BEATS 100% OF USERS WITH JAVA... RUNTIME: 0 ms

*/

class Solution {
    public int missingNumber(int[] nums) {
        int sum_from_nums = 0;
        int len = nums.length;
        int sum_from_len = ((len + 1) * len) / 2; // calculate the sum based on length
                                                  // ie, n * (n+1) / 2 to find sum of numbers
                                                  // between 0 to n;
        for(int i : nums)
            sum_from_nums += i;
        return sum_from_len - sum_from_nums;
    }
}

