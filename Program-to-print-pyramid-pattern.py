# 8. Program to print pyramid pattern
def printPattern(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(i,end="")        
        print("")
    for i in range(n - 1,0,-1): 
        for j in range(i,0,-1): 
            print(i,end="")        
        print("")
n = int(input("enter the number:"))
printPattern(n)
