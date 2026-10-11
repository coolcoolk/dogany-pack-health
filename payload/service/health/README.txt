program.yaml -- session prescription program state (DGN-301)
=============================================================

Location: files/program/program.yaml (agent workspace)
Writer:   main session ONLY (one-writer invariant, spec section 1.1)
Readers:  rx-calc (DET helper; health-brief's morning session line), logging-turn reconcile

SCHEMA FIELDS
-------------

version: int
  Schema version. Current: 1.

split_ref: string
  Reference to the ledger_goal mid detail.split field (source of truth for the
  declared split). Not duplicated here -- this is a pointer only.

rotation: list of strings
  Ordered rotation queue. Each entry is a session_type.code value in kit_life.db.
  rx-calc reads workouts.session_type_id for the last completed weight session,
  looks up the code, and advances to the next item in this list (wrapping at end).
  Example: [앞A, 뒷A, 앞B, 뒷B]

days: mapping of session_type.code -> day plan
  One entry per rotation day. Each day plan has:

  exercises: list of exercise slots
    Each slot:
      slot: int
        Slot number within the day (1-based). rx renders in slot order.

      name: string (English snake_case)
        Canonical exercise name. Used as the key for progression tracking.
        Follow focus_areas vocabulary convention (e.g., incline_barbell_press).

      display: string (Korean or descriptive)
        User-facing name for the prescription message.

      weight_kg: float or null
        The SEED: the owner-declared starting weight, written once by
        program-init. It is NOT the current working weight. rx-calc reads it
        only while no working set of this lift was ever logged; from the first
        logged working set on, the progression base is the last logged working
        load (rx-calc resolve_base_weight, program state step A). null = no
        seed: the first session is a calibration prescription (RIR 2 probe).
        NEVER set this to a guessed value -- only the owner's word seeds it.

      sets: int
        Number of working sets.

      rep_range: [lo, hi]
        Target rep range. Spec defaults (OQ-A):
          compound: [6, 10]
          isolation/accessory: [10, 15]
        rx-calc uses hi as the advancement threshold (top set >= hi -> weight up).

      progression: "double" | "hold"
        double = normal double-progression (advancing weight when top set >= hi).
        hold = maintenance/rehab slot -- no weight change ever.

      (no miss_streak, no last) -- RETIRED card fields. The miss streak is
        derived from workout_sets (rx-calc derive_miss_streak: consecutive
        newest sessions whose top working set fell below rep_range[0] at the
        same load; a load change ends the run). Two misses -> deload. The last
        result is workout_sets itself. A card that still carries either key
        is not read.

      safety_note: null or string
        If this slot has a safety substitution from a ledger_constraint safety row,
        record the reason here in one line. Written once at program card creation
        (P1) or when a new safety row arrives (main session reconcile via m3 flag).
        Example: "스쿼트 계열 대체 -- 무릎 재활력 (injury_knee)"

      inc_override: null or float
        Per-slot increment override in kg (m8). null = use OQ-A defaults:
          upper body / accessory: 2.5 kg
          lower body / hip hinge: 5.0 kg
        Set a numeric value only when the equipment step differs from defaults
        (e.g., a machine with 10 kg plate increments: inc_override: 10.0).
        Requires owner approval (mention when setting).

  focus_slot: null or int
    The slot number designated as the focus area extra slot for this day.
    Derived from ledger_goal long detail.focus_areas at P1 creation.
    Example: focus_areas=[back] -> 뒷A focus_slot: 4 (the extra back slot).
    null = no designated focus slot for this day.

changelog: (retired as a weight log) -- weights are no longer written to the
  card, so there is no per-weight-update line to append. The weight history
  is workout_sets; program-level changes (the why) live in
  program-history.json.

CALIBRATION PROTOCOL (spec section 3.2)
----------------------------------------
A slot with no seed and no logged working load gets a calibration rx:
  "RIR 2 기준 (2회 여유 남는 무게)으로 무게를 잡고 세트당 실사용 무게를 알려달라"
The first logged working set ends calibration -- nothing is written back to
the card; the next session reads that load from workout_sets and the
double-progression arithmetic runs on it.

VERSIONING (spec section 1.4)
------------------------------
No git versioning (the agent workspace is not a git repo).
The card is STRUCTURE only. Its writers are program-init (the whole file)
and lattice-set (one slot's explicit lattice override; a machine's grid goes
to the kit's machine-upd instead). No session writes state into it: weight,
miss streak and last result are computed from workout_sets on every read
(program state steps A/B, 2026-09-30 / 2026-10-03).

CLEANUP (spec section 1.4 / m5)
---------------------------------
rx/ prescription files are NOT in cleanup-files.sh sweep scope.
They accumulate without auto-deletion. Weekly review provides manual cleanup guide.
After pack code delta (cleanup-files.sh rx/ scope addition), 90-day retention applies.
program.yaml itself: no rotation, permanent.

OPEN QUESTIONS (tracking)
--------------------------
OQ-F: structured workout_sets table (future) -- when it lands, weight/reps SoT
      migrates from program.yaml + workouts.note to workout_sets. Migration design
      separate (DGN-285 adjacent). program.yaml remains interim until then.
