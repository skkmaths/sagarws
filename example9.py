# compute the derivative of sinx using the difference formula

import numpy as np

h = 0.1
tol = 1e-5

error_norm = 1.0

sinprime = 0.0;

while error_norm > tol:
     sinprime = (np.sin(np.pi*0.5+h)-np.sin(np.pi*0.5) )/h
     h = h/10
     print(" d/dx of sinx at pi/2 is:", sinprime)
