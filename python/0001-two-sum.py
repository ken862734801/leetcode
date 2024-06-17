class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices:
                return [i, indices[diff]]
            else:
                indices[diff] = i