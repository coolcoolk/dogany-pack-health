#!/usr/bin/env python3
# exercise_catalog.py -- the reviewed source of the 2026-09-26 taxonomy
# expansion, and the one place a lift's STABILIZER roles live today.
#
# WHY THIS FILE EXISTS
#   The planner (program-plan) only offers lifts that carry a muscle map (E9:
#   a map is never invented at runtime). The shipped seed had no bench press,
#   leg press, push-up, plank or lunge, so none of them could ever be planned.
#   Adding them is pack product knowledge, so it is written ONCE, here, as a
#   full creation-gate record, and the seed block in health_taxonomy_seed.sql
#   is GENERATED from it (`exercise_catalog.py --emit-sql`). A test holds the
#   two byte-identical, so the seed cannot drift from this table.
#
# THE CREATION GATE (worklog 2026-09-26-muscle-fatigue-function-tracking,
# owner 11:05 "종목 생성 시 세부 근육 연결 필수"): every lift carries
#   movement + equipment (+grip)   -> exercise_movement_grip
#   pattern                        -> exercise_pattern (substitution by pattern)
#   muscles {muscle: role}         -> exercise_muscle_map (primary|secondary)
#   subregions [(node, w, grade)]  -> exercise_subregion_map
#   stabilizers (node, ...)        -> HERE ONLY (see below); () = none, stated
#   fatigue high|med|low           -> exercise_fatigue_cost
#   rep_class compound|isolation|hold|core -> what program-plan's dose() must
#                                     derive from the rows above (tested)
#
# WHY STABILIZERS ARE NOT A SEED ROW YET
#   exercise_muscle_map.role is CHECK(primary|secondary) in the kit DDL, and a
#   stabilizer there would earn volume credit (rx-calc actual_sets). The spec
#   (muscle-fatigue-spec A2.4) puts them in ax_tag(tag_group='stabilizes') +
#   ax_exercise_tag -- but that tag hangs off an ax_exercise row, which a
#   machine/cable lift cannot have until ax-jit registers its machine. So the
#   roles are recorded here, for every lift in the shipped taxonomy, and the
#   spec's P1 tag seed materialises them. Nodes are restricted to muscle_node
#   rows that exist today (rotator_cuff / obliques are P1 node additions).
#
# SUBREGION RULE (same as the moved rows): per coarse muscle the subregion
#   weights sum to the role credit (primary 1.0, secondary 0.5). An extra
#   'functional' node (adductors on a squat) mirrors the existing rows.
#   Back is split trapezius (back_upper) / latissimus (back_lats) / erector
#   (back_erectors); a vertical pull or a supported row carries NO erector
#   share (worklog 11:25: the lat-pulldown erector mapping was an error).
#   Splits with no measured bias are 'even' -- no weight here is a new claim.
#
# stdlib only. Imported by tests; run directly to print the seed block.

import sys

# Movements whose work is a HOLD (seconds), not reps. ax_exercise cannot carry
# them without a hold_sec number nobody measured, so they get no seeded
# ax_exercise row and program-plan asks their amount (field move).
# ax_engine.HOLD_MOVEMENTS mirrors this tuple (a test keeps them equal).
HOLD_MOVEMENTS = ("plank", "wall_sit")

ROLE_CREDIT = {"primary": 1.0, "secondary": 0.5}

CHEST3 = (("chest_lower", 0.33, "even"), ("chest_mid", 0.33, "even"),
          ("chest_upper", 0.34, "even"))
TRI_HALF = (("triceps_lat_med", 0.25, "even"), ("triceps_long", 0.25, "even"))
TRI_FULL = (("triceps_lat_med", 0.5, "even"), ("triceps_long", 0.5, "even"))
BI_HALF = (("biceps_distal", 0.25, "even"), ("biceps_prox", 0.25, "even"))
BI_FULL = (("biceps_distal", 0.5, "even"), ("biceps_prox", 0.5, "even"))
FOREARM_HALF = (("brachioradialis", 0.25, "even"),
                ("forearm_flexors", 0.25, "even"))
BACK_NO_ERECTOR = (("back_lats", 0.5, "even"), ("back_upper", 0.5, "even"))
GLUTE_HALF = (("glute_max", 0.25, "even"), ("glute_med", 0.25, "even"))
GLUTE_FULL = (("glute_max", 0.5, "even"), ("glute_med", 0.5, "even"))
QUADS = (("quads", 1.0, "group"),)
HAMS_FULL = (("hamstrings", 1.0, "group"),)
HAMS_HALF = (("hamstrings", 0.5, "group"),)
ADDUCTORS = (("adductors", 0.5, "functional"),)
ABS = (("abs", 1.0, "group"),)
# kit_life 056 D5 sub-node shares (literature estimates, grade 'C'), used only
# by the two CLOSE_GAPS lifts the migration rewrites by name, so a fresh seed
# lands exactly where a migrated DB does. Same credit as the group row they
# replace (quads 1.0 / calves 1.0); only the split is new.
QUADS_SQUAT = (("rect_fem", 0.15, "C"), ("vast_lat", 0.45, "C"),
               ("vast_med", 0.40, "C"))
