#字符串方法调用

s = "TaBcAa"

# 首字母大写，其他字母小写
print(s.capitalize())
print(s.casefold())
# 字符串转大小写
print(s.lower())
print(s.upper())
# 统计字符串中指定字符的个数，以及统计的位置
print(s.count('a',3,6))

print("字符串格式化方式====")
template="{0},{1} and {2}"
print("by position: ", template.format('spam','ham','eggs'))
template="{motto},{pork} and {food}"
print("by keyword: ", template.format(motto='spam', pork='ham', food='eggs'))
template="{motto},{0} and {food}"
print("by both: ", template.format('ham',motto='spam', pork='ham', food='eggs'))
template="{},{} and {}"
print("by relative position: ", template.format('spam','ham','eggs'))

template = '%s, %s and %s'
print(template % ('spam','ham','eggs'))