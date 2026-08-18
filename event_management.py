"""
event_management.py
Owned by: Member 2 (Name - Student ID)

Handles: creating, updating, and viewing events.
"""

def add_event():
    print("\n--- Add New Event ---")

    event_id = generate_event_id()

    name = input("Event name: ").strip()
    while not name:
        name = input("Event name cannot be empty. Enter event name: ").strip()

    date = input("Event date (YYYY-MM-DD): ").strip()
    while not is_valid_date(date):
        date = input("Invalid format. Enter date as YYYY-MM-DD: ").strip()

    venue = input("Venue: ").strip()
    while not venue:
        venue = input("Venue cannot be empty. Enter venue: ").strip()

    capacity = get_valid_capacity()

    events[event_id] = {
        "name": name,
        "date": date,
        "venue": venue,
        "capacity": capacity,
        "registered": 0
    }

    print(f"Event added successfully with ID: {event_id}")


def is_valid_date(date_str):
    """Checks format YYYY-MM-DD using simple string checks."""
    parts = date_str.split("-")
    if len(parts) != 3:
        return False
    year, month, day = parts
    if not (len(year) == 4 and len(month) == 2 and len(day) == 2):
        return False
    return year.isdigit() and month.isdigit() and day.isdigit()


def get_valid_capacity():
    while True:
        raw = input("Capacity: ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Capacity must be a positive whole number. Try again.")

def view_events():
    print("\n--- All Events ---")
    if not events:
        print("No events available yet.")
        return

    print(f"{'ID':<6}{'Name':<25}{'Date':<12}{'Venue':<20}{'Cap':<6}{'Left':<6}")
    print("-" * 75)
    for event_id, details in events.items():
        seats_left = details["capacity"] - details["registered"]
        print(f"{event_id:<6}{details['name']:<25}{details['date']:<12}"
              f"{details['venue']:<20}{details['capacity']:<6}{seats_left:<6}")

def update_event():
    print("\n--- Update Event ---")
    view_events()

    if not events:
        return

    event_id = input("\nEnter Event ID to update: ").strip().upper()
    if event_id not in events:
        print(f"Event ID '{event_id}' not found.")
        return

    print("Which field do you want to update?")
    print("1. Name\n2. Date\n3. Venue\n4. Capacity")
    field_choice = input("Choose (1-4): ").strip()

    if field_choice == "1":
        new_name = input("New name: ").strip()
        if new_name:
            events[event_id]["name"] = new_name
    elif field_choice == "2":
        new_date = input("New date (YYYY-MM-DD): ").strip()
        if is_valid_date(new_date):
            events[event_id]["date"] = new_date
        else:
            print("Invalid date format. No change made.")
    elif field_choice == "3":
        new_venue = input("New venue: ").strip()
        if new_venue:
            events[event_id]["venue"] = new_venue
    elif field_choice == "4":
        new_capacity = get_valid_capacity()
        if new_capacity < events[event_id]["registered"]:
            print("Capacity can't be lower than current registrations. No change made.")
        else:
            events[event_id]["capacity"] = new_capacity
    else:
        print("Invalid choice.")
        return

    print("Event updated successfully.")