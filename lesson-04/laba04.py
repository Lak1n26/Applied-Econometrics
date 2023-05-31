import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import scipy
import seaborn as sns
from scipy.stats import kruskal


# Дисперсионный анализ Крускала-Уоллиса

data = pd.read_csv("Employees.csv" , sep=';')
data = data[["AGE", "SALARY"]]
bins = [0, 35, 50, 200]
data["age_category"] = pd.cut(data["AGE"], bins)
data = data.groupby("age_category")

# print(data.groups.keys())
# print(data.get_group(pd.Interval(0, 35, closed='right')))

gr1_sal = data.get_group(pd.Interval(0, 35, closed='right'))["SALARY"]
gr2_sal = data.get_group(pd.Interval(35, 50, closed='right'))["SALARY"]
gr3_sal = data.get_group(pd.Interval(50, 200, closed='right'))["SALARY"]


plt.scatter(["0-34"] * 75, gr1_sal)
plt.scatter(["35-49"] * 24, gr2_sal)
plt.scatter(["50+"] * 1, gr3_sal)
plt.show()

plt.bar(["<34"], gr1_sal.mean())
plt.bar(["35-49"], gr2_sal.mean())
plt.bar(["50+"], gr3_sal.mean())
plt.show()


H, p_value = kruskal(*[data.get_group(group)['SALARY'] for group in data.groups])
print(f"{H=}")
print(f"{p_value=}")

