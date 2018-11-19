one_wds = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
teen_wds = {10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
ten_wds = {0:0,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}

def evalHun(n):
    hd_wd = 0
    hundreds = int(n/100)
    if hundreds > 0:
        hd_wd = one_wds[hundreds]+7
        ten_wd = evalTen(n%100)
        if ten_wd > 0:
            hd_wd += 3
        return hd_wd + ten_wd
    return evalTen(n)
    
def evalTen(n):
    tens = int(n/10)
    if tens == 1:
        return teen_wds[n]
    return ten_wds[tens] + one_wds[n%10]

thousand = 11
maxNum = 1000

#thousand = 0
#maxNum = 6

sNum = 0 + thousand
for i in range(1,maxNum):
    x = evalHun(i)
    print("[test] Sum of %d: %d" % (i, x))
    sNum += x
print("The sum of the letters in the words from 1 to %d is: %d" % (maxNum,sNum))
