"""
reporting.py
Owned by: Member 4 (NURAIN BADRISYIA BINTI MOHD GHAZALI - 202307010013)

Handles: searching events/participants and generating reports.
"""

from data_store import events, registrations, Color


def search_menu():
    """Sub-menu for search options."""
    print("\n--- Search ---")
    print("1. Search by Participant Name")
    print("2. Search by Event")
    sub_choice = input("Choose an option: ").strip()
    if sub_choice == "1":
        search_participant()
    elif sub_choice == "2":
        search_event()
    else:
        print("Invalid option.")


def search_participant():
    """
    TODO:
      - Ask for a name (or partial name) to search
      - Loop through `registrations`, match name (case-insensitive)
      - Display matching results with their event details
    """
    keyword = input("Enter participant name to search: ").strip().lower()

    if not keyword:
        print("Search term cannot be empty.")
        return

    results = []
    for reg_id, reg in registrations.items():
        if keyword in reg["participant_name"].lower():
            results.append((reg_id, reg))

    if not results:
        print(f"{Color.RED}No participants found matching '{keyword}'.{Color.RESET}")
        return

    print(f"\nFound {len(results)} matching participant(s):")
    print("-" * 60)
    for reg_id, reg in results:
        event = events.get(reg["event_id"])
        event_name = event["name"] if event else "Unknown Event"
        print(f"Registration ID : {reg_id}")
        print(f"Name            : {reg['participant_name']}")
        print(f"IC Number       : {reg['ic_number']}")
        print(f"Contact         : {reg['contact']}")
        print(f"Event           : {event_name} ({reg['event_id']})")
        print(f"Status          : {reg['status']}")
        print("-" * 60)

def search_event():
    """
    TODO:
      - Ask for event name or ID
      - Display matching event(s) and their registration count
    """
    keyword = input("Enter event ID or event name to search: ").strip()

    if not keyword:
        print("Search term cannot be empty.")
        return

    matches = {}

    # 1. Try an exact event_id match first (IDs are case-sensitive, e.g. "E001")
    if keyword in events:
        matches[keyword] = events[keyword]
    else:
        # 2. Fall back to a partial, case-insensitive name match
        keyword_lower = keyword.lower()
        for event_id, event in events.items():
            if keyword_lower in event["name"].lower():
                matches[event_id] = event

    if not matches:
        print(f"{Color.RED}No events found matching '{keyword}'.{Color.RESET}")
        return

    print(f"\nFound {len(matches)} matching event(s):")
    print("-" * 60)
    for event_id, event in matches.items():
        # Count how many registrations point at this event_id
        registration_count = sum(
            1 for reg in registrations.values() if reg["event_id"] == event_id
        )
        print(f"Event ID        : {event_id}")
        print(f"Name            : {event['name']}")
        print(f"Date            : {event['date']}")
        print(f"Venue           : {event['venue']}")
        print(f"Capacity        : {event['capacity']}")
        print(f"Registered      : {event['registered']}")
        print(f"Total Bookings  : {registration_count} (incl. waitlisted)")
        print("-" * 60)


def report_menu():
    """Sub-menu for report options."""
    print("\n--- Reports ---")
    print("1. Attendee List for an Event")
    print("2. Overall Statistics (capacity usage, most popular event)")
    sub_choice = input("Choose an option: ").strip()
    if sub_choice == "1":
        generate_attendee_report()
    elif sub_choice == "2":
        generate_summary_report()
    else:
        print("Invalid option.")


def generate_attendee_report():
    """
    TODO:
      - Ask for event_id
      - List all registrations for that event with status
    """
    event_id = input("Enter event ID: ").strip()

    if event_id not in events:
        print(f"{Color.RED}Event ID '{event_id}' not found.{Color.RESET}")
        return

    event = events[event_id]
    attendees = [
        (reg_id, reg)
        for reg_id, reg in registrations.items()
        if reg["event_id"] == event_id
    ]

    print(f"\n--- Attendee List: {event['name']} ({event_id}) ---")
    print(f"Venue: {event['venue']}  |  Date: {event['date']}")
    print(f"Capacity: {event['capacity']}  |  Registered: {event['registered']}")

    if not attendees:
        print("No one has registered for this event yet.")
        return

    confirmed = [(rid, r) for rid, r in attendees if r["status"] == "Confirmed"]
    waitlisted = [(rid, r) for rid, r in attendees if r["status"] == "Waitlisted"]

    print(f"\nConfirmed ({len(confirmed)}):")
    if confirmed:
        for reg_id, reg in confirmed:
            print(f"  {reg_id} - {reg['participant_name']} ({reg['contact']})")
    else:
        print("  None")

    print(f"\nWaitlisted ({len(waitlisted)}):")
    if waitlisted:
        for reg_id, reg in waitlisted:
            print(f"  {reg_id} - {reg['participant_name']} ({reg['contact']})")
    else:
        print("  None")


def generate_summary_report():
    """
    TODO:
      - Calculate % capacity filled per event
      - Identify most popular event (highest registered/capacity ratio)
      - Show total participants across all events
      - Demonstrates computational thinking: pattern recognition +
        abstraction (turning raw records into meaningful insights)
    """
    if not events:
        print("No events availablen yet.")
        return
    
    print("\n--- Overall Statistics ---")
    print(f"{'Event ID':<10}{'Name':<30}{'Capacity':<10}{'Registered':<12}{'% Filled':<10}")
    print("-" * 72)

    most_popular_id = None
    highest_ratio = -1.0

    for event_id, event in events.items():
        capacity = event["capacity"]
        registered = event["registered"]

         # Guard against divide-by-zero if capacity was ever set to 0
        ratio = (registered / capacity) if capacity > 0 else 0
        percent_filled = ratio * 100

        print(
            f"{event_id:<10}{event['name']:<30}{capacity:<10}"
            f"{registered:<12}{percent_filled:<9.1f}%"
        )

        if ratio > highest_ratio:
            highest_ratio = ratio
            most_popular_id = event_id

    total_participants = len(registrations)
    total_confirmed = sum(1 for r in registrations.values() if r["status"] == "Confirmed")
    total_waitlisted = sum(1 for r in registrations.values() if r["status"] == "Waitlisted")

    print("-" * 72)
    print(f"Total registrations (all events): {total_participants}")
    print(f"  Confirmed : {total_confirmed}")
    print(f"  Waitlisted: {total_waitlisted}")

    if most_popular_id:
        most_popular = events[most_popular_id]
        print(
            f"\n{Color.YELLOW}Most Popular Event: {most_popular['name']} ({most_popular_id}) "
            f"- {highest_ratio * 100:.1f}% full{Color.RESET}"
        )


# Optional: allows this file to be tested on its own during development
if __name__ == "__main__":
    search_menu()