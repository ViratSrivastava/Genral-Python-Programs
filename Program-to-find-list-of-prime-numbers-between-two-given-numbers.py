# 4. Program to find list of prime numbers between two given numbers
lower = int(input("Enter first number:"))
upper = int(input("Enter second number:"))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num> 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
