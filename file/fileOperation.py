# 向文件中写入数据
print('写文件开始')
f = open("data.txt",'w')
f.write("Hello\n")
f.write('world\n')
f.close()
print('写文件结束')

# 读取文件
print('读文件')
f = open("data.txt")
text = f.read()
print(text)

## 按行读取文件内容
print('按行读取文件内容')
for line in open("data.txt"):
    print(line)