# Form Objects

Form objects turn “params + validation + persistence” into a testable, reusable object so controllers stay orchestration-only and models stay invariant-only.

## When to load

- You are building a multi-field create/update flow with non-trivial validation.
- Params map to multiple models or require normalization.
- You want one place to manage error messages for a form.

## When NOT to load

- It is a single-model write with simple validations (keep it in the model).
- You need a domain workflow with side effects/transactions (use a service object).
- You need authorization rules (use policies).

## Core rules

- Form objects own: input mapping, validation, and the write call.
- Prefer `ActiveModel::Model` + `ActiveModel::Attributes` for non-AR forms.
- Keep `save`/`call` as the single entrypoint; return a simple result.
- Keep DB writes inside a transaction when multiple records change.
- Avoid callbacks inside form objects; be explicit.

## Minimal examples

Minimal `ActiveModel` form:

```ruby
# app/forms/projects/create_form.rb
class Projects::CreateForm
  include ActiveModel::Model
  include ActiveModel::Attributes

  attribute :name, :string
  attribute :owner_id, :integer

  validates :name, presence: true

  def save
    return false unless valid?

    Project.transaction do
      @project = Project.create!(name:, owner_id:)
    end

    true
  rescue ActiveRecord::RecordInvalid
    false
  end

  attr_reader :project
end
```

Controller stays orchestration-only:

```ruby
def create
  form = Projects::CreateForm.new(project_params.merge(owner_id: current_user.id))

  if form.save
    redirect_to project_path(form.project), notice: "Created"
  else
    render :new, status: :unprocessable_entity
  end
end
```

## Anti-patterns

- Form object doing authorization or request-specific branching.
- Form object becoming a “service object” with unrelated side effects.
- Duplicating model invariants in the form instead of relying on model validations.
- Returning raw exceptions to controllers instead of a stable failure mode.

## Checklist

- Controller only wires params/actor and renders.
- Form owns input mapping + validation + `save`.
- Multi-record writes are transactional.
- Failure mode is stable (errors available without exceptions).
- Unit tests cover success + validation failure.
