# Thin MVC Architecture

Keep Rails maintainable by putting each rule in its smallest correct home: controllers orchestrate, models enforce invariants, POROs execute workflows, concerns share cohesive behavior.

## When to load

- You are deciding where new logic should live (`controller`, `model`, `concern`, `service`, `query`).
- A model/controller is growing and needs extraction.
- You need a repeatable placement rule for team consistency.
- You are introducing POROs to reduce callback-heavy or action-heavy code.

## When NOT to load

- The task is pure SQL/indexing/migration strategy (use `../database/SKILL.md`).
- The task is API contract/versioning design (use `../api/SKILL.md`).
- The task is frontend-only behavior with no Rails domain logic.

## Core rules

- `Controller`: request/response orchestration only (`params`, auth, render/redirect, status).
- `Model`: data invariants only (validations, associations, small persistence-level behavior).
- `Concern`: shared, cohesive behavior for one layer and one bounded context.
- `Service object (PORO)`: multi-step workflows, side effects, transactions, integrations.
- `Query object (PORO)`: reusable filtering/sorting/reporting; returns relation or readonly result.
- Prefer explicit method calls over hidden callbacks for business flows.

## Common patterns

- `app/controllers/*`: thin action -> call service/query -> serialize response.
- `app/models/concerns/*`: focused modules like `Publishable`, `Taggable`, `SoftDeletable`.
- `app/controllers/concerns/*`: shared auth, pagination, locale, strong-params helpers.
- `app/services/*`: `Result` object with `success?`, `value`, `error`.
- `app/queries/*`: chainable `ActiveRecord::Relation` with explicit filters.
- Keep names domain-first: `Orders::Checkout`, `Users::Search`, `Invoices::Overdue`.

## Minimal examples

Thin controller action (orchestrate only):

```ruby
class ProjectsController < ApplicationController
  def create
    result = Projects::Create.call(params: project_params, actor: current_user)

    if result.ok?
      redirect_to project_path(result.value), notice: "Created"
    else
      flash.now[:alert] = result.error
      render :new, status: :unprocessable_entity
    end
  end

  private

  def project_params
    params.require(:project).permit(:name)
  end
end
```

Thin model (invariants only):

```ruby
class Project < ApplicationRecord
  validates :name, presence: true
end
```

## Anti-patterns

- Fat controllers doing branching, calculations, and persistence decisions.
- Fat models with workflow orchestration, API calls, and cross-domain branching.
- God concerns that mix unrelated responsibilities across domains.
- Service objects that just wrap one model method without adding boundaries.
- Query logic duplicated across controllers/scopes/services.
- Hidden business behavior inside callbacks that surprises callers.

## Checklist

- Does controller code stay mostly IO + orchestration?
- Does model code enforce invariants, not app workflows?
- Is shared behavior extracted into a focused concern with one reason to change?
- Is multi-step business logic moved to a PORO service?
- Is repeated filtering/reporting moved to a query object?

## References

- Rails Guides: https://guides.rubyonrails.org/
- ActiveSupport::Concern: https://api.rubyonrails.org/classes/ActiveSupport/Concern.html
- Rails Style Guide: https://rails.rubystyle.guide/
