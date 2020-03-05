class Solution:
    def is_all_start(self, p):
        for char in p:
            if char != "*":
                return False
        return True

    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0:
            if len(p) == 0:
                return True
            return self.is_all_start(p)

        if len(p) == 0:  # len(s) is > 0!!!
            return False

        for (index, char) in enumerate(s):
            if p[index] in [char, "?"]:
                return self.isMatch(s[1:len(s)], p[1:len(p)])

            if p[index] == "*":
                if len(p) >= 2:
                    if p[1] == "*":
                        return self.isMatch(s[0:len(s)], p[1:len(p)]) # len(p) is 1

                    if p[1] in [char, "?"]:
                        return self.isMatch(s[1:len(s)], p[1:len(p)]) #or self.isMatch(s[1:len(s)], p[0:len(p)])
                    return self.isMatch(s[1:len(s)], p[0:len(p)])

                return self.isMatch(s[1:len(s)], p[0:len(p)]) # len(p) is 1
            return False

        return True


s=Solution()

s.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
"b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")

assert s.isMatch("aaaa", "***a") == True
assert s.isMatch("ho", "**ho") == True
assert s.isMatch("c", "*?*") == True
assert s.isMatch("abefcdgiescdfimde", "ab*cd?i*de") == True
assert s.isMatch("ab", "?*") == True
assert s.isMatch("aa", "a") == False
assert s.isMatch("aa", "aa") == True
assert s.isMatch("ab", "*") == True
assert s.isMatch("cb", "?a") == False
assert s.isMatch("adceb", "*a*b") == True
assert s.isMatch("acdcb", "a*c?b") == False
assert s.isMatch("aaa", "aaaa") == False
