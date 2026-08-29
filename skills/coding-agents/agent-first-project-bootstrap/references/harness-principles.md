# Harness Engineering Principles

Use these principles when bootstrapping an agent-first software repository.

## Repository knowledge is authoritative

Put durable project knowledge in the repository: architecture, decisions, plans, schemas, tests, setup, operations, and acceptance criteria. Prompts should reference that knowledge rather than restating it indefinitely.

## Give agents a map, not a manual

Keep top-level instructions short and navigational. Use progressive disclosure: agents start from a concise entry point and load deeper documents only when relevant.

## Constrain boundaries, not local implementation

Make product outcomes, architectural invariants, security rules, interfaces, and acceptance criteria explicit. Allow agents substantial autonomy in local implementation choices.

## Mechanical enforcement beats repeated reminders

If a rule matters repeatedly, encode it in tests, schemas, static checks, CI, generated artifacts, or other executable mechanisms when practical.

## Agent legibility is an engineering property

A capable agent should be able to inspect the repository and determine what the system does, how to run it, why it failed, what changed, and how to validate a fix.

## Improve the harness when the agent struggles

Repeated friction is evidence about the environment. Add the missing fixture, documentation, helper, observability, validation, or invariant instead of repeatedly compensating in prompts.

## Tight feedback loops compound

Prefer small coherent changes, focused tests, self-review, independent review where available, and immediate repair of discovered harness weaknesses.

## The harness is part of the product

Tests, logs, local tooling, plans, ADRs, reproducibility, and agent-facing documentation are not peripheral developer conveniences. In an agent-first project they directly determine development quality and velocity.