CALF_SEATED = (("calf_gastroc", 0.15, "C"), ("calf_soleus", 0.85, "C"))

# New variation splits use existing detailed nodes and neutral accounting
# shares, not measured activation ratios. Sources describe the movement family
# and form in movement_catalog.py; 'even' makes that evidence limit explicit.
QUADS_EVEN = (("rect_fem", 0.34, "even"), ("vast_lat", 0.33, "even"),
              ("vast_med", 0.33, "even"))
HAMS_EVEN = (("hams_lateral", 0.5, "even"), ("hams_medial", 0.5, "even"))
CALVES_EVEN = (("calf_gastroc", 0.5, "even"), ("calf_soleus", 0.5, "even"))


def _ex(movement, equipment, pattern, muscles, subregions, stabilizers,
        fatigue, rep_class, grip=None, unilateral=False, tempo=None):
    return {"movement": movement, "equipment": equipment, "grip": grip,
            "pattern": pattern, "muscles": dict(muscles),
            "subregions": tuple(subregions), "stabilizers": tuple(stabilizers),
            "fatigue": fatigue, "rep_class": rep_class,
            "unilateral": unilateral, "tempo": tempo}


PRESS = {"chest": "primary", "triceps": "secondary", "shoulders": "secondary"}
PRESS_SUB = CHEST3 + (("front_delt", 0.5, "functional"),) + TRI_HALF

