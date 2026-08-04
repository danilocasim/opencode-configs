# Controller Concerns

Use controller concerns to share request-layer plumbing so actions stay thin and business logic remains in POROs/models.

## When to load

- Multiple controllers share auth/pagination/filtering/serialization setup.
- You need consistent request handling (`before_action`, parameter helpers, error rendering).
- Controllers are duplicating cross-cutting request concerns.

## When NOT to load

- Shared logic is domain workflow or business policy branching (use service/policy PORO).
- Shared logic is model-level invariant or query behavior (use model/query).
- The concern applies to only one controller.

## Core rules

- Controller concerns handle HTTP concerns, not domain decisions.
- Keep public surface small: helper methods + minimal callbacks.
- Keep side effects explicit in actions/services, not hidden in concern callbacks.
- Keep strong-params helpers close to resource naming.

## Common patterns

- `Authenticatable`: current user lookup and auth guard.
- `Paginatable`: parse page/per_page and apply pagination.
- `Filterable`/`Sortable`: sanitize allowed sort/filter params.
- `ErrorRenderable`: map exceptions to consistent JSON/HTML responses.
- `LocaleSwitching`: safe locale extraction from params/header/session.

## Minimal examples

```ruby
# app/controllers/concerns/error_renderable.rb
module ErrorRenderable
  extend ActiveSupport::Concern

  included do
    rescue_from ActiveRecord::RecordNotFound, with: :render_not_found
  end

  private

  def render_not_found
    respond_to do |format|
      format.html { render file: Rails.public_path.join("404.html"), status: :not_found, layout: false }
      format.json { render json: { error: "not_found" }, status: :not_found }
    end
  end
end
```

```ruby
class Api::V1::ProjectsController < ApplicationController
  include ErrorRenderable

  def show
    project = Project.find(params[:id])
    render json: { id: project.id, name: project.name }
  end
end
```

## Anti-patterns

- Concern performing writes, transactions, or multi-step domain workflows.
- Concern with action-specific branching that only one controller needs.
- Massive `included do` block with callback order dependencies.
- Catch-all rescue logic that masks domain errors.

## Checklist

- Is the concern purely request/response plumbing?
- Can actions still be read top-to-bottom without hidden surprises?
- Are callbacks minimal and order-safe?
- Is domain logic delegated to service/query/policy objects?
- Are behaviors covered by request specs?

## References

- Action Controller Overview: https://guides.rubyonrails.org/action_controller_overview.html
- Rails API: https://api.rubyonrails.org/classes/ActionController/Base.html
