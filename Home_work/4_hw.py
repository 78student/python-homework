#4.1
class Rectangle:

    def __init__(self, width:int, height:int):
        assert (width>0 and height>0)
        self.width=width
        self.height=height

    def square (self)->int:
        return self.width*self.height

    def perimeter (self)->int:
        return (self.width+self.height)*2

rec1=Rectangle(3,5)
rec2=Rectangle(7,2)
rec3=Rectangle(10,5)
print('rec1.square=',rec1.square())
print('rec2.square=',rec2.square())
print('rec3.square=',rec3.square())
print('rec1.perimeter=',rec1.perimeter())
print('rec2.perimeter=',rec2.perimeter())
print('rec3.perimeter=',rec3.perimeter())


#4.2
class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition (self):
        return self.a+self.b

    def multiplication  (self):
        return self.a*self.b

    def division (self):
        return self.a/self.b

    def subtraction (self):
        return self.a-self.b
math=Math(10,5)
print('addition=',math.addition())
print('multiplication=',math.multiplication())
print('division=',math.division())
print('subtraction=',math.subtraction())

#4.3
class Button:

    def __init__(self,text, type, locator=''):
        self.text=text
        self.type=type


    def click(self):
        return f'Клик по кнопке {self.text}'

for t in ['Text Box','Check Box','Radio Button','Web Tables','Buttons','Links','Broken Links - Images','Upload and Download','Dynamic Properties']:
    b = Button(t, 'Кнопка')
    print(b.text)
    print(b.click())



