class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        r = 0
        while r < len(nums):
            if nums[r] == val:
                nums.pop(r)
            else:
                r+=1
        return len(nums)
