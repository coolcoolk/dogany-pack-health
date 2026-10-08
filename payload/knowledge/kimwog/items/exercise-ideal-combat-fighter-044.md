---
# Body-ideal archetype sprint 2026-09-30. "격투기 선수 같은 몸" -- mixed
# power-endurance at a fixed weight class. Filed with the weight-cut conflict
# stated in the open: the sport's own nutrition position stand describes
# supervised acute water cuts, and the pack's safety boundary catches
# dehydration to make a number (exercise/harm-route-boundary-031).
id: exercise/ideal-combat-fighter-044
domain: exercise
grade: A (position stand -- energy-system demands and weight-cut practice as described); D (archetype picture)
lane: "@performance-lit"
locale: universal
as_of: 2025
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/40059405/"  # Ricci AA et al. J Int Soc Sports Nutr 2025 -- ISSN position stand, MMA and combat sports: matches >4 min can be >70% aerobic with alactic/glycolytic bursts; off-camp weight 12-15% above division; supervised acute water loss ~2-4% within 24 h described; 'long-term effects of frequent weight cuts on health and performance are unknown'
  - "https://pubmed.ncbi.nlm.nih.gov/24864135/"  # Helms 2014 -- dehydration and electrolyte manipulation can be dangerous (physique context)
  - "exercise/harm-route-boundary-031"
  - "exercise/ideal-crossfit-functional-036"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE AGENT DOES NOT COACH A WATER CUT. The position stand describes
      supervised acute dehydration as practice in the sport and states the
      long-term health effects of frequent cuts are unknown. Under the pack's
      boundary, dehydration to make a number is a caught route: keep the goal
      (fight at a weight class, look and move like a fighter), refuse the
      route, dissuade once, and point to the athlete's supervised team for
      anything about a real weigh-in. Marked contested because the sport's own
      body sanctions what this pack refuses.
    grade: A
claim: >
  The combat / fighter ideal is a lean, dense, mobile body built for repeated
  high-power bursts over several minutes: strong through hips, trunk, neck and
  grip, with a large aerobic base (a bout longer than about four minutes can
  draw more than 70 percent of its energy aerobically, with alactic and
  glycolytic bursts on top), at or near a weight class. It is distinguished from
  CrossFit-type fitness by the fixed body-weight class, contact and the
  skill-specific demands, and from endurance by the repeated-burst profile. The
  sport's own nutrition position stand describes acute weight cutting whose
  long-term effects are unknown; the pack does not coach that route.
reasoning: >
  Energy-system demands and weight-cut practice are taken from the ISSN 2025
  position stand, which is the authoritative description of the sport's
  practice (graded as a position stand of what IS done, not an endorsement).
  The conflict with the pack's safety boundary is carried as a refraction note
  and the contested flag.
---

# exercise/ideal-combat-fighter-044 -- 격투기 선수형

**한 줄 그림:** 군살 없이 단단하고, 몇 분 동안 폭발적인 동작을 반복해도 숨이 버티는 몸 -- 체급 안에서.

## Distinguishing features

Repeated power bursts + aerobic base; trunk/neck/grip strength; mobility for
kicks and ground work; weight class.

## Measurable here

- `body_weight` (class), `body_fat_pct`, `skeletal_muscle_kg`.
- `e1rm_<lift>` for a lower-body and a pulling compound.
- Workouts `minutes` / `avg_hr` for conditioning and sparring logged as
  sessions; practice picks `conditioning`, `power`, `mixed_circuit`.

## Not measurable here

Round-based work capacity, repeated-sprint ability, skill, grip strength, neck
strength, hydration status. No tokens.

## Training emphasis and practice

Interval conditioning matched to round length, strength and power twice a week,
trunk and neck, mobility. Gradual long-term weight management (not acute cuts).

## Failure modes

Acute weight cuts (caught route); concussion and contact injury (sport, not
gym); overtraining from stacking sparring on hard lifting.

## Combines / conflicts

Close to CrossFit-type fitness (work capacity) with a weight constraint;
conflicts with open bodybuilding mass and with powerlifting if the class is
light.

Grappling-first ideals (씨름, wrestling, judo, BJJ -- grip, clinch, lift and
throw, possibly a heavy class) are their own row:
exercise/ideal-grappler-ssireum-wrestler-047. This row stays the
striking-leaning / MMA picture.
