class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        strS = {}
        strT = {}

        for char in s:
            strS[char] = strS.get(char, 0) + 1

        for char in t:
            strT[char] = strT.get(char, 0) + 1

        if strS == strT:
            return True

        else:
            return False