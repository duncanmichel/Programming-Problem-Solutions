"""
Longest Common Subsequence
From Interviewing.io problem specification
Examples
"ABAZDC,"BACBAD" => "ABAD"
"AGGTAB","GXTXAYB" = > "GTAB"
"aaaa","aa" => "aa"
"ABBA","ABCABA" => ABBA
"""

#recursive Solution
firstInput = input()
secondInput = input()
if len(firstInput) >= len(secondInput):
    string1 = secondInput
    string2 = firstInput
else:
    string1 = firstInput
    string2 = secondInput
s1_size = len(string1)
s2_size = len(string2)

def recursiveSubstring(index1,index2,cur_substring):
    if index1 == s1_size or index2 == s2_size:
        return cur_substring
    if string1[index1] == string2[index2]:
        cur_substring += string1[index1]
        return recursiveSubstring(index1+1,index2+1,cur_substring)
    sub1 = recursiveSubstring(index1+1,index2,cur_substring)
    sub2 = recursiveSubstring(index1,index2+1,cur_substring)
    sub3 = recursiveSubstring(index1+1,index2,"")
    if len(sub1) >= max(len(sub2), len(sub3)):
        return sub1
    elif len(sub2) >= max(len(sub1) , len(sub3)):
        return sub2
    else:
        return sub3
        
print(recursiveSubstring(0,0,""))
