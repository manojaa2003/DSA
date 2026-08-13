class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        count = 0
        while r < len(nums):
            if nums[l] == nums[r]:
                count +=1
                if count>2:
                    nums.pop(r)
                else:
                    r+=1
            else:
                l = r
                count = 0
        return  len(nums)
        