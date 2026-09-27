class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        a = ""

        for ch in s:
            if ch.isalnum():
                a = a + ch

        n = len(a)

        for i in range(n):
            if a[i] != a[n - i - 1]:
                return False

        return True