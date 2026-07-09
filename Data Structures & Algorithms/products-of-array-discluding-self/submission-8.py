class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [nums[0]]
        rs = len(nums) - 1
        r = [nums[rs]]
        lc = nums[0]
        rc = nums[rs]

        for i in range(1, len(nums)):
            lc = lc * nums[i]
            l.append(lc)
        for i in range(rs-1,-1, -1):
            rc = rc * nums[i]
            r.append(rc)
        print(l)
        r = r[::-1]
        print(r)
        for i in range(len(nums)):
            left = l[i-1] if i > 0 else 1
            right = r[i+1] if i < len(nums)-1 else 1
            print(left)
            print(right)
            nums[i] = left * right
        return nums
        