# New rows. Movement names are chosen so muscle-preset --validate still
# reconstructs every map from movement_muscle_base (+ grip delta) exactly.
CATALOG = {
    # chest -- flat press (barbell / dumbbell / bodyweight), fly, dip
    "bench_press": _ex("flat_press", "barbell", "horizontal_push", PRESS,
                       PRESS_SUB, ("back_upper", "back_lats", "forearms"),
                       "high", "compound", grip="pronated"),
    "dumbbell_bench_press": _ex("flat_press", "dumbbell", "horizontal_push",
                                PRESS, PRESS_SUB, ("back_upper", "forearms"),
                                "med", "compound", grip="pronated"),
    "push_up": _ex("flat_press", "bodyweight", "horizontal_push", PRESS,
                   PRESS_SUB, ("abs", "glute_max"), "low", "compound"),
    "pec_deck_fly": _ex("fly_isolation", "machine", "isolation",
                        {"chest": "primary"}, CHEST3, (), "low", "isolation"),
    "dip": _ex("dip", "bodyweight_assist", "horizontal_push",
               {"chest": "primary", "triceps": "primary",
                "shoulders": "secondary"},
               CHEST3 + TRI_FULL + (("front_delt", 0.5, "functional"),),
               ("abs", "back_upper"), "med", "compound"),
    # back -- horizontal pulls without a bent-over torso: no erector share
    "seated_cable_row": _ex("pull_compound", "cable", "horizontal_pull",
                            {"back": "primary", "biceps": "secondary"},
                            BACK_NO_ERECTOR + BI_HALF,
                            ("back_erectors", "forearms"), "low", "compound"),
    "dumbbell_row": _ex("pull_compound", "dumbbell", "horizontal_pull",
                        {"back": "primary", "biceps": "secondary"},
                        BACK_NO_ERECTOR + BI_HALF,
                        ("abs", "back_erectors", "forearms"), "med",
                        "compound", unilateral=True),
    # shoulders
    "dumbbell_shoulder_press": _ex(
        "overhead_press", "dumbbell", "vertical_push",
        {"shoulders": "primary", "triceps": "secondary"},
        (("front_delt", 1.0, "functional"),) + TRI_HALF,
        ("abs", "back_upper"), "med", "compound", grip="pronated"),
    "dumbbell_lateral_raise": _ex(
        "lateral_raise", "dumbbell", "isolation", {"shoulders": "primary"},
        (("side_delt", 1.0, "functional"),), ("back_upper",), "low",
        "isolation"),
    # arms
    "dumbbell_curl": _ex("curl", "dumbbell", "isolation",
                         {"biceps": "primary"}, BI_FULL, ("forearms",), "low",
                         "isolation", grip="supinated"),
    "lying_triceps_extension": _ex("tricep_isolation", "ez_bar", "isolation",
                                   {"triceps": "primary"}, TRI_FULL,
                                   ("forearms",), "low", "isolation", grip="pronated"),
    # legs -- bilateral
    "leg_press": _ex("squat", "machine", "squat",
                     {"quads": "primary", "glutes": "secondary"},
                     QUADS + GLUTE_HALF + ADDUCTORS, (), "med", "compound"),
    "leg_extension": _ex("leg_extension", "machine", "isolation",
                         {"quads": "primary"}, QUADS, (), "low", "isolation"),
    "goblet_squat": _ex("squat", "dumbbell", "squat",
                        {"quads": "primary", "glutes": "secondary"},
                        QUADS + GLUTE_HALF + ADDUCTORS,
                        ("abs", "back_erectors", "back_upper"), "med",
                        "compound"),
    "hip_thrust": _ex("hip_thrust", "barbell", "hinge",
                      {"glutes": "primary", "hamstrings": "secondary"},
                      GLUTE_FULL + HAMS_HALF, ("abs", "adductors"), "med",
                      "compound"),
    "hip_abduction_machine": _ex("hip_abduction", "machine", "isolation",
                                 {"glutes": "primary"},
                                 (("glute_med", 1.0, "functional"),), (),
                                 "low", "isolation"),
    # legs -- unilateral (lunge variants, single-leg hinge)
    "walking_lunge": _ex("split_squat", "dumbbell", "squat",
                         {"quads": "primary", "glutes": "primary"},
                         QUADS + GLUTE_FULL + ADDUCTORS, ("abs", "forearms"),
                         "med", "compound", unilateral=True),
    "reverse_lunge": _ex("split_squat", "dumbbell", "squat",
                         {"quads": "primary", "glutes": "primary"},
                         QUADS + GLUTE_FULL + ADDUCTORS, ("abs", "forearms"),
                         "med", "compound", unilateral=True),
    "bodyweight_lunge": _ex("split_squat", "bodyweight", "squat",
                            {"quads": "primary", "glutes": "primary"},
                            QUADS + GLUTE_FULL + ADDUCTORS, ("abs",), "low",
                            "compound", unilateral=True),
    "single_leg_rdl": _ex("single_leg_hinge", "dumbbell", "hinge",
                          {"hamstrings": "primary", "glutes": "primary"},
                          HAMS_FULL + GLUTE_FULL,
                          ("back_erectors", "adductors", "forearms"), "med",
                          "compound", unilateral=True),
    # Additional common variants; Korean names and sources in movement_catalog.py.
    "front_squat": _ex("squat", "barbell", "squat",
                       {"quads": "primary", "glutes": "secondary"},
                       QUADS + GLUTE_HALF + ADDUCTORS,
                       ("abs", "back_erectors"), "high", "compound"),
    "box_squat": _ex("squat", "barbell", "squat",
                     {"quads": "primary", "glutes": "secondary"},
                     QUADS + GLUTE_HALF + ADDUCTORS,
                     ("abs", "back_erectors"), "med", "compound"),
    "step_up": _ex("split_squat", "bodyweight", "squat",
                    {"quads": "primary", "glutes": "primary"},
                    QUADS + GLUTE_FULL + ADDUCTORS, ("abs",), "low",
                    "compound", unilateral=True),
    "dumbbell_rdl": _ex("hinge_bilateral", "dumbbell", "hinge",
                           {"hamstrings": "primary", "glutes": "secondary"},
                           HAMS_FULL + GLUTE_HALF,
                           ("back_erectors", "forearms"), "med", "compound"),
    "kettlebell_deadlift": _ex("hinge_bilateral", "kettlebell", "hinge",
                                {"hamstrings": "primary", "glutes": "secondary"},
                                HAMS_FULL + GLUTE_HALF,
                                ("back_erectors",), "med", "compound"),
    "incline_push_up": _ex("flat_press", "bodyweight", "horizontal_push",
                            PRESS, PRESS_SUB, ("abs", "glute_max"), "low",
                            "compound"),
    "cable_chest_press": _ex("flat_press", "cable", "horizontal_push",
                              PRESS, PRESS_SUB, ("abs",), "med", "compound"),
    "chest_supported_dumbbell_row": _ex(
        "pull_compound", "dumbbell", "horizontal_pull",
        {"back": "primary", "biceps": "secondary"},
        BACK_NO_ERECTOR + BI_HALF, ("forearms",), "low", "compound"),
    "single_arm_cable_row": _ex(
        "pull_compound", "cable", "horizontal_pull",
        {"back": "primary", "biceps": "secondary"},
        BACK_NO_ERECTOR + BI_HALF, ("forearms", "abs"), "low", "compound",
        unilateral=True),
    "landmine_press": _ex("overhead_press", "barbell", "vertical_push",
                          {"shoulders": "primary", "triceps": "secondary"},
                          (("front_delt", 1.0, "functional"),) + TRI_HALF,
                          ("abs", "back_upper"), "med", "compound",
                          unilateral=True),
    # 2026-09-27 strength variety; Korean labels / family sources live in
    # movement_catalog.py. No activation, prep or cooldown additions.
    "single_leg_press": _ex(
        "squat", "machine", "squat",
        {'quads': 'primary', 'glutes': 'secondary'},
        QUADS_EVEN + GLUTE_HALF + ADDUCTORS, (),
        "med", "compound", unilateral=True),
    "seated_leg_curl": _ex(
        "leg_curl", "machine", "isolation",
        {'hamstrings': 'primary'},
        HAMS_EVEN, (),
        "low", "isolation"),
    "single_leg_lying_curl": _ex(
        "leg_curl", "machine", "isolation",
        {'hamstrings': 'primary'},
        HAMS_EVEN, (),
        "low", "isolation", unilateral=True),
    "cable_glute_kickback": _ex(
        "glute_extension", "cable", "isolation",
        {'glutes': 'primary'},
        (('glute_max', 1.0, 'functional'),), ('abs',),
        "low", "isolation", unilateral=True),
    "single_arm_dumbbell_bench_press": _ex(
        "flat_press", "dumbbell", "horizontal_push",
        PRESS,
        PRESS_SUB, ('abs', 'back_upper', 'forearms'),
        "med", "compound", unilateral=True, grip="pronated"),
    "seated_machine_row": _ex(
        "pull_compound", "machine", "horizontal_pull",
        {'back': 'primary', 'biceps': 'secondary'},
        BACK_NO_ERECTOR + BI_HALF, ('forearms',),
        "low", "compound"),
    "inverted_row": _ex(
        "pull_compound", "bodyweight_assist", "horizontal_pull",
        {'back': 'primary', 'biceps': 'secondary'},
        BACK_NO_ERECTOR + BI_HALF, ('abs', 'glute_max', 'forearms'),
        "low", "compound", grip="pronated"),
    "machine_shoulder_press": _ex(
        "overhead_press", "machine", "vertical_push",
        {'shoulders': 'primary', 'triceps': 'secondary'},
        (('front_delt', 1.0, 'functional'),) + TRI_HALF, (),
        "med", "compound"),
    "pike_push_up": _ex(
        "overhead_press", "bodyweight", "vertical_push",
        {'shoulders': 'primary', 'triceps': 'secondary'},
        (('front_delt', 1.0, 'functional'),) + TRI_HALF, ('abs', 'back_upper'),
        "med", "compound"),
    "machine_lateral_raise": _ex(
        "lateral_raise", "machine", "isolation",
        {'shoulders': 'primary'},
        (('side_delt', 1.0, 'functional'),), ('back_upper',),
        "low", "isolation"),
    "single_arm_dumbbell_lateral_raise": _ex(
        "lateral_raise", "dumbbell", "isolation",
        {'shoulders': 'primary'},
        (('side_delt', 1.0, 'functional'),), ('back_upper',),
        "low", "isolation", unilateral=True),
    "seated_dumbbell_reverse_fly": _ex(
        "rear_delt_isolation", "dumbbell", "isolation",
        {'shoulders': 'primary'},
        (('rear_delt', 1.0, 'functional'),), ('back_upper',),
        "low", "isolation"),
    "cable_reverse_fly": _ex(
        "rear_delt_isolation", "cable", "isolation",
        {'shoulders': 'primary'},
        (('rear_delt', 1.0, 'functional'),), ('back_upper',),
        "low", "isolation"),
    "cable_curl": _ex(
        "curl", "cable", "isolation",
        {'biceps': 'primary'},
        BI_FULL, ('forearms',),
        "low", "isolation", grip='supinated'),
    "dumbbell_overhead_triceps_extension": _ex(
        "tricep_isolation", "dumbbell", "isolation",
        {'triceps': 'primary'},
        TRI_FULL, ('forearms', 'abs'),
        "low", "isolation"),
    "dumbbell_triceps_kickback": _ex(
        "tricep_isolation", "dumbbell", "isolation",
        {'triceps': 'primary'},
        TRI_FULL, ('forearms', 'abs'),
        "low", "isolation", unilateral=True),
    "single_leg_calf_raise": _ex(
        "calf_raise", "bodyweight", "isolation",
        {'calves': 'primary'},
        CALVES_EVEN, ('abs', 'glute_med'),
        "low", "isolation", unilateral=True),
    "dumbbell_standing_calf_raise": _ex(
        "calf_raise", "dumbbell", "isolation",
        {'calves': 'primary'},
        CALVES_EVEN, ('abs', 'forearms'),
        "low", "isolation"),
    "leg_press_calf_raise": _ex(
        "calf_raise", "machine", "isolation",
        {'calves': 'primary'},
        CALVES_EVEN, (),
        "low", "isolation"),
    "crunch": _ex(
        "crunch", "bodyweight", "core",
        {'abs': 'primary'},
        ABS, (),
        "low", "isolation"),
    "reverse_crunch": _ex(
        "crunch", "bodyweight", "core",
        {'abs': 'primary'},
        ABS, (),
        "low", "isolation"),
    "machine_crunch": _ex(
        "crunch", "machine", "core",
        {'abs': 'primary'},
        ABS, (),
        "low", "isolation"),
    # 2026-09-27 barbell staples. Neutral shares, not activation measurements.
    "close_grip_bench_press": _ex(
        "close_grip_press", "barbell", "horizontal_push",
        {"triceps": "primary", "chest": "secondary", "shoulders": "secondary"},
        TRI_FULL + (("chest_lower", 0.165, "even"),
                    ("chest_mid", 0.165, "even"), ("chest_upper", 0.17, "even"),
                    ("front_delt", 0.5, "functional")),
        ("back_upper", "back_lats", "forearms"), "high", "compound", grip="close"),
    "decline_bench_press": _ex(
        "flat_press", "barbell", "horizontal_push", PRESS, PRESS_SUB,
        ("back_upper", "back_lats", "forearms"), "high", "compound", grip="pronated"),
    "barbell_reverse_lunge": _ex(
        "split_squat", "barbell", "squat",
        {"quads": "primary", "glutes": "primary"},
        QUADS_EVEN + GLUTE_FULL + ADDUCTORS,
        ("abs", "back_erectors"), "high", "compound", unilateral=True),
    "barbell_split_squat": _ex(
        "split_squat", "barbell", "squat",
        {"quads": "primary", "glutes": "primary"},
        QUADS_EVEN + GLUTE_FULL + ADDUCTORS,
        ("abs", "back_erectors"), "high", "compound", unilateral=True),
    "good_morning": _ex(
        "hinge_bilateral", "barbell", "hinge",
        {"hamstrings": "primary", "glutes": "secondary"},
        HAMS_EVEN + GLUTE_HALF, ("back_erectors", "abs"), "high", "compound"),
    "sumo_deadlift": _ex(
        "hip_hinge_deadlift", "barbell", "hinge",
        {"hamstrings": "primary", "glutes": "primary", "back": "secondary"},
        HAMS_EVEN + GLUTE_FULL + ADDUCTORS +
        (("back_erectors", 0.17, "even"), ("back_lats", 0.165, "even"),
         ("back_upper", 0.165, "even")),
        ("abs", "forearms", "adductors"), "high", "compound"),
    "barbell_shrug": _ex(
        "shrug", "barbell", "isolation", {"back": "primary"},
        # Explicit zero lat credit: shrug elevates the scapula, not a row.
        (("back_upper", 1.0, "functional"), ("back_lats", 0.0, "functional")),
        ("forearms", "abs", "back_erectors"), "low", "isolation", grip="pronated"),
    "barbell_glute_bridge": _ex(
        "hip_thrust", "barbell", "hinge",
        {"glutes": "primary", "hamstrings": "secondary"},
        GLUTE_FULL + HAMS_HALF, ("abs", "adductors"), "med", "compound"),
    "barbell_seal_row": _ex(
        "pull_compound", "barbell", "horizontal_pull",
        {"back": "primary", "biceps": "secondary"},
        BACK_NO_ERECTOR + BI_HALF, ("forearms",), "med", "compound", grip="pronated"),
    "dumbbell_crunch": _ex(
        "crunch", "dumbbell", "core", {"abs": "primary"}, ABS, (),
        "low", "isolation"),
    # 2026-09-27 grip/equipment variants. Shares are accounting estimates.
    # Grip research supports variants, not upper/lower lat activation ratios.
    "underhand_barbell_row": _ex(
        "pull_compound", "barbell", "horizontal_pull",
        {"back": "primary", "biceps": "secondary"},
        (("back_lats", 0.45, "even"), ("back_upper", 0.4, "even"),
         ("back_erectors", 0.15, "even")) + BI_HALF,
        ("forearms", "abs", "rear_delt"), "high", "compound", grip="supinated"),
    "wide_grip_lat_pulldown": _ex(
        "pull_compound", "cable", "vertical_pull",
        {"back": "primary", "biceps": "secondary"},
        BACK_NO_ERECTOR + BI_HALF, ("forearms",), "low", "compound", grip="wide"),
    "close_grip_lat_pulldown": _ex(
        "pull_compound", "cable", "vertical_pull",
        {"back": "primary", "biceps": "secondary"},
        BACK_NO_ERECTOR + BI_HALF, ("forearms",), "low", "compound", grip="close"),
    "neutral_grip_lat_pulldown": _ex(
        "pull_compound", "cable", "vertical_pull",
        {"back": "primary", "biceps": "secondary", "forearms": "secondary"},
        BACK_NO_ERECTOR + BI_HALF + FOREARM_HALF,
        ("abs",), "low", "compound", grip="neutral"),
    "underhand_lat_pulldown": _ex(
        "pull_compound", "cable", "vertical_pull",
        {"back": "primary", "biceps": "secondary"},
        BACK_NO_ERECTOR + BI_HALF, ("forearms",), "low", "compound", grip="supinated"),
    "neutral_grip_pullup": _ex(
        "pull_compound", "bodyweight_assist", "vertical_pull",
        {"back": "primary", "biceps": "secondary", "forearms": "secondary"},
        BACK_NO_ERECTOR + BI_HALF + FOREARM_HALF,
        ("abs",), "med", "compound", grip="neutral"),
    "kettlebell_swing": _ex(
        "kettlebell_swing", "kettlebell", "hinge",
        {"glutes": "primary", "hamstrings": "secondary"},
        GLUTE_FULL + HAMS_HALF, ("abs", "back_erectors", "forearms"),
        "med", "compound", grip="pronated"),
    "kettlebell_goblet_squat": _ex(
        "squat", "kettlebell", "squat",
        {"quads": "primary", "glutes": "secondary"},
        QUADS_EVEN + GLUTE_HALF + ADDUCTORS,
        ("abs", "back_erectors", "forearms"), "med", "compound"),
    "single_arm_kettlebell_row": _ex(
        "pull_compound", "kettlebell", "horizontal_pull",
        {"back": "primary", "biceps": "secondary", "forearms": "secondary"},
        BACK_NO_ERECTOR + BI_HALF + FOREARM_HALF,
        ("abs", "back_erectors"), "med", "compound", grip="neutral", unilateral=True),
    "kettlebell_clean": _ex(
        "kettlebell_clean", "kettlebell", "hinge",
        {"glutes": "primary", "hamstrings": "secondary"},
        GLUTE_FULL + HAMS_HALF, ("abs", "back_erectors", "forearms", "front_delt"),
        "med", "compound", unilateral=True),
    "trap_bar_deadlift": _ex(
        "trap_bar_hinge", "trap_bar", "hinge",
        {"quads": "primary", "glutes": "primary", "hamstrings": "secondary",
         "forearms": "secondary"},
        QUADS_EVEN + GLUTE_FULL + HAMS_HALF + FOREARM_HALF,
        ("abs", "back_erectors", "back_upper"), "high", "compound", grip="neutral"),
    "trap_bar_shrug": _ex(
        "shrug", "trap_bar", "isolation",
        {"back": "primary", "forearms": "secondary"},
        (("back_upper", 1.0, "functional"), ("back_lats", 0.0, "functional")) + FOREARM_HALF,
        ("abs", "back_erectors"), "low", "isolation", grip="neutral"),
    "ez_bar_curl": _ex(
        "curl", "ez_bar", "isolation", {"biceps": "primary"},
        BI_FULL, ("forearms",), "low", "isolation", grip="supinated"),
    "ez_bar_reverse_curl": _ex(
        "reverse_curl", "ez_bar", "isolation",
        {"forearms": "primary", "biceps": "secondary"},
        (("brachioradialis", 0.5, "even"), ("forearm_extensors", 0.5, "even")) + BI_HALF,
        (), "low", "isolation", grip="pronated"),
    "medicine_ball_slam": _ex(
        "ball_slam", "medicine_ball", "hinge",
        {"abs": "primary", "back": "secondary", "shoulders": "secondary"},
        ABS + (("back_lats", 0.25, "even"), ("back_upper", 0.25, "even"),
               ("front_delt", 0.5, "functional")),
        ("glute_max", "back_erectors", "forearms"), "med", "compound"),
    "rotational_medicine_ball_throw": _ex(
        "ball_rotation", "medicine_ball", "core", {"abs": "primary"},
        ABS, ("glute_max", "front_delt", "back_erectors"),
        "med", "isolation", unilateral=True),
    # core -- holds (seconds are asked, never filled)
    "plank": _ex("plank", "bodyweight", "core", {"abs": "primary"}, ABS,
                 ("front_delt", "glute_max"), "low", "hold"),
    "side_plank": _ex("plank", "bodyweight", "core", {"abs": "primary"}, ABS,
                      ("glute_med", "front_delt"), "low", "hold",
                      unilateral=True),
    # 2026-09-29 goal practice rows (breath_trunk / whole_body picks). Only
    # the matching practice slot offers them (compose_rank_rules.json
    # practice_effects); shares are accounting estimates, not measurements.
    # tempo 3030 (3 s up, 3 s down): a slow controlled movement, so its sets
    # count toward controlled_tempo_share_sets (Pilates = controlled
    # movement, not holds; owner 2026-09-30 19:51). Seeded as ax_exercise.tempo.
    "roll_down": _ex("crunch", "bodyweight", "core", {"abs": "primary"}, ABS,
                     (), "low", "isolation", tempo="3030"),
    "hollow_hold": _ex("plank", "bodyweight", "core", {"abs": "primary"}, ABS,
                       ("front_delt",), "low", "hold"),
    "bear_crawl": _ex(
        "crawl", "bodyweight", "core",
        {"abs": "primary", "shoulders": "secondary", "quads": "secondary"},
        ABS + (("front_delt", 0.5, "functional"), ("quads", 0.5, "group")),
        ("glute_max", "back_upper"), "low", "isolation"),
    "turkish_get_up": _ex(
        "get_up", "kettlebell", "core",
        {"abs": "primary", "shoulders": "secondary", "glutes": "secondary"},
        ABS + (("front_delt", 0.5, "functional"),) + GLUTE_HALF,
        ("glute_med", "back_upper", "forearms"), "med", "isolation"),
}

