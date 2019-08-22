import matplotlib.pyplot as plt
from Sistema import function
import pylab

a = function()

(x1, x2, x3) = a

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax.set_yscale('log')
plt.plot(x1)
plt.title("0.10")

ax = fig.add_subplot(2, 2, 3)
ax.set_yscale('log')
plt.plot(x2)
plt.title("1.0")

ax = fig.add_subplot(2, 2, 4)
ax.set_yscale('log')
plt.plot(x3)
plt.title("10")
plt.show()
fig.savefig("1.png")
