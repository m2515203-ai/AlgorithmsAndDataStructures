
import pandas as pd
from geopy.distance import geodesic
from matplotlib import pyplot as plt

from pracitc.geo.function import calculate_distances

df1 = pd.read_csv('data_01.csv')
df2 = pd.read_csv('data_02.csv')
df3 = pd.read_csv('data_03.csv')
df4 = pd.read_csv('data_04.csv')



# Добавление столбца distant для всех DataFrame
df1['distant'] = calculate_distances(df1)
df2['distant'] = calculate_distances(df2)
df3['distant'] = calculate_distances(df3)
df4['distant'] = calculate_distances(df4)

# Просмотр результатов
print("DataFrame 1:")
print(df1.head(10))
print(f"\nОбщее пройденное расстояние: {df1['distant'].sum():.2f} метров")

plt.figure(figsize=(12, 8))

datasets = [df1, df2, df3, df4]
dataset_names = ['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4']

for df, name in zip(datasets, dataset_names):
    plt.plot(df['distant'], label=name)

plt.xlabel('Номер точки')
plt.ylabel('Расстояние (метры)')
plt.title('Расстояние между точками')
plt.legend()
plt.grid(True)
plt.show()
