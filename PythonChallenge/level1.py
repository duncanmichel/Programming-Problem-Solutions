ciphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"
"""
My Version (Caesar Cipher)
"""

def caesar (keynum=0,ct=""):
  def shift (x=""):
    if x in [" ",".","(",")","'"]:
      return x
    else:
      return chr((ord(x)+keynum)%122)

  pt = ''.join(list(map(shift,ct)))
  return pt

#print (caesar(2,ciphertext))
print (caesar(2,url))

"""
Using Maketrans() -- not working yet

from string import maketrans   # Required to call maketrans function.

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)

#print(ciphertext.translate(trantab))
"""
