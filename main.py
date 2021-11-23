import matplotlib.pyplot as plt
import re

p1 = []
p2 = []
data = []

file = open("DS9.txt", 'r')

l = [line.strip() for line in file]

print(l[1].split(","))

for i in range(len(l)):
    l[i].split()

print(l[1].split(","))
print(l)
for i in range(len(l)):
    for j in range(len(l[i])):
        if j == 0:
            p1.append(l[i][0])
        else:
            p2.append(960 - data[i][1])


plt.figure('Draw')

plt.scatter(p1, p2)

plt.savefig("DS.jpg")
plt.show()
plt.close()
