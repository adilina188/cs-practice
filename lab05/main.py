from logstats import parse_event

events = []
with open('events.log', 'r', encoding = 'utf-8') as file :
    for line in file:
        try:
            events.append(parse_event(line))
            print(parse_event(line))
        except ValueError:
            continue
        
print(events)
    