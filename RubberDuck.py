# +---------------------------------------------------------------+
# |                        RubberDuck                             |
# +---------------------------------------------------------------+
# | - __color: str = "yellow"               @class-variable       |
# | - __quack_volume: int                                         |
# +---------------------------------------------------------------+
# | + __init__(quack_volume=5)                                    |
# | + squeak(): None                         [@static-method]     |
# | + get_color(): str                       [@class-method]      |
# | + boost_volume(): None                   [@instance-method]   |
# | + quack_volume: int                      [@property]          |
# | + quack_volume(value: int): None         [@setter]            |
# | + __str__(): str                         [@instance-method]   |
# +---------------------------------------------------------------+

# RubberDuck quack_volume=5 color='yellow'  # __str__ output

class RubberDuck:

    __color: str = 'Yellow'

    def __init__(self, quack_volume=5):
        self. __quack_volume = quack_volume

    @staticmethod
    def squeak():
        print('duck is squeaking')

    @classmethod
    def get_color(cls):
        return cls.__color

    def boost_volume(self):
        self.__quack_volume *= 2

    @property
    def quack_volume(self):
        return self.quack_volume

    @quack_volume.setter
    def quack_volume(self,value: int):
        if value < 0:
            self.__quack_volume = 0
        else:
            self.__quack_volume = value

    def __str__(self)-> str:
        return f"Duck(color={self.get_color()}, quack_volume={self.__quack_volume})"

duck = RubberDuck()
print(duck)

RubberDuck.squeak()

duck.quack_volume = 10
print("🔊 New volume:", duck.quack_volume)

duck.boost_volume()
print("🚀 Boosted volume:", duck.quack_volume)

print("🎨 Default color:", RubberDuck.get_color())



