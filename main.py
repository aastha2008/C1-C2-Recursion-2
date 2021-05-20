'''
04/29/2021
Recursion 


'''

#Factorial 
#5! = 5 * 4 * 3 * 2 * 1 * 1
#5!n= 5 * 4!
#.  = 5 * 4 * 3 * 2!
#.  = 5 * 4 * 3 * 2 * 1!
#.  = 5 * 4 * 3 * 2 * 1 * 0!
#.  = 5 * 4 * 3 * 2 * 1 * 1

# 1. With a Loop 
#num = int(input("Enter a positive int: "))

factorial = 1

#for i in range(1, num+1):
  #factorial *= i


# 2. With a Recursive Function 
def factorial(n):
  if (n == 0):
    return 1
  else:
    return n * factorial(n-1)

num = int(input("Enter a positive int: "))

print("The factorial of " + str(num) + " is " + str(factorial(num)))

#Fibonacci Sequence 
#0,1,1,2,3,5,8,13,21,....
# 10th number

# 1. With a loop

