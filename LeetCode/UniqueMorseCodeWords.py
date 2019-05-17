"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps 
to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be 
written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a 
word.
Return the number of different transformations among all words we have.
Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations, "--...-." and "--...--.".
Note:
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
        "-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        translate = dict(zip(alphabet,morse))
        transformations = []
        for name in words:
            transformations.append("".join([translate[char] for char in name]))  
        return len(set(transformations))

"""
My Solution:
Runtime: 36 ms, faster than 96.08% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.2 MB, less than 29.64% of Python3 online submissions for Unique Morse Code Words.
"""

"""
Fastest Solution (24ms):
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
        "-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for word in words:
            rep = []
            for c in word:
                rep.append(mapping[ord(c)-ord('a')])
            s.add("".join(rep))
        return len(s)

Smallest Memory (12148 kb):
class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        morselist = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
        "...","-","..-","...-",".--","-..-","-.--","--.."]
        myset = set()
        for word in words:
            myset.add(''.join([morselist[ord(char)-ord('a')] for char in word]))
        return len(myset)
"""
