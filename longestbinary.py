import math
from tabnanny import check


def toBinary(num):
    strn = ""
    while num:
        remainder = num % 2
        num = math.floor(num/2)
        strn += str(remainder)
    return strn[::-1]

def toNumber(binary):
    num = 0
    count = 0

    binary = int(binary)

    while binary:
        num += (binary % 10)*(2**count)
        binary = binary // 10
        count+=1
    return num
# print(toNumber(toBinary(89)))

# s = 000011
s = "1001010"
k = 5
checked = {}
max = 0
# for x in range(len(s),0,-1):
#     for y in range(0,len(s) - x + 1):
#         # this is the substring
#         sub = s[y:y+x]
#         try:
#             number = checked[sub.lstrip('0')]
#         except:
#             number = toNumber(sub)
#             # print(number)
#             checked[sub.lstrip('0')] = number
#         if number <= k:
#             l = len(sub)
#             if (max < l):
#                 max =l

l = list(s)
# l.sort()
k = int(toBinary(k))
binary = ''.join(l)
while int(binary) > k:
    one_from_left = l.index('1')
    l.pop(one_from_left)
    binary = ''.join(l)
print(len(binary))