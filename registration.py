"""
registration.py
Owned by: Member 3 (Name - Student ID)

Handles: registering participants, cancelling registrations,
and basic input validation (e.g. IC number format).
"""

import re
from data_store import events, registrations, generate_registration_id


def register_participant():
    """
    Register a participant for a chosen event.
    TODO:
      - Show available events (can import and call view_events() from
        event_management.py, or just loop through `events` here)
      - Ask for event_id, validate it exists
      - Ask for participant name, IC/passport number, contact number
      - Validate inputs (non-empty name, use validate_ic_format() below)
      - Check event capacity:
          if events[event_id]['registered'] < capacity -> status "Confirmed"
          else -> status "Waitlisted"
      - Increment events[event_id]['registered'] only if Confirmed
      - Store in `registrations` dict using generate_registration_id()
    """
    print("\n--- Register Participant ---")
    print("[TODO: implement register_participant]")


def cancel_registration():
    """
    Cancel an existing registration.
    TODO:
      - Ask for registration_id
      - Validate it exists
      - Remove from `registrations`
      - Decrement events[event_id]['registered'] if it was Confirmed
      - (Optional/advanced) auto-promote next Waitlisted participant
    """
    print("\n--- Cancel Registration ---")
    print("[TODO: implement cancel_registration]")


def validate_ic_format(ic_number):
    """
    Basic validation for Malaysian IC format (e.g. 990101-14-5566).
    Returns True/False. Good example of pattern recognition (computational
    thinking concept) for your report.
    """
    pattern = r"^\d{6}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ic_number))


# Optional: allows this file to be tested on its own during development
if __name__ == "__main__":
    register_participant()