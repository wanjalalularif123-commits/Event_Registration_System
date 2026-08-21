"""
registration.py
Owned by: NUR NADHIRAH NAJWA BINTI RAZALI (202307010064)

Handles: registering participants, cancelling registrations,
and basic input validation (e.g. IC number format).
"""

import re
from data_store import events, registrations, generate_registration_id


def register_participant():
    """
    Register a participant for a chosen event.
    """
    print("\n---Register Participant---")
 
    if not events:
        print("No event available yet. Ask an organiser to add one first.")
        return
 
    # Show available events so the user can pick an ID
    print("Available events:")
    for event_id, event in events.items():
        available = event["capacity"] - event["registered"]
        print(
            f"  [{event_id}] {event['name']} | {event['date']} | {event['venue']} | "
            f"{available} spots left"
        )
 
    event_id = input("\nEnter Event ID to register for: ").strip().upper()
    event = events.get(event_id)
    if not event:
        print(f"No event found with ID {event_id}.")
        return
 
    # Name - must be non-empty and not purely numeric
    participant_name = input("Participant name: ").strip()
    while not participant_name or participant_name.isdigit():
        participant_name = input("Invalid name. Participant name: ").strip()
 
    # IC number - validated against Malaysian IC format
    ic_number = input("IC number (format 990101-14-5566): ").strip()
    while not validate_ic_format(ic_number):
        ic_number = input(
            "Invalid IC format. Please use format 990101-14-5566: "
        ).strip()
 
    # Contact number - must be non-empty
    contact = input("Contact number: ").strip()
    while not contact:
        contact = input("Contact number cannot be empty. Contact number: ").strip()
 
    # Check capacity and decide status
    if event["registered"] < event["capacity"]:
        status = "Confirmed"
        event["registered"] += 1
    else:
        status = "Waitlisted"
        print(f"Note: '{event['name']}' is full. Participant will be waitlisted.")
 
    reg_id = generate_registration_id()
    registrations[reg_id] = {
        "event_id": event_id,
        "participant_name": participant_name,
        "ic_number": ic_number,
        "contact": contact,
        "status": status,
    }
 
    print(f"Registration complete. ID: {reg_id} | Status: {status}")
    return reg_id
 
 
def cancel_registration():
    """
    Cancel an existing registration.
    """
    print("\n--- Cancel Registration ---")
    reg_id = input("Enter Registration ID to cancel: ").strip().upper()
    registration = registrations.get(reg_id)
 
    if not registration:
        print(f"No registration found with ID {reg_id}.")
        return
 
    event_id = registration["event_id"]
    event = events.get(event_id)
    was_confirmed = registration["status"] == "Confirmed"
 
    del registrations[reg_id]
    print(f"Registration {reg_id} cancelled.")
 
    if not event:
        return
 
    if was_confirmed:
        event["registered"] = max(0, event["registered"] - 1)
        _promote_next_waitlisted(event_id, event)
 
 
def _promote_next_waitlisted(event_id, event):
    """
    Advanced/optional: promote the earliest-registered waitlisted
    participant for the given event to Confirmed, if there's now room.
    """
    if event["registered"] >= event["capacity"]:
        return
 
    for reg in registrations.values():
        if reg["event_id"] == event_id and reg["status"] == "Waitlisted":
            reg["status"] = "Confirmed"
            event["registered"] += 1
            print(
                f"Promoted waitlisted participant '{reg['participant_name']}' to Confirmed."
            )
            return
 
 
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
    