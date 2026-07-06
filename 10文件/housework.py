# filename = 'learning_python.txt'
# with open(filename, 'w', encoding='utf-8') as f:
#     f.write("In Python you can create a 类 and 继承 it\n")
#     f.write("In Python you can 判断事情是否满足条件\n")
#     f.write("In Python you can 用函数库里面的函数\n")
#     f.write("In Python you can 使用各种类型的数据\n")
# print("文件已创建！\n")

# try:
#     # 第一次打印：读取整个文件
#     print("=" * 50)
#     print("方法1：读取整个文件")
#     print("=" * 50)
#     with open(filename, 'r', encoding='utf-8') as file_object:
#         contents = file_object.read()
#         print(contents)

#     # 第二次打印：遍历文件对象
#     print("\n" + "=" * 50)
#     print("方法2：遍历文件对象")
#     print("=" * 50)
#     with open(filename, 'r', encoding='utf-8') as file_object:
#         for line in file_object:
#             print(line.rstrip())

#     # 第三次打印：存储在列表中，在 with 块外打印
#     print("\n" + "=" * 50)
#     print("方法3：存储在列表中，在 with 块外打印")
#     print("=" * 50)
#     with open(filename, 'r', encoding='utf-8') as file_object:
#         lines = file_object.readlines()
    
#     # 在 with 块外使用列表
#     for line in lines:
#         print(line.rstrip())

# except FileNotFoundError:
#     print(f"错误：找不到文件 '{filename}'")
# except Exception as e:
#     print(f"发生错误: {e}")

name = input('请输入名字:')
filename = 'guest.txt'
with open(filename,'w') as f:
    f.write(name)

while True:
    name = input('请输入名字:')
    print(f"{name}.title(),hello!")
    filename = 'guest.txt'
    with open(filename,'w') as f:
        f.write(name + '\n')
    if name == 'quit':
        break

