#相对文件路径Linux和OS X 
#           /Windows系统中，在文件路径中使用反斜杠（\）而不是斜杠（/）
#然而都可以
# 使用绝对路径，可读取系统任何地方的文件

#读取整个文件
# with open("10文件/圆周率.txt") as file_object:
#     contents = file_object.read()
#     # print(contents)
#     print(contents.rstrip())#删除多末尾出来的空行，

#Python自会在合适的时候自动将其关闭

#逐行读取
#每行末尾都有两个换行符：一个文件，另一个来自print语句
# filename = "10文件/圆周率.txt"
# with open(filename) as file_object:
#     for line in file_object:
#         # print(line)
#         print(line.rstrip())

#创建一个包含文件各行内容的列表
# filename = "10文件/圆周率.txt"
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:      #ValueError: I/O operation on closed file.
#     # print(line)
#     print(line.rstrip())

#使用文件的内容
filename = "10文件/圆周率.txt" 
with open(filename) as file_object: 
    lines = file_object.readlines()
pi_string = '' 
for line in lines: 
    # pi_string += line.rstrip()
    pi_string += line.strip() #删除左边的空格
print(pi_string) 
print(len(pi_string))

# 打印到小数点后50位
# print(pi_string[:52] + "...")

#圆周率值中包含你的生日吗
birthday = input('Enter your birthday:')
if birthday in pi_string:
    print('yeah!')
else:
    print('no!')

