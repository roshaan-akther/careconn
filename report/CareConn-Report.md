# CareConn

## A Community Help Platform

### Continuous Assessment 05

**Module:** System Development Using Software Architecture and Design Patterns

**Module Code:** [Module Code]

**Group Members:**

| Name | Registration Number |
|---|---|
| Roshaan | [Registration Number] |
| Wasit | [Registration Number] |
| Nuha | [Registration Number] |
| Masheef | [Registration Number] |
| Chamudi | [Registration Number] |
| Fahmidha | [Registration Number] |

**Submission Date:** 09 November 2026

**Institution:** [Institution Name]

---

## Table of Contents

[To be generated in Word]

---

## List of Figures

[To be generated in Word]

---

## List of Tables

[To be generated in Word]

---

## Abstract

CareConn is a web-based community help platform that connects people who need everyday assistance with volunteers in their local area. The system allows a seeker to post a help request, allows volunteers to browse and accept requests, and tracks each request from creation to completion and rating. CareConn is built with Python, Flask, SQLAlchemy, SQLite, Jinja2, HTML, CSS and JavaScript, and uses Basecoat UI for the interface. The system applies the Layered Architecture style and the Strategy design pattern. The layered structure separates presentation, application, domain and data access concerns, while the Strategy pattern allows the volunteer matching algorithm to be selected and changed at runtime. The system was tested with automated unit and integration tests and with manual user flows. All implemented tests passed, and the main functions of the system work correctly.

---

# 1. Introduction

## 1.1 Background

Communities contain people who need small amounts of help from time to time. An elderly person may need groceries. A person with limited mobility may need a tap repaired. A student may need help completing an online form. These needs are often simple, but they can be difficult to solve alone.

At the same time, many people are willing to help. The barrier is not willingness. The barrier is coordination. Volunteers do not know who needs help, where the need is, or how urgent it is.

CareConn is a web platform that solves this coordination problem. It provides one place where help requests can be posted and where volunteers can find and accept them.

## 1.2 Purpose

The purpose of CareConn is to make asking for help normal, simple and safe. The system is designed for people who are not confident with technology, so the interface uses plain language, large controls and a small number of steps.

## 1.3 Overview of the System

CareConn supports three roles:

- **Seeker:** a person who needs help. A seeker posts requests, tracks their status and rates the volunteer after completion.
- **Volunteer:** a person who offers help. A volunteer sets skills and availability, browses open requests, accepts a request and updates its status.
- **Admin:** a person who oversees the platform. An admin views users and requests and monitors activity.

The main request lifecycle is:

`open → assigned → in_progress → completed`

After completion, the seeker can rate the volunteer from one to five.

---

# 2. Problem Statement

## 2.1 The Problem

People who need everyday help often do not have an easy way to ask for it. Existing methods such as phone calls, notice boards and social media posts are informal, unstructured and difficult to track. Requests get lost, volunteers do not know who needs help, and there is no record of what was completed.

Volunteers face the opposite problem. They are willing to help, but they do not know where the need is, whether it is nearby, or whether their skills match the request.

## 2.2 Justification

A dedicated platform is justified because it provides structure for a process that is currently ad hoc. CareConn gives seekers a clear way to ask, gives volunteers a clear way to respond, and gives the community a record of completed help. The system also introduces accountability through ratings and admin oversight.

The problem is real, common and human. It is not a technical problem created for the assignment. It is a problem that exists in most neighbourhoods, and a simple web application can reduce it.

---

# 3. Objectives and Scope

## 3.1 Objectives

The objectives of CareConn are:

1. To allow seekers to create help requests with a category, urgency level and location.
2. To allow volunteers to register their skills and availability.
3. To match volunteers to requests using a selectable strategy.
4. To allow volunteers to accept, start and complete requests.
5. To allow seekers to rate volunteers after completion.
6. To notify users when important events occur.
7. To provide admin oversight of users and requests.
8. To provide a simple, accessible interface for non-technical users.
9. To apply Layered Architecture in the system structure.
10. To apply the Strategy design pattern in the matching function.

## 3.2 Intended Users

- **Seekers:** elderly people, people with disabilities, people living alone, and any person who needs short-term help.
- **Volunteers:** community members who can offer time, skills or transport.
- **Admins:** community organisers or platform managers.

## 3.3 Scope

