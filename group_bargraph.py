import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('stationary.xlsx')
print(df)

year = [2021, 2022, 2023]
x = df['Pencil']
x1 = df['Pen']
xaxis = np.arange(len(year))

plt.bar(xaxis - 0.2, x, 0.4, label='Pencil')  
plt.bar(xaxis + 0.2, x1, 0.4, label='Pen')    

plt.xticks(xaxis, year)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.legend()
plt.show()
