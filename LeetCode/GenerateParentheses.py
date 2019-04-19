"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = {0:[""],1:["()"],2:["()()","(())"]}
        ans = []
        
        def genNparen(num):
            ret = []
            if num in memo: return memo[num]
            for x in range(0,num):
                for paren in genNparen(x):
                    ret += ["("+paren+")"+tail for tail in genNparen(num-x-1)]
            memo[num] = list(set(ret))
            return memo[num]
        
        if n in memo:
            ans = memo[n]
        else:
            ans = genNparen(n)
        
        return ans
'''
#is failing at 5 and above, no clear reason
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursiveParen(num):
            if num == 0:
                return ["","",""]
            ans = []
            for parens in recursiveParen(num-1):
                ans.append("("+parens+")")
                ans.append(parens+"()")
                ans.append("()"+parens)
            if num%2!=0 or num//2 >= num-1: return list(set(ans))
            print('checking',num//2)
            for parens in recursiveParen(num//2):
                ans.append(parens+parens)
            return list(set(ans))
        
        return recursiveParen(n)
'''

"""
My Solution:
Runtime: 40 ms, faster than 84.64% of Python3 online submissions for Generate Parentheses.
Memory Usage: 13.6 MB, less than 5.10% of Python3 online submissions for Generate Parentheses.
"""

"""
Fastest Solution (32ms):
class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

Smallest Memory (12396 kb):
class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n <= 0:
            return []
        
        if n == 1:
            return ["()"]
        else:
            prev = self.generateParenthesis(n-1)
            fresh = set()
            for line in prev:
                fresh.add("()" + line)
                fresh.add(line + "()")
                fresh.add("(" + line + ")")
                for i in range(1,len(line)):
                    fresh.add(line[:i] + "()" + line[i:])
            return list(fresh)
"""
