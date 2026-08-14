"""
event_management.py
Owned by: Member 2 (Name - Student ID)

Handles: creating, updating, and viewing events.
"""

from data_store import events, generate_event_id


def add_event():
    """
    Add a new event to the system.
    TODO:
      - Prompt for name, date, venue, capacity
      - Validate capacity is a positive integer (basic error handling)
      - Validate date format (e.g. YYYY-MM-DD) using simple string checks
      - Store in `events` dict using generate_event_id()
    """
    print("\n--- Add New Event ---")
    # event_id = generate_event_id()
    # name = input("Event name: ").strip()
    # date = input("Event date (YYYY-MM-DD): ").strip()
    # venue = input("Venue: ").strip()
    # capacity = ... (validate positive integer)
    # events[event_id] = {
    #     "name": name,
    #     "date": date,
    #     "venue": venue,
    #     "capacity": capacity,
    #     "registered": 0
    # }
    # print(f"Event added successfully with ID: {event_id}")
    print("[TODO: implement add_event]")


def update_event():
    """
    Update details of an existing event (e.g. change venue/capacity).
    TODO:
      - Show list of events, ask which event_id to update
      - Ask which field to update, validate new value
      - Handle event_id not found
    """
    print("\n--- Update Event ---")
    print("[TODO: implement update_event]")


def view_events():
    """
    Display all events in a readable, formatted table.
    TODO:
      - Loop through `events` dict
      - Show ID, name, date, venue, capacity, seats remaining
      - Handle empty case (no events yet)
    """
    print("\n--- All Events ---")
    if not events:
        print("No events available yet.")
        return
    print("[TODO: implement formatted event listing]")


# Optional: allows this file to be tested on its own during development
if __name__ == "__main__":
    add_event()
    view_events()