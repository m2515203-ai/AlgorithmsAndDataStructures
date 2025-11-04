
import pandas as pd
from geopy.distance import geodesic
from matplotlib import pyplot as plt

from pracitc.geo.function import calculate_distances, show_grafic, show_distant, show_speed, calculate_direction

df1 = pd.read_csv('data_01.csv')
df2 = pd.read_csv('data_02.csv')
df3 = pd.read_csv('data_03.csv')
df4 = pd.read_csv('data_04.csv')

df1['distant'] = calculate_distances(df1)
df2['distant'] = calculate_distances(df2)
df3['distant'] = calculate_distances(df3)
df4['distant'] = calculate_distances(df4)

df1['speed'] = calculate_distances(df1)
df2['speed'] = calculate_distances(df2)
df3['speed'] = calculate_distances(df3)
df4['speed'] = calculate_distances(df4)

df1['direction'] = calculate_direction(df1)
df2['direction'] = calculate_direction(df2)
df3['direction'] = calculate_direction(df3)
df4['direction'] = calculate_direction(df4)
datasets = [df1, df2, df3, df4]


show_distant([df1])
show_distant([df2])
show_distant([df3])
show_distant([df4])
show_distant(datasets)

print(f"\nОбщее пройденное расстояние: df 1 {df1['distant'].sum():.2f} метров")
print(f"\nОбщее пройденное расстояние: df 2 {df2['distant'].sum():.2f} метров")
print(f"\nОбщее пройденное расстояние: df 3 {df3['distant'].sum():.2f} метров")
print(f"\nОбщее пройденное расстояние: df 4 {df4['distant'].sum():.2f} метров")

show_speed([df1])
show_speed([df2])
show_speed([df3])
show_speed([df4])
show_speed(datasets)

show_distant([df1])
show_distant([df2])
show_distant([df3])
show_distant([df4])
show_distant(datasets)