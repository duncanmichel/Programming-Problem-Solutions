"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears 
in at most one part, and return a list of integers representing the size of these parts.
Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""

#hash table based greedy solution
class Solution(object):
    def partitionLabels(self, S):
        size = len(S)
        if size == 0:
            return []
        if size == 1:
            return [1]
        breakIndex = size
        FIRST,LAST = 0,1
        firstlast = {x:[size,-1] for x in set(S)}
        for index in range(size):
            char = S[index]
            if index < firstlast[char][FIRST]:
                firstlast[char][FIRST] = index
            if index > firstlast[char][LAST]:
                firstlast[char][LAST] = index
        breakpoints = []
        templast = 0
        for key,[first,last] in sorted(firstlast.items(),key = lambda x: x[1][0]):
            if first > templast:
                breakpoints += [first]
            if last > templast:
                templast = last
        
        if breakpoints == []:
            return [size]
        ans = []
        for point in breakpoints:
            ans += [point - sum(ans)]
        ans += [size - sum(ans)]
        return ans

"""
My Solution:
Runtime: 32 ms, faster than 61.94% of Python online submissions for Partition Labels.
Memory Usage: 11.9 MB, less than 6.31% of Python online submissions for Partition Labels.
"""

#slower recursive solution
class Solution(object):
    def partitionLabels(self, S):
        size = len(S)
        if size == 0:
            return []
        if size == 1:
            return [1]
        breakIndex = size
        for index in range(1,size):
            #print("index",index,"set1",set(S[:index]),"set2",set(S[index:]),"intersection",set(S[:index]) & set(S[index:]))
            if set(S[:index]) & set(S[index:]) == set([]):
                breakIndex = index
                break
        return [breakIndex] + self.partitionLabels(S[breakIndex:])
        
"""
My Solution:
Runtime: 216 ms, faster than 5.40% of Python online submissions for Partition Labels.
Memory Usage: 11.9 MB, less than 6.31% of Python online submissions for Partition Labels.
"""

"""
Fastest Solution (24ms):
class Solution(object):
    def partitionLabels(self, S):
        letterRanges = {}
        for i in xrange(len(S)):
            c = S[i]
            if c not in letterRanges:
                letterRanges[c] = [i, i]
            letterRanges[c][1] = i
        
        answer = []
        currentRange = [0, 0]
        for letterRangeKV in sorted(letterRanges.items(), key=lambda kv: kv[1][0]):
            letterRange = letterRangeKV[1]
            if letterRange[0] > currentRange[1]:
                answer.append(currentRange[1] - currentRange[0] + 1)
                currentRange = letterRange
            if letterRange[1] > currentRange[1]:
                currentRange[1] = letterRange[1]
        answer.append(currentRange[1] - currentRange[0] + 1)
        return answer

Smallest Memory (10492 kb):
class Solution(object):
    def partitionLabels(self, S):
        myDic = {}
        
        for indx in xrange(len(S)):
            key = ord(S[indx]) - ord('a')
            if myDic.get(key) == None:
                myDic[key] = [indx, indx]
            else:
                myDic[key][1] = indx
                
        myList = []
        for val in myDic.values():
            myList.append((val[0], val[1]))
        
        #print(myList)
        myList.sort()
        i = 0
        for j in range(1,len(myList)):
            
            #print(" i {}, j {}, strt {}, end {} ". format(i, j, myList[j][0], myList[i][1]))
            if myList[j][0] <= myList[i][1]:
                myList[i] = (myList[i][0], max(myList[j][1], myList[i][1]) )
            else:
                i += 1
                myList[i] = myList[j]
       
        outList = []
        for ele in myList[: i + 1]:
            outList.append(ele[1]-ele[0]+1)
        return outList
"""
