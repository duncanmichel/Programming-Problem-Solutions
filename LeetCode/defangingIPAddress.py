"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
Constraints:
The given address is a valid IPv4 address.
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))

"""
My Solution:
Runtime: 40 ms, faster than 23.37% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
"""

"""
Fastest Solution (20 ms):
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

Least Memory:
[none yet]
"""
