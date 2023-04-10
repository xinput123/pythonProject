import sys

print(sys.platform)
print(2**100)
x = 'Spam'
print(x * 8)

# % 即格式化的意思
S = '%s, eggs, and %s'% ('spam', 'SPAM!')
print(S)

M=['bb','aa','cc']
M.sort()
print(M)

D ={'a':1, 'b':2, 'c':3}
Ks = list(D.keys())
print('字典D的key:', Ks)
for key in Ks:
    print(key, '=>', D[key])

# 元组具有不可变性
T=(1,2,3,4)