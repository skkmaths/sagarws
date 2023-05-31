import numpy as np
import matplotlib as plt

a = [1, 2, "sudarshan", 0, 1]
b = (1,2,3)

k = "best"


c, d, e = b
print(a)

a.append(20)
a.remove("sudarshan")
print(a)
print(c,d,e,k)

a = np.arange(1,10,2)
b = np.linspace(0,1, 10)

print(a)
print(b)


x = np.random.rand(10)
print(x)
y = x**4
y[6]+=100000
for i in range(10):
    print("%4d %40.8e %40.8e" %  (i, x[i], y[i]))



# compute approximately sin(x)  using difference quotient formula
# compute a recurring sequence which converges to 2