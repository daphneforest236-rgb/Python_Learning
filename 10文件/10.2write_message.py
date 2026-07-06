# 要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。
#（'r'）、写入（'w'）、附加（'a'）或让你能够读取和写入文件的模式（'r+'）
# 因为如果指定文件已存在，Python将在返回文件对象前清空该文件。

filename = 'programming.txt'
with open(filename,'w') as f:
    f.write('I love programming\n')
    f.write("I love creating new games.\n")

#将内容附加到文件末尾，而不是覆盖文件原来的内容
with open(filename, 'a') as f: 
    f.write("I also love finding meaning in large datasets.\n") 
    f.write("I love creating apps that can run in a browser.\n")





