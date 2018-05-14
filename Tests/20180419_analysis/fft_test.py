import pandas
import matplotlib.pyplot as plt
#import seaborn
#%matplotlib inline

rawcorridor=pandas.read_csv('./strong_10m.csv', skiprows=2, header=None).values
x=np.linspace(0,len(rawcorridor))
y=rawcorridor.flatten()
yf=scipy.fftpack.fft(y)
yf[0]=0
xf=np.linspace(0,.5, len(y))
fig, ax = plt.subplots()
ax.plot(xf, yf)
plt.show()

