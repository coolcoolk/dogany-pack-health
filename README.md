# Dogany Health Trainer

Dogany Health Trainer is a workout and diet coaching pack for a Dogany agent.
It turns an agent into a personal trainer: it builds a weight-training program
with you, runs each workout set by set in chat, and coaches your eating
against a daily target.

Health Trainer is not a standalone app. It installs onto an existing Dogany
agent and works on top of Dogany LifeKit, which keeps the records.

## Requirements

- A Dogany agent on framework **2.6.0 or later**.
- **Dogany LifeKit 2.38.0 or later** (below 3.0.0) installed on the same
  agent. LifeKit owns the database. This pack adds coaching on top of it.

## Install

Install it with the framework's pack installer, from the agent's framework
checkout:

```
scripts/pack/pack_install.sh <agent-slug> <agent-root> --pack pack_health
```

Run it again with `--upgrade` to move an installed agent to a newer version.

The installer reads `pack-manifest.json` and copies the payload into the
agent's instance: the chat skills, the coaching command line under
`service/health`, the routines and the default config. Your data stays on
your machine, in the agent's own LifeKit database.

When the agent's own setup finishes, it continues straight into a short health
setup: your goal, where you train, how often, and what equipment you have.

## What it covers

**Program**
- A guided program consult: goal, place, frequency, days and split, then a
  program card with exercises, sets, reps and loads.
- Program review and rebalancing when your schedule, goal or equipment
  changes. Sites that need care get warm-up and preparation drills, not
  silent exercise swaps.

**Live workout session**
- Set-by-set guidance in chat: the next set's weight and reps, a set table
  after every recorded set, rest timers and hold timers.
- Load progression from your own history, with the reason shown next to the
  number whenever the coach's call differs from the calculated one.
- Pain and form notes during a set, with follow-up and a program review.

**Diet**
- A daily calorie and macro card, remaining amounts, and planned meals that
  show on today's card before you eat them.
- Protein coaching that only suggests what you actually have.

**Form demos**
- A library of 3D exercise form demos shown before the first set of a new
  exercise.

## Languages

User-facing text ships in Korean and English.

## License

Dogany Health Trainer is licensed under the PolyForm Strict License 1.0.0
together with the Dogany Extension Permission. See `LICENSE` and `NOTICE` at
the root of this repository.
