class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        minimum = nums[0]
        for i in range(n):
            if nums[i] < minimum:
                minimum = nums[i]
        return minimum