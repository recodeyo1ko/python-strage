def find_nearest_water_station(target_distance):
    nearest_station = round(target_distance / 5) * 5
    return nearest_station

target_distance = int(input())

nearest_station = find_nearest_water_station(target_distance)
print(nearest_station)