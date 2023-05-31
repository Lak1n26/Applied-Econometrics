import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

data = pd.read_csv("BinChoice.csv", sep=';')
cols = ['Y', 'x1', 'x2', 'x3', 'x4', 'x5']

# заменяем разделитель запятую на точку
def sep_zap(st):
    try:
        st = st.split(',')
        return float('.'.join(st))
    except:
        return st

for col in cols:
    for elem in data[col]:
        data[col] = data[col].replace(elem, sep_zap(elem))


# column_indices = [1, 2, 3, 4, 5]  # Индексы столбцов
column_indices = [1, 3, 4]  # Индексы столбцов
args = data.iloc[:, column_indices]


# Подготовка данных
X = args
# X = data[[data['x1'], data['x2'], data['x3'], data['x4']]] # Матрица признаков
Y = data['Y']  # Вектор целевой переменной (бинарный)


# Создаем модель логит-регрессии
logit_model = sm.Logit(Y, X)

# Обучаем модель
logit_result = logit_model.fit()

# Выводим результаты
print(logit_result.summary())

# корреляционная матрица
correlation_matrix = X.corr()
print(correlation_matrix)

# предельные эффекты
marginal_effects = logit_result.get_margeff()
print(marginal_effects.summary())

# график "ящик с усами"
# plt.boxplot(X, labels=['x1', 'x2', 'x3', 'x4', 'x5'])
plt.boxplot(X, labels=['x1', 'x3', 'x4'])
plt.show()

log_likelihood = logit_result.llf
print("Log-Likelihood:", log_likelihood)


# Вывод графика остатков
residuals = logit_result.resid_generalized
plt.scatter(range(len(residuals)), residuals)
plt.xlabel("Номер наблюдения")
plt.ylabel("Остатки")
plt.title("График остатков логит-модели")
plt.show()


# Вывод графика предсказанных значений
predicted_values = logit_result.predict(X)
plt.scatter(range(len(Y)), Y, color='blue', label='Фактические значения')
plt.scatter(range(len(Y)), predicted_values, color='red', label='Предсказанные значения')
plt.xlabel("Номер наблюдения")
plt.ylabel("Вероятность")
plt.title("График предсказанных значений логит модели")
plt.legend()
# plt.show()


probit_model = sm.Probit(Y, X)  # Пробит-модель
probit_result = probit_model.fit()  # Применение метода максимального правдоподобия

# Вывод результатов модели
print(probit_result.summary())

# Вывод графика предсказанных значений
predicted_values = probit_result.predict(X)
plt.scatter(range(len(Y)), Y, color='blue', label='Фактические значения')
plt.scatter(range(len(Y)), predicted_values, color='red', label='Предсказанные значения')
plt.xlabel("Номер наблюдения")
plt.ylabel("Вероятность")
plt.title("График предсказанных значений пробит модели")
plt.legend()
plt.show()

p_values = probit_result.pvalues
print("p_values:")
print(round(p_values.astype(float), 2))