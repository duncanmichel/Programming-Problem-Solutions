"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.
Each day, whether the cell is occupied or vacant changes according to the following rules:
If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
Example 1:
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
Example 2:
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
Note:
cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        size = len(cells)
        def changeCell(index,prevDay):
            cells[index] = 1 if (prevDay[index-1]+prevDay[index+1])%2==0 else 0
        print ("Day 0 :",cells)
        N= N%14 + 14
        #if N == 0:
        #    cells[0],cells[size-1] = 0,0
        for day in range(N):
            prevDay = list(cells)
            for i in range(1,size-1):
                changeCell(i,prevDay)
            if day==0:
                cells[0],cells[size-1] = 0,0
            print ("Day",day+1,":",cells)
        
        return cells

"""
My solution:
Runtime: 56 ms, faster than 35.44% of Python3 online submissions for Prison Cells After N Days.
Memory Usage: 13.3 MB, less than 7.69% of Python3 online submissions for Prison Cells After N Days.
"""

"""
Fastest Solution (40 ms):
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        N=N%14
        N=14 if N==0 else N
        temp=[]
        for i in range(N):
            temp.append(0)
            for cell in range(1,7):
                if cells[cell-1]==0 and cells[cell+1]==0:
                    temp.append(1)
                elif cells[cell-1]==1 and cells[cell+1]==1:
                    temp.append(1)
                else:
                    temp.append(0)
            temp.append(0)
            cells=temp.copy()
            temp.clear()
        
        return cells

Smallest Memory (12336 kb):
class Solution:
    def prisonAfterNDays(self, cells: 'List[int]', N: 'int') -> 'List[int]':
        def evolve(binary):
            result = binary<<1^binary>>1^255
            return result&126
        def resume(binary):
            return [binary>>7-i&1 for i in range(8)]

        current, step = 0, 0
        for i in range(8): current = (current<<1) + cells[i]
        loop = [current]
        while 1:
            current, step = evolve(current), step + 1
            if step==N: return resume(current)
            if current in loop: break
            loop.append(current)
        start = loop.index(current)
        looplen = step - start
        return resume(loop[(N - start) % looplen + start])
"""
