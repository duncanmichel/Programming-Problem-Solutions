"""
Reverse bits of a given 32 bits unsigned integer.
Example 1:
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 
which its binary representation is 00111001011110000010100101000000.
Example 2:
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 
which its binary representation is 10101111110010110010011101101001.
Note:
Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as 
signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether 
it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents 
the signed integer -3 and the output represents the signed integer -1073741825.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        nbin = bin(n)
        nstr = str(nbin)
        nlist = list(nstr[2:])
        nlist = ['0']*(32-len(nlist)) + nlist
        print(''.join(nlist))
        nbinmap = map(int,nlist)
        exp = 0
        ans = 0
        
        for digit in nbinmap:
            ans += digit * 2**exp
            exp += 1
        
        return ans

"""
My Solution:
Runtime: 32 ms, faster than 17.25% of Python online submissions for Reverse Bits.
Memory Usage: 11.7 MB, less than 5.38% of Python online submissions for Reverse Bits.
"""

"""
Fastest Solution (16ms):
class Solution:
    def reverseBits(self, n):
        s = bin(n)[2:]
        s = "0"*(32 - len(s)) + s
        t = s[::-1]
        return int(t,2)

Alt Fastest (24ms) [bit manipulation solution]:
class Solution:
    def reverseBits(self, n):
        v = 0
        for _ in range(32):
            v <<= 1
            v += n&1
            n >>= 1
        return v

Smallest Memory (10456 kb):
class Solution:
    def reverseBits(self, n):
        temp = n
        a = 0
        i = 32
        while i:
            r = temp%2
            temp = temp//2
            i-=1
            a = a*2 +r
        return a
"""
