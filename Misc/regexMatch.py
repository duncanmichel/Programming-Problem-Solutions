###
Based on an interviewing.io problem I saw, I paused and created a solution as it came to me.
###

def regexMatch(test_str: str, pattern: str):

  def compare():
    if pattern[0] == '.':
      return True
    elif pattern[0] == test_str[0]:
      return True
    else:
      return False

  def lookAheadStar():
    if pattern[1] == "*":
      return True
    else:
      return False

  if test_str == '' and pattern == '': #both string and pattern empty (the base condition)
    return True
  elif test_str == '' or pattern == '': #one or the other string (exclusive) is empty
    return False
  elif len(pattern) > 1 and lookAheadStar():
    if compare():
      return regexMatch(test_str, pattern[2:]) or regexMatch(test_str[1:], pattern[2:]) or regexMatch(test_str[1:], pattern) #no star pattern, last char of star pattern, and continued star pattern, respectively
    else:
      return regexMatch(test_str, pattern[2:])
  elif compare():
    return regexMatch(test_str[1:], pattern[1:]) #consume and check next char
  else:
    return False

#TEST CASES
print(regexMatch("", "") == True) #edge case both empty
print(regexMatch("abc", "") == False) #edge case empty pattern
print(regexMatch("", "abc") == False) #edge case empty string
print(regexMatch("aaa", "aaa") == True) #a-z basic test for true
print(regexMatch("aaa", "aba") == False) #a-z basic test for true
print(regexMatch("aaa", "a.a") == True) #wildcard basic test for true
print(regexMatch("aaa", "a*") == True) #star pattern basic test for true
print(regexMatch("aaa", "a*b") == False) #star pattern basic test for false
print(regexMatch("b", "a*b") == True) #star pattern successive basic test for true
print(regexMatch("sjdhflkjshgkjhs", ".*") == True) #universal accept test for true
print(regexMatch("abcef", "ab*bc*cd*..") == True) #complex
print(regexMatch("abbccdd", "ab*bc*cd*..") == True) #complex
