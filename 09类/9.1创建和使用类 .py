# #dog类
# class Dog():
#     """一次模拟小狗的简单尝试"""
#     def __init__(self,name,age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         print(f"{self.name}坐下了")
#     def roll_over(self):
#         """模拟小狗被命令时打滚"""
#         print(f"{self.name}打滚了")
# #实例
# my_dog = Dog('旺财', 3)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog's age is " + str(my_dog.age) + " years old.")
# my_dog.sit() 
# my_dog.roll_over()

# #汽车类
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#     #读取
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#     #更新
#     def update_odometer(self,mileage):
#         #禁止里程表读数回调
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     #将里程表读数增加指定的量
#     def increment_odometer(self,miles):
#         #禁止增量为负值
#         if miles < 0:
#             print("You can't roll back an odometer!")
#         else:
#             self.odometer_reading += miles


# # my_new_car = Car('audi','a4',2016)
# # print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer()
# # my_new_car.update_odometer(25)
# # my_new_car.read_odometer()

# # my_used_car = Car('subaru', 'outback', 2013) 
# # print(my_used_car.get_descriptive_name()) 
# # my_used_car.update_odometer(23500) 
# # my_used_car.read_odometer() 
# # my_used_car.increment_odometer(100) 
# # my_used_car.read_odometer()


# class Battery():
#     def __init__(self,battery_size=70):
#         self.battery_size = battery_size
#     def upgrade_battery(self):
#         if self.battery_size != 85:
#             self.battery_size = 85
#             print("电瓶已升级至 85kWh。")
#         else:
#             print("电瓶已经是最高规格。")
#     def describe_battery(self):
#         print('This car has a' + str(self.battery_size) + '-kWh battery.')
#     def get_range(self): 
#         #电瓶的续航里程
#         if self.battery_size == 70: 
#             range = 240 
#         elif self.battery_size == 85: 
#             range = 270 
#         message = "This car can go approximately " + str(range) + " miles on a full charge." 
#         print(message)

# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#     # def describe_battery(self): 
#     #     """打印一条描述电瓶容量的消息""" 
#     #     print("This car has a " + str(self.battery_size) + "-kWh battery.")
#         self.battery = Battery()


# my_tesla = ElectricCar('tesla','model s',2016)
# print(my_tesla.get_descriptive_name())
# #my_tesla.describe_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


#restaurant类
class restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def discribe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name.title()}.")
        print(f"Cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")
res1 = restaurant('麦当劳','快餐')
res2 = restaurant('肯德基','快餐')
res1.discribe_restaurant()
res1.open_restaurant()
res2.discribe_restaurant()

class IceCreamStand(restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def show_flavors(self):
        print(f"我们提供的冰淇淋口味有: {', '.join(self.flavors)}")

my_ice_cream = IceCreamStand('甜心小店', '冰淇淋', ['香草', '巧克力', '草莓'])
my_ice_cream.show_flavors()