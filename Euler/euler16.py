"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

for _ in range(int(input())):
    print(sum(map(int, str(2 ** int(input())))))
    
"""
Solution I'm working on but doesn't give right answer:

power = 1000
product = 2**power
print("2 to the power of "+str(power)+" is "+str(product))
powsum = 0
while product > 0:
  x = int(product%10)
  powsum += x
  product = int((product-x)/10)
  if product < 1000:
    print("[DEBUG] the product is now "+str(product)+" and the sum is "+str(powsum))
print("The sum of the digits of the product is "+str(powsum))
"""
