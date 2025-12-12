# LC 238.Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf_l = [1]
        for i in range(len(nums)-1):
            pf_l.append(pf_l[i] * nums[i])
        
        pf_r = [1]
        count = 0
        for i in range(len(nums)-1, 0, -1):
            pf_r.append(pf_r[count] * nums[i])
            count += 1

        # print(f"pfl: {pf_l}, pfr: {pf_r}")
        
        answer = []
        for i in range(len(nums)):
            # print(f"i: {i}, -i-1: {-i-1}")
            answer.append(pf_l[i] * pf_r[-i-1])
        return answer