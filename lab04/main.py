import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    average = average_by_city(records)
    best = warmest_city(average)
    print(len(records))
    print(0)

    if best is None:
        print(0)
    else:
        print(average[best])
if __name__ == "__main__":
    main()
