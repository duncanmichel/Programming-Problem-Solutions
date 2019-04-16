"""
Code Chef problem
https://www.codechef.com/DRI22019/problems/DIC007
Razo  is a brilliant student in maths. One day his mother asked him about his rank in his class, but he didn't like the school's system 
of ranking so he refused to give the answer. Help Razo's mother to find the rank of his son. School has strange way of ranking the 
students. They rank students according to lexicographical order of their surnames.
Class contains N+1 students including Razo.
Some characters in student's surnames are missing and missing part is replaced with ∗ in the surname. Razo's surname will never 
contains ∗ in it. You have to tell all possible rank of Razo, when you arrange N surnames with Razo's surname lexicographically.
Input:
The first line contains integer N (1≤N≤100000), denoting the number of surnames to process.The following N+1 lines contains student's 
surname, one surname per line.The N+1 th line contains Razo's surname. Each string contains only lowercase Latin letters, its length is 
between 1 and 100, inclusive.
Output:
Print all possible rank of Razo in a single line, separated by spaces.
Sample Input 1:
2
hacker
code
rank
Sample Output 1 :
3
Sample Input 2:
2
**cker
*o*e
rank
Sample Output 2:
1 2 3
"""

# cook your dish here
def isLexoLesser(name1,name2):
    if name1 == name2 or name1 == "" or name2 == "":
        return True
    elif name2[0] == "*":
        return True #if name1[0] != "a" else isLexoLesser(name1[1:],name2[1:])
    elif ord(name1[0]) < ord(name2[0]):
        return True
    elif ord(name1[0]) > ord(name2[0]):
        return False
    else:
        return isLexoLesser(name1[1:],name2[1:])
    
numStudents = int(input())
studentArray = []
for i in range(numStudents):
    studentArray.append(input())
#studentArray.sort()
razoName = input()
rank = 1
for name in studentArray:
    if not isLexoLesser(razoName,name):
        rank += 1
#print(studentArray)
print(" ".join(map(str,range(rank,numStudents+2))))

'''
Accepted Solution:
# cooking
n = int(input())
names = []

for nIndex in range(n):
    names.append(input())

raza = input()
raza_len = len(raza)
min_rank = 1
max_rank = n+1

# for name in names:
#     if raza_len > len(name):
#         min_rank = min_rank + 1
#     elif raza_len < len(name):
#         max_rank = max_rank - 1
#     else:
#         min_name = name.replace('*', 'a')
#         max_name = name.replace('*', 'z')
#         if raza < min_name:
#             max_rank = max_rank - 1
#         elif raza > max_name:
#             min_rank = min_rank + 1

for name in names:
    min_name = name.replace('*', 'a')
    max_name = name.replace('*', 'z')
    if raza < min_name:
        max_rank = max_rank - 1
    elif raza > max_name:
        min_rank = min_rank + 1
            
possible_ranks = list(range(min_rank, max_rank+1))
# print(min_rank, max_rank)
print(*possible_ranks)
'''
