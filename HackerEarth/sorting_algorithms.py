"""
Bubble Sort
Complexity: 
The complexity of bubble sort is O(n**2) in both worst and average cases, because the entire array needs to be iterated for every element.

You have been given an array A of size N . you need to sort this array non-decreasing oder using bubble sort. However, you do not 
need to print the sorted array . You just need to print the number of swaps required to sort this array using bubble sort
Input Format
The first line consists of a single integer N denoting size of the array. The next line contains N space separated integers denoting 
the elements of the array.
Output Format 
Print the required answer in a single line
"""
size = int(input())
numlist = list(map(int,input().split()))
numswaps = 0
temp = 0
swap = True

for i in range(0,size-1):
    if not swap:
        break
    swap = False
    for j in range(0,size-1):
        if numlist[j] > numlist[j+1]:
            temp = numlist[j]
            numlist[j] = numlist[j+1]
            numlist[j+1] = temp
            numswaps += 1
            swap = True
print(numswaps)

"""
Selection Sort
Time Complexity:
To find the minimum element from the array of N elements, N-1 comparisons are required. After putting the minimum element in its proper 
position, the size of an unsorted array reduces to N-1 and then N-2 comparisons are required to find the minimum in the unsorted array.
Therefore (N-1) + (N-2 ) + ....... + 1 = ( N \cdot (N-1) ) / 2 comparisons and N swaps result in the overall complexity of O( N^2 ).

Consider an Array a of size N
Iterate from 1 to N
In i^{th} iteration select the i^{th} minimum and swap it with a[i]
You are given an array a, size of the array N and an integer x. Follow the above algorithm and print the state of the array after 
x iterations have been performed.
Input Format
The first line contains two integer N and x denoting the size of the array and the steps of the above algorithm to be performed 
respectively. The next line contains N space separated integers denoting the elements of the array.
Output Format
Print N space separated integers denoting the state of the array after x steps
Constraints
1 \le N \le 100
1 \le a[i] \le 100
1 \le x \le N
"""
[size,iterations] = map(int,input().split())
numlist = list(map(int,input().split()))
temp = 0

for x in range(0,size):
    if iterations == 0:
        break
    minimum = x
    for y in range(x+1,size):
        if numlist[y] < numlist[minimum]:
            minimum = y
    if minimum != x: #swap
        temp = numlist[x]
        numlist[x] = numlist[minimum]
        numlist[minimum] = temp
    iterations -= 1

print(' '.join(list(map(str,numlist))))


