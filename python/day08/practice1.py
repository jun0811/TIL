class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    def __init__(self, name, species, age = 1):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        self.age = age
    def bark(self):
        print('왈왈!')
    @classmethod
    def get_status(cls):
        print('Birth: {0}, Current: {1}'.format(cls.birth_of_dogs, cls.num_of_dogs))
    def __del__(self):
        Doggy.num_of_dogs -= 1
        # 아래에 코드를 작성하시오.



d1 = Doggy('초코', '푸들') 

d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

Doggy.get_status()

del d1 

Doggy.get_status()
d1 = Doggy('초코', '푸들') 
Doggy.get_status()