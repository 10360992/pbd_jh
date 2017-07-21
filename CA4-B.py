#B8IT105, Programming for Big Data, CA4-Part B.
#10360992, Jelena Horosko, 21.07.2017.

import math 

#1. add function using lambda function, which takes two variables x and y and adds them
add = lambda x,y : x+y

#Test cases for lambda x+y
print
print 'Add lambda results are:'
print add(2,2)# prints result
print add(-3,3)
print add(0,-2)
print add(2,-4)
print add(1.3,-3.0)
print add(-1.5,4.0)


#2. add function using reduce function
add = reduce(lambda a,b: a+b,[4,6,7,2,5,7])
print
print 'Add lambda reduce result is:', add


#3. subtract lambda operator takes two variables (x and y) and subtracts y from x.
subtract = lambda x,y : x-y 

#test cases for lambda x-y 
print 
print 'Substract lambda results are:'
print subtract(1,-1)
print subtract(-1,1)
print subtract (0,-1)
print subtract (1.5,2.5)
print subtract (-3.5,-6.5)
print subtract (7.5,-6.5)


#4.add Map with lambda function, takes variables and repeats the same operation on a sequence or list. 
#The map function can use lambda functions
#Takes two arguments eg r = map(func, seq).

a = [4,-2,1,3]
b = [11,-11,13,7]
c = [5, 4, -3, 0]
map(lambda x,y,z:-x+y+z, a,b,c)
map(lambda x,y,z:x-y+z, a,b,c)
map(lambda x,y,z:x+y-z, a,b,c)
print 
print 'Add map with lambda operator results are:'
print map(lambda x,y,z:x+y+z, a,b,c)
print map(lambda x,y,z:x+y-z, a,b,c)
print map(lambda x,y,z:x-y-z, a,b,c)


#5.add function using function reduce lambda on a list of values
add = reduce(lambda a,b: a+b,[5,4,6,8,3,1,6])#5+4=9,9+6=15,<...>=33
print 
print 'Add function using function reduce lambda on a list of values results are:'
print add


#6.subtract function using function reduce on a list of values
subtract = reduce(lambda a,b: a-b,[4,3,8,9,6,2,3])# 4-3=1, 1-8=-7<...>=-27
print 
print 'Substract function using function reduce lambda on a list of values results are:'
print subtract


#7.Multiply function using list and map function
def multiply(a,b):
	return (a*b)
a = [2,4,5,7,8,9,10]
b = [1,0,-9,4,7,8,0.7]
result = map(multiply,a,b)
print 
print 'Multiply function using list and map function  results are:'
print result


#8.Division function using Map and lists
def division(a,b):
	
	if b == 0:
		print 'wrong, cannot divide by 0'
	else: 
		return (a/b)
a = [5,3,2,55,18,4,9,1]	
b = [2,1,4,5,6,7,3,4]
result = map(division,a,b)
print 
print 'Division function using map and lists function results are:'
print result


#9. Square function using lists and map function
def square(a):
	return a**2
	
a=[5,2,-2,-3,0.2,5,1]
result = map(square,a)
print 
print 'Square function using map and lists function results are:'
print result

#9. Cube function using lists and map function
def cube(a):
	return a**3
	
a=[4,3,-3,-4,1,0.5,11]
result = map(cube,a)
print 
print 'Cube function using map and lists function results are:'
print result


#10.modulo function, using two numbers, map function
def modulo (a,b):
	if b==0:
		return 'undefined'
	else:
		return a%b
a = [1,3,8,11,15,17,18,9]	
b = [2,1,4,5,7,4,8,2]
result = map(modulo,a,b)
print 
print 'Modulo function using map and lists function results are:'
print result


#11.List Comprehension
a = [1,2,3,4,5,6,7]
b = [2,3,4,4,6,7,8]
c = [3,4,5,6,7,8,9]
d = [(x,y,z) for x in a for y in b for z in c]
print  
print 'List comprehension results are:'
print d 