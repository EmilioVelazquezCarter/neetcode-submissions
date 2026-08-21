class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            print(i, num)
            diff = target - num
            if diff in d:
                return[d[diff], i]
            else:
                d[num] = i































        # d = {}
        # for i, n in enumerate(nums):
        #     diff = target - n

        #     if diff in d:
        #         return [d[diff], i]

        #     d[n] = i
        #     # print(d, i, n)
