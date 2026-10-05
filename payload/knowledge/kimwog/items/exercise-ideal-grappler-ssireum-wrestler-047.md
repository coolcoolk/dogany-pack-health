---
# Body-ideal archetype sprint, pass 2 (owner ask 2026-09-30 19:57/20:02).
# "씨름 선수 / 레슬러 몸" -- the owner's example: thick trunk, neck and grip,
# hip drive, an isometric-dynamic mix. Split off from the combat row (044),
# which reads striking-first (round-based bursts, lean at a class). Grappling
# pulls the whole force-velocity curve UP (maximal strength), spends much of
# the bout in grip and clinch isometrics, and in 씨름 runs to a 140 kg open
# class -- so its body-weight direction can be UP, the opposite of 044.
id: exercise/ideal-grappler-ssireum-wrestler-047
domain: exercise
grade: A (rule text -- how a 씨름 bout is contested, as a definition); B (reviews -- grappler physiological profile); C (weight classes via press, not the federation rulebook); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 2001-2019
contested: yes
sources:
  - "https://ich.unesco.org/en/RL/traditional-korean-wrestling-ssirum-ssireum-01533"  # UNESCO Representative List 2018 (joint DPRK/ROK inscription) -- 'two opponents try to push each other to the ground using a satpa (a fabric strap connecting the waist and leg)'; techniques use torso, hands and legs. (The common 'any body part above the knee touches the ground' loss rule is NOT in this text; not relied on.)
  - "https://www.korea.net/NewsFocus/Culture/view?articleId=165752"  # Korea.net 2018 -- wrestlers grab the satba wrapped round the opponent's waist and one thigh and try to knock the opponent down
  - "http://www.samdailbo.com/news/articleView.html?idxno=158407"  # press 2021-02-13 -- men's 민속씨름 classes: 백두 140 kg, 한라 105, 금강 90, 태백 <=80
  - "https://www.idomin.com/news/articleView.html?idxno=763109"  # press explainer of amateur classes by school level: university/general 경장 <=75 kg up to 장사 <=140 kg
  - "https://pubmed.ncbi.nlm.nih.gov/28030533/"  # Chaabene H et al. J Strength Cond Res 2017 -- wrestler attributes review: anaerobic power/capacity discriminate successful wrestlers across ages, classes and styles; maximal dynamic, ISOMETRIC and explosive strength and strength endurance closely related to high-level performance; flexibility not a key variable
  - "https://pubmed.ncbi.nlm.nih.gov/26993133/"  # James LP et al. Sports Med 2016 -- systematic review, 23 studies, grappling vs striking: grappling's high-force demands shift the whole force-velocity curve up via maximal strength; striking shows smaller force gains and more velocity-end gains; greater aerobic power generally not what separates superior competitors
  - "https://pubmed.ncbi.nlm.nih.gov/11482542/"  # Tsuyama K et al. Eur J Appl Physiol 2001 -- college wrestlers: higher isometric cervical extension strength and larger neck-extensor CSA than judo athletes
  - "https://pubmed.ncbi.nlm.nih.gov/27632843/"  # Lee K et al. J Sport Rehabil 2017 -- critically appraised topic: no study links cervical strength to neck-injury risk in wrestling; evidence poor
  - "https://pubmed.ncbi.nlm.nih.gov/30899740/"  # Rhi S et al. J Exerc Rehabil 2019 -- college ssireum athletes, short-term weight reduction programme with a 50% limited diet (n=6)
  - "https://pubmed.ncbi.nlm.nih.gov/26644679/"  # Noh JW et al. J Phys Ther Sci 2015 -- 25 elite ssireum athletes: left-right lean-mass and torque asymmetries (arms and legs)
  - "exercise/ideal-combat-fighter-044"
  - "exercise/ideal-powerlifting-040"
  - "exercise/harm-route-boundary-031"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      HOW THIS DIFFERS FROM THE COMBAT ROW (044). 044 is the striking-leaning
      fighter: repeated bursts over rounds on an aerobic base, lean at a
      class, mobility for kicks. The grappler is force-first: maximal and
      isometric strength (grip fights, clinch, the satba hold), hip drive to
      lift and turn an opponent, a thick neck and trunk that resist being
      bent. Separate the two by asking what the user pictures -- being hit and
      moving (044) or gripping, lifting and throwing (047). MMA sits between
      them and keeps the 044 row.
    grade: B
  - note: >
      THE HEAVY END IS A SPORT CATEGORY, NOT A HEALTH TARGET. 백두급 runs to
      140 kg; wanting "a 씨름 body" never licenses gaining fat to a class, and
      making a lighter class by acute dieting or dehydration (a college
      ssireum programme used a 50% restricted diet) is the caught route of
      exercise/harm-route-boundary-031 -- same stance as 044. Contested for
      that reason: the sport's own practice includes what the pack refuses.
    grade: D
