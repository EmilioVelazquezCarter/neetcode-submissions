#[2,3,4,4,5,10,20]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxseq = 0
        for i in nums:
            if i-1 not in s:
                n = i+1
                seqs = 1
                while n in s:
                    seqs += 1
                    n += 1
                maxseq = max(maxseq, seqs)
        return maxseq

                
             

        




