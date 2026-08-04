---
name: system-design
description: Comprehensive system design patterns - architecture, data modeling, API design, UX flows, UI specs
---

# System Design Skill

Reference patterns for comprehensive system design across all dimensions.

## When to Load This Skill

Load this skill when:

- Designing new systems or major features
- Working on architecture decisions
- Defining data models and APIs
- Specifying UX flows or UI components
- Reviewing existing designs

---

## Architecture Patterns

### Layered Architecture

```
┌─────────────────────────────┐
│      Presentation Layer     │  UI, API endpoints
├─────────────────────────────┤
│      Application Layer      │  Use cases, orchestration
├─────────────────────────────┤
│        Domain Layer         │  Business logic, entities
├─────────────────────────────┤
│     Infrastructure Layer    │  DB, external services
└─────────────────────────────┘
```

### Microservices Boundaries

- **Bounded contexts** - Each service owns its domain
- **Data ownership** - Services own their data, expose via API
- **Async communication** - Events for cross-service coordination
- **API gateway** - Single entry point, routing, auth

### Event-Driven Patterns

- **Event sourcing** - Store events, derive state
- **CQRS** - Separate read/write models
- **Saga pattern** - Distributed transactions via events
- **Outbox pattern** - Reliable event publishing

---

## Data Modeling

### Entity Design

```
Entity: [Name]
Purpose: [Why this entity exists]

Attributes:
- id: UUID (PK) - Immutable identifier
- [field]: [type] ([constraints]) - [purpose]
- created_at: timestamp - Audit trail
- updated_at: timestamp - Audit trail

Relationships:
- belongs_to [Entity] (FK: entity_id)
- has_many [Entity] (via entity_id)
- has_one [Entity] (via entity_id, unique)
- many_to_many [Entity] (via join table)

Indexes:
- [field] - [query pattern this optimizes]
- [field1, field2] - Composite for [pattern]

Constraints:
- unique([fields])
- check([condition])
```

### Relationship Patterns

| Pattern         | When to Use                               |
| --------------- | ----------------------------------------- |
| Foreign key     | Strong consistency, cascade deletes       |
| Soft reference  | Cross-service, eventual consistency       |
| Denormalization | Read performance, accept write complexity |
| Join table      | Many-to-many with metadata                |

### Migration Strategy

1. **Additive first** - Add columns, make nullable
2. **Backfill** - Populate new columns
3. **Switch** - Update code to use new schema
4. **Cleanup** - Remove old columns (separate deploy)

---

## API Design

### RESTful Conventions

```
# Collection operations
GET    /api/v1/resources          # List (paginated)
POST   /api/v1/resources          # Create
GET    /api/v1/resources/:id      # Read
PUT    /api/v1/resources/:id      # Full update
PATCH  /api/v1/resources/:id      # Partial update
DELETE /api/v1/resources/:id      # Delete

# Nested resources
GET    /api/v1/users/:id/posts    # User's posts

# Actions (when CRUD doesn't fit)
POST   /api/v1/resources/:id/archive
POST   /api/v1/resources/:id/publish
```

### Request/Response Patterns

```json
// Success response
{
  "data": { ... },
  "meta": { "request_id": "..." }
}

// Collection response
{
  "data": [ ... ],
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 20,
    "total_pages": 5
  }
}

// Error response
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human readable message",
    "details": [
      { "field": "email", "message": "Invalid format" }
    ]
  },
  "meta": { "request_id": "..." }
}
```

### Versioning Strategy

- **URL versioning**: `/api/v1/`, `/api/v2/` - Most explicit
- **Header versioning**: `Accept: application/vnd.api+json;version=1`
- **Sunset headers**: Communicate deprecation timeline

---

## UX Flow Specification

### Flow Template

```
Flow: [Name]
Trigger: [What initiates this flow]
Actor: [Who performs this]
Preconditions: [What must be true before]

Steps:
1. [Action] → [System response]
   - Success: [Next step]
   - Error: [Error handling]

2. [Action] → [System response]
   ...

Postconditions: [What's true after completion]

Edge Cases:
- [Scenario]: [How handled]
```

### State Definitions

```
State: [Component/Page] States

| State | Trigger | Display | Actions Available |
|-------|---------|---------|-------------------|
| Empty | No data | Empty state message | [CTA] |
| Loading | Data fetch | Skeleton/spinner | None |
| Error | Fetch failed | Error message | Retry |
| Partial | Some data | Available items | Load more |
| Complete | All loaded | Full content | All actions |
```

### Error UX Patterns

