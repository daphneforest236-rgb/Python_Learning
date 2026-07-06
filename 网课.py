#print函数的sep和end参数
# print("哈哈哈","嘿嘿嘿","嘻嘻嘻",sep="|")
# print("哈哈哈","嘿嘿嘿","嘻嘻嘻",end="|")

#布尔类型大小写 True 1和False 0
#复数z = a + bj  数学思维理解就可以,j 不能随便改
#str带引号才是字符串
#格式化输出
#  %s %d %4d %0d 
#  %f 默认后6位小数，遵循四舍五入 %.3f 默认后3位小数，遵循四舍五入 
#  print("我叫%s,今年%d岁了" % ("小明",18))
#  %%  
#  f"{表达式}"  print(f"我叫{name},今年{age}岁了") print(f"我叫{'小明'},今年{18}岁了")

#运算符
#算术运算符 // 取整除,向下取整(不管四舍五入的规则,只要后面有小数就直接舍弃)  % 取余数(前浮后浮) ** 
#赋值运算符 print(5-=2) 纯数字不能使用,报语法错误
#input()函数  
#  input("请输入你的名字:")  
#  input()函数返回值是字符串类型,如果想要输入数字,需要使用int()函数进行转换
#转义字符 
# \t 四个字符(缩进) \\t 不会打印 \\\t 打印\    
# \r 回车,将当前位置移到本行开头
# r原生字符串默认不转义
# \" \' \\

#if语句  if elif else  if嵌套
#while循环  break continue
#for循环  range()函数  for i in range(1,10,2)

#字符串编码
# unicode编码 所有字符都是两个字节,好处是字符与数字之间转换速度更快,坏处是占用空间大 
# utf-8编码 精准,对不同的字符用不同的长度表示,优点节省空间,缺点字符与数字的转换速度慢,每次都需要计算字符要用多少空间 
# gbk编码  gb2312编码
#字符串编码转换
# a = "hello" 
# a1 = a.encode()  #将字符串转换为字节类型a1 = a.encode("utf-8")
# a2 = a1.decode()  #将字节类型转换为字符串类型utf-8
# print(a,type(a))
# print(a1,type(a1))
# print(a2,type(a2))
#字符串的运算符 .
# +拼接  *重复输出 print("好好学习天天向上\n"*5)  sep=""
#成员运算符  
# 作用:检查字符串中是否包含了某个字符或多个字符
# in | not in如果包含的话返回true不好包含返回false  
# name = "daphne" 
# print("s" in name)
#下标   
#  从左往右从0开始     从右往左从-1开始 不能超出范围
#切片 
#  截取其中一部分操作[开始位置:结束位置:步长] 包前不包后 name[0:3]  name[3:]  name[:3]  name[-1:] e name[:-1]  name[-1:-5]
#  间隔默认为1  正数表示从左往右.负数表示从右往左
#  name[0:3:2]  name[0:3:-1]  name[::-1] enhpad
# 字符串常见操作
#   查找find() 检查某个字符串是否包含在字符串中,在就返回这个字符串开始位置的下标,否则就返回-1
#   find(子字符串,开始位置,结束位置)  开始位置和结束位置可以省略,表示在整个字符串中查找
# name = "bingbing"
# print(name.find('i'))
# print(name.find('bing'))
# print(name.find('b',3))
# print(name.find('b',5))
# print(name.find('b',3,5))
# print(name.find('b',3,4)) #包前不包后

#   检查index()同上,没找到就报错
#   index(子字符串,开始位置,结束位置)  #包前不包后

#   count() 返回子字符串在整个字符串中出现次数,没有返回0  
#   #包前不包后
# name = "bingbing"
# print(name.count('b'))  #2
# print(name.count('a'))  #0
# print(name.count('b',1))#1

#  替换replace(旧内容,新内容,替换次数)替换次换可忽略默认全部替换
#  分隔split('分割符',分割次数) 以列表的形式返回.如果字符串中不包含分割内容就不分割,作为整体列表返回
#  join()  
#  strip()  lstrip()  rstrip()
#  判断startswith()  endswith()  isupper()  islower()  
#  isalpha()  isdigit()  isalnum()  isspace()
#  upper()  lower()  title()  capitalize()  swapcase()
#列表 list  
#元组 tuple  
#字典 dict  
#集合 set