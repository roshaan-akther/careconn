# CareConn — Diagram Set & Generation Prompts

Use these with any text-to-diagram / image generator (draw.io AI, Mermaid, PlantUML, Eraser, Lucid, Napkin, etc.).
Generate diagrams one at a time. Keep the same visual language everywhere.

---

## 1. Diagram Inventory (what the report needs)

| # | Diagram | Purpose in report | Priority |
|---|---------|-------------------|----------|
| D1 | Layered Architecture Diagram | Show Presentation → Service → Domain → Data → SQLite and dependency rule | MUST |
| D2 | Strategy Pattern UML Class Diagram | Show `MatchingStrategy` interface, 4 concrete strategies, `MatchingService` | MUST |
| D3 | Entity–Relationship Diagram (ERD) | Database design: users, volunteer_profiles, help_requests, ratings, notifications | MUST |
| D4 | Use Case Diagram | Actors: Seeker, Volunteer, Admin and their goals | MUST |
| D5 | Sequence Diagram — Post Request & Match | Seeker → route → RequestService → repo → DB → MatchingService → strategy | MUST |
| D6 | Sequence Diagram — Accept, Complete & Rate | Volunteer accepts, completes; seeker rates; notifications | MUST |
| D7 | State / Activity Diagram — Request Lifecycle | open → assigned → in_progress → completed (+ rating) | MUST |
| D8 | Deployment Diagram | Browser → Flask app → SQLite file | SHOULD |
| D9 | Component Diagram | Blueprints, services, repositories, strategies, models | SHOULD |
| D10 | UI Wireframes (3 screens) | Seeker dashboard, volunteer dashboard, admin dashboard | SHOULD |
| D11 | Data Flow Diagram (Level 1) | External entities and data stores | NICE |

Minimum for full marks: **D1–D7**. Add D8–D10 if time allows.

---

## 2. Global Style Specification (use for every diagram)

- Clean, minimal, academic, presentation-ready.
- White background. No gradients, no clip art, no shadows, no decorative icons.
- Palette: deep navy `#1F3864` for primary shapes, indigo `#4F46E5` for accents, slate `#64748B` for secondary text, light grey `#EEF1F6` for fills.
- Font: Inter or Arial, 12–14 pt labels, bold titles.
- Rounded rectangles (8 px radius), 1.5 px borders, generous spacing.
- Every shape must have a readable label. No unlabeled arrows.
- Arrows: solid for dependency/call, dashed for data flow or return, open arrowheads.
- Title at top; small legend where needed.
- Export as PNG (300 dpi) and SVG. Aspect ratio: 16:9 for wide diagrams, portrait for ERD if needed.
- Text must be spelled exactly as given (class names, route names, statuses).

---

## 3. MASTER PROMPT (copy-paste)

