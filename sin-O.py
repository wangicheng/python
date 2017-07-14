import matplotlib.pyplot as plt
import math

fig = plt.figure(figsize=(8,8), dpi=100)
s = math.pi/180

for i in range(-90, 91):
    plt.scatter(math.cos(i*s),math.sin(i*s)) 
for i in range(-90, 91):
    plt.scatter(0-math.cos(i*s),math.sin(i*s))
plt.scatter(0.4,0.4)
plt.scatter(-0.4,0.4)
plt.show()