"""
Bubble Sort
Complexity: 
The complexity of bubble sort is O(n**2) in both worst and average cases, because the entire array needs to be iterated for every 
element.

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


"""
Insertion Sort

Time Complexity:
In worst case,each element is compared with all the other elements in the sorted array. For N elements, there will be N^2 comparisons. 
Therefore, the time complexity is O(N^2)

You have been given an A array consisting of N integers. All the elements in this array are guaranteed to be unique. For each position 
i in the array A you need to find the position A[i] should be present in, if the array was a sorted array. You need to find this for 
each i and print the resulting solution.
Input Format:
The first line contains a single integer N denoting the size of array A. The next line contains N space separated integers denoting 
the elements of array A.
Output Format:
Print N space separated integers on a single line , where the Ith integer denotes the position of A[i] if this array were sorted.
Constraints:
1 \le N \le 100
1 \le A[i] \le 100
"""

size = int(input())
originalnumlist = list(map(int,input().split()))
numlist = []
answer = []
for item in originalnumlist:
    numlist += [item] # create a copy
    answer += [item] # create a copy
temp = 0

# --- Begin Insertion Sort Logic --- #
for x in range(0,size):
    temp = numlist[x]
    place = x
    while (place > 0) and (numlist[place-1] > temp):
        numlist[place] = numlist[place-1]
        place -= 1
    numlist[place] = temp
# --- End Insertion Sort Logic --- #
    
for count in range(0,size):
    answer[count] = numlist.index(originalnumlist[count]) + 1

print(' '.join(list(map(str,answer))))


"""
Merge Sort

Time Complexity:
The list of size N is divided into a max of log N parts, and the merging of all sublists into a single list takes O(N) time, the worst 
case run time of this algorithm is O(N Log N)

Given an array A on size N, you need to find the number of ordered pairs (i, j) such that i < j and A[i] > A[j].
Input:
First line contains one integer, N, size of array.
Second line contains N space separated integers denoting the elements of the array A.
Output:
Print the number of ordered pairs (i, j) such that i < j and A[i] > A[j].
Constraints:
1 \le N \le 10^6
1 \le A[i] \le 10^6
"""

#Merge Sort (Recursive)
def merge(left,right):
    #print("[DEBUG:merge] Merging " + str(left) + " and " + str(right))
    result = []
    for l_item in left:
        if (right != []):
            while (l_item > right[0]):
                result.append(right.pop(0))
                if right == []:
                    break
        result.append(l_item)
    if right != []:
        for item in right:
            result.append(item)
    return result

def mergesort(nlist,end): #start = 0
    mid = int(end/2)
    if end == 0:
        return nlist
    else:
        return merge(mergesort(nlist[:mid+1],mid),mergesort(nlist[mid+1:],end-(mid+1)))
        
size = int(input())
numlist = list(map(int,input().split()))
answer = mergesort(numlist,size-1)
print(answer)

#Merge Sort


