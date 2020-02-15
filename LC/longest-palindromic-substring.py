class Solution:

    def __init__(self):
        self.longest = ""

    def isPalindrome(self, s):
        last_index = len(s) - 1
        mid_index = int(len(s) / 2)  # floor

        for index, c in enumerate(s):
            if index >= mid_index:
                break

            if c == s[last_index]:
                last_index -= 1
                continue
            return False
        return True

    def set_longest(self, candidate):
        if len(self.longest) < len(candidate):
            self.longest = candidate

    def longestPalindrome(self, s: str) -> str:
        last_index = len(s)

        for index in range(len(s)):
            s_sliced = s[index: last_index]

            print(s_sliced)
            if self.isPalindrome(s_sliced):
                self.set_longest(s_sliced)
                continue       

        return self.longest


solution = Solution()
assert solution.isPalindrome("a") is True
assert solution.isPalindrome("bb") is True
assert solution.isPalindrome("aba") is True
assert solution.isPalindrome("abba") is True
assert solution.isPalindrome("abcba") is True
assert solution.isPalindrome("abcdba") is False
assert solution.isPalindrome("abcddcba") is True

assert solution.longestPalindrome("abb") == "bb"
assert solution.longestPalindrome("babad") == "aba"
assert solution.longestPalindrome("bb") == "bb"
assert solution.longestPalindrome("babbad") == "abba"
assert solution.longestPalindrome("babbabbd") == "bbabb"
#assert solution.longestPalindrome("abc..a..cbad") == "bbabb"
