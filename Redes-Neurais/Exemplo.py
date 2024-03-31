from sklearn.datasets import make_regression
x, y = make_regression(n_samples=200, n_features=1, noise=30)

import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Exemplo de Regressão')
plt.show()
