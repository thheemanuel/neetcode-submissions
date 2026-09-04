class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()

        t = s[::-1]

        print(t)
        print(s)

        if s != t:
            return False
        else:
            return True
