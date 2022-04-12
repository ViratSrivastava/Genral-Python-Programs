# Program to count the number of each vowels

vowels = 'aeiou'

ip_str = input("inter the string:")

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)