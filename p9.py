class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


p = Point(1, 2) + Point(3, 4)

print(p)
print(p == Point(4, 6), p == Point(0, 0))











#EXTRA PRACTICE QUESTION
'''import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __sub__(self, other):       #Extra Question 
        return Point(self.x - other.x, self.y - other.y)
    
    def __len__(self):
        return round(math.sqrt(self.x**2 + self.y**2))


print("\n\nErtra Question")
p1 = Point(5, 7)
p2 = Point(2, 3)

print(p1 - p2)
print(len(p1))'''