def remove_duplicates(tickets_dict):
    cleaned = {}
    for severity, tickets_list in tickets_dict.items():
        seen = set()
        unique_tickets = []
        for ticket in tickets_list:
            if ticket not in seen:
                unique_tickets.append(ticket)
                seen.add(ticket)
        cleaned[severity] = unique_tickets
    return cleaned


def assign_tickets_by_type(types, tickets):
    cleaned_tickets = remove_duplicates(tickets)
    result = {}
    assigned_tickets = set()
    for severity_level in sorted(types.keys()):
        severity_name = types[severity_level]
        current_tickets = cleaned_tickets.get(severity_level, [])
        unique_to_this_level = []
        for ticket in current_tickets:
            if ticket not in assigned_tickets:
                unique_to_this_level.append(ticket)
                assigned_tickets.add(ticket)
        
        result[severity_name] = unique_to_this_level
    
    return result

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = assign_tickets_by_type(types, tickets)

print(tickets_by_type)