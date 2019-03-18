"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap 
after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being 
trapped. Thanks Marcos for contributing this image!
Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

#not working yet
class Solution:
    def trap(self, height: List[int]) -> int:
        
        water = 0
        maxnum = 0
        maxlist = []
        
        for num in height:
            if num > maxnum:
                maxlist.append(num)
                maxnum = num
        
        maxnum = 0
        maxlistb = []
        for num in reversed(height):
            if num > maxnum:
                maxlistb.append(num)
                maxnum = num
        
        for num in reversed(maxlistb[:len(maxlistb)-1]):
            maxlist.append(num)
            
        #maxlist.pop(0) #first value
        lp = 0 #left pointer
        rp = 0 #right pointer
        if maxlist == [] or height == []:
            return water
        
        while lp < len(height)-1:
            print("lp",lp,"rp",rp,"maxnums",maxlist,"water",water)
            if rp < len(height)-1:
                rp += 1
            if maxlist == []:
                break
            if height[rp] >= maxlist[0]:
                ht = min(height[lp],height[rp])
                for x in range(lp+1,rp):
                    water += ht - height[x]
                lp = rp
                maxlist.pop(0)
                pass
        
        return water


"""
My Solution

"""

"""
Fastest Solution

"""
