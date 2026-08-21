class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


























        # seen = set()

        # # for i in nums:
        # #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False
        return len(set(nums)) < len(nums)