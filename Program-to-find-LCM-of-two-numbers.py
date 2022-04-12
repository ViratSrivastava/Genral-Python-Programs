 
# 10. Program to find LCM of two numbers
def compute_lcm(x, y):
 
  
   if x > y:
       greater = x
   else:
       greater = y
 
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
 
   return lcm
 
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
 
print("The L.C.M. is", compute_lcm(num1, num2))
