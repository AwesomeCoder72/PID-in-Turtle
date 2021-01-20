from matplotlib import pyplot as plt
import json

# y = [x for x in range(-100, 100)]
# y = input("> ")
# y = y.splitlines()
# x = json.loads(y)

with open("values.json", 'r') as jsonfile:
    jsondict = json.load(jsonfile)

print(jsondict["values"])
plt.plot(jsondict["values"])
plt.axhline(y=jsondict["desired"], color='r', linestyle='-')
plt.show()