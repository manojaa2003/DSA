class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        max_len = 0
        sett = set()
        r = 0

        while r < len(s):
            if s[r] not in sett:
                sett.add(s[r])
                lenn = (r-l)+1
                max_len = max(max_len,lenn)
                r+=1
            else:
                sett.remove(s[l])
                l += 1
        return max_len
                




        