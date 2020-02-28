"""
REGEX
> findall(regex, input)
> search(regex, input)
> split(regex, input, times)
> sub(regex, sub, input)

Metacharacters
> [] set         e.g [0-9], [a-zA-Z]
> ^  starts with
> $  ends wit
> .  any char
> *  zero or more
> +  one or more
> {} specific  e.g {2}
> |  either or
> () group ???

Special Sequences
\w alphanumeric
\W non-alphanumeric
\d numeric
\D non-numeric
\s whitespace
\S non-whitespace

Match
> span() -> tuple
> group() -> substring
"""

import re

# Decimal number
def is_decimal(input):
  regex = "\s.(-|+).\d+"
  result = re.search(regex, input)

  if (result and result.span() == (0, len(input))):
    return True
  return False

assert is_decimal("0") == True
assert is_decimal(" 0.1 ") == True
assert is_decimal("abc") == False
assert is_decimal("1 a") == False
assert is_decimal("2e10") == False
assert is_decimal(" -90e3   ") == True
assert is_decimal(" 1e") == False
assert is_decimal("e3") == False
assert is_decimal(" 6e-1") == True
assert is_decimal(" 99e2.5 ") == False
assert is_decimal("53.5e93") == True
assert is_decimal("-+3") == False
assert is_decimal("95a54e53") == False