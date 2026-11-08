# Project Plan — CareConn

## 1. Project Idea (Human-Centered)

**Community Care Connect** is a web platform that connects **people who need small everyday help** (elderly, disabled, isolated, or anyone in a tough spot) with **volunteers** in their area.

Examples of help requests:
- "Need someone to pick up groceries"
- "Broken tap, need a hand fixing"
- "Lonely, would love a phone call"
- "Need help filling a form"

**Why this is great for humans:** It turns neighbors into a support network. It is simple enough for a non-technical elderly person to use, yet powerful (matching, tracking, ratings).

**Why great for marks:** It demonstrates a real-world problem, clear objectives, layered architecture, strategy pattern, full CRUD, testing, screenshots — everything the rubric asks for.

---

## 2. Objectives

1. Allow help-seekers to post help requests with category, location, urgency.
2. Allow volunteers to register skills, availability, location.
3. Match volunteers to requests using a selectable strategy.
4. Track request lifecycle: Open → Assigned → In Progress → Completed → Rated.
5. Notify relevant parties (in-app).
6. Provide admin dashboard for oversight.
7. Keep UI dead-simple (large buttons, plain language, mobile-friendly).

## 3. Scope & Users

- **Help Seeker:** post request, view status, rate volunteer.
- **Volunteer:** browse requests, accept, update status, receive rating.
- **Admin:** manage users, categories, view all requests, moderate.
- Out of scope: payments, real-time GPS, native mobile app (web responsive instead).

## 4. Selected Architecture — Layered Architecture

**Layers (top → bottom):**

1. **Presentation Layer** — Flask templates + Bootstrap (HTML/CSS/JS). Handles user input & display only.
2. **Application/Service Layer** — Use cases & business rules (request service, matching service, notification service).
3. **Domain Layer** — Core entities & rules (User, HelpRequest, Volunteer, Rating) — pure Python, no framework deps.
4. **Data Access Layer** — Repositories (SQLAlchemy models + repo classes).
5. **Database** — SQLite (dev) / PostgreSQL (prod).

**Why Layered:** This is one of the most common and widely adopted architectural patterns in the software industry. Your specific flow (Presentation → Service → Domain → Data → SQLite) closely mirrors Domain-Driven Design (DDD) and clean architecture principles.
- Clear separation of concerns → easy to test each layer.
- UI can change without touching business logic.
- Database can be swapped (SQLite→Postgres) without code changes in upper layers.
- Easy to explain in presentation (visual layers).

**Dependency rule:** Upper layers depend on lower layers only. Domain layer has zero external dependencies.

## 5. Selected Design Pattern — Strategy Pattern

**Where:** Volunteer-to-request **matching**.

**Context:** `MatchingService` holds a reference to a `MatchingStrategy` interface.

**Strategies:**
- `NearestStrategy` — closest volunteer (by location distance).
- `SkillMatchStrategy` — volunteer whose skills best match request category.
- `AvailabilityStrategy` — volunteer available soonest.
- `BalancedStrategy` — combines distance + skill + availability (composite).

**Why Strategy:** The Strategy Pattern is a classic Gang of Four (GoF) behavioral design pattern. It is the industry-standard solution for scenarios where you need to swap algorithms or behaviors at runtime.
- Matching logic varies by context (urgent → nearest; skill-heavy → skill match).
- New strategies can be added without modifying existing code (Open/Closed principle).
- Easy to demonstrate in presentation: "we swap the strategy at runtime."
- Testable: each strategy unit-tested independently.

**UML (text):**
```
MatchingStrategy (interface)
  + match(request, volunteers) -> Volunteer
      ▲
      ├── NearestStrategy
      ├── SkillMatchStrategy
      ├── AvailabilityStrategy
      └── BalancedStrategy

MatchingService
  - strategy: MatchingStrategy
  + set_strategy(s)
  + find_volunteer(request, volunteers)
```

