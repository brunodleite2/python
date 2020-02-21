class Solution:
    def __init__(self):
        self.longest = ""

    def is_palindrome_in_place(self, s):
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

    def is_palindrome(self, s):
        s_reversed = s[::-1]
        if (s == s_reversed):
            return True
        return False

    def set_longest(self, candidate):
        if len(self.longest) <= len(candidate):
            print ("Update longest %s", candidate)
            self.longest = candidate

    def longestPalindrome(self, s: str) -> str:
        self.longest = ""
        last_index = len(s)

        for index in range(len(s)):
            last = last_index

            while last >= index:
                s_sliced = s[index: last]

                last -= 1
                if self.is(s_sliced):
                    self.set_longest(s_sliced)   
                    break                 

        return self.longest


solution = Solution()
assert solution.is_palindrome("a") is True
assert solution.is_palindrome("bb") is True
assert solution.is_palindrome("aba") is True
assert solution.is_palindrome("abba") is True
assert solution.is_palindrome("abcba") is True
assert solution.is_palindrome("abcdba") is False
assert solution.is_palindrome("abcddcba") is True

assert solution.longestPalindrome("abb") == "bb"
assert solution.longestPalindrome("babad") == "aba"
assert solution.longestPalindrome("bb") == "bb"
assert solution.longestPalindrome("babbad") == "abba"
assert solution.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