claim: >
  The grappler / 씨름 / wrestler ideal is a thick, strong body built to grip,
  lift and turn another person: a heavy trunk and neck, strong hips and legs
  for drive, and grip and upper-back strength that holds for long isometric
  contests, on top of high anaerobic power and enough aerobic fitness to
  recover between efforts. Reviews of wrestlers find anaerobic power and
  maximal, isometric and explosive strength separate better from worse
  athletes while flexibility does not, and grappling athletes shift the whole
  force-velocity curve upward where strikers gain mostly at the speed end.
  In 씨름 the bout is won by putting the opponent down while both hold the
  satba, and the classes run from 80 kg to 140 kg, so the ideal may be heavy.
  It differs from the combat/striking row by being force- and grip-first and
  not necessarily lean, and from powerlifting by the grip, the isometric-
  dynamic mix against a moving opponent and the conditioning.
reasoning: >
  The rule of the bout is the UNESCO inscription text (a definition, graded as
  rule). The class limits are from two press explainers, not the federation rulebook itself, so they carry a lower grade.
  The profile is a narrative review of wrestlers (Chaabene 2017) plus a
  systematic review that explicitly contrasts grappling and striking (James
  2016). Neck findings are one cross-sectional comparison; the neck-injury
  benefit of neck training is unproven (Lee 2017). The picture and gym
  translation are craft.
---

# exercise/ideal-grappler-ssireum-wrestler-047 -- 씨름 / 레슬러 / 그래플러형

**한 줄 그림:** 굵은 몸통과 목, 놓지 않는 악력, 상대를 들어 돌리는 엉덩이 힘 -- 버티다가 한순간 터뜨리는 몸.

## Distinguishing features

Maximal and isometric strength over speed; grip and upper-back holding; hip
drive (lift, turn, throw); thick neck and trunk; anaerobic power with an
aerobic base. Body weight can go UP (heavy classes), unlike the striking row.

## Measurable here

- `e1rm_<deadlift>`, `e1rm_<squat>` (hip drive), `e1rm_<row>` or pulling.
- `zero_load_control_share_sets` -- a partial fit for the isometric side
  (holds, carries logged as holds).
- `body_weight`, `skeletal_muscle_kg`, `body_fat_pct` (class and
  composition context).
- Segmental `lean_trunk_kg` / arm-leg asymmetry (readable, not a strand token;
  elite ssireum athletes show left-right differences); mat sessions as
  workouts `minutes`.

## Not measurable here

Grip strength, neck strength or girth, carries, anaerobic power, the isometric
duration of a hold. Proposed: `grip_kg`, `neck_cm`, `carry_kg_m_<carry>`.

## Training emphasis and practice

Heavy hip-hinge and squat, rows and pulls, loaded carries and isometric
holds (static-dynamic pairing: hold then drive), grip work (towel / thick
handle), neck strengthening progressed gently, rotational trunk work, short
high-intensity intervals. Picks: `power`, `mixed_circuit`, `conditioning`.

## Failure modes

Weight manipulation for a class (caught route); lower-back and neck overload;
left-right asymmetry left unaddressed; loss of conditioning behind pure
strength work.

## Combines / conflicts

Aligns with powerlifting (max strength) and weightlifting/athletic power (hip
drive); overlaps the combat row in conditioning. Conflicts with endurance and
climbing (strength-to-weight), and with men's physique leanness if the user
wants a heavy class.
