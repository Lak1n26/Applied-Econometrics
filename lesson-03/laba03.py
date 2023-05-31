import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import scipy
import seaborn as sns

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

# print(data.columns)


print("H0 - средняя продолжительность жизнь в городе и в сельской местности одинакова")
print("H1 - средняя продолжительность жизнь в городе и в сельской местности различна")
print()
print("T-test для незавимисимых переменных")
print(stats.ttest_ind(data['в городе'], data['в сел.мест']))
ttest = stats.ttest_ind(data['в городе'], data['в сел.мест'])
print(f"Т.к p-value = {ttest[1]} < 0.05, то H0 отвергаем в пользу H1.")
print("Следовательно, средняя продолжительность жизнь в городе и в сельской местности различна.")