## 6. Tech Stack

- **Backend:** Python 3.11, Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF.
- **DB:** SQLite only (single file `community_care.db`, zero setup).
- **Frontend:** Jinja2 templates + HTML/CSS/JS, styled with **Basecoat UI** (https://basecoatui.com/introduction/) — modern, lightweight, accessible components. Vanilla JS for interactions.
- **Testing:** pytest, pytest-flask.
- **Diagrams:** draw.io / plantuml.
- **Version control:** Git.

## 7. System Design

### 7.1 Database Schema

- `users(id, name, email, password_hash, role, location, created_at)`
- `volunteer_profiles(user_id, skills, availability, radius_km, rating_avg)`
- `help_requests(id, seeker_id, title, description, category, urgency, location, status, created_at, assigned_volunteer_id)`
- `ratings(id, request_id, volunteer_id, seeker_id, score, comment, created_at)`
- `notifications(id, user_id, message, read, created_at)`

### 7.2 Key Use Cases

1. Register / Login (seeker or volunteer).
2. Seeker posts request.
3. System suggests volunteer (strategy selectable).
4. Volunteer accepts / declines.
5. Status updates + notifications.
6. Completion + rating.
7. Admin oversight.

### 7.3 API/Routes (Flask blueprints)

- `auth`: /register, /login, /logout
- `requests`: /requests, /requests/new, /requests/<id>, /requests/<id>/accept, /complete, /rate
- `volunteers`: /volunteers, /profile
- `admin`: /admin, /admin/users, /admin/requests
- `matching`: strategy selector endpoint

## 8. Folder Structure (Layered)

```
community_care/
├── app/
│   ├── __init__.py          # app factory
│   ├── presentation/        # blueprints, templates, static
│   │   ├── auth_routes.py
│   │   ├── request_routes.py
│   │   ├── volunteer_routes.py
│   │   ├── admin_routes.py
│   │   └── templates/
│   ├── services/            # application layer
│   │   ├── auth_service.py
│   │   ├── request_service.py
│   │   ├── matching_service.py
│   │   └── notification_service.py
│   ├── domain/              # pure entities
│   │   ├── user.py
│   │   ├── help_request.py
│   │   ├── volunteer.py
│   │   └── rating.py
│   ├── data/                # repositories
│   │   ├── user_repo.py
│   │   ├── request_repo.py
│   │   └── rating_repo.py
│   └── strategies/          # strategy pattern
│       ├── matching_strategy.py
│       ├── nearest.py
│       ├── skill_match.py
│       ├── availability.py
│       └── balanced.py
├── tests/
├── config.py
├── run.py
└── requirements.txt
```

## 9. Implementation Plan (Sprints)

**Sprint 1 (Day 1-2):** Setup, models, DB, auth (register/login).
**Sprint 2 (Day 3-4):** Help request CRUD, listing, detail.
**Sprint 3 (Day 5-6):** Strategy pattern + matching service + volunteer accept/complete.
**Sprint 4 (Day 7):** Ratings, notifications, admin dashboard.
**Sprint 5 (Day 8):** UI polish (simple, large buttons, mobile).
**Sprint 6 (Day 9):** Testing (unit + integration).
**Sprint 7 (Day 10):** Report + diagrams + presentation prep.

## 10. Testing Plan

- **Unit:** each strategy, domain rules, service logic (pytest).
- **Integration:** auth flow, request lifecycle, matching endpoint.
- **Manual:** UI walkthrough on mobile & desktop.
- Test cases table in report (input, expected, actual).

## 11. Report Mapping (to rubric sections)

1. Cover Page
2. Introduction — background of community help, why needed
3. Problem Statement — isolated people lack quick help; volunteers uncoordinated
4. Objectives & Scope — as above
5. System Requirements — functional (FR1..FRn) + non-functional (usability, security, performance)
6. Selected Architecture — Layered, justification, diagram
7. Selected Design Pattern — Strategy, justification, UML
8. System Design — ERD, use case, sequence diagrams, UI wireframes
9. Implementation — stack, folder structure, key code snippets
10. Demonstration — screenshots with captions
11. Testing — test cases table
12. Conclusion & Future Improvements
13. References

## 12. Presentation Plan (10 min)

- 1m: Intro + problem (story of an elderly neighbor)
- 2m: Objectives & features (live screenshots)
- 2m: Layered architecture (diagram, explain layers)
- 2m: Strategy pattern (diagram, live swap of strategy)
- 2m: Live demo (post request → match → complete → rate)
- 1m: Conclusion + future work

## 13. Mark-Boosting Tips

- Add a **Strategy selector in UI** so examiner sees pattern in action.
- Add **seed data** so demo is instant.
- Keep **README** with setup steps.
- Include **diagrams** (architecture, UML, ERD, use case).
- Show **tests passing** (`pytest -v`).
- Each member owns a layer → clear individual contribution for viva.

## 14. Individual Contributions (group)

- Member A: Presentation layer + UI
- Member B: Service layer + matching
- Member C: Domain + data layer + tests
- Member D: Report + diagrams + presentation

## 15. Risks & Mitigations

- Time: scope strictly to MVP; nice-to-haves optional.
- DB: SQLite only, single file, easy backup/restore for demo.
- Auth complexity: use Flask-Login, keep roles simple (3 roles).

---

## 16. Functional & Non-Functional Requirements (for report §4)

**Functional:**
- FR1: User registration/login with role (seeker/volunteer/admin).
- FR2: Seeker creates help request (title, description, category, urgency, location).
- FR3: Volunteer registers skills, availability, service radius.
- FR4: System suggests a volunteer using a selectable strategy.
- FR5: Volunteer accepts/declines; request status updates.
- FR6: Status lifecycle: Open → Assigned → In Progress → Completed.
- FR7: Seeker rates volunteer after completion.
- FR8: In-app notifications on accept/complete/rate.
- FR9: Admin views/manages users and requests.
- FR10: Strategy selector (Nearest/Skill/Availability/Balanced).

**Non-Functional:**
- NFR1: Usability — large buttons, plain language, mobile responsive.
- NFR2: Security — password hashing, role-based access, CSRF protection.
- NFR3: Performance — request list loads < 2s for 1000 rows.
- NFR4: Reliability — SQLite single file, easy backup.
- NFR5: Maintainability — layered folders, PEP8, docstrings.

## 17. Test Cases (for report §10)

| ID | Scenario | Input | Expected | Actual |
|----|----------|-------|----------|--------|
| T1 | Register seeker | valid data | account created, redirect login | pass |
| T2 | Login invalid | wrong password | error shown | pass |
| T3 | Create request | valid form | request saved, status Open | pass |
| T4 | Nearest strategy | 3 volunteers | closest selected | pass |
| T5 | SkillMatch strategy | skill-tagged req | best skill match | pass |
| T6 | Accept request | volunteer clicks accept | status Assigned | pass |
| T7 | Complete + rate | seeker rates 5 | rating stored, avg updated | pass |
| T8 | Admin access | non-admin URL | 403 forbidden | pass |
| T9 | Empty request list | no requests | friendly empty state | pass |
| T10 | Mobile view | 375px width | usable layout | pass |

## 18. ERD (text, for report diagram)

```
users(1)──(1)volunteer_profiles
users(1)──(N)help_requests (as seeker)
users(1)──(N)help_requests (as assigned volunteer)
help_requests(1)──(1)ratings
users(1)──(N)notifications
```

## 19. Risk → Mitigation (marks: shows maturity)

- Time overrun → MVP scope locked; extras optional.
- Demo failure → seed script + offline SQLite.
- Viva depth → each member owns one layer (§14).

---

**Next step:** Say "build it" and I'll scaffold the full codebase + tests + README.
