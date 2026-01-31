time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

time_values = time_string.split(',')

total_minutes = 0

for value in time_values:
    components = value.split()
    
    for component in components:
        if 'h' in component:
            hours = int(component.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in component:
            minutes = int(component.replace('m', ''))
            total_minutes += minutes
        elif 's' in component:
            seconds = int(component.replace('s', ''))
            total_minutes += seconds // 60

print(total_minutes)