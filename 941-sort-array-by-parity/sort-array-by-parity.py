class Solution(object):
    def sortArrayByParity(self, nums):
        l = 0
        r = 1

        while r < len(nums):
            if nums[r] % 2 == 0 :
                nums[l],nums[r] = nums[r],nums[l]
                r += 1
                l += 1
            elif nums[l] == 0 or nums[l] % 2 == 0:
                r += 1
                l += 1
            else:
                r += 1
        return nums
        