#!/usr/bin/python3

class MyClass:
    def method(self):
        return 'instant method invoked', self
    
    @classmethod
    def classmethod(cls):
        return 'class method invoked', cls
    
    @staticmethod
    def staticmethod():
        return "static method invoked"
    
obj = MyClass()

print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

print()

print(MyClass.classmethod())
print(MyClass.staticmethod())


'''
Output:

('instant method invoked', <__main__.MyClass object at 0x0000022EC737B7F0>)
('class method invoked', <class '__main__.MyClass'>)
static method invoked

('class method invoked', <class '__main__.MyClass'>)
static method invoked
'''