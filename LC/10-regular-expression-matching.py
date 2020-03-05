class Solution:
    def isMatch2(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))

        return first_match and self.isMatch(text[1:], pattern[1:])

    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        if s_len == 0:
            if p_len == 0:
                return True

            if p[p_len - 1] == "*" and p_len >= 2:
                return self.isMatch(s[0:s_len], p[0:p_len-2])

            return False

        if not p_len: # p == 0 and s > 0
            return False

        actual = s[s_len -1]
        exp = p[p_len - 1]

        # Match!
        if exp in [actual, "."]:
            return self.isMatch(s[0:s_len -1], p[0:p_len -1])

        # No match
        if (p_len - 2 < 0):
            return False

        next_p = p[p_len - 2]
        if exp == "*":
            if next_p in [actual , "."]:
                return self.isMatch(s[0:s_len - 1], p[0:p_len])

            return self.isMatch(s[0:s_len], p[0:p_len-2])

        # No match at all
        return False

s = Solution()
assert s.isMatch("aaa","ab*a*c*a") == True
assert s.isMatch("aaa", "aaaa") == False
assert s.isMatch("aa", "a") == False
assert s.isMatch("aa", "aa") == True
assert s.isMatch("ab", ".*") == True
assert s.isMatch("aab", "c*a*b") == True
assert s.isMatch("mississippi", "mis*is*p*.") == False