# Lifts that already had a pattern + fatigue row but NO muscle map (so the
# planner could never offer them). Only the missing tables are written; their
# existing pattern / fatigue rows are asserted equal by the test.
CLOSE_GAPS = {
    "smith_seated_calf_raise": _ex("calf_raise", "smith_machine", "isolation",
                                   {"calves": "primary"},
                                   CALF_SEATED, (), "low", "isolation"),
    "wall_sit": _ex("wall_sit", "bodyweight", "squat", {"quads": "primary"},
                    QUADS_SQUAT, ("glute_max",), "low", "hold"),
}

# New movement names -> movement_muscle_base rows (preset reconstruction).
NEW_MOVEMENTS = {
    "kettlebell_swing": {"glutes": "primary", "hamstrings": "secondary"},
    "kettlebell_clean": {"glutes": "primary", "hamstrings": "secondary"},
    "trap_bar_hinge": {"quads": "primary", "glutes": "primary", "hamstrings": "secondary"},
    "reverse_curl": {"forearms": "primary", "biceps": "secondary"},
    "ball_slam": {"abs": "primary", "back": "secondary", "shoulders": "secondary"},
    "ball_rotation": {"abs": "primary"},
    "close_grip_press": {"triceps": "primary", "chest": "secondary",
                         "shoulders": "secondary"},
    "shrug": {"back": "primary"},
    "glute_extension": {"glutes": "primary"},
    "flat_press": {"chest": "primary", "triceps": "secondary",
                   "shoulders": "secondary"},
    "dip": {"chest": "primary", "triceps": "primary", "shoulders": "secondary"},
    "hip_thrust": {"glutes": "primary", "hamstrings": "secondary"},
    "hip_abduction": {"glutes": "primary"},
    "single_leg_hinge": {"hamstrings": "primary", "glutes": "primary"},
    "hinge_bilateral": {"hamstrings": "primary", "glutes": "secondary"},
    "plank": {"abs": "primary"},
    "wall_sit": {"quads": "primary"},
    "crawl": {"abs": "primary", "shoulders": "secondary", "quads": "secondary"},
    "get_up": {"abs": "primary", "shoulders": "secondary", "glutes": "secondary"},
}

