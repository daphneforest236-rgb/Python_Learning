# name = input("请输入你的姓名:")
# age = input("请输入你的年龄:")
# print("Hello, " + name.title() + " !你今年" + age + "岁.")
# 90.60
# num = input("请输入分数:")
# if num >= 90:
#     print("优秀")
# elif num >= 60:
#     print("及格")
# else:
#     print("优秀")

# scorces = [11,12,13,14,15]
# print(scorces[0])
# print(scorces[-1])
# scorces.append(66)
# print(scorces)
# print(scorces.pop())
# print(scorces)
# for i in scorces:
#     if

# dic = {name:'daphne',age:'13',score:'55'}

# def ad(a,b):
#     sum = a + b
#     return sum

# print(ad(4,5))

# def average(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum / len(list)
# q = [1,2,3,4,5,6]
# print(average(q))

class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def introduce(self):
        print(f"Hello,my name is {self.name.title()}.I'm {self.age} years old.I got {self.score} last exam!")
    def is_pass(self):
        return self.score >= 60
    
def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

stu1 = Student("daphne",12,99)
stu2 = Student("daph",18,69)
stu3 = Student("daphnnnn",32,49)
stu = [stu1,stu2,stu3]
list1 = []
list2 = []
for i in stu:
    i.introduce()
    list1.append(i.score)
    if(i.is_pass()):
        list2.append(i.name)
print("及格学生:",list2)
print("平均分:",average(list1))
list1.sort()
print("最高分:",list1[-1])
'''做一个简单的学生管理程序。
定义 Student 类，包含 name、age、score
有 introduce() 方法
有 is_pass() 方法

创建多个学生对象，放进列表
遍历学生列表，输出所有学生信息
输出及格学生
输出平均分
输出最高分学生'''

