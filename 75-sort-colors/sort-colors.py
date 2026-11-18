class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            l = 0
            r = 1
            while r < len(nums):
                if nums[r] <= nums[l]:
                    nums[r],nums[l] = nums[l],nums[r]
                    l +=1 
                    r += 1
                else:
                    r+=1
                    l+=1
        return nums
