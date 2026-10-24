def parse_record(line):
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError("В записи должно быть три поля")
    city = parts[0].strip() # strip() - удаление лишних  пробелов
    temp = parts[1].strip()
    date = parts[2].strip()
    if city == "" or date == "":
        raise ValueError("Город и дата должны быть заполнены") # вызывается ошибка если дата или город пустые
    try: 
        temp = float(temp) # если температура  не float :
    except ValueError:
        raise ValueError("Темпратура должна быть числом") # вызываем ошибку
    return {"city": city,"temperature": temp ,"date": date}

def read_valid(lines):
    records = []
    skip = 0
    for line in lines:
        if line.strip() == "":
            continue   
        try:
            record = parse_record(line)
            records.append(record)
        except ValueError:
            continue
    return records

def average_by_city(records):
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        temp = record["temperature"]

        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1
    average = {}
    for city in total :
        average[city] = total[city] / count[city]
    return average

def warmest_city(records):
    average = average_by_city(records)
    best = None
    for city in average:
        if best is None or average[city] > average[best]:
            best = city
    return best