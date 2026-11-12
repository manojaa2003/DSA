class Solution(object):
    def moveZeroes(self, nums):

        l = 0
        r = 0

        while r < len(nums):
            if nums[r] != 0:
                nums[r],nums[l] = nums[l],nums[r]
                l += 1
            r+=1

        