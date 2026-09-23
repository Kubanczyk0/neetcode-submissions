class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for i, num in enumerate(nums):
            if num not in d:
                d[num] = i
            elif num in d:
                return True
        else:
            return False
        