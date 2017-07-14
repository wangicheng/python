def simpson(f, a, b, N):
    """
    Approximate the definite integral of f(x) from a to b by the
    Simpson's rule, using N subintervals, N must be even integer.
 
    For example:
    simpson(lambda x: x**2+2*x+1,0.0,3.0,100)

    if N%2==0:
        n = N
    else:
        n = N+1
         
    h = float(b - a) / n;
    S = float(f(a))
  
    for i in range(1, n, 2):
        x = a + h * i
        S += 4 * f(x)
  
    for i in range(2, n-1, 2):
        x = a + h * i
        S += 2 * f(x)
  
    S += f(b)
    S = h*S/3
  
    return S

def addfun(x):
    return 1/x

#s = simpson(lambda x: addfun(x),1,100000000,100)
#print(s)


from scipy.integrate import quad

def f(x):
    return 1/x

x_lower = 1 # the lower limit of x
x_upper = 1000000000000000 # the upper limit of x

val, abserr = quad(f, x_lower, x_upper)
print ("integral value =", val, ", absolute error =", abserr)

"""
import matplotlib.pyplot as plt
import math

fig = plt.figure(figsize=(8,8), dpi=100)
s = math.pi/180

for i in range(0, 90):
    plt.scatter(math.cos(i*s),math.sin(i*s)) 
plt.show()  