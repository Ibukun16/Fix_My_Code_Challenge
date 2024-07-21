#!/usr/bin/python3
""" Define class for a square """

class square():
    """ Description of a square class """
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """ Define an instance for square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Description of a perimeter instance """
        return (self.height * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())