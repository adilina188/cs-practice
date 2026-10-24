import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records, skip = read_valid(lines)
average = average_by_city(records)
best = warmest_city(average)
print("Корректные записи :", len(records))
print("Необработанные записи с ошибками :", skip)
if best is None:
    print(0)
else:
    print("Средняя температура самого теплого города :", average[best])