"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are 
the coordinates of its top-right corner.
Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or 
edges do not overlap.
Given two (axis-aligned) rectangles, return whether they overlap.
Example 1:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
"""

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        r1x1,r1y1,r1x2,r1y2 = rec1
        r2x1,r2y1,r2x2,r2y2 = rec2
        
        if r1x2-r1x1==0 or r1y2-r1y1==0 or r2x2-r2x1==0 or r2y2-r2y1==0: #line, no area
            return False
        
        if r2x1 >= r1x2 or r2x2 <= r1x1 or r2y1 >= r1y2 or r2y2 <= r1y1: #out of bounds
            return False
        
        return True

"""
My Solution:
Runtime: 28 ms, faster than 14.29% of Python online submissions for Rectangle Overlap.
Memory Usage: 11.7 MB, less than 5.88% of Python online submissions for Rectangle Overlap.
"""

"""
Fastest Solution (16ms):
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        for idx, num in enumerate(rec2):
            if idx == 0:
                if rec1[2] <= num:
                    return False
            elif idx == 1:
                if rec1[3] <= num:
                    return False
            elif idx == 2:
                if rec1[0] >= num:
                    return False
            else:
                if rec1[1] >= num:
                    return False
        return True
        
Alt Fastest (20ms):
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or  # left
            rec1[3] <= rec2[1] or  # bottom
            rec1[0] >= rec2[2] or  # right
            rec1[1] >= rec2[3])    # top

Smallest Memory (10540 kb):
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        if rec1[0] >= rec2[2]: return False
        if rec1[2] <= rec2[0]: return False
        if rec1[1] >= rec2[3]: return False
        if rec1[3] <= rec2[1]: return False
        
        return True
"""
