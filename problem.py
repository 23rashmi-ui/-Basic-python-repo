# what is the output of the following code ? write iterations.
x = 0
while x < 10:
  if x % 2 == 0:
    x += 3
  else:
    x += 1
print(x,end="")
'''Iterations
Initially, x = 0.
Iteration
x < 10
Condition x % 2 == 0
Update to x
1
True (0 < 10)
True (even)
0 + 3 = 3
2
True (3 < 10)
False (odd)
3 + 1 = 4
3
True (4 < 10)
True (even)
4 + 3 = 7
4
True (7 < 10)
False (odd)
7 + 1 = 8
5
True (8 < 10)
True (even)
8 + 3 = 11
6
False (11 < 10)
Loop stops
output:11 '''
