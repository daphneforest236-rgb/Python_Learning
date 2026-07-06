from restaurant import restaurant

class IceCreamStand(restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def show_flavors(self):
        print(f"我们提供的冰淇淋口味有: {', '.join(self.flavors)}")

my_ice_cream = IceCreamStand('甜心小店', '冰淇淋', ['香草', '巧克力', '草莓'])
my_ice_cream.show_flavors()