def parse_record(line):
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError("В записи должно быть три поля")
    city = parts[0].strip()
    temp = parts[1].strip()
    date = parts[2].strip()
    if city = "" or date = "":
        raise ValueError("Город и дата должны бфть заполнены")
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Темпратура должна быть числом")
    return city, temp, date

def read_valid(lines):
    record = []
    for line in lines:
        if line.strip() == "":
            continue   
        try:
            record = parse_record(lines)
        except ValueError:
            continue
        records.append(record)
    return records

