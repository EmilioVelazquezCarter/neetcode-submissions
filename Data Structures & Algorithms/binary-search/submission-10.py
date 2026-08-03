class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            h1 = nums[left:mid+1]
            h2 = nums[mid:right]
            if target == nums[mid]:
                return mid
            elif target in h1:
                right = mid -1
            else:
                left = mid +1
        return -1
            # print(left, right, mid)



        