- **Inline validation** - Immediate feedback, don't wait for submit
- **Optimistic updates** - Show success, rollback on failure
- **Retry with backoff** - Automatic retry for transient errors
- **Graceful degradation** - Partial functionality over complete failure

---

## UI Component Specification

### Component Template

```
Component: [Name]
Purpose: [What this component does]
Location: [Where it appears]

Props:
- [prop]: [type] (required|optional) - [description]
  - Default: [value]
  - Validation: [rules]

States:
- Default: [description]
- Hover: [description]
- Active: [description]
- Disabled: [description]
- Loading: [description]
- Error: [description]

Events:
- onClick: [handler description]
- onChange: [handler description]

Layout:
- Container: [sizing, spacing]
- Children: [arrangement]

Responsive:
- Mobile (<640px): [behavior]
- Tablet (640-1024px): [behavior]
- Desktop (>1024px): [behavior]

Accessibility:
- Role: [ARIA role]
- Label: [aria-label or labelledby]
- Keyboard: [tab order, shortcuts]
```

### Layout Patterns

```
# Page layouts
┌──────────────────────────────────┐
│            Header                │
├────────┬─────────────────────────┤
│        │                         │
│  Nav   │        Content          │
│        │                         │
├────────┴─────────────────────────┤
│            Footer                │
└──────────────────────────────────┘

# Card grid
┌────────┐ ┌────────┐ ┌────────┐
│  Card  │ │  Card  │ │  Card  │
└────────┘ └────────┘ └────────┘
┌────────┐ ┌────────┐ ┌────────┐
│  Card  │ │  Card  │ │  Card  │
└────────┘ └────────┘ └────────┘

# Form layout
┌─────────────────────────────────┐
│ Label                           │
│ ┌─────────────────────────────┐ │
│ │ Input                       │ │
│ └─────────────────────────────┘ │
│ Helper text                     │
└─────────────────────────────────┘
```

### Design Token References

```
Spacing: 4, 8, 12, 16, 24, 32, 48, 64 (px)
Radius: 4 (sm), 8 (md), 12 (lg), 9999 (full)
Shadows: sm, md, lg, xl (elevation levels)
Transitions: 150ms (fast), 200ms (normal), 300ms (slow)
```

---

## Implementation Planning

### Step Sizing

- **< 30 minutes** - Ideal step size
- **Atomic** - One logical change
- **Testable** - Can verify independently
- **Reversible** - Can be rolled back

### Step Template

```
Step [N]: [Title]
Estimate: [X] minutes
Dependencies: [Previous steps required]

Changes:
- [File]: [What changes]
- [File]: [What changes]

Implementation notes:
- [Guidance for the implementing agent]

Verification:
- [ ] [How to test this step worked]
```

### Phase Boundaries

- **Phase 1: Foundation** - Data model, core entities
- **Phase 2: Core Logic** - Business rules, validation
- **Phase 3: API Layer** - Endpoints, contracts
- **Phase 4: UI Shell** - Layout, navigation
- **Phase 5: UI Features** - Components, interactions
- **Phase 6: Polish** - Error handling, edge cases
- **Phase 7: Operations** - Monitoring, deployment

---

## Document Navigation

### Cross-Reference Format

When designs span multiple sections or files, use explicit links:

```markdown
See [Section Name](#anchor) for details on [topic].
Implements the flow defined in [UX > Flow Name](./ux-flows.md#flow-name).
Uses component spec from [UI > Component](./ui-specs.md#component).
```

### Design Index Template

```markdown
# [Feature] Design Index

| Document                             | Description                     | Status      |
| ------------------------------------ | ------------------------------- | ----------- |
| [overview.md](./overview.md)         | Problem, goals, success metrics | Complete    |
| [architecture.md](./architecture.md) | System design, data flow        | Complete    |
| [data-model.md](./data-model.md)     | Entities, relationships         | In Review   |
| [api.md](./api.md)                   | Endpoint contracts              | Draft       |
| [ux.md](./ux.md)                     | User flows, states              | Draft       |
| [ui.md](./ui.md)                     | Component specs                 | Not Started |
| [plan.md](./plan.md)                 | Implementation steps            | Not Started |
```

### Handoff Checklist

Before handing to coding agents, verify:

- [ ] All entities defined with attributes and relationships
- [ ] All API endpoints specified with request/response shapes
- [ ] All user flows documented with error handling
- [ ] All UI components specified with states
- [ ] Implementation steps are < 30 min each
- [ ] Cross-references link to correct sections
- [ ] Open questions are explicitly marked
