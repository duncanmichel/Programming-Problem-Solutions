"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second 
first-level revision.
You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision 
number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
Example 4:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
Example 5:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is 
default 
to "0"
Note:
Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
Version strings do not start or end with dots, and they will not be two consecutive dots.
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        versionA = list(map(int,version1.split(".")))
        versionB = list(map(int,version2.split(".")))
        sizeA,sizeB = len(versionA),len(versionB)
        indexA,indexB = 0,0
        
        while indexA < sizeA and indexB < sizeB:
            if versionB[indexB] < versionA[indexA]:
                return 1
            elif versionB[indexB] > versionA[indexA]:
                return -1
            indexB += 1
            indexA += 1
        
        while indexA < sizeA:
            if versionA[indexA] != 0:
                return 1
            indexA += 1
            
        while  indexB < sizeB:
            if versionB[indexB] != 0:
                return -1
            indexB += 1
            
        return 0

"""
My Solution:
Runtime: 36 ms, faster than 85.72% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.2 MB, less than 6.19% of Python3 online submissions for Compare Version Numbers.
"""

"""
Fastest Solution (28ms):
class Solution:
    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        first = version1.split('.')
        second = version2.split('.')
        while len(first) < len(second):
            first.append("0")
        while len(second)< len(first):
            second.append("0")
        
        for a, b in zip(first, second):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        if len(first) > len(second):
            return 1
        elif len(first) < len(second):
            return -1
        else:
            return 0

Smallest Memory (12184 kb):
class Solution:
    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        version1, version2 = self.normalize(version1, version2)
        
        if version1 == version2:
            return 0
        
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        for index, value in enumerate(version1):
            v1 = int(value)
            v2 = int(version2[index])
            if v1 < v2:
                return -1
            elif v2 < v1:
                return 1
            
        return 0
    
    def normalize(self, version1: 'str', version2: 'str') -> 'Tuple[str, str]':
        version1 = self.cleanVersion(version1)
        version2 = self.cleanVersion(version2)
        version1 = self.padVersion(version1, version2.count('.'))
        version2 = self.padVersion(version2, version1.count('.'))
        return (version1, version2)
    
    def cleanVersion(self, version: 'str') -> 'str':
        return '.'.join([field.lstrip('0') or '0' for field in version.split('.')])
    
    def padVersion(self, version: 'str', groupCount: 'int') -> 'str':
        versionGroupCount = version.count('.')
        
        if versionGroupCount < groupCount:
            return version + '.0' * (groupCount - versionGroupCount)
        return version
"""
