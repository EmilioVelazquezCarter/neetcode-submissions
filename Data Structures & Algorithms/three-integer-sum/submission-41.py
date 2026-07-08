class Solution:  #[-4,-1,-1,0,1,2]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

        # trips = []
        # nums = sorted(nums)
        # for i in range(len(nums) - 1):
        #     l, r = i + 1, len(nums) - 1
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     while l < r:
        #         s = nums[l] + nums[r] + nums[i]
        #         if nums[l] == nums[l-1]:
        #             l+=1
        #             continue
        #         # elif nums[r] == nums[r+1]:
        #         #     r -= 1
        #         #     continue
        #         if s < 0:
        #             l += 1
        #         elif s > 0:
        #             r -= 1
        #         elif s == 0:
        #             ls = [nums[l], nums[r], nums[i]]
        #             trips.append(ls)
        #             l += 1
        #             r -= 1
        # return trips

