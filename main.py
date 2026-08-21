"""
main.py
Owned by: Member 1 (Name - Student ID) - Core System & Integration

Community Event Registration System
BIT2083 - Fundamental of Computational Thinking (Python)
SDG 11: Sustainable Cities and Communities

Run this file to start the application:
    python main.py
"""

from data_store import Color
from event_management import add_event, view_events, update_event
from registration import register_participant, cancel_registration
from reporting import search_menu, report_menu


def display_menu():
    """Display the main menu and return the user's choice."""
    print(f"\n{Color.BLUE}" + "=" * 50 + f"{Color.RESET}")
    print(f"{Color.BLUE} COMMUNITY EVENT REGISTRATION SYSTEM{Color.RESET}")
    print(f"{Color.BLUE} SDG 11: Sustainable Cities and Communities{Color.RESET}")
    print(f"{Color.BLUE}" + "=" * 50 + f"{Color.RESET}")
    print("1. Add New Event")
    print("2. View All Events")
    print("3. Update Event")
    print("4. Register Participant")
    print("5. Cancel Registration")
    print("6. Search Participant / Event")
    print("7. Generate Report")
    print("8. Exit")
    print(f"{Color.BLUE}" + "=" * 50 + f"{Color.RESET}")

    choice = input("Enter your choice (1-8): ").strip()
    return choice


def exit_program():
    """Handle clean program exit."""
    print("\nThank you for using the Community Event Registration System.")
    print("Goodbye!")


def main():
    """Main program loop - ties all modules together."""
    print("Welcome to the Community Event Registration System!")

    while True:
        choice = display_menu()

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            update_event()
        elif choice == "4":
            register_participant()
        elif choice == "5":
            cancel_registration()
        elif choice == "6":
            search_menu()
        elif choice == "7":
            report_menu()
        elif choice == "8":
            exit_program()
            break
        else:
            print(f"{Color.RED}Invalid choice. Please enter a number between 1 and 8.{Color.RESET}")


if __name__ == "__main__":
    main()