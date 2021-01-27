import numpy as np  # funkcje numpy median, mean, std, min, max
import statistics as st  # statistics median_high(), median_law(), pstdev(), stdev(), pvariance(), variance(), mode()
import scipy.stats as sc
import pandas as pd
import matplotlib.pyplot as plt

data = np.loadtxt("MDR_RR_TB_burden_estimates_2020-10-29.csv", delimiter=',', skiprows=1, usecols=12)
print(np.max(data))
print(dane.max())
print(np.median(data))

data_1 = np.loadtxt("Wzrost.csv", delimiter=',', skiprows=0)
print("odchyl std:", st.stdev(data_1))
print("odchyl std2", st.pstdev(data_1))
print("median high:", st.median_high(data_1))
print("median low:", st.median_low(data_1))
print("stdev:", st.stdev(data_1))
print("pstdev:", st.pstdev(data_1))
print("variance:", st.variance(data_1))
print("pvariance:", st.pvariance(data_1))

print(sc.ttest_1samp(data, 0))

dataF = pd.read_csv("brain_size.csv", delimiter=";", skiprows=0)
print(np.mean(dataF['VIQ']))
print(dataF['Gender'].value_counts())

X = np.arange(0, len(dataF.index))
plt.plot(X, dataF['VIQ'])
plt.plot(X, dataF['PIQ'])
plt.plot(X, dataF['FSIQ'])
plt.show()

fem = dataF.loc[dataF['Gender'] == 'Female']
x_row = np.arange(0, len(fem.index))
plt.plot(x_row, fem['VIQ'])
plt.plot(x_row, fem['PIQ'])
plt.plot(x_row, fem['FSIQ'])
plt.show()