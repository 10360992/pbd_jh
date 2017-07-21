#B8IT105, Programming for Big Data, CA4-Part B.
#Jelena Horosko, 10360992, 21.07.2017.

#print
#print ("This is the program to calculate few math functions")
#print


#1 add function
add <- function (x,y)							
{return (paste("The sum of the two numbers is", (x+y)))}

add (1,1)
add (1,3)
add (-1,1)
add (1,-1)
add (3,-1)
add (3,0)
add (0.5,0.3)

#2 substract function									
substract <- function (x,y)
{return (paste("The difference of the two numbers is", (x-y)))}

substract (1,1)
substract (1,3)
substract (-1,1)
substract (1,-1)
substract (3,-1)
substract (3,0)
substract (0.5,0.3)

#3 multiply function 
multiply <- function (x,y)
{return(paste("The product of two numbers is", (x*y)))}

multiply (1,1)
multiply (1,3)
multiply (-1,1)
multiply (1,-1)
multiply (3,-1)
multiply (3,0)
multiply (0.5,0.3)

#4 dividing function 
divide <- function (x,y)
{return(paste("The result of division of two numbers is", (x/y)))}

divide (1,1)
divide (1,3)
divide (-1,1)
divide (1,-1)
divide (3,-1)
divide (3,0)
divide (0.5,0.3)


#5 square function
square <- function (x)
{return(paste("The product of squaring two numbers is", (x*x)))}

square (1)
square (3)
square (-1)
square (-3)
square (-1.5)
square (0)
square (0.5)

#6 power function 
power <- function (x,y)
{return(paste("The number raised to the power of another number", (x**y)))}

power (1,3)
power (1,5)
power (-1,3)
power (1.5,5)
power (3,4)
power (0,3)
power (0.5,3)

#7 factorial function
fact<- function(x){
  return(paste("The factorial of",x,"is",(factorial(x))))
  }

fact(5)
fact(1)
fact(0)
fact(10)
fact(6)
fact(-3)

#8 square root of a number function
squareroot <- function (x)
{return(paste("The squareroot of number x is", (x**0.5)))}

squareroot (1)
squareroot (3)
squareroot (-1)
squareroot (9)
squareroot (25)
squareroot (0)
squareroot (2.5)

#9 cuberoot of a number function
cuberoot <- function (x)
{return(paste("The squareroot of number x is", (x**0.3333)))}

cuberoot (1)
cuberoot (3)
cuberoot (-1)
cuberoot (9)
cuberoot (25)
cuberoot (0)
cuberoot (2.5)

#10 Modulo function
modulo <- function (x,y)
{return(paste("The result of numbers xmody is", (x%%y)))}

modulo (3,3)
modulo (1,5)
modulo (-1,3)
modulo (1.5,5)
modulo (3,4)
modulo (0,3)
modulo (0.5,3)


