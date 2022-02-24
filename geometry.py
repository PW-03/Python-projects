

class Rectangle:
    """
    Function that checks if a point is inside a given rectangle.
    The rectangle has its sides parallel to the coordinate axes and is
    defined by the coordinates of its bottom-left corner and the width and the height.
    """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    

    def is_inside(self, x, y):
        startx = self.x
        starty = self.y
        height = self.height
        width = self.width

        topy = height - starty
        rightx = width - startx

        if x >= startx and x <= rightx and y >= starty and y <= topy:
            print("true")
        else:
            print("false")

class Circle:
    """
    Function that checks if a point is inside a given circle.
    The circle is defined by the coordinates of its centre and the radius.
    """
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def is_inside(self, x, y):
        centerx = self.x
        centery = self.y
        radius = self.radius
        p = ((x - centerx)**2 + (y - centery)**2)
        if p < (radius)**2:
            print("True")
        else:
            print("False")

class Test:

 if __name__ == "__main__":
    # rect = Rectangle(2, 5, 4, 12)
    # rect.is_inside(5,6)
    circle = Circle(10,10,10)
    circle.is_inside(10,10)