The scope of the system includes:

- User registration and login.
- Role-based access for seeker, volunteer and admin.
- Help request creation and listing.
- Volunteer matching with four strategies.
- Request status management.
- Ratings and notifications.
- Admin viewing of users and requests.
- A public learning page and an architecture page for demonstration.

## 3.4 Out of Scope

The following are outside the scope of this project:

- Online payments or donations.
- Real-time chat or messaging.
- GPS tracking or live location.
- Native mobile applications.
- Email or SMS notifications.
- Automated identity verification.

---

# 4. System Requirements

## 4.1 Functional Requirements

| ID | Requirement |
|---|---|
| FR1 | The system shall allow a user to register as a seeker or volunteer. |
| FR2 | The system shall allow a registered user to log in and log out. |
| FR3 | The system shall restrict actions based on the user role. |
| FR4 | The system shall allow a seeker to create a help request with title, description, category, urgency and location. |
| FR5 | The system shall list open help requests. |
| FR6 | The system shall recommend a volunteer using a matching strategy. |
| FR7 | The system shall allow a volunteer to accept an open request. |
| FR8 | The system shall allow the assigned volunteer to start and complete a request. |
| FR9 | The system shall allow a seeker to rate a volunteer after completion. |
| FR10 | The system shall notify users when a request is accepted, completed or rated. |
| FR11 | The system shall allow an admin to view all users and all requests. |
| FR12 | The system shall allow the matching strategy to be changed at runtime. |
| FR13 | The system shall provide a public page explaining how CareConn works. |
| FR14 | The system shall provide a page that displays the implemented architecture and design pattern. |

## 4.2 Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR1 | Usability: the interface shall use plain language, clear labels and large touch-friendly controls. |
| NFR2 | Security: passwords shall be stored using hashing, and access shall be role-based. |
| NFR3 | Performance: the request list shall load within two seconds for a normal dataset. |
| NFR4 | Reliability: the SQLite database shall be stored in a single file that can be backed up easily. |
| NFR5 | Maintainability: the code shall follow a layered structure with clear separation of concerns. |
| NFR6 | Portability: the system shall run on any machine with Python and the required packages. |
| NFR7 | Accessibility: the interface shall be responsive and usable on mobile and desktop screens. |
| NFR8 | Consistency: the interface shall use one visual style across all pages. |

## 4.3 Assumptions and Constraints

- Users have access to a modern web browser.
- The system runs on a local Flask development server for the demonstration.
- SQLite is sufficient for the expected demonstration workload.
- The matching distance is simplified to a location comparison and does not use real geographic coordinates.

---

# 5. Selected Software Architecture

## 5.1 Chosen Architecture

The selected architecture is **Layered Architecture**.

This is one of the most common and widely adopted architectural patterns in the software industry. The specific flow used in CareConn is:

`Presentation → Service → Domain → Data Access → SQLite`

This flow closely mirrors Domain-Driven Design and clean architecture principles.

## 5.2 Description of the Layers

### 5.2.1 Presentation Layer

The presentation layer contains the Flask blueprints and the Jinja2 templates. It handles HTTP requests, reads form data, calls the service layer and renders the response. It does not contain business rules or direct database queries.

Main modules:

- `auth_routes.py`
- `request_routes.py`
- `volunteer_routes.py`
- `admin_routes.py`
- `learn_routes.py`
- `arch_routes.py`

### 5.2.2 Application and Service Layer

The service layer contains the use cases of the system. It coordinates repositories, applies business rules and triggers notifications.

Main classes:

- `AuthService`
- `RequestService`
- `MatchingService`

### 5.2.3 Domain Layer

The domain layer contains the core entities and their relationships. It does not depend on Flask or on the database layer.

Main entities:

- `User`
- `VolunteerProfile`
- `HelpRequest`
- `Rating`
- `Notification`

### 5.2.4 Data Access Layer

The data access layer contains repositories that read and write data. It hides SQLAlchemy queries from the service layer.

Main classes:

- `UserRepo`
- `RequestRepo`
- `VolunteerRepo`
- `RatingRepo`
- `NotificationRepo`

### 5.2.5 Database Layer

The database layer is a single SQLite file named `community_care.db`. It stores all persistent data for the system.

## 5.3 Justification

Layered Architecture was selected for the following reasons:

