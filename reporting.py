"""
reporting.py
Owned by: Member 4 (Name - Student ID)

Handles: searching events/participants and generating reports.
"""

from data_store import events, registrations


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
    print("[TODO: implement search_participant]")


def search_event():
    """
    TODO:
      - Ask for event name or ID
      - Display matching event(s) and their registration count
    """
    print("[TODO: implement search_event]")


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
    print("[TODO: implement generate_attendee_report]")


def generate_summary_report():
    """
    TODO:
      - Calculate % capacity filled per event
      - Identify most popular event (highest registered/capacity ratio)
      - Show total participants across all events
      - Demonstrates computational thinking: pattern recognition +
        abstraction (turning raw records into meaningful insights)
    """
    print("[TODO: implement generate_summary_report]")


# Optional: allows this file to be tested on its own during development
if __name__ == "__main__":
    search_menu()