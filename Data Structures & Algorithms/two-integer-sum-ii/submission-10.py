class Solution:
    def twoSum(self, nums: List[int], trgt: int) -> List[int]:
        l, r = 0, len(nums) - 1
        outp = []
        while l < r:
            s = nums[l] + nums[r]
            if s < trgt:
                l += 1
            elif s > trgt:
                r -= 1
            elif s == trgt:
                outp = [l+1, r+1]
                return outp




        