1. **Separation of concerns.** Each layer has one responsibility, so the code is easier to understand and maintain.
2. **Testability.** Business rules can be tested without the user interface, and strategies can be tested without a database.
3. **Replaceability.** The database can be replaced without changing the presentation or service layers, because all database access is isolated in repositories.
4. **Teamwork.** Each group member can work on a different layer with minimal conflict.
5. **Clarity for demonstration.** The layers are easy to explain and easy to show in a presentation.
6. **Industry relevance.** Layered Architecture is widely used in enterprise applications, so the design is realistic.

## 5.4 Dependency Rule

The dependency rule is simple: upper layers may depend on lower layers, but lower layers must not depend on upper layers. The domain layer has no dependency on Flask, on SQLAlchemy or on the user interface. The data access layer depends on the domain layer. The service layer depends on the domain and data access layers. The presentation layer depends on the service layer.

[add-image-01-layered-architecture.png]

*Figure 5.1: Layered architecture of CareConn.*

## 5.5 Practical Application

The architecture is not only documented. It is implemented in the folder structure of the project:

```text
app/
  presentation/     # routes and templates
  services/         # business logic
  domain/           # entities
  data/             # repositories and seed data
  strategies/       # matching strategies
```

Each request follows the same path. For example, when a seeker posts a request, the presentation layer receives the form, the service layer creates the request, the repository writes it to SQLite, and the matching service selects a volunteer.

## 5.6 Trade-offs

Layered Architecture can introduce extra code for simple operations, because a request passes through several layers. For a small system, this can feel indirect. However, the benefit is a clean structure that is easy to test and easy to extend. The trade-off is acceptable for this project.

---

# 6. Selected Design Pattern

## 6.1 Chosen Pattern

The selected design pattern is the **Strategy Pattern**.

The Strategy Pattern is a classic Gang of Four (GoF) behavioral design pattern. It is the industry-standard solution for scenarios where algorithms or behaviors must be swapped at runtime.

## 6.2 Problem Solved

CareConn needs to recommend a volunteer for a help request. There is no single correct way to do this. In some cases the nearest volunteer is best. In other cases the volunteer with the right skills is best. In other cases availability is the most important factor.

If all of these rules were written inside one method with many `if` statements, the code would become difficult to read, difficult to test and difficult to extend.

The Strategy Pattern solves this by moving each matching algorithm into its own class. The `MatchingService` holds a reference to a strategy and delegates the matching work to it. The strategy can be changed at runtime without changing the service.

## 6.3 Structure

Participants in the pattern:

- **Context:** `MatchingService`
- **Strategy interface:** `MatchingStrategy`
- **Concrete strategies:**
  - `NearestStrategy`
  - `SkillMatchStrategy`
  - `AvailabilityStrategy`
  - `BalancedStrategy`

`MatchingService` provides two methods:

- `set_strategy(name)`: selects and creates a concrete strategy.
- `find(request)`: delegates to the current strategy.

Each concrete strategy implements:

- `match(request, volunteers)`: returns the best volunteer or `None`.

## 6.4 Justification

The Strategy Pattern was selected for the following reasons:

1. It directly matches a real variation in the problem, because matching can reasonably be done in different ways.
2. It follows the Open/Closed Principle. A new strategy can be added without modifying existing strategy classes.
3. It makes each algorithm small, focused and independently testable.
4. It makes the pattern visible in the user interface, because the volunteer can change the strategy from the dashboard.
5. It is easy to demonstrate during the presentation.

## 6.5 Implementation

The interface is defined as an abstract class:

```python
from abc import ABC, abstractmethod

class MatchingStrategy(ABC):
    @abstractmethod
    def match(self, request, volunteers):
        pass
```

A concrete strategy implements the interface:

```python
class SkillMatchStrategy(MatchingStrategy):
    def match(self, request, volunteers):
        if not volunteers:
            return None
        category = (request.category or "").lower()

        def score(pair):
            skills = [s.strip().lower() for s in (pair[1].skills or "").split(",")]
            return (0 if category in skills else 1, -pair[1].rating_avg)

        return sorted(volunteers, key=score)[0]
```

The context delegates to the selected strategy:

