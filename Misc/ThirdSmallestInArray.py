"""
Interviewing.io question I saw
"""

#assumes no duplicates or that duplicates are able to be ignored
import math
def findXSmallestInArray (input_array: list, x: int):
  if len(input_array)-1 < x: #if list too small
    return 0 
  def findMin(prev_min):
    this_min = math.inf
    for num in input_array:
      if prev_min < num < this_min:
        this_min = num
    return this_min
  
  current_min = -math.inf
  for i in range(0,x):
    current_min = findMin(current_min)
  return current_min

def thirdSmallest(input_array: list):
  return findXSmallestInArray (input_array,3)

test = [4, 9, 1, 32, 12]
print(thirdSmallest(test)) #returns 9

#if we care about duplicates [NOT WORKING YET]
import math
def findXSmallestInArray (input_array: list, x: int):
  if len(input_array)-1 < x: #if list too small
    return 0 
  mins = {}
  def findMin(prev_min):
    this_min = math.inf
    for array_index in range(0,len(input_array)):
      num = input_array[array_index]
      print("prev:",prev_min,", num:",num,", cur:",this_min,", iteration:",iteration)
      if prev_min <= num <= this_min:
        if num not in mins.keys():
          this_min = num
          mins[this_min] = [array_index]
        elif array_index not in mins[num]:
          this_min = num
          mins[this_min] += [array_index]
        print("mins: ",mins)
    #fix mins
    delKeys = []
    for key in mins.keys():
      if key > this_min:
        delKeys += [key]
    for key in delKeys:
      mins.pop(key)
    return this_min
  
  current_min = -math.inf
  for iteration in range(0,x):
    current_min = findMin(current_min)
  return current_min

def thirdSmallest(input_array: list):
  return findXSmallestInArray (input_array,3)

test = [4, 4, 9, 1, 32, 12]
print(thirdSmallest(test))
