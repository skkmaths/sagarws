import numpy as np

x = np.linspace(0,1, 10)
n = x.size
print ( "Example of using for loop")
for i in range(n):
    print("number:", x[i])

init  = 0
print("Example of using while loop")
while init < n:
    print("number:", x[init])
    init = init+1

    