import math

import pandas as pd
from geopy.distance import geodesic
from matplotlib import pyplot as plt


def show_grafic(datasets, text, param):

    dataset_names = ['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4']
    for df, name in zip(datasets, dataset_names):
        plt.plot(df[param], label=name)

    plt.xlabel('Номер точки')
    plt.ylabel(text)
    plt.title(text)
    plt.legend()
    plt.grid(True)
    plt.show()


def show_distant(datasets):
    show_grafic(datasets,"Расстояние (метры)", 'distant')

def show_speed(datasets):
    show_grafic(datasets,"Скорость км\ч",'speed')

def show_direction(datasets):
    show_grafic(datasets,"Азимут в °",'direction')

def calculate_distances(df):
    distances = [None]
    for i in range(1, len(df)):
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


def calculate_speed(df):
    speeds = [None]
    for i in range(1, len(df)):
        cur = df.iloc[i]
        prev = df.iloc[i - 1]
        if pd.notna(cur['timestamp']) and pd.notna(cur['distance']) and \
                pd.notna(prev['timestamp']) and pd.notna(prev['distance']):
            time_diff = cur['timestamp'] - prev['timestamp']
            speed_kmh = (cur['distance'] / time_diff) * 3.6
            speeds.append(speed_kmh)
        else:
            speeds.append(None)

    return speeds


def calculate_direction(df):
    directions = [None]

    for i in range(1, len(df)):
        cur = df.iloc[i]
        prev = df.iloc[i - 1]

        if pd.notna(cur['lat']) and pd.notna(cur['lon']) and \
                pd.notna(prev['lat']) and pd.notna(prev['lon']):
            # Координаты предыдущей и текущей точек
            lat1 = math.radians(prev['lat'])
            lon1 = math.radians(prev['lon'])
            lat2 = math.radians(cur['lat'])
            lon2 = math.radians(cur['lon'])

            # Вычисление азимута
            dlon = lon2 - lon1
            x = math.sin(dlon) * math.cos(lat2)
            y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)

            bearing = math.atan2(x, y)
            bearing = math.degrees(bearing)
            bearing = (bearing + 360) % 360

            directions.append(bearing)
        else:
            directions.append(None)

    return directions
