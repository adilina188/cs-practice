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
    return city, temp, date

def read_valid(lines):
    records = []
    for line in lines:
        if line.strip() == "": #если строка пустая
            continue   
        try:
            record = parse_record(line)
        except ValueError:
            continue
        records.append(record)
    return records

def average_by_city(records):
    total = {}
    count = {}
    for city, temp, date in records:
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
    average = {}
    for city in total :
        average[city] = total[city] / count[city]
    return average

def warmest_city(average):
    if len(average) == 0:
        return None
    best = ""
    for city in average:
        if best == "" or average[city] > average[best]:
            best = city
    return best