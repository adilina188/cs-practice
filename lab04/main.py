import sys
from stats import average_by_city, read_valid, warmest_city, parse_record

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

skip = 0
for line in lines:
    if line.strip() == "":
        continue
    try:
        parse_record(line)
    except ValueError:
        skip += 1

average = average_by_city(records)
best = warmest_city(records)

print(len(records))
print(skip)

if best is None:
    print(0)
else:
    print(average[best])