> Generate a set of clean, minimal, academic software-design diagrams for a web application called **CareConn** — a community platform where people who need everyday help ("seekers") are matched with local volunteers.
>
> **Global style:** white background, no decoration, no gradients. Font Inter/Arial. Primary colour deep navy #1F3864, accent indigo #4F46E5, secondary text slate #64748B, light fill #EEF1F6. Rounded rectangles, 1.5 px borders, solid arrows for dependencies and dashed arrows for data/returns. Every shape and arrow must be labelled. Title at top. High resolution, 16:9, export PNG and SVG.
>
> Produce the following diagrams, one image per diagram, all in the same visual style:
>
> **D1 — Layered Architecture.** Five horizontal layers stacked top to bottom: (1) Presentation Layer — Flask blueprints and Jinja templates, listing `auth_routes`, `request_routes`, `volunteer_routes`, `admin_routes`, `learn_routes`, `arch_routes`; (2) Application/Service Layer — `AuthService`, `RequestService`, `MatchingService`; (3) Domain Layer — `User`, `VolunteerProfile`, `HelpRequest`, `Rating`, `Notification`; (4) Data Access Layer — `UserRepo`, `RequestRepo`, `VolunteerRepo`, `RatingRepo`, `NotificationRepo`; (5) Database — SQLite (`community_care.db`). Draw downward dependency arrows labelled "depends on" between adjacent layers. Add a side note: "Upper layers depend on lower layers only."
>
> **D2 — Strategy Pattern UML Class Diagram.** Show an abstract class/interface `MatchingStrategy` with method `match(request, volunteers)`. Show four concrete classes extending it: `NearestStrategy`, `SkillMatchStrategy`, `AvailabilityStrategy`, `BalancedStrategy`, each implementing `match`. Show `MatchingService` with attributes `strategy: MatchingStrategy` and `strategy_name: str`, and methods `set_strategy(name)` and `find(request)`. Draw a composition arrow from `MatchingService` to `MatchingStrategy` labelled "delegates to", and inheritance arrows from each concrete strategy to `MatchingStrategy`. Add a note: "Strategy selected at runtime via the UI."
>
> **D3 — Entity–Relationship Diagram.** Entities and attributes: `users(id PK, name, email, password_hash, role, location, created_at)`; `volunteer_profiles(user_id PK/FK, skills, availability, radius_km, rating_avg, rating_count)`; `help_requests(id PK, seeker_id FK, title, description, category, urgency, location, status, assigned_volunteer_id FK, created_at)`; `ratings(id PK, request_id FK, volunteer_id FK, seeker_id FK, score, comment, created_at)`; `notifications(id PK, user_id FK, message, read, created_at)`. Relationships: users 1—1 volunteer_profiles; users 1—many help_requests (as seeker); users 1—many help_requests (as assigned volunteer); help_requests 1—many ratings; users 1—many notifications. Label cardinalities. Mark PK and FK clearly.
>
> **D4 — Use Case Diagram.** Actors on the left/right: `Seeker`, `Volunteer`, `Admin`. Seeker use cases: Register/Login, Post Help Request, View Request Status, Rate Volunteer. Volunteer use cases: Register/Login, Browse Open Requests, Accept Request, Start Work, Mark Complete, Edit Profile. Admin use cases: Login, View Users, View Requests, Monitor Activity. Shared use cases connected to the system boundary. Keep it uncluttered; group by actor with a system boundary labelled "CareConn".
>
> **D5 — Sequence Diagram: Post Request and Match.** Participants left to right: `Seeker`, `request_routes`, `RequestService`, `RequestRepo`, `SQLite`, `MatchingService`, `MatchingStrategy`, `VolunteerRepo`. Sequence: Seeker submits form → route validates → `RequestService.create(...)` → `RequestRepo.create(...)` → SQLite INSERT → return request → `MatchingService.find(request)` → `strategy.match(request, volunteers)` → `VolunteerRepo.all_with_profiles()` → SQLite SELECT → return suggested volunteer → route renders detail page. Label returns with dashed arrows.
>
> **D6 — Sequence Diagram: Accept, Complete and Rate.** Participants: `Volunteer`, `request_routes`, `RequestService`, `RequestRepo`, `NotificationRepo`, `SQLite`, `Seeker`, `RatingRepo`, `VolunteerRepo`. Sequence: Volunteer POST accept → `RequestService.accept` → status `assigned` + `assigned_volunteer_id` → notifications to seeker and volunteer → Volunteer POST start → status `in_progress` → Volunteer POST complete → status `completed` + notification to seeker → Seeker POST rate(score, comment) → `RatingRepo.create` → `VolunteerRepo.update_rating` → notification to volunteer. Show DB writes and dashed returns.
>
> **D7 — State Diagram: Request Lifecycle.** States: `OPEN` → `ASSIGNED` → `IN_PROGRESS` → `COMPLETED`. Transition labels: "volunteer accepts" (open→assigned), "volunteer starts work" (assigned→in_progress), "volunteer marks complete" (in_progress→completed), "seeker rates volunteer" (completed→completed, self-transition labelled "rating recorded"). Mark initial state and final state.
>
> **D8 — Deployment Diagram.** Nodes: `User Browser` (HTML/CSS/JS, Basecoat UI) → HTTPS → `Flask Application Server` (Python 3, Flask, blueprints, services, strategies) → `SQLite Database` (`community_care.db`). Label protocols and artifacts.
>
> **D9 — Component Diagram.** Group components: Presentation (`auth_routes`, `request_routes`, `volunteer_routes`, `admin_routes`, `learn_routes`, `arch_routes`), Services (`AuthService`, `RequestService`, `MatchingService`), Domain (`User`, `VolunteerProfile`, `HelpRequest`, `Rating`, `Notification`), Data (`UserRepo`, `RequestRepo`, `VolunteerRepo`, `RatingRepo`, `NotificationRepo`), Strategies (`MatchingStrategy`, `NearestStrategy`, `SkillMatchStrategy`, `AvailabilityStrategy`, `BalancedStrategy`), Database (SQLite). Show allowed dependency arrows only downward.
>
> **D10 — UI Wireframes.** Three side-by-side low-fidelity screens in one image: (a) Seeker Dashboard — top pill nav, heading "My Requests", right-aligned "+ New Help Request" button, list cards with status badges and View buttons; (b) Volunteer Dashboard — "My Assignments" first, then "Open Requests" with Accept/Details buttons, then a "Matching Strategy" card; (c) Admin Dashboard — three summary tiles (Users, Requests, Open), Users table, Requests table. Monochrome wireframe style, labels in navy.
>
> **D11 — Data Flow Diagram Level 1.** External entities: Seeker, Volunteer, Admin. Processes: 1.0 Manage Accounts, 2.0 Post Request, 3.0 Match Volunteer, 4.0 Manage Assignment, 5.0 Rate Volunteer, 6.0 Notify Users. Data stores: D1 users, D2 volunteer_profiles, D3 help_requests, D4 ratings, D5 notifications. Show labelled data flows.
>
> Keep all diagrams visually consistent, uncluttered, and fully labelled. Do not invent features that are not listed.

