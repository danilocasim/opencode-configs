# Pundit Policies

Policies make authorization explicit and testable. Keep rules out of controllers/models and avoid scattering `if current_user...` checks across the codebase.

## When to load

- You are adding or refactoring authorization rules.
- You need `PolicyScope` for index/search pages.
- You want consistent patterns for `authorize` and scoping.

## When NOT to load

- You are designing API auth (tokens/sessions) rather than authorization rules.
- You need data-level constraints enforced by the DB (use DB constraints).

## Core rules

- Controller orchestrates: `authorize(record)` and `policy_scope(scope)`.
- Policies are pure; no DB writes and no side effects.
- Prefer policy methods named after actions (`show?`, `update?`).
- Use `Scope` objects for collection access; keep scopes simple and composable.
- Keep policy dependencies explicit (actor + record); avoid pulling globals.

## Minimal examples

Policy + scope:

```ruby
# app/policies/project_policy.rb
class ProjectPolicy < ApplicationPolicy
  def show?
    record.public? || record.owner_id == user.id
  end

  def update?
    record.owner_id == user.id
  end

  class Scope < Scope
    def resolve
      scope.where(public: true).or(scope.where(owner_id: user.id))
    end
  end
end
```

Controller usage:

```ruby
def index
  @projects = policy_scope(Project).order(created_at: :desc)
end

def update
  project = Project.find(params[:id])
  authorize(project)
  # ...
end
```

## Anti-patterns

- Authorization rules embedded in models or queries.
- Policy methods that mutate records.
- Policies that depend on controller params/session state.
- Scopes that load everything then filter in Ruby.

## Checklist

- Every controller action calls `authorize` or uses `policy_scope`.
- Policies are pure and fast.
- Scope queries run in SQL.
- Specs cover allow + deny for the key actions.
