"""
data_store.py
Shared in-memory data storage used by all other modules.
Do NOT put menu logic or feature functions here - only shared data
and simple helpers that generate IDs.

------------------------------------------------------------
SHARED DATA STRUCTURE (all members must agree on this)
------------------------------------------------------------
events = {
    "E001": {
        "name": "Neighbourhood Clean-Up Day",
        "date": "2026-09-10",
        "venue": "Taman Sri Rakyat",
        "capacity": 50,
        "registered": 0
    },
    ...
}

registrations = {
    "R001": {
        "event_id": "E001",
        "participant_name": "Ali bin Ahmad",
        "ic_number": "990101-14-5566",
        "contact": "012-3456789",
        "status": "Confirmed"      # "Confirmed" or "Waitlisted"
    },
    ...
}
------------------------------------------------------------
"""

# ANSI color codes for terminal text (shared across all modules)
class Color:
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"   # always reset after coloring, or it colors everything after too


# Global in-memory storage (shared across the whole program)
events = {}
registrations = {}

# Internal counters used to auto-generate IDs
_event_counter = 0
_registration_counter = 0


def generate_event_id():
    """Auto-generate a new event ID like E001, E002..."""
    global _event_counter
    _event_counter += 1
    return f"E{_event_counter:03d}"


def generate_registration_id():
    """Auto-generate a new registration ID like R001, R002..."""
    global _registration_counter
    _registration_counter += 1
    return f"R{_registration_counter:03d}"