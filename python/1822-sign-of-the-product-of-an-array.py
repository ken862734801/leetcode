class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        if product == 0:
            return 0
        elif product < 0:
            return -1
        else:
            return 1