```python
class MatchingService:
    def __init__(self, strategy_name="balanced"):
        self.set_strategy(strategy_name)

    def set_strategy(self, name):
        cls = STRATEGIES.get(name, BalancedStrategy)
        self.strategy = cls()
        self.strategy_name = name

    def find(self, request):
        volunteers = VolunteerRepo.all_with_profiles()
        return self.strategy.match(request, volunteers)
```

The available strategies are registered in a dictionary:

```python
STRATEGIES = {
    "nearest": NearestStrategy,
    "skill": SkillMatchStrategy,
    "availability": AvailabilityStrategy,
    "balanced": BalancedStrategy,
}
```

## 6.6 Runtime Behaviour

The volunteer dashboard contains a matching strategy selector. When the volunteer changes the strategy and submits the form, the `set_strategy` method updates the active strategy. The next time a request is viewed, the new strategy is used. This demonstrates the pattern in action and shows that the algorithm is truly interchangeable.

[add-image-02-strategy-pattern-uml.png]

*Figure 6.1: UML class diagram of the Strategy pattern in CareConn.*

## 6.7 Trade-offs

The Strategy Pattern adds more classes than a single method with conditional logic. For four strategies, the extra structure is justified because each strategy has a clear purpose and can be tested separately. The pattern also makes the code easier to extend if more strategies are added later.

---

# 7. System Design

## 7.1 Design Overview

The system is designed around the request lifecycle. A seeker creates a request. The system recommends a volunteer. A volunteer accepts the request. The volunteer starts and completes the work. The seeker rates the volunteer. Notifications are created at the important steps.

## 7.2 Use Case Design

The main actors are Seeker, Volunteer and Admin.

Seeker use cases:

- Register and login.
- Post a help request.
- View request status.
- Rate a volunteer.

Volunteer use cases:

- Register and login.
- Browse open requests.
- Accept a request.
- Start work.
- Mark a request complete.
- Edit profile.

Admin use cases:

- Login.
- View users.
- View requests.
- Monitor activity.

[add-image-04-use-case.png]

*Figure 7.1: Use case diagram.*

## 7.3 Database Design

The database contains five tables.

### 7.3.1 users

Stores all accounts.

| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| name | String | User name |
| email | String | Unique |
| password_hash | String | Hashed password |
| role | String | seeker, volunteer or admin |
| location | String | User location |
| created_at | DateTime | Creation time |

### 7.3.2 volunteer_profiles

Stores volunteer-specific data.

| Column | Type | Notes |
|---|---|---|
| user_id | Integer | Primary key and foreign key to users |
| skills | String | Comma separated skills |
| availability | String | Availability description |
| radius_km | Integer | Service radius |
| rating_avg | Float | Average rating |
| rating_count | Integer | Number of ratings |

### 7.3.3 help_requests

Stores help requests.

| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| seeker_id | Integer | Foreign key to users |
| title | String | Request title |
| description | Text | Request details |
| category | String | Request category |
| urgency | String | low, normal or high |
| location | String | Request location |
| status | String | open, assigned, in_progress or completed |
| assigned_volunteer_id | Integer | Foreign key to users |
| created_at | DateTime | Creation time |

### 7.3.4 ratings

Stores ratings after completion.

| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| request_id | Integer | Foreign key to help_requests |
| volunteer_id | Integer | Foreign key to users |
| seeker_id | Integer | Foreign key to users |
| score | Integer | 1 to 5 |
| comment | Text | Optional comment |
| created_at | DateTime | Creation time |

### 7.3.5 notifications

Stores in-app notifications.

| Column | Type | Notes |
|---|---|---|
| id | Integer | Primary key |
| user_id | Integer | Foreign key to users |
| message | String | Notification text |
| read | Boolean | Read status |
| created_at | DateTime | Creation time |

[add-image-03-erd.png]

*Figure 7.2: Entity relationship diagram.*

## 7.4 Sequence Design: Post Request and Match

When a seeker submits a request, the presentation layer calls `RequestService.create`. The service calls `RequestRepo.create`, which writes the request to SQLite. The service then calls `MatchingService.find`, which delegates to the active strategy. The strategy reads volunteers through `VolunteerRepo` and returns the best match. The route then renders the request detail page with the suggestion.

[add-image-05-sequence-post-match.png]

*Figure 7.3: Sequence diagram for posting a request and matching a volunteer.*

## 7.5 Sequence Design: Accept, Complete and Rate

