class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            desired = target - num
            if desired in d and d[desired] != i:
                return [i, d[desired]]
        