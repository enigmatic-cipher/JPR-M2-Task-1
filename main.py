"""
Given a string as input, count the number of special characters in the string. Note that in this problem any character that is not an alphabet or a digit is a special character.
Input: "hello#2$$BD*"
Output: Special:4
"""

st = "hello#2$$BD*"
ln = len(st)
count = 0
for i in range(0,ln):
  ch = st[i]
  if (ch>="A" and ch<="Z") or (ch>="a" and ch<="z") or (ch>="0" and ch<="9"):
    pass
  else:
    count = count + 1
print(f"Special:{count}")
