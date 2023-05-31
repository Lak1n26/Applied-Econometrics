import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import scipy
from scipy.stats import chi2_contingency

# Лаба 2 Зависимость между полом и колой-пепси (файл Adstudy)

data = pd.read_csv("Adstudy.csv", sep=";").set_index("NAME")
print("Первоначальные данные")
print(data[["GENDER", "ADVERT"]].head())

col1 = data["GENDER"]
col2 = data["ADVERT"]

# Строим таблицу сопряженности
contingency_table = pd.crosstab(col1, col2)
print("")
print("Таблица сопряженности")
print(contingency_table)


# Рассчитываем критерий Пирсона и p-value
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print("")
print(f"Хи^2 = {chi2}")
print(f"p-value = {p_value}")
print(f"количество степеней свободы = {dof}")
# degrees of freedom: (rows - 1) * (cols - 1)
print("ожидаемые значения:")
print(expected)

# Если p-значение меньше заданного уровня значимости,
# то гипотеза отвергается, что означает, что существует статистическая связь между переменными.

# `expected` - это ожидаемые значения, рассчитанные на основании нулевой гипотезы о том, что нет связи между переменными.
# Эти значения можно сравнить с фактическими значениями в таблице сопряженности, чтобы определить,
# насколько они отличаются друг от друга и насколько значима эта разница.

