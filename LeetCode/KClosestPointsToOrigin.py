"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

import math
import hashlib
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist (pointlist):
            return (pointlist[0]**2 + pointlist[1]**2)**0.5
        
        def listhash(pointlist):
            return hashlib.md5("".join(map(str,pointlist)).encode()).digest()
        
        pointsByHash = {listhash(point):point for point in points}
        distances = {listhash(point):dist(point) for point in points}
        
        ans = []
        
        for listHash,dist in sorted(distances.items(), key = lambda item: item[1]):
            ans.append(pointsByHash[listHash])
            K -= 1
            if K == 0:
                break
        return ans

"""
My Solution:
Runtime: 708 ms, faster than 7.20% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.4 MB, less than 5.20% of Python3 online submissions for K Closest Points to Origin.
"""

"""
#I realize my shortsightedness, in seeing this solution, is that I don't need to calculate square root, because the scaling
#of dist is same without it. Also, hashing function and dictionaries not necessary if I just sort the list itself
Fastest Solution (288ms):
class Solution:
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        return list(sorted(points, key=lambda x: x[0]*x[0]+x[1]*x[1]))[:K]

Smallest Memory (15980 kb):
class Solution:
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        
        dist = lambda i: points[i][0]**2 + points[i][1]**2
        
        def sort(l, r, K):
            
            while l < r :
                
                i = random.randint(l, r)
                points[l], points[i] = points[i], points[l]
            
                mid = partition(l, r)
            
                if K == mid :
                    break
                elif K < mid:
                    r = mid-1
                else:
                    l = mid+1
                
        def partition(l, r):
            
            start = l
            pivot = dist(l)
            
            l += 1
            
            while True :
                
                while l < r and dist(l)<pivot :
                    l += 1
                while l <= r and pivot<=dist(r) :
                    r -= 1
                    
                if l >= r :
                    break
                    
                points[l], points[r] = points[r], points[l]
            
            points[start], points[r] = points[r], points[start]
            return r
        
        sort(0, len(points)-1, K)
        return points[:K]
"""