# Stabilizer roles of the lifts that were already in the seed (spec A2.4 draft
# seed, restricted to nodes that exist; () = none, stated on purpose).
EXISTING_STABILIZERS = {
    "back_squat": ("back_erectors", "abs", "adductors"),
    "barbell_row": ("back_erectors", "forearms", "rear_delt"),
    "bicep_curl": ("forearms",),
    "bulgarian_split_squat": ("glute_med", "adductors"),
    "cable_crunch": (),
    "cable_fly": (),
    "cable_lateral_raise": (),
    "chest_press_machine": (),
    "chest_supported_t_bar_row": ("forearms",),
    "chinup": ("forearms",),
    "deadlift": ("back_erectors", "forearms", "adductors"),
    "face_pull": (),
    "hammer_curl": (),
    "incline_barbell_press": ("back_upper",),
    "incline_dumbbell_curl": ("forearms",),
    "incline_dumbbell_press": ("back_upper",),
    "lat_pulldown": ("forearms",),
    "leg_curl": (),
    "leg_raise": ("quads",),
    "overhead_press": ("abs", "back_erectors"),
    "overhead_press_smith_seated": (),
    "pendlay_row": ("back_erectors", "forearms", "rear_delt"),
    "preacher_curl": (),
    "pullup": ("forearms", "abs"),
    "rdl": ("back_erectors", "forearms", "adductors"),
    "reverse_pecdec": (),
    "seated_calf_raise": (),
    "single_leg_extension": (),
    "standing_calf_raise": ("abs",),
    "tricep_overhead_extension": (),
    "tricep_pushdown_rope": (),
    "v_squat": (),
}

