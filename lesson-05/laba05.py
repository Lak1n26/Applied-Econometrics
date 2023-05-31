import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import scipy
import seaborn as sns
from factor_analyzer import FactorAnalyzer


data = pd.read_csv("EXAM.csv", sep=';')
cols = ['GEOMETRY', 'READING', 'GRAMMER', 'DRAWING', 'CALCULUS', 'HISTORY',
       'WRITING', 'SPELLING']
data = data[cols]

# заменить разделитель запятую на точку
def sep_zap(st):
    try:
        st = st.split(',')
        return float('.'.join(st))
    except:
        return st

for col in cols:
    for elem in data[col]:
        data[col] = data[col].replace(elem, sep_zap(elem))

fa = FactorAnalyzer(n_factors=2)
fa.fit(data)

print("Собственные значения:")
ev, v = fa.get_eigenvalues()
print(ev)

plt.scatter(range(1, data.shape[1] + 1), ev)
plt.plot(range(1, data.shape[1] + 1), ev)
plt.title('График каменистой осыпи для определения необходимого \
          кол-ва факторов')
plt.xlabel('Факторы')
plt.ylabel('Собственные значения')
plt.axhline(y=1, c='k')
plt.show()

print('Коэффициенты факторов:\n', fa.loadings_)

# Коэффициенты факторов:
#  [[-0.00725502  0.94707079]
#  [ 0.98271675 -0.0182399 ]
#  [ 0.95117413 -0.00221673]
#  [-0.01301095  0.95321595]
#  [ 0.01796074  0.8548581 ]
#  [ 0.9599764  -0.01480702]
#  [ 0.96065685 -0.00511069]
#  [ 0.89019108  0.03714201]]

# первый фактор сильно влияет на Чтение, Грамматику, Историю , Письмо, Выступления
# второй фактор - Геометрия, Рисование, История

print('Ковариации между факторами:\n', fa.get_communalities())
print('Общая дисперсия данных, объясненная факторами:\n', fa.get_factor_variance())

factors = pd.DataFrame(fa.transform(data), columns=['FACTOR_1', 'FACTOR_2'])
print(factors)



'''
data = pd.read_csv("Исходные данные Экономика.csv", sep=';', encoding="cp1251").set_index("Область")

print(data.head)

cols = ['Номер округа', 'Валовой рег продукт, млн',
       'Стоимость основных фондов, млн', 'Число предприятий и организаций',
       'Организации с участием иностранного капитала',
       'Добыча полезных ископаемых, млн', 'Обрабатывающие производства, млн',
       'Продукция сх, млн', 'Сх 1995', 'Число предприятий рыбоводства',
       'Инвестиции в основной капитал, млн']

def sep_zap(st):
    try:
        st = st.split(',')
        return float('.'.join(st))
    except:
        return st

for col in cols:
    for elem in data[col]:
        data[col] = data[col].replace(elem, sep_zap(elem))


factors_2 = data[['Валовой рег продукт, млн', 'Стоимость основных фондов, млн', 'Число предприятий и организаций']]
fa = FactorAnalyzer(n_factors=2)
fa.fit(factors_2)

print('Коэффициенты факторов:\n', fa.loadings_)
print('Ковариации между факторами:\n', fa.get_communalities())
print('Общая дисперсия данных, объясненная факторами:\n', fa.get_factor_variance())

'''















'''
data = pd.read_csv("Factor.csv", sep=';')
def sep_zap(st):
    try:
        st = st.split(',')
        return float('.'.join(st))
    except:
        return st
cols = ['WORK_1', 'WORK_2', 'WORK_3', 'HOBBY_1', 'HOBBY_2', 'HOME_1', 'HOME_2',
       'HOME_3', 'MISCEL_1', 'MISCEL_2']
for col in cols:
    for elem in data[col]:
        data[col] = data[col].replace(elem, sep_zap(elem))
# print(data)


fa = FactorAnalyzer(n_factors=6)
fa.fit(data)
print(fa.loadings_) # матрицу загрузок факторов, которая показывает, как каждый столбец связан с каждым из двух факторов


print()
print()

ev, v = fa.get_eigenvalues()
print(f"Собственные значения = {ev}")
print(f"собственные значения = {v}")


print('Коэффициенты факторов:\n', fa.loadings_)
print('Ковариации между факторами:\n', fa.get_communalities())
print('Общая дисперсия данных, объясненная факторами:\n', fa.get_factor_variance())
'''
