import numpy as np
import matplotlib.pyplot as plt

num = [5, 10, 25, 50]
means = []


for j in num:
	np.random.seed(5)
	x = [np.mean(
		np.random.randint(
			-80, 80, j)) for _i in range(1000)]
	means.append(x)

k = 0
fig, ax = plt.subplots(2, 2, figsize =(6,6))

for i in range(0, 2):
	for j in range(0, 2):
		ax[i, j].hist(means[k], 10, density = True)
		ax[i, j].set_title(label = num[k])
		k = k + 1
plt.show()