SEEDABLE_EQUIPMENT = ("barbell", "dumbbell", "ez_bar", "t_bar",
                      "bodyweight_assist", "bodyweight", "kettlebell",
                      "trap_bar", "medicine_ball")
FREEWEIGHT_EQUIPMENT = ("barbell", "dumbbell", "ez_bar", "t_bar", "kettlebell",
                        "trap_bar", "medicine_ball")
# Keep previously shipped ULIDs stable. An existing seeded DB may already
# hold 17-31; reusing one for a new name would silently skip that new row.
ORIGINAL_AX_NAMES = (
    'bench_press', 'bodyweight_lunge', 'dip', 'dumbbell_bench_press',
    'dumbbell_curl', 'dumbbell_lateral_raise', 'dumbbell_row',
    'dumbbell_shoulder_press', 'goblet_squat', 'hip_thrust',
    'lying_triceps_extension', 'push_up', 'reverse_lunge',
    'single_leg_rdl', 'walking_lunge',
    # Previously shipped expansion IDs 32 onward, in their original order.
    'box_squat',
    'chest_supported_dumbbell_row',
    'dumbbell_rdl',
    'front_squat',
    'incline_push_up',
    'kettlebell_deadlift',
    'landmine_press',
    'step_up',
    # Shipped strength expansion IDs 40 onward; append-only.
    'crunch',
    'dumbbell_overhead_triceps_extension',
    'dumbbell_standing_calf_raise',
    'dumbbell_triceps_kickback',
    'inverted_row',
    'pike_push_up',
    'reverse_crunch',
    'seated_dumbbell_reverse_fly',
    'single_arm_dumbbell_bench_press',
    'single_arm_dumbbell_lateral_raise',
    'single_leg_calf_raise',
    # Barbell staples; reserve these IDs before any future expansion.
    'barbell_glute_bridge',
    'barbell_reverse_lunge',
    'barbell_seal_row',
    'barbell_shrug',
    'barbell_split_squat',
    'close_grip_bench_press',
    'decline_bench_press',
    'dumbbell_crunch',
    'good_morning',
    'sumo_deadlift',
    # Grip/equipment additions, IDs 61 onward; append-only.
    'ez_bar_curl',
    'ez_bar_reverse_curl',
    'kettlebell_clean',
    'kettlebell_goblet_squat',
    'kettlebell_swing',
    'medicine_ball_slam',
    'neutral_grip_pullup',
    'rotational_medicine_ball_throw',
    'single_arm_kettlebell_row',
    'trap_bar_deadlift',
    'trap_bar_shrug',
    'underhand_barbell_row',
    # Goal practice rows (2026-09-29); append-only.
    'bear_crawl',
    'roll_down',
    'turkish_get_up',
)

