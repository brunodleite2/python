class Solution:
    """ def __init__(self):
        expected_char = None

    def __get_expected_char(self, : string) -> str:

        return
    """
    """ def isMatch(self, s: str, p: str) -> bool:
        p_index = 0

        # expected char
        # anything

        for actual in s:
            if (p_index >= len(p)):
                return False

            exp = p[p_index]
            print("E=%s A=%s" % (exp, actual))


            #

            if actual != exp and exp != ".":
                return False


            # Actual == Exp
            if p_index + 1 == len(p): # Last one
                p_index += 1
                continue

            p_next_index = p[p_index + 1]

            if p_next_index == "*":
                continue

            p_index += 1

        print("XXXX")
        return True """


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