---

## 4. Per-diagram prompts (if your generator handles one at a time)

### D1 — Layered Architecture
> Draw a minimalist layered architecture diagram, portrait 16:9, for CareConn (Flask + SQLite). Five stacked horizontal rounded rectangles, top to bottom: Presentation Layer (Flask blueprints + Jinja templates: auth_routes, request_routes, volunteer_routes, admin_routes, learn_routes, arch_routes); Application/Service Layer (AuthService, RequestService, MatchingService); Domain Layer (User, VolunteerProfile, HelpRequest, Rating, Notification); Data Access Layer (UserRepo, RequestRepo, VolunteerRepo, RatingRepo, NotificationRepo); Database (SQLite community_care.db). Downward arrows labelled "depends on". Side note: "Upper layers depend only on lower layers." Palette navy #1F3864, indigo #4F46E5, light fill #EEF1F6, white background, Inter font, fully labelled, no decoration.

### D2 — Strategy Pattern UML
> Draw a UML class diagram of the Strategy design pattern for CareConn. Abstract class `MatchingStrategy` with method `+ match(request, volunteers)`. Four subclasses with inheritance arrows to it: `NearestStrategy`, `SkillMatchStrategy`, `AvailabilityStrategy`, `BalancedStrategy`, each with `+ match(request, volunteers)`. `MatchingService` has `- strategy: MatchingStrategy`, `- strategy_name: str`, `+ set_strategy(name)`, `+ find(request)`, with a composition arrow labelled "delegates to" pointing to `MatchingStrategy`. Add the note "Selected at runtime from the UI." Minimal UML boxes, compartment lines, navy/indigo palette, white background.

### D3 — ERD
> Draw a clean crow's-foot ERD, portrait, for CareConn. Entities and attributes exactly: users(id PK, name, email, password_hash, role, location, created_at); volunteer_profiles(user_id PK/FK, skills, availability, radius_km, rating_avg, rating_count); help_requests(id PK, seeker_id FK, title, description, category, urgency, location, status, assigned_volunteer_id FK, created_at); ratings(id PK, request_id FK, volunteer_id FK, seeker_id FK, score, comment, created_at); notifications(id PK, user_id FK, message, read, created_at). Relationships: users 1—1 volunteer_profiles; users 1—N help_requests (seeker); users 1—N help_requests (assigned volunteer); help_requests 1—N ratings; users 1—N notifications. Clearly mark PK/FK and cardinalities. Minimal, white background, navy headers.

### D4 — Use Case
> Draw a clean UML use case diagram for CareConn. System boundary rectangle labelled "CareConn". Actors: Seeker, Volunteer, Admin. Seeker use cases: Register/Login, Post Help Request, View Request Status, Rate Volunteer. Volunteer: Register/Login, Browse Open Requests, Accept Request, Start Work, Mark Complete, Edit Profile. Admin: Login, View Users, View Requests, Monitor Activity. Use stick figures, ovals, solid association lines. Keep it uncluttered and fully labelled.

### D5 — Sequence: Post & Match
> Draw a UML sequence diagram for "Post Request and Match". Lifelines left to right: Seeker, request_routes, RequestService, RequestRepo, SQLite, MatchingService, MatchingStrategy, VolunteerRepo. Messages in order: Seeker → request_routes: submit request form; request_routes → RequestService: create(...); RequestService → RequestRepo: create(...); RequestRepo → SQLite: INSERT; SQLite --> RequestRepo: request; RequestRepo --> RequestService: request; RequestService --> request_routes: request; request_routes → MatchingService: find(request); MatchingService → MatchingStrategy: match(request, volunteers); MatchingStrategy → VolunteerRepo: all_with_profiles(); VolunteerRepo → SQLite: SELECT; SQLite --> VolunteerRepo: volunteers; VolunteerRepo --> MatchingStrategy: volunteers; MatchingStrategy --> MatchingService: suggested volunteer; MatchingService --> request_routes: suggestion; request_routes --> Seeker: render detail page. Dashed return arrows. Fully labelled.