# Technical lifts require an explicit compose profile opt-in. This is catalog
# metadata only; it does not change taxonomy rows or volume credit.
for _table in (CATALOG, CLOSE_GAPS):
    for _name, _entry in _table.items():
        _entry['technical'] = any(token in _name for token in
                                  ('clean', 'snatch', 'swing', 'turkish', 'get_up', 'jerk', 'slam', 'throw'))

AX_ULID_START = 17          # 01KZAXEX...0001-0016 are the 2026-09-14 rows
AX_STAMP = "2026-09-26T00:00:00Z"


def stabilizers(name):
    """Stabilizer nodes of a shipped lift, or None when unknown."""
    for table in (CATALOG, CLOSE_GAPS):
        if name in table:
            return table[name]["stabilizers"]
    return EXISTING_STABILIZERS.get(name)


def _q(v):
    return "NULL" if v is None else "'%s'" % v


def _w(w):
    return repr(float(w))


def sql_lines():
    """The generated seed block, statement per line, fixed order."""
    out = []
    names = sorted(CATALOG)
    gaps = sorted(CLOSE_GAPS)
    both = sorted(names + gaps)
    allx = dict(CATALOG, **CLOSE_GAPS)
    out.append("-- exercise_muscle_map (+%d rows)" % sum(
        len(allx[n]["muscles"]) for n in both))
    for n in both:
        for m in sorted(allx[n]["muscles"]):
            out.append("INSERT OR IGNORE INTO exercise_muscle_map VALUES"
                       "(%s,%s,%s);" % (_q(n), _q(m), _q(allx[n]["muscles"][m])))
    out.append("-- exercise_subregion_map (+%d rows)" % sum(
        len(allx[n]["subregions"]) for n in both))
    for n in both:
        for sub, w, grade in sorted(allx[n]["subregions"]):
            out.append("INSERT OR IGNORE INTO exercise_subregion_map VALUES"
                       "(%s,%s,%s,%s);" % (_q(n), _q(sub), _w(w), _q(grade)))
    out.append("-- exercise_movement_grip (+%d rows)" % len(both))
    for n in both:
        e = allx[n]
        out.append("INSERT OR IGNORE INTO exercise_movement_grip VALUES"
                   "(%s,%s,%s,%s);" % (_q(n), _q(e["movement"]),
                                       _q(e["equipment"]), _q(e["grip"])))
    out.append("-- exercise_fatigue_cost (+%d rows)" % len(names))
    for n in names:
        out.append("INSERT OR IGNORE INTO exercise_fatigue_cost VALUES"
                   "(%s,%s,'explicit');" % (_q(n), _q(CATALOG[n]["fatigue"])))
    out.append("-- exercise_pattern (+%d rows)" % len(names))
    for n in names:
        out.append("INSERT OR IGNORE INTO exercise_pattern VALUES(%s,%s);"
                   % (_q(n), _q(CATALOG[n]["pattern"])))
    out.append("-- movement_muscle_base (+%d rows)" % sum(
        len(v) for v in NEW_MOVEMENTS.values()))
    for mv in sorted(NEW_MOVEMENTS):
        for m in sorted(NEW_MOVEMENTS[mv]):
            out.append("INSERT OR IGNORE INTO movement_muscle_base VALUES"
                       "(%s,%s,%s);" % (_q(mv), _q(m), _q(NEW_MOVEMENTS[mv][m])))
    seed = [n for n in names if CATALOG[n]["equipment"] in SEEDABLE_EQUIPMENT
            and CATALOG[n]["movement"] not in HOLD_MOVEMENTS]
    out.append("-- ax_exercise (+%d rows, same derivation rule as above)"
               % len(seed))
    new_names = sorted(set(seed) - set(ORIGINAL_AX_NAMES))
    ids = {name: AX_ULID_START + i for i, name in
           enumerate(ORIGINAL_AX_NAMES)}
    ids.update({name: AX_ULID_START + len(ORIGINAL_AX_NAMES) + i
                for i, name in enumerate(new_names)})
    for n in seed:
        e = CATALOG[n]
        ulid = "01KZAXEX%018d" % ids[n]
        movement = "isolation" if e["pattern"] == "isolation" else "compound"
        load = ("freeweight" if e["equipment"] in FREEWEIGHT_EQUIPMENT
                else "bodyweight")
        out.append(
            "INSERT OR IGNORE INTO ax_exercise SELECT '%s',@@OWNING_AGENT@@,"
            "'%s','%s','reps','%s',%s,NULL,NULL,'active','%s','%s' WHERE "
            "NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='%s');"
            % (ulid, n, movement, load, _q(e.get("tempo")), AX_STAMP,
               AX_STAMP, n))
    return out


BLOCK_BEGIN = "-- @@CATALOG-2026-09-26 BEGIN (generated: exercise_catalog.py --emit-sql)"
BLOCK_END = "-- @@CATALOG-2026-09-26 END"


def main(argv):
    if argv[1:] != ["--emit-sql"]:
        sys.stderr.write("usage: exercise_catalog.py --emit-sql\n")
        return 2
    print(BLOCK_BEGIN)
    for line in sql_lines():
        print(line)
    print(BLOCK_END)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
