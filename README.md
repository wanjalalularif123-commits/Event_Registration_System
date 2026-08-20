# Community Event Registration System

**BIT2083 — Fundamental of Computational Thinking: Python**  
**Final Project — 40%**  
**SDG 11 — Sustainable Cities and Communities**

---

## 1. Project Overview

The **Community Event Registration System** is a Python-based application designed to support the organization and management of community events. The system allows users to manage events, register or cancel participants, search records, and generate reports through a simple menu-driven interface.

The project supports **SDG 11: Sustainable Cities and Communities** by helping community organizers manage events and venue capacity more efficiently while encouraging community participation.

---

## 2. Group Members

| No. | Name | Student ID | Class Code | Program |
|:---:|---|:---:|:---:|:---:|
| 1 | Wan Jalalularif Bin Wan Mohd Anuar | 202307010067 | 202605F0812 | BIT |
| 2 | Nur Nadhirah Najwa Binti Razali | 202307010064 | 202605F0812 | BIT |
| 3 | Kristy Jade Luther | 202307010100 | 202605F0812 | BCSSE |
| 4 | Thilak A/L Kamalish Kumar | 202309010104 | 202605F0812 | BIT |
| 5 | Nurain Badrisyia Binti Mohd Ghazali | 202307010013 | 202605F0813 | BCSSE |

---

## 3. Project Structure

```text
event_registration_system/
│
├── main.py
├── data_store.py
├── event_management.py
├── registration.py
├── reporting.py
└── README.md
```

### File Responsibilities

| File | Responsibility | Assigned Member |
|---|---|:---:|
| `main.py` | Main menu, program loop, and module integration | Member 1 |
| `data_store.py` | Shared event and registration data | Shared |
| `event_management.py` | Add, update, and view events | Member 2 |
| `registration.py` | Register and cancel participants | Member 3 |
| `reporting.py` | Search functions and report generation | Member 4 |
| `README.md` | Project information and instructions | Team |

> **Member 5 — Documentation & QA** works across the project documentation, UML diagrams, presentation slides, testing, and quality assurance rather than having a separate Python module.

---

## 4. Member Responsibilities

### Member 1 — Main Program & Integration

- Develop the main menu
- Control the main program loop
- Import and connect all modules
- Ensure the complete system runs correctly

### Member 2 — Event Management

- Add new events
- Update existing event information
- Display available events
- Manage event details

### Member 3 — Participant Registration

- Register participants for events
- Cancel participant registrations
- Validate registration information
- Manage participant records

### Member 4 — Search & Reporting

- Search event and participant records
- Generate event reports
- Display registration information
- Summarize system data

### Member 5 — Documentation & Quality Assurance

- Prepare project documentation
- Create UML diagrams
- Prepare presentation slides
- Conduct system testing
- Record test results and identify issues

---

## 5. How to Run

Make sure all project files are stored in the same folder.

Open a terminal inside the project folder and run:

```bash
python main.py
```

> **Important:** Keep all Python files in the same folder because `main.py` imports functions directly from the other modules.

---

## 6. GitHub Collaboration Workflow

### Step 1 — Create the Repository

One team member creates a new GitHub repository.

**Suggested repository name:**

```text
community-event-registration
```

Upload the starter files and push them to the `main` branch.

### Step 2 — Clone the Repository

Each member clones the repository:

```bash
git clone https://github.com/YOUR-USERNAME/community-event-registration.git
cd community-event-registration
```

### Step 3 — Create Your Branch

| Member | Suggested Branch |
|---|---|
| Member 1 | `feature/main-integration` |
| Member 2 | `feature/event-management` |
| Member 3 | `feature/registration` |
| Member 4 | `feature/reporting` |

Example:

```bash
git checkout -b feature/event-management
```

### Step 4 — Work on Your Assigned File

Example for Member 2:

```bash
git add event_management.py
git commit -m "Implement event management functions"
git push origin feature/event-management
```

### Step 5 — Create a Pull Request

After pushing your branch:

1. Open the GitHub repository
2. Go to **Pull Requests**
3. Select **New Pull Request**
4. Select your feature branch
5. Set `main` as the destination branch
6. Review the changes
7. Merge after approval

### Step 6 — Pull Latest Changes

Before starting a new work session:

```bash
git checkout main
git pull origin main
```

---

## 7. Team Development Rules

1. Work mainly on your assigned file.
2. Do not edit another member's module without coordinating with them.
3. Do not push unfinished work directly to `main`.
4. Use your own feature branch.
5. Use clear and meaningful commit messages.
6. Pull the latest version before starting new work.
7. Test your module before creating a Pull Request.
8. Member 1 coordinates changes involving `main.py` and final integration.

---

## 8. Testing

Each module can be tested individually before integration.

Example:

```bash
python event_management.py
```

After individual testing, run the complete system:

```bash
python main.py
```

### Testing Checklist

- [ ] Main menu displays correctly
- [ ] Events can be added
- [ ] Event information can be updated
- [ ] Events can be viewed
- [ ] Participants can register
- [ ] Registrations can be cancelled
- [ ] Search functions work correctly
- [ ] Reports display correct information
- [ ] Invalid inputs are handled correctly
- [ ] All modules integrate successfully
- [ ] Program runs without unexpected errors

---

## 9. SDG 11 Alignment

### Sustainable Cities and Communities

The **Community Event Registration System** supports **SDG 11** by providing a simple digital solution for organizing and managing local community events.

The system contributes by:

- Improving the organization of community activities
- Supporting efficient venue capacity management
- Reducing manual registration processes
- Improving access to event and participant information
- Encouraging participation in local community activities

By improving how community events are organized and monitored, the system demonstrates how digital technologies can contribute to more **organized, inclusive, and sustainable communities**.

---

## 10. Project Summary

The **Community Event Registration System** demonstrates the application of fundamental computational thinking and Python programming concepts in a practical community-based system.

The project applies **modular programming, functions, loops, conditional statements, data structures, testing, and GitHub collaboration**. Its modular structure allows each team member to develop a specific component independently before all components are integrated into the final application.