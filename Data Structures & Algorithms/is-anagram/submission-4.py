class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if len(t) != len(s):
            return False

        
        map = {}


        for char in s:

            map[char] = map.get(char, 0) + 1
        
        for char in t:

            map[char] = map.get(char, 0) - 1


        for v in map.values():
            if v != 0:
                return False
        
        return True

