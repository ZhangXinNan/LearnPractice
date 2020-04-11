

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def keys(self):
        return ("x", "y")
    
    def __getitem__(self, item):
        return getattr(self, item)

class Quad:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.lt = Point(x1, y1)
        self.rt = Point(x2, y2)
        self.rb = Point(x3, y3)
        self.lb = Point(x4, y4)

    def keys(self):
            return ("lt", "rt", "rb", "lb")

    def __getitem__(self, item):
        return dict(getattr(self, item))

class TextLine:
    def __init__(self, q):
        self.quad = Quad(*q)
        self.words = None

    def keys(self):
        return ("quad", "words")
    
    def __getitem__(self, item):
        return dict(getattr(self, item))

a = Point(5, 6)
b = Point(100, 150)
da = dict(a)
db = dict(b)

print(da, type(da))
print(db)

q = Quad(1,2,3,4,5,6,7,8)
print(dict(q))

text = TextLine((1,2,3,4,5,6,7,8))
text.words = "zhang"
print(dict(text))