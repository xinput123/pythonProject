import os

# 输入要查询的字符串
# text = input("input text : ")
# path = input("path : ")

text = "python"
## 在文件中查找指定字符串
def getfiles(path):
    os.chdir(path)
    files = os.listdir()

    for file_name in files:
        abs_path = os.path.abspath(file_name)

        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            # print("文件:", abs_path)
            f = open(file_name, "r")
            if text in f.read():
                f = 1
                print(text + " found in " + abs_path)

getfiles("/Users/xinput/github/pythonProject/file/files")

