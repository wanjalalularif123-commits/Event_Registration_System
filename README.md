# Community Event Registration System

BIT2083 Fundamental of Computational Thinking: Python — Final Project (40%)
**SDG 11: Sustainable Cities and Communities**

## Group Members
| Name | Student ID |Class code | Program |
|------|-----------|------------|---------|
|WAN JALALULARIF BIN WAN MOHD ANUAR |202307010067 |202605F0812 |BIT |
|NUR NADHIRAH NAJWA BINTI RAZALI |202307010064 |202605F0812 |BIT |
|KRISTY JADE LUTHER |202307010100 |202605F0812 |BCSSE|
|THILAK A/L KAMALISH KUMAR |202309010104 | |BIT |
|NURAIN BADRISYIA BINTI MOHD GHAZALI |202307010013 | |BCSSE|

## Project Structure

```
event_registration_system/
├── main.py              # Member 1 - Menu, main loop, integration
├── data_store.py         # Shared data (events, registrations dicts)
├── event_management.py   # Member 2 - Add/update/view events
├── registration.py       # Member 3 - Register/cancel participants
├── reporting.py           # Member 4 - Search + reports
└── README.md
```

Member 5 (Documentation & QA) works across the report, UML diagram,
slides, and testing — not a separate code file.

## How to Run

```bash
python main.py
```

Make sure all files stay in the same folder — `main.py` imports directly
from the other modules.

## How to Work on This as a Group (GitHub)

### 1. One person creates the repo
- Create a new repository on GitHub (e.g. `community-event-registration`)
- Upload these starter files and push to the `main` branch

### 2. Everyone else clones it
```bash
git clone https://github.com/YOUR-USERNAME/community-event-registration.git
cd community-event-registration
```

### 3. Each member works in their own file + branch (avoids conflicts)
```bash
git checkout -b feature/event-management     # Member 2 example
# ...edit event_management.py...
git add event_management.py
git commit -m "Implement add_event and view_events"
git push origin feature/event-management
```
Then open a Pull Request on GitHub into `main` so the team can review
before merging.

**Suggested branch names:**
- `feature/event-management` (Member 2)
- `feature/registration` (Member 3)
- `feature/reporting` (Member 4)
- `feature/main-integration` (Member 1)

### 4. Pull latest changes before you start working each session
```bash
git checkout main
git pull origin main
```

### 5. Only edit your own file where possible
Since each member owns a separate `.py` file, you'll rarely get merge
conflicts. If `main.py` needs changes (e.g. new menu option), Member 1
should coordinate that.

## Testing
Each module can be run on its own for quick testing, e.g.:
```bash
python event_management.py
```
This runs the small test block at the bottom of that file without
needing the full menu system.

## SDG 11 Justification
This project supports SDG 11 (Sustainable Cities and Communities) by
making local community events easier to organise, track, and manage —
helping community organisers use resources (venue capacity, planning)
more efficiently and improving civic participation.
