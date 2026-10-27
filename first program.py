# print("hello world")
''' To print numbers from 1 to 11 that are divisible by 3 or 5, here is the correct Python code:'''
n = int(input("Enter the number:"))
for n in range(1,12):
  if  n%3 == 0:
    print(n)
  elif n%5 == 0:
    print(n)
'''Explanation
range(1, 12) generates numbers from 1 to 11.

n % 3 == 0 checks whether n is divisible by 3.

n % 5 == 0 checks whether n is divisible by 5.

print(n) prints the number, not the letter "n".'''
''' output: Enter the number:4
3
5
6
9
10'''
