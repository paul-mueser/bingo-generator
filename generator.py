import sys
import random
import csv

def main(content, player_count, event_index):
    events = get_events_dict(content, event_index)

    event_csv_data = []
    for i in range(1, 6):
        if i not in events:
            continue
        events_raw = events.get(i).get("items")
        event_csv_data.extend(events_raw)

    f = open("events.csv", "w", encoding='utf-8', newline='')
    writer = csv.writer(f)
    writer.writerows(event_csv_data)
    f.close()

    for p in range(1, player_count + 1):
        selected_events = []
        for i in range(1, 6):
            if i not in events:
                continue
            category_count = events.get(i).get("count")
            category_events = events.get(i).get("items")
            random.shuffle(category_events)
            selected_events.extend(category_events[:category_count])

        random.shuffle(selected_events)
        selected_events = [event[0] for event in selected_events]

        selected_events_csv_data = []
    
        for x in range(5):
            for y in range(5):
                selected_events_csv_data.append([x + 1, y + 1, selected_events[(x*5)+y]])
        
        f = open(f"player_{p}.csv", "w", encoding='utf-8', newline='')
        writer = csv.writer(f)
        writer.writerows(selected_events_csv_data)
        f.close()
            



def get_events_dict(content, event_index):
    content = content.split("---\n")
    events = {}
    for i in range(0, len(content), 2):
        tmp = content[i].strip()
        tmp = tmp.split("|")
        categoryId = int(tmp[0].strip())
        categoryCount = int(tmp[1].strip())
        if categoryId not in events:
            events[categoryId] = {"count": categoryCount, "items": []}
        items, event_index = get_events_for_category(categoryId, content[i+1], event_index)
        events[categoryId]["items"].extend(items)
        
    return events

def get_events_for_category(categoryId, text, event_index):
    items = []
    lines = text.strip().split("\n")
    for line in lines:
        tmp = line.split("|")
        event = tmp[0].strip()
        amountneeded = int(tmp[1].strip())
        amountbased = 1 if amountneeded > 1 else 0

        item = [event_index, event, amountneeded, amountbased, categoryId]
        items.append(item)
        event_index += 1
    return items, event_index


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or len(args) < 2:
        print("Please provide at least an event file and a number of players.")
        sys.exit(1)
    
    event_file = args[0]
    player_count = int(args[1])
    event_index = 1
    if len(args) > 2:
        event_index = int(args[2])
    
    with open(event_file, encoding='utf-8') as file:
        content = file.read()

    main(content, player_count, event_index)