When a volunteer accepts a request, the service updates the status to `assigned`, stores the volunteer ID and creates notifications. When the volunteer starts work, the status becomes `in_progress`. When the volunteer marks it complete, the status becomes `completed` and the seeker is notified. When the seeker rates the volunteer, a rating is stored, the volunteer average is updated and the volunteer is notified.

[add-image-06-sequence-accept-complete-rate.png]

*Figure 7.4: Sequence diagram for accept, complete and rate.*

## 7.6 State Design

A request moves through four states. It starts as `open`. It becomes `assigned` when a volunteer accepts. It becomes `in_progress` when the volunteer starts work. It becomes `completed` when the volunteer marks it complete. A completed request can receive a rating, which is recorded without changing the status.

[add-image-07-state-lifecycle.png]

*Figure 7.5: State diagram of the request lifecycle.*

## 7.7 Component Design

The component diagram shows the main modules and their dependencies. Presentation components depend on service components. Service components depend on domain and data components. Data components depend on the domain and the database. Strategies are used by the matching service.

[add-image-08-component-diagram.png]

*Figure 7.6: Component diagram.*

## 7.8 Data Flow Design

The level-1 data flow diagram shows how data moves between external entities, processes and data stores. Seekers, volunteers and admins interact with account, request, matching, assignment, rating and notification processes. The processes read and write the users, volunteer_profiles, help_requests, ratings and notifications stores.

[add-image-09-dfd-level-1.png]

*Figure 7.7: Level-1 data flow diagram.*

## 7.9 Deployment Design

CareConn is deployed as a Flask application. The user accesses the system through a browser. The browser sends HTTP requests to the Flask server. The server uses SQLAlchemy to read and write the SQLite database file.

[add-image-10-deployment.png]

*Figure 7.8: Deployment diagram.*

## 7.10 User Interface Design

The interface uses a floating pill navigation bar, rounded cards, clear headings and large controls. The design is intentionally simple so that non-technical users can complete tasks quickly.

Design principles:

- One primary action per screen.
- Plain language instead of technical terms.
- Status badges with readable labels.
- Role-specific dashboards.
- Responsive layout for mobile and desktop.
- Consistent colours and spacing.

Wireframes:

[add-image-11-wireframe-admin-dashboard.jpeg]

*Figure 7.9: Admin dashboard wireframe.*

[add-image-12-wireframe-volunteer-dashboard.jpeg]

*Figure 7.10: Volunteer dashboard wireframe.*

[add-image-13-wireframe-seeker-dashboard.jpeg]

*Figure 7.11: Seeker dashboard wireframe.*

---

# 8. System Implementation

## 8.1 Technology Stack

| Layer | Technology |
|---|---|
| Programming language | Python 3 |
| Web framework | Flask |
| Database | SQLite |
| ORM | Flask-SQLAlchemy |
| Authentication | Flask-Login |
| Forms and validation | Flask-WTF and WTForms |
| Templating | Jinja2 |
| Frontend | HTML, CSS, JavaScript |
| UI components | Basecoat UI |
| Icons | Lucide |
| Testing | pytest and pytest-flask |
| Version control | Git |

## 8.2 Project Structure

```text
community_care/
├── app/
│   ├── __init__.py
│   ├── presentation/
│   │   ├── auth_routes.py
│   │   ├── request_routes.py
│   │   ├── volunteer_routes.py
│   │   ├── admin_routes.py
│   │   ├── learn_routes.py
│   │   ├── arch_routes.py
│   │   ├── templates/
│   │   └── static/
│   ├── services/
│   │   └── services.py
│   ├── domain/
│   │   └── models.py
│   ├── data/
│   │   ├── repositories.py
│   │   └── seed.py
│   └── strategies/
│       └── matching_strategy.py
├── tests/
├── config.py
├── run.py
└── requirements.txt
```

## 8.3 Implementation of the Layered Architecture

The folder structure directly reflects the layers. Routes do not query the database directly. They call services. Services call repositories. Repositories use SQLAlchemy models. This keeps each layer focused and makes the code easier to test.

For example, the request route does not contain SQL. It calls `RequestService.create`. The service calls `RequestRepo.create`. The repository performs the database operation.

## 8.4 Implementation of the Strategy Pattern