### D6 — Sequence: Accept, Complete & Rate
> Draw a UML sequence diagram "Accept, Complete and Rate". Lifelines: Volunteer, request_routes, RequestService, RequestRepo, NotificationRepo, SQLite, Seeker, RatingRepo, VolunteerRepo. Messages: Volunteer → route: accept request; route → RequestService: accept(...); RequestService → RequestRepo: update_status(assigned, volunteer_id); RequestRepo → SQLite: UPDATE; RequestService → NotificationRepo: create(seeker, "..."); RequestService → NotificationRepo: create(volunteer, "..."); Volunteer → route: start; route → RequestService: start(...); RequestService → RequestRepo: update_status(in_progress); Volunteer → route: complete; route → RequestService: complete(...); RequestService → RequestRepo: update_status(completed); RequestService → NotificationRepo: create(seeker, "Please rate"); Seeker → route: rate(score, comment); route → RequestService: rate(...); RequestService → RatingRepo: create(...); RatingRepo → SQLite: INSERT; RequestService → VolunteerRepo: update_rating(...); VolunteerRepo → SQLite: UPDATE; RequestService → NotificationRepo: create(volunteer, "You received a rating"). Dashed returns.

### D7 — State Diagram
> Draw a minimalist UML state machine for a CareConn help request. States in a horizontal flow: OPEN → ASSIGNED → IN_PROGRESS → COMPLETED, then a self-loop on COMPLETED labelled "seeker rates volunteer". Transition labels: "volunteer accepts" (OPEN→ASSIGNED), "volunteer starts work" (ASSIGNED→IN_PROGRESS), "volunteer marks complete" (IN_PROGRESS→COMPLETED). Black initial dot before OPEN; final ring after COMPLETED. Clean, labelled, navy/indigo palette.

### D8 — Deployment
> Draw a UML deployment diagram for CareConn. Three nodes: "User Browser" containing "HTML/CSS/JS · Basecoat UI"; "Flask Application Server" containing "Python 3 · Flask · Blueprints · Services · Strategies"; "SQLite Database" containing "community_care.db". Connect Browser → Flask with "HTTPS/HTTP", Flask → SQLite with "SQLAlchemy". Use 3D or plain node boxes, minimal, fully labelled.

### D9 — Component
> Draw a UML component diagram for CareConn. Components grouped in four bands: Presentation (auth_routes, request_routes, volunteer_routes, admin_routes, learn_routes, arch_routes); Services (AuthService, RequestService, MatchingService); Domain (User, VolunteerProfile, HelpRequest, Rating, Notification); Data (UserRepo, RequestRepo, VolunteerRepo, RatingRepo, NotificationRepo); Strategies (MatchingStrategy, NearestStrategy, SkillMatchStrategy, AvailabilityStrategy, BalancedStrategy); one Database node (SQLite). Show only downward dependency arrows from Presentation to Services to Domain/Data to Database. Minimal, labelled.

### D10 — UI Wireframes
> Draw three low-fidelity wireframes side by side in one image, monochrome with navy labels. (a) Seeker Dashboard: floating pill nav, "My Requests" heading, "+ New Help Request" button on the right, list of request cards with status badges and View buttons. (b) Volunteer Dashboard: "My Assignments" section first, then "Open Requests" cards with Accept and Details buttons, then a "Matching Strategy" selector card. (c) Admin Dashboard: three summary tiles (Users, Requests, Open), a Users table, a Requests table. Clean rectangles, placeholder text lines, no colour except navy/indigo.

### D11 — DFD Level 1
> Draw a level-1 data flow diagram for CareConn. External entities: Seeker, Volunteer, Admin. Processes: 1.0 Manage Accounts, 2.0 Post Request, 3.0 Match Volunteer, 4.0 Manage Assignment, 5.0 Rate Volunteer, 6.0 Notify Users. Data stores: D1 users, D2 volunteer_profiles, D3 help_requests, D4 ratings, D5 notifications. Show labelled data flows between entities, processes, and stores. Use circles for processes, open rectangles for stores, rectangles for entities. Minimal, fully labelled.

---

## 5. Accuracy anchors (paste into any prompt if the generator drifts)

- Architecture: **Layered** (not MVC, not microservices).
- Pattern: **Strategy** (not Factory, not Observer).
- Stack: **Python 3 · Flask · SQLAlchemy · SQLite · Jinja2 · HTML/CSS/JS · Basecoat UI**.
- Statuses: `open`, `assigned`, `in_progress`, `completed`.
- Roles: `seeker`, `volunteer`, `admin`.
- Entities: `users`, `volunteer_profiles`, `help_requests`, `ratings`, `notifications`.
- Strategy classes: `MatchingStrategy`, `NearestStrategy`, `SkillMatchStrategy`, `AvailabilityStrategy`, `BalancedStrategy`.
- Service: `MatchingService.set_strategy(name)`, `MatchingService.find(request)`.
- Do not invent payments, chat, GPS, or mobile apps — they are out of scope.
