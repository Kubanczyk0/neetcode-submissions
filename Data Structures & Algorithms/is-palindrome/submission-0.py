class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""

        for char in s:
            if char.isalnum():
                c += char.lower()

        i = 0
        j = len(c) - 1

        while i < j:
            if c[i] != c[j]:
                return False

            i += 1
            j -= 1

        else:
            return True


        