The strategy pattern is implemented in `app/strategies/matching_strategy.py`. The abstract class defines the contract. Each concrete strategy implements the contract. `MatchingService` selects a strategy from the `STRATEGIES` dictionary. The active strategy is stored in memory for the running application.

The volunteer dashboard exposes the strategy choice to the user. This makes the pattern visible and demonstrable.

## 8.5 Key Modules

### 8.5.1 Authentication

`AuthService` handles registration and login. Passwords are hashed with Werkzeug. `Flask-Login` manages the user session. Role checks are performed in routes before sensitive actions.

### 8.5.2 Requests

`RequestService` handles creation, acceptance, start, completion and rating. Each action updates the status and creates the relevant notifications.

### 8.5.3 Matching

`MatchingService` delegates to the active `MatchingStrategy`. The strategies are:

- `NearestStrategy`: prefers volunteers in the same location.
- `SkillMatchStrategy`: prefers volunteers whose skills match the request category.
- `AvailabilityStrategy`: prefers volunteers with the broadest availability.
- `BalancedStrategy`: combines location, skills, availability and rating.

### 8.5.4 Repositories

Repositories isolate database access. `UserRepo` handles users and volunteer profiles. `RequestRepo` handles requests. `RatingRepo` handles ratings. `NotificationRepo` handles notifications.

### 8.5.5 Admin

The admin dashboard shows summary counts, a users table and a requests table. Admin access is restricted to users with the admin role.

## 8.6 Database Setup and Seed Data

The database is created automatically when the application starts. The seed module inserts demo data if the database is empty. The seed data includes one admin, four seekers, five volunteers and five help requests across Sri Lankan locations such as Colombo, Gampaha, Kandy, Galle and Jaffna.

Demo accounts:

| Role | Email | Password |
|---|---|---|
| Admin | admin@care.com | admin123 |
| Seeker | nimal@care.com | pass123 |
| Volunteer | rohan@care.com | pass123 |

## 8.7 Running the System

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

The application runs at `http://127.0.0.1:5000`.

## 8.8 Design Decisions

- SQLite was chosen because it requires no separate server and is easy to demonstrate.
- Server-rendered templates were chosen because they are simple, fast and easy to understand.
- The matching distance is simplified to a same-location comparison. This keeps the demonstration predictable and avoids external map services.
- The admin role is view-only in this version. Managing users and requests is listed as future work.

---

# 9. System Demonstration

This section shows the main screens and explains how each one supports the user.

## 9.1 Login

The login page provides email and password fields and three demo buttons for quick access. The demo buttons fill the form and submit it, which makes the presentation faster.

[add-image-14-screenshot-login.png]

*Figure 9.1: Login page.*

## 9.2 Registration

A new user registers with a name, email, password, role and location. The role determines the dashboard and the actions available after login.

[add-image-19-screenshot-register.png]

*Figure 9.2: Registration page.*

## 9.3 Seeker Dashboard

The seeker dashboard lists the seeker's requests and provides a clear "New Help Request" button on the right. Each request shows its status and a View button.

[add-image-15-screenshot-seeker-dashboard.png]

*Figure 9.3: Seeker dashboard.*

## 9.4 New Help Request

The request form collects the title, description, category, urgency and location. The category list matches the seeded data categories so that all request types can be created.

[add-image-16-screenshot-new-request.png]

*Figure 9.4: New help request form.*

## 9.5 Requests List

The open requests page shows all requests that are waiting for a volunteer. Each card shows the category, urgency and location.

[add-image-20-screenshot-requests-list.png]

*Figure 9.5: Open requests list.*

## 9.6 Request Detail and Matching

The request detail page shows the full request, its status and the assigned volunteer if one exists. When the request is open, the system shows a recommended volunteer and makes clear that the recommendation is only a suggestion.

[add-image-21-screenshot-request-detail.png]

*Figure 9.6: Request detail page with recommendation.*

## 9.7 Volunteer Dashboard

The volunteer dashboard shows the volunteer's assignments first, then the open requests. Each open request has Accept and Details buttons. The matching strategy selector is shown at the bottom.

[add-image-17-screenshot-volunteer-dashboard.png]

*Figure 9.7: Volunteer dashboard.*

## 9.8 Start and Complete

After accepting a request, the volunteer can start work and then mark the request complete. The status badge updates at each step.

## 9.9 Rating

After completion, the seeker sees a rating form with a score from one to five and an optional comment. Submitting the form stores the rating and updates the volunteer average.

[add-image-22-screenshot-rating.png]

*Figure 9.8: Rating form.*

## 9.10 Volunteer Profile

The volunteer profile page allows the volunteer to update skills, availability and service radius. The page also shows the average rating.

[add-image-23-screenshot-volunteer-profile.png]

*Figure 9.9: Volunteer profile page.*

## 9.11 Notifications

The notifications page lists in-app notifications. Unread notifications are highlighted, and opening the page marks them as read.

[add-image-24-screenshot-notifications.png]

*Figure 9.10: Notifications page.*

## 9.12 Admin Dashboard

The admin dashboard shows summary counts for users, requests and open requests. It also shows a users table and a requests table with status badges and links to request details.

[add-image-18-screenshot-admin-dashboard.png]

*Figure 9.11: Admin dashboard.*

[add-image-28-screenshot-admin-requests.png]

*Figure 9.12: Admin requests table.*

## 9.13 Architecture Page

The architecture page displays the implemented layers and the real class and function names extracted from the source code. It also shows the Strategy pattern structure. This page supports the presentation and demonstrates that the architecture is implemented, not only documented.

[add-image-25-screenshot-architecture-page.png]

*Figure 9.13: Architecture page.*

## 9.14 Learn Page

The learn page explains CareConn in plain language. It covers why the platform exists, who it is for, how it works and common questions. It is available without login.

[add-image-26-screenshot-learn-page.png]

*Figure 9.14: Learn page.*

---

# 10. Testing

## 10.1 Testing Approach

Testing was carried out at three levels:

1. **Unit testing:** individual strategies and small logic units.
2. **Integration testing:** Flask routes, authentication and request flows.
3. **Manual testing:** full user flows in the browser.

The automated tests use pytest. The test application uses an in-memory SQLite database so that tests do not affect the development database.

## 10.2 Automated Tests

The test suite covers:

- Strategy selection for nearest, skill, availability and balanced strategies.
- Empty volunteer lists.
- User registration and login.
- Request creation.
- Admin access control.

Command:

```bash
pytest -v
```

Result:

```text
8 passed
```

[add-image-27-pytest-results.png]

*Figure 10.1: Automated test results.*

## 10.3 Test Cases

| ID | Scenario | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T1 | Register seeker | Valid name, email and password | Account created and redirected to login | Account created | Pass |
| T2 | Login with invalid password | Valid email and wrong password | Error message shown | Error message shown | Pass |
| T3 | Create help request | Valid title, description, category, urgency and location | Request saved with status open | Request saved as open | Pass |
| T4 | Nearest strategy | Two volunteers in different locations | Same-location volunteer selected | Correct volunteer selected | Pass |
| T5 | Skill match strategy | Request category matches a volunteer skill | Volunteer with matching skill selected | Correct volunteer selected | Pass |
| T6 | Availability strategy | Volunteers with different availability | Volunteer with broadest availability selected | Correct volunteer selected | Pass |
| T7 | Balanced strategy | Mixed volunteer data | A valid volunteer is returned | Valid volunteer returned | Pass |
| T8 | Empty volunteer list | No volunteers | No match returned | None returned | Pass |
| T9 | Accept request | Volunteer accepts an open request | Status becomes assigned | Status changed to assigned | Pass |
| T10 | Start request | Assigned volunteer starts work | Status becomes in_progress | Status changed to in_progress | Pass |
| T11 | Complete request | Volunteer marks request complete | Status becomes completed | Status changed to completed | Pass |
| T12 | Rate volunteer | Seeker submits score and comment | Rating stored and volunteer average updated | Rating stored and average updated | Pass |
| T13 | Admin access control | Non-admin opens admin URL | Access denied | Access denied | Pass |
| T14 | Mobile layout | Page viewed at 375 px width | Layout remains usable | Layout usable | Pass |

## 10.4 Manual Testing

The following flows were tested manually in the browser:

- Register as a seeker and post a request.
- Register as a volunteer and accept a request.
- Start and complete a request.
- Rate a volunteer as the seeker.
- Change the matching strategy.
- Open the admin dashboard as an admin.
- Open the learn page without logging in.

All flows completed without errors.

The automated suite contains eight tests. Test cases T9 to T14 were verified through integration scripts and manual browser testing. The results in Table 10.1 reflect the combined automated and manual testing.

## 10.5 Testing Limitations

- The automated tests cover the main flows but do not provide full code coverage.
- The distance calculation is a simplified location comparison and is not tested against real geographic data.
- Browser testing was performed on one desktop browser and one mobile viewport.

---

# 11. Conclusion and Future Improvements

## 11.1 Summary

CareConn is a working community help platform that connects seekers with volunteers. The system supports registration, login, request creation, volunteer matching, acceptance, status tracking, completion, rating, notifications and admin oversight.

The system applies Layered Architecture in its folder structure and code dependencies. It applies the Strategy design pattern in the volunteer matching function, with four interchangeable strategies and a runtime selector. Both the architecture and the pattern are implemented in working code and are visible in the application.

## 11.2 Achievements Against Objectives

All main objectives were achieved:

- Seekers can post and track requests.
- Volunteers can register skills and accept requests.
- Matching can be changed at runtime.
- Requests move through a complete lifecycle.
- Seekers can rate volunteers.
- Notifications are created for key events.
- Admins can view users and requests.
- The interface is simple and responsive.
- The layered architecture is implemented.
- The Strategy pattern is implemented and demonstrable.

## 11.3 Limitations

- The admin role is view-only and cannot edit or delete records.
- The distance calculation is a simple location comparison, not real geographic distance.
- Notifications are in-app only. No email or SMS is sent.
- There is no chat between seekers and volunteers.
- SQLite is suitable for demonstration but not for large-scale production use.
- Automated test coverage is focused on the main flows.

## 11.4 Future Improvements

- Add real geographic distance using coordinates or a map service.
- Add email and SMS notifications.
- Add in-app messaging between seeker and volunteer.
- Add admin actions to edit, suspend or delete users and requests.
- Add request editing and cancellation for seekers.
- Add pagination and search for large request lists.
- Add database migrations for production deployment.
- Add stronger security controls such as CSRF protection and rate limiting.
- Add a mobile application for wider accessibility.
- Add reporting and analytics for community organisers.

---

# 12. References

1. Gamma, E., Helm, R., Johnson, R. and Vlissides, J. (1994) *Design Patterns: Elements of Reusable Object-Oriented Software*. Boston: Addison-Wesley.
2. Fowler, M. (2002) *Patterns of Enterprise Application Architecture*. Boston: Addison-Wesley.
3. Flask (2026) *Flask Documentation*. Available at: https://flask.palletsprojects.com/ (Accessed: 09 November 2026).
4. SQLAlchemy (2026) *SQLAlchemy Documentation*. Available at: https://docs.sqlalchemy.org/ (Accessed: 09 November 2026).
5. Python Software Foundation (2026) *Python Documentation*. Available at: https://docs.python.org/3/ (Accessed: 09 November 2026).
6. Basecoat UI (2026) *Basecoat Documentation*. Available at: https://basecoatui.com/introduction/ (Accessed: 09 November 2026).
7. MDN Web Docs (2026) *HTML, CSS and JavaScript Reference*. Available at: https://developer.mozilla.org/ (Accessed: 09 November 2026).
8. Richards, M. and Ford, N. (2020) *Fundamentals of Software Architecture*. Sebastopol: O'Reilly Media.
9. Martin, R. C. (2017) *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Boston: Prentice Hall.
10. Pallets Projects (2026) *Flask-Login Documentation*. Available at: https://flask-login.readthedocs.io/ (Accessed: 09 November 2026).

---

# Appendix A: Team Contributions

| Member | Contribution |
|---|---|
| Roshaan | Project coordination, backend architecture, request lifecycle, matching service, integration |
| Wasit | Presentation layer, seeker and volunteer routes, UI implementation |
| Nuha | Domain model and database design, repositories, seed data |
| Masheef | Strategy pattern implementation and automated testing |
| Chamudi | Admin dashboard, notifications, report diagrams and documentation |
| Fahmidha | User interface design, learn page, screenshots, presentation preparation |

---

# Appendix B: Demo Accounts

| Role | Email | Password |
|---|---|---|
| Admin | admin@care.com | admin123 |
| Seeker | nimal@care.com | pass123 |
| Seeker | kamala@care.com | pass123 |
| Volunteer | rohan@care.com | pass123 |
| Volunteer | dilani@care.com | pass123 |
