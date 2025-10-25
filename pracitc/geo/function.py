import pandas as pd
from geopy.distance import geodesic


def calculate_distances(df):
    distances = [None]  # Первая точка - расстояние 0
    for i in range(1, len(df)):
        # Проверка на наличие координат
        cur = df.iloc[i]
        prev = df.iloc[i - 1]
        if pd.notna(cur['lat']) and pd.notna(cur['lon']) and \
                pd.notna(prev['lat']) and pd.notna(prev['lon']):
            point1 = (prev['lat'], prev['lon'])
            point2 = (cur['lat'], cur['lon'])
            distance = geodesic(point1, point2).meters
            distances.append(distance)
        else:
            distances.append(None)

    return distances
