def parse_event(line):
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")
    
    parts = line.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("Неверный формат")
    time = parts[0]
    level = parts[1]
    message = parts[2]
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("Неизвестный уровень")
    return {"time": time,"level": level,"message": message}
def count_levels(lines):
    counts = {"BROKEN": 0,"DEBUG": 0,"INFO": 0,"WARNING": 0,"ERROR": 0}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
    return counts