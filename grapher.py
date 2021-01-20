from matplotlib import pyplot as plt

y = [x for x in range(-100, 100)]
print(y)
plt.plot(y)
plt.axhline(y=90, color='r', linestyle='-')
plt.show()