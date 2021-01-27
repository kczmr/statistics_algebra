import pandas as pd
import numpy as np
import scipy.stats as scs
import statistics as st
import matplotlib.pyplot as plt

data = {'val': [1, 2, 3, 4, 5, 6], 'prob': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]}
dataF = pd.DataFrame(data=data)

# Zad 1
print('max', np.max(dataF['val']))
print('min', np.min(dataF['val']))
print("std", np.std(dataF['val']))
print('mean', np.mean(dataF['val']))

# Zad 2
berno = scs.bernoulli.rvs(0.3, size=100)
bino = scs.binom.rvs(1, 0.3, size=100)
poiso = scs.poisson.rvs(0.3, size=100)
print('bernoulli', berno)
print('binom', bino)
print('poisson', poiso)

# Zad 3
print('Bernoulli mean', np.mean(berno))
print('Binom mean', np.mean(bino))
print('Poisson mean', np.mean(poiso))
print('Bernoulli variance', st.variance(berno))
print('Binom variance', st.variance(bino))
print('Poisson variance', st.variance(poiso))
print('Bernoulli kurtosis', scs.kurtosis(berno))
print('Binom kurtosis', scs.kurtosis(bino))
print('Poisson kurtosis', scs.kurtosis(poiso))
print('Bernoulli skewnes', scs.skew(berno))
print('Binom skewnes', scs.skew(bino))
print('Poisson skewnes', scs.skew(poiso))

# Zad 4
X = np.arange(0, 100)
plt.plot(X, berno)
plt.plot(X, bino)
plt.plot(X, poiso)
plt.show()

# Zad 5
bim1 = scs.binom.pmf(20, 20, 0.4)
print(np.sum(bim1))
print(bim1)

# Zad 6
nor = scs.norm.rvs(0, 2, 100)
print('max', np.max(nor))
print('min', np.min(nor))
print("std", np.std(nor))
print('mean', np.mean(nor))