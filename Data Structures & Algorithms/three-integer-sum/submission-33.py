class Solution:  #[-4,-1,-1,0,1,2]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = set()
        trip = []
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                # if nums[l] == nums[l+1]:
                #     l += 1
                # elif nums[r] == nums[r-1]:
                #     r -= 1
                s = nums[l] + nums[r] + nums[i]
                
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                elif s == 0:
                    ls = (nums[l], nums[r], nums[i])
                    trips.add(ls)
                    l += 1
                    r -= 1
        for i in trips:
            trip.append(list(i))
        return trip

