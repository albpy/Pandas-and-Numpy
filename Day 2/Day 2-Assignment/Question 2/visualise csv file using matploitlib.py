import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
df=pd.read_csv('/root/Downloads/dataset.csv')
from numpy import genfromtxt
r=genfromtxt('/root/Downloads/dataset.csv', delimiter=',')
style.use('ggplot')
plt.plot(r,'g', label='line one', linewidth=2)
plt.xlabel('Range')
plt.ylabel('Numbers')
plt.title('First Plot')
plt.legend()
plt.show()
