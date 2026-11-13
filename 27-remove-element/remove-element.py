class Solution(object):
    def removeElement(self, nums, val):
        l = 0

        while l < len(nums):
            if nums[l] == val:
                nums.pop(l)
                l-=1
            l+=1
        return len(nums)
        