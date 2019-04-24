"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
Note:
1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""

#Final Solution, O[N] time, about 3x O[N] space complexity, short circuits some checks by strictly checking the set of trustees, 
#excluding those who already trusted others. Also, by comparing a count instead of a set or list, it removes some overhead, although
#it comes with the assumption that no single relationship is recorded twice
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        trustees = set([person[1] for person in trust])
        townspeople = set([person[0] for person in trust])
        counts = {x:0 for x in range(1,N+1)}
        judge = -1
        for person,trustee in trust:
            counts[trustee] += 1
        for person in trustees - townspeople:
            if counts[person] == N-1:
                judge = person        
        return judge

"""
My Solution:
Runtime: 116 ms, faster than 63.62% of Python3 online submissions for Find the Town Judge.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Find the Town Judge.
"""

#This solution optimizes on the previous one [below] by doing only one check of dictionary keys and by not creating a citizens array 
#piecemeal during relationship inspection
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        trustees = {x:[] for x in range(1,N+1)}
        townspeople = {x:False for x in range(1,N+1)}
        judge = -1
        for townperson,trustee in trust:
            if not townspeople[townperson]: townspeople[townperson] = True
            trustees[trustee].append(townperson)
        citizens = set([x for x in range(1,N+1)])
        #print("citizens is",citizens)
        #print("townspeople is",townspeople)
        #print("trustees is",trustees)
        for person in trustees.keys():
            #print(person,"truth value is",townspeople[person],"set diff is",citizens - set(trustees[person]))
            if not townspeople[person] and citizens - set(trustees[person]) == set([person]):
                judge = person
        return judge

"""
My Solution:
Runtime: 128 ms, faster than 42.20% of Python3 online submissions for Find the Town Judge.
Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions for Find the Town Judge.
"""

#least optimal, but technically correct solution
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        trustSources = {}
        citizens = []
        TRUSTEE = 1
        TOWNSPERSON = 0
        judge = -1
        for trustRelationship in trust:
            truster = trustRelationship[TOWNSPERSON]
            trusted = trustRelationship[TRUSTEE]
            if trusted in trustSources:
                trustSources[trusted].append(truster)
            else:
                trustSources[trusted] = [truster]
            citizens += [truster] if truster not in citizens else []
            citizens += [trusted] if trusted not in citizens else []
        #print("citizens is ",citizens)
        #print("trust hashmap is ",trustSources)
        for person in trustSources.keys():
            if set(citizens) - set(trustSources[person]) == set([person]): #judge
                judge = person
                break
        for person in trustSources.keys():
            if judge in trustSources[person]:
                judge = -1
        return judge
"""
My Solution:
Runtime: 1508 ms, faster than 5.08% of Python3 online submissions for Find the Town Judge.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Find the Town Judge.
"""

"""
Fastest Solution (92ms):
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        nojudges = {t[0] for t in trust}
        if len(nojudges) != N-1:
            return -1
        judge = N*(N+1)//2 - sum(nojudges)
        
        if [t[1] for t in trust].count(judge) == N-1:
            return judge
        else:
            return -1

Alt Fastest (96ms):
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        
        people = [0]*(N+1)
        for i in trust:
            people[i[0]] = -1
            if people[i[1]] != -1:
                people[i[1]] += 1

        judge = -1
        
        for i in range(len(people)):
            if people[i] == N-1:
                judge = i

        return  judge

Smallest Memory ():
[not enough data at time of submission]
