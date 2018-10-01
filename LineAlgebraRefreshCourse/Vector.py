#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:56:07 2018

@author: Yuvaraja Manikandan G
"""
import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                return ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            #self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')
            
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    
    def __eq__(self, rhs):
        return self.coordinates == rhs.coordinates
    
    def __add__(self, rhs):
        return Vector(tuple(sum(x) for x in zip(self.coordinates, rhs.coordinates)))
    
    def __sub__(self, rhs):
        return Vector(tuple(x-y for x, y in zip(self.coordinates, rhs.coordinates)))
    
    def time_scalar(self, rhs):
        return Vector(tuple(Decimal(rhs) * x for x in self.coordinates))
        #if isinstance(rhs, Vector):
        #    return tuple(x * y for x,y in zip(self.coordinates, rhs.coordinates))
        
    def magnitude(self):
        _sum = sum([x*x for x in self.coordinates])
        return Decimal(math.sqrt(_sum))
    
    def normalized(self): # Normaliation of the vector - Finding the unit of the vector
        try:
            _magnitude = self.magnitude()
            if _magnitude == 0:
                return _magnitude   # to avoid 'divide by zero' error
            return self.time_scalar(Decimal('1.0')/_magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
    
    def iszero(self, tolerance=1e-10):
        for i in range(self.dimension):
            if self.coordinates[i] != 0:
                return False
        return True
        #return self.magnitude() < tolerance
    
    def dotproduct(self, rhs):
        return sum([x*y for x,y in zip(self.coordinates, rhs.coordinates)])
    
    def angle(self, rhs, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = rhs.normalized()
            _dotproduct = u1.dotproduct(u2)
            _magnituredProduct = u1.magnitude() * u2.magnitude()
            '''
            if not self.iszero() and not rhs.iszero() and _dotproduct == 0:
                # Teta is 0
                # 90 degree
                return math.cos(math.radians(90))
            if _dotproduct == _magnituredProduct:
                # Teta is 1
                # 0 degree
                return math.cos(math.radians(0))
            if _dotproduct == (-1 * _magnituredProduct):
                # Teta is -1
                # 180 degree
                return math.cos(math.radians(180))
            '''
            angle_in_radians = math.acos(_dotproduct/_magnituredProduct)
            #angle_in_radians = math.acos(_dotproduct)
            
            if in_degrees:
                degrees_per_radian = 180.0 / math.pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e
                
    def isparallel(self, rhs):
        return (
                self.iszero() or
                rhs.iszero() or
                self.angle(rhs) == 0 or
                self.angle(rhs) == math.pi
                )
        #self.magnitude() == rhs.magnitude()
    
    def isorthogonal(self, rhs, tolerance=1e-10):
        return abs(self.dotproduct(rhs)) < tolerance

v1 = Vector([1,2,3])
v2 = Vector([1,2,3])
v3 = Vector([-1,2,3])

print(v1)
print(v2)
print(v3)

print(v1 == v2)
print(v1 == v3)

print(type(v1.coordinates),v1.coordinates)

print(v1+v2)
print(v1+v3)

print(v1-v2)
print(v1-v3)

print(v1.time_scalar(2))
print(v3.time_scalar(2))

#print(v1*v1)
#print(v1*v3)

# Quiz - 1
v1 = Vector([8.218,-9.341])
v2 = Vector([-1.129,2.111])
print(v1+v2)

# Quiz - 2
v1 = Vector([7.119,8.215])
v2 = Vector([-8.223,0.878])
print(v1-v2)

# Quiz - 3
v3 = Vector([1.671,-1.012,-0.318])
print('v3 scalar mult: %s' %(v3.time_scalar(7.41)))

'''
print(v2)
print('v1 magnitude: ' + str(v1.magnitude()))
print('v2 magnitude: %s' % str(v2.magnitude()))
#print(v2.magnitude())
print('v3 magnitude: ' + str(v3.magnitude()))

print('v1 unit: ' + str(v1.unit()))
print('v2 unit: ' + str(v2.unit()))
print('v3 unit: ' + str(v3.unit()))
'''

v1 = Vector([-1,1,1])
print(v1)
print('v1 normalized: ' + str(v1.normalized()))
print(v1.normalized().magnitude())

# Quit - 4
v1 = Vector([-0.221,7.437])
print('v1 magnitude: ' + str(v1.magnitude()))

# Quit - 5
v2 = Vector([8.813,-1.331,-6.247])
print('v2 magnitude: ' + str(v2.magnitude()))

# Quit - 6
v1 = Vector([5.581,-2.136])
print('v1 normalized: ' + str(v1.normalized()))
#print(v1.normalized().magnitude()) ==> 0.9999999999999999

# Quit - 7
v2 = Vector([1.996,3.108,-4.554])
print('v2 normalized: ' + str(v2.normalized()))
#print(v2.normalized().magnitude()) ==> 1.0


v1 = Vector([1,2,-1])
v2 = Vector([3,1,0])
print('v1.v2 dotproduct: ' + str(v1.dotproduct(v2)))
print('Angle between v1 and v2 : ' + str(v1.angle(v2)))

# Quiz - 8
v = Vector([7.887,4.138])
w = Vector([-8.802,6.776])
print('v.w dotproduct: ' + str(v.dotproduct(w)))

# Quiz - 9
v = Vector([-5.955,-4.904,-1.874])
w = Vector([-4.496,-8.755,7.103])
print('v.w dotproduct: ' + str(v.dotproduct(w)))

# Quiz - 10
v = Vector([3.183,-7.627])
w = Vector([-2.668,5.319])
print('Angle between v and w: ' + str(v.angle(w)))

# Quiz - 11
v = Vector([7.35,0.221,5.188])
w = Vector([2.751,8.259,3.985])
print('Angle between v and w: ' + str(v.angle(w, True),))

print()
print()

v = Vector([-7.579,-7.88])
w = Vector([22.737,23.64])
print('v and v are parallel: ' + str(v.isparallel(v)))
print('v and v are orthogonal: ' + str(v.isorthogonal(v)))

v = Vector([-7.579,-7.88])
w = Vector([22.737,23.64])
print('v and v*-1 are parallel: ' + str(v.isparallel(v.time_scalar(-1))))
print('v and v*-1 are orthogonal: ' + str(v.isorthogonal(v.time_scalar(-1))))


# Quiz - 12
v = Vector([-7.579,-7.88])
w = Vector([22.737,23.64])
print(v.magnitude(), w.magnitude())
print('v and w are parallel: ' + str(v.isparallel(w)))
print('v and w are orthogonal: ' + str(v.isorthogonal(w)))

# Quiz - 13
v = Vector([-2.029,9.97,4.172])
w = Vector([-9.231,-6.639,-7.245])
print('v and w are parallel: ' + str(v.isparallel(w)))
print('v and w are orthogonal: ' + str(v.isorthogonal(w)))

# Quiz - 14
v = Vector([-2.328,-7.284,-1.214])
w = Vector([-1.821,1.072,-2.94])
print('v and w are parallel: ' + str(v.isparallel(w)))
print('v and w are orthogonal: ' + str(v.isorthogonal(w)))

# Quiz - 15
v = Vector([2.118,4.827])
w = Vector([0.,0.])
print('v and w are parallel: ' + str(v.isparallel(w)))
print('v and w are orthogonal: ' + str(v.isorthogonal(w)))