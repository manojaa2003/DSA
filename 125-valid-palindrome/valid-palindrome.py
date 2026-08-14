class Solution(object):
    def isPalindrome(self, s):
        sti = re.sub(r'[^A-Za-z0-9]','',s).lower()
        
        if sti == sti[::-1]:
            return True
        return False

        