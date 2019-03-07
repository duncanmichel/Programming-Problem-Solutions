"""
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question 
marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program 
should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the 
string, then your program should return false as well. 
For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 
6 and 4, and 3 question marks between 5 and 5 at the end of the string. 
Use the Parameter Testing feature in the box below to test your code with different argum
"""

def QuestionsMarks(str): 
    
    threeQ = False 
    addTen = False 
    validStr = False 
    firstNum = 0
    qct = 0
    
    name = "09?"
    for c in str:
        if 47< ord(c) <58: # nums
            if firstNum + int(c) == 10:
                addTen = True 
                if threeQ:
                    #print("[DEBUG] qct:",qct,"threeQ:",threeQ,"firstNum:",firstNum,"cur c:",c)
                    validStr = True 
                    firstNum = int(c)
                    threeQ = False
                    qct = 0
                else:
                    #print("[DEBUG] qct:",qct,"threeQ:",threeQ,"firstNum:",firstNum,"cur c:",c,"INVALID STR")
                    validStr = False 
                    break
            else:
                #print("[DEBUG] qct:",qct,"threeQ:",threeQ,"firstNum:",firstNum,"cur c:",c)
                firstNum = int(c)
                threeQ = False
                qct = 0
        elif ord(c)==63: # ?
            qct += 1
            #print("[DEBUG] qct:",qct,"threeQ:",threeQ,"firstNum:",firstNum,"cur c:",c)
            if qct == 3:
                threeQ = True 
            elif qct > 3:
                threeQ = False 
            
            
        
    
    if addTen and validStr:
        return "true"
    else:
        return "false"
    
# keep this function call here  
print QuestionsMarks(raw_input())
