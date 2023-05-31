import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Лаба 1

filename = "Продолж жизни.csv"

data = pd.read_csv(filename, sep=";", encoding="cp1251").set_index("Unnamed: 0")
cols = ['в городе', 'в сел.мест']

# установить разделить как точку вместо запятой
def sep_zap(st):
       try:
              st = st.split(',')
              return float('.'.join(st))
       except:
              return st
for elem in data["в сел.мест"]:
       data["в сел.мест"] = data["в сел.мест"].replace(elem, sep_zap(elem))
for elem in data["в городе"]:
       data["в городе"] = data["в городе"].replace(elem, sep_zap(elem))

print(data.describe())

mediana = pd.Series(data.mean())
disp = pd.Series(data.var())

print(f"Mediana = \n{mediana}")
print(f"Dispersia = \n{disp}")
print(f"Разброс = \n{data.max() - data.min()}") # разброс


low = data["в городе"].mean() - 0.95 * (data["в городе"].std() / np.sqrt(66))
high = data["в сел.мест"].mean() + 0.95 * (data["в сел.мест"].std() / np.sqrt(66))

print(f"Доверительный интервал средней = [{low}, {high}]")


areas = list(data.index.values)

h_fig, h_ax = plt.subplots(2)
h_ax[0].hist(data["в городе"], 30)
h_ax[1].hist(data["в сел.мест"], 30)


fig, ax = plt.subplots(2)

ax[0].plot(areas, data["в городе"], color='blue')
ax[0].plot(areas, data["в сел.мест"], color="red")

ax[1].scatter(areas, data["в городе"], marker='o')
ax[1].scatter(areas, data["в сел.мест"], marker='D')
ax[0].tick_params(axis='x', rotation=90)
ax[1].tick_params(axis='x', rotation=90)

# sm.qqplot(data["в городе"], line='45')
# sm.qqplot(data["в сел.мест"], line='45')

plt.show()



