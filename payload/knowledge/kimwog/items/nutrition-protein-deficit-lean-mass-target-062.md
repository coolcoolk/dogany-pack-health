---
# Meal-protein sprint 2026-10-06 (dispatch task kw-meal-protein). Owns the
# DEFICIT protein target: how much daily protein to aim for while losing weight
# and trying to keep lean mass, including the older-adult floor and the kidney
# boundary. Item 002 keeps the general (energy-balance) 1.4-2.0 g/kg range;
# this item takes over the hypocaloric carve-out that 002's refraction note
# used to carry, because the re-audit found that carve-out was quoted in the
# wrong unit (see note 1). Every abstract below was re-read via PubMed
# E-utilities on 2026-10-06; Morton 2018 breakpoint CI and p-value were read in
# the Europe PMC full text; Refalo 2025 from the AUT open repository record.
# Item number >= 062 per dispatcher (sibling branches hold 057-061).
id: nutrition/protein-deficit-lean-mass-target-062
domain: nutrition
lane: "@obs-inferential"
grade: B
locale: universal
as_of: 2013-2026
contested: yes
sources:
  - "https://doi.org/10.1123/ijsnem.2017-0273"  # Hector AJ, Phillips SM. Protein recommendations for weight loss in elite athletes: a focus on body composition and performance. Int J Sport Nutr Exerc Metab 2018;28(2):170-177. PMID 29182451 -- current deficit recommendation 1.6-2.4 g/kg/day, end of range set by deficit severity and training
  - "https://doi.org/10.3945/ajcn.115.119339"  # Longland TM, Oikawa SY, Mitchell CJ, Devries MC, Phillips SM. Am J Clin Nutr 2016;103(3):738-746. PMID 26817506 -- RCT, n=40 young men, ~40% deficit, 4 wk, RT+HIIT 6 d/wk: 2.4 vs 1.2 g/kg/day, LBM +1.2 vs +0.1 kg (4-compartment)
  - "https://doi.org/10.1096/fj.13-230227"  # Pasiakos SM, Cao JJ, Margolis LM, et al. FASEB J 2013;27(9):3837-3847. PMID 23739654 -- RCT, n=39 adults, 0.8 vs 1.6 vs 2.4 g/kg/day in a 31-day deficit: smaller FFM share of weight loss at 1.6 and 2.4 than at 0.8
  - "https://doi.org/10.1123/ijsnem.2013-0054"  # Helms ER, Zinn C, Rowlands DS, Brown SR. Int J Sport Nutr Exerc Metab 2014;24(2):127-138. PMID 24092765 -- systematic review (6 studies, 13 groups): 2.3-3.1 g/kg of FAT-FREE MASS, scaled up with deficit severity and leanness
  - "https://doi.org/10.1519/SSC.0000000000000888"  # Refalo MC, Trexler ET, Helms ER. Effect of dietary protein on fat-free mass in energy restricted, resistance-trained individuals: an updated systematic review with meta-regression. Strength Cond J 2025 (online 2025-01-22). 29 studies, Bayesian: >97% probability of a linear dose-response; per g/kgBM beta 0.07 (95% HDI -0.01 to 0.14), per g/kgFFM beta 0.06 (0.01 to 0.12); authors call the findings exploratory. Not PubMed-indexed; read at openrepository.aut.ac.nz handle 10292/18694
  - "https://doi.org/10.1007/s40279-026-02494-5"  # Lopez-Moreno M, Quesada G, Lopez-Gil JF. Sports Med 2026 (online 2026-08-06). PMID 42560437 -- Current Opinion re-analysing Refalo's studies: higher BASELINE protein intake may mean diminishing returns from more protein
  - "https://doi.org/10.1136/bjsports-2017-097608"  # Morton RW, Murphy KT, McKellar SR, et al. Br J Sports Med 2018;52(6):376-384. PMID 28698222, PMC5867436 -- 49 RCTs, mostly energy balance: breakpoint 1.62 g/kg/day, 95% CI 1.03-2.20, biphasic fit p=0.079; authors suggest ~2.2 as the prudent upper figure
  - "https://doi.org/10.1002/jcsm.12922"  # Nunes EA, Colenso-Semple L, McKellar SR, et al. J Cachexia Sarcopenia Muscle 2022;13(2):795-810. PMID 35187864 -- 74 RCTs: LBM benefit at >=1.6 g/kg/day under 65, at 1.2-1.59 g/kg/day at 65+, with RT (moderate certainty)
  - "https://doi.org/10.1111/sms.14075"  # Murphy C, Koehler K. Scand J Med Sci Sports 2022;32(1):125-137. PMID 34623696 -- meta-regression: an energy deficit of ~500 kcal/day prevented RT lean-mass gains; strength gains were spared
  - "https://doi.org/10.1093/nutrit/nuv065"  # Kim JE, O'Connor LE, Sands LP, Slebodnik MB, Campbell WW. Nutr Rev 2016;74(3):210-224. PMID 26883880 -- 20 RCTs, adults >50 losing weight: higher protein (>=25% energy or >=1.0 g/kg/day) retained more lean mass
  - "https://doi.org/10.1016/j.jamda.2013.05.021"  # Bauer J, Biolo G, Cederholm T, et al. PROT-AGE Study Group. J Am Med Dir Assoc 2013;14(8):542-559. PMID 23867520 -- >65 y: at least 1.0-1.2 g/kg/day; >=1.2 if active; 1.2-1.5 with acute or chronic disease; eGFR <30 not on dialysis is the exception
  - "https://doi.org/10.1016/j.clnu.2014.04.007"  # Deutz NE, Bauer JM, Barazzoni R, et al. ESPEN Expert Group. Clin Nutr 2014;33(6):929-936. PMID 24814383 -- healthy older people at least 1.0-1.2; malnourished or ill 1.2-1.5 g/kg/day
  - "https://doi.org/10.1093/jn/nxy197"  # Devries MC, Sithamparapillai A, Brimble KS, Banfield L, Morton RW, Phillips SM. J Nutr 2018;148(11):1760-1775. PMID 30383278 -- 28 RCTs, adults WITHOUT kidney disease: change in GFR did not differ on higher-protein diets
  - "https://doi.org/10.1016/j.kint.2023.10.018"  # KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of CKD. Kidney Int 2024;105(4S):S117-S314. PMID 38490803 -- CKD G3-G5 not on dialysis: 0.8 g/kg/day; avoid >1.3 g/kg/day in CKD at risk of progression (2C)
  - "https://doi.org/10.1186/s12970-017-0177-8"  # Jager R, et al. ISSN position stand: protein and exercise. J Int Soc Sports Nutr 2017;14:20. PMID 28642676 -- the stand that carries "2.3-3.1 g/kg/d" for hypocaloric lean-mass retention WITHOUT the fat-free-mass qualifier of its source (re-audit note 1)
  - "source:nutrition/protein-intake-002 -- the general (energy-balance) daily range; its hypocaloric note is corrected by this item"
  - "source:nutrition/weight-loss-rate-lean-mass-012 -- the rate-of-loss side of the same question"
  - "source:nutrition/energy-availability-threshold-010 -- the floor below which a deficit stops being a diet question"
  - "source:nutrition/body-composition-measurement-floor-011 -- why a user cannot verify lean-mass retention week to week"
  - "source:nutrition/self-report-underreporting-007 -- the logged intake is a floor, not the true intake"
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: ask
      rescale:
        per_unit_low: 1.6     # g protein per kg body weight per day, deficit + resistance training
        per_unit_high: 2.4
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: body_fat_pct
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: renal_condition
      type: categorical
      role: hard
      unknown_policy: hedge
      gate:
        allowed: [none, healthy]
refraction_notes:
  - note: >
      RE-AUDIT, UNIT ERROR CORRECTED. The often-quoted 2.3-3.1 g/kg band for
      keeping lean mass in a deficit comes from Helms 2014, which states it per
      kilogram of FAT-FREE MASS. The ISSN 2017 stand reprinted it as g/kg/d with
      no qualifier, and nutrition/protein-intake-002 inherited that reading.
      Applied to body weight it overstates the target for anyone carrying body
      fat. At 20 percent body fat, 2.3-3.1 g/kg FFM is about 1.8-2.5 g/kg body
      weight, which sits inside the 1.6-2.4 g/kg body-weight band this item
      rescales. Never multiply 2.3-3.1 by total body weight.
    grade: A
  - note: >
      THE UPPER END IS NOT SETTLED. Under energy balance, Morton 2018 found a
      plateau near 1.6 g/kg (CI 1.03-2.20; the two-phase fit itself was not
      significant, p=0.079). In a deficit, Refalo 2025 found a linear rise with
      no plateau, but the per-body-weight slope interval crosses zero and the
      authors call the result exploratory. A 2026 commentary adds that people
      who already eat a lot of protein may gain less from more. Speak 1.6 as
      the evidence-backed floor and 2.4 as the upper end of current guidance.
      Do not present a figure above 2.4 g/kg body weight as needed.
    grade: B
  - note: >
      THE HIGH END IS FOR THE LEAN, THE LONG AND THE HARD-DIETING. Refalo's
      dose-response was stronger at lower body fat, in interventions longer than
      four weeks and in men. Hector and Phillips set the end of the range by
      deficit severity and training load. A user with plenty of body fat on a
      modest deficit is well served near the bottom of the band. A lean user on
      a long, steep cut is the case for the top.
    grade: C
  - note: >
      PROTEIN DOES NOT BUY BACK A STEEP DEFICIT. Across RT trials, a deficit of
      about 500 kcal/day was enough to stop lean-mass gains, while strength
      gains held. More protein is one lever. The size of the deficit (012) and
      continued resistance training are the others, and protein cannot replace
      either.
    grade: B
  - note: >
      OLDER ADULTS: A HIGHER FLOOR, A THINNER CEILING. For people over 65, the
      PROT-AGE and ESPEN expert groups set at least 1.0-1.2 g/kg/day, 1.2 or more
      for the active, and 1.2-1.5 with acute or chronic illness. In older adults
      losing weight, higher-protein diets kept more lean mass (20 RCTs). With
      resistance training, the lean-mass benefit appeared at 1.2-1.59 g/kg/day
      at 65+ (Nunes 2022). No trial was found that tests the 1.6-2.4 band in
      older adults who are dieting. For an older dieting user, the floor to
      speak is 1.2 g/kg. The 1.6-2.4 band is an extrapolation from younger
      samples (GAPS.md).
    grade: B
  - note: >
      KIDNEY BOUNDARY. In adults without kidney disease, higher-protein diets
      did not change GFR over time (28 RCTs). In stated chronic kidney disease
      the target here does NOT apply. KDIGO 2024 suggests 0.8 g/kg/day for CKD
      G3-G5 and avoiding more than 1.3 g/kg/day where CKD is at risk of
      progressing. That is a low-certainty (2C) recommendation, but it is the
      recommendation. When renal_condition is stated and is not none or
      healthy, withdraw the specific number and refer to the user's clinician.
      When it is unknown, give the number with the general-population caveat.
      Do not block it, because the healthy-adult kidney data are reassuring.
    grade: A
claim: >
  During an energy deficit with resistance training, daily protein of about
  1.6-2.4 g per kg of body weight is the current recommended range for keeping
  lean mass. The low end is the better-supported floor. The upper end is
  guidance, and the size of any benefit above the floor is unresolved. Two RCTs
  anchor the range. In a 31-day deficit, 1.6 and 2.4 g/kg both reduced the share
  of weight lost as fat-free mass compared with 0.8 g/kg. In a steep four-week
  deficit with intense training, 2.4 g/kg produced a lean-mass gain (+1.2 kg)
  where 1.2 g/kg produced none (+0.1 kg). The often-quoted 2.3-3.1 g/kg band is
  per kg of fat-free mass, not body weight. For adults over 65, expert groups set
  a floor of at least 1.0-1.2 g/kg/day, rising to 1.2 or more when active or
  ill. In older adults losing weight, higher protein retains more lean mass. In
  stated chronic kidney disease these targets do not apply.
reasoning: >
  The direction (more protein than the 0.8 g/kg adult RDA keeps more lean mass
  during weight loss) is consistent across controlled trials in young adults,
  athletes and older adults, and across expert groups. That puts the claim at the
  RCT-level band. It stops short of the top because the deficit-specific trials
  are small and short (n=39-40, 4-5 weeks). The one deficit-specific
  dose-response synthesis is self-described as exploratory, its body-weight slope
  interval crosses zero, and the energy-balance plateau it is set against was
  itself not statistically significant. That disagreement over the upper end is
  the contested flag. The floor is not contested. The re-audit finding is the
  part that changes a shipped number. The FFM-based 2.3-3.1 band lost its unit
  between Helms 2014 and the ISSN 2017 stand. Item 002 spoke it against body
  weight, which would hand a 90 kg user with 25 percent body fat a target of up
  to 279 g/day instead of about 209 g (3.1 x 67.5 kg FFM). That is a material
  overstatement, so this item takes ownership of the deficit target and 002's
  note is corrected to point here. The older-adult floor is expert consensus
  resting on tracer and RCT data. It is stated as a floor, not a ceiling, and
  the absence of a deficit trial in older adults at the athletic band is carried
  as a gap rather than filled by extrapolation. The kidney gate is hard because
  the one population with a guideline against high protein is exactly the one
  the healthy-adult GFR data exclude.
---

# nutrition/protein-deficit-lean-mass-target-062

When someone is losing weight and lifting, the protein question is how much to
eat so that the weight lost is mostly fat. The current answer is about 1.6 to 2.4
grams per kilogram of body weight a day. Two randomised trials carry most of the
weight. In one, both 1.6 and 2.4 g/kg protected fat-free mass better than the
standard adult allowance. In the other, young men on a steep four-week deficit
with hard training gained lean mass on 2.4 g/kg and none on 1.2 g/kg.

The top of the range is less certain than the bottom. A 2025 meta-regression of
29 deficit studies found the benefit kept rising with intake and never levelled
off. Its authors call that result exploratory, and the interval on the
body-weight slope includes zero. The best-known plateau estimate, around 1.6
g/kg, comes mostly from people who were not dieting, and its fitted curve was not
statistically significant either. So 1.6 is the floor to lean on. 2.4 is where
current guidance stops, not a proven extra gain.

One widely repeated number had the wrong unit. The 2.3 to 3.1 g/kg band traces
back to a 2014 review that gives it per kilogram of fat-free mass. A 2017
position stand reprinted it without that qualifier, and this warehouse's general
protein item picked it up. Multiplied by total body weight, it inflates the
target for anyone with body fat. Converted correctly, it lands inside the
1.6-2.4 band.

## 한국어 요약 (답변용)

- 감량 중에 근력 운동을 하면서 근육을 지키려면 단백질은 하루 **체중 1 kg당 1.6~2.4 g**이 현재 권고
  범위다. 근거가 단단한 쪽은 하한 1.6이다. 2.4는 지금 권고가 닿는 상한일 뿐, 더 먹으면 더 지켜진다는
  게 확인된 숫자가 아니다.
- 흔히 도는 "2.3~3.1 g/kg"는 **제지방량 1 kg당** 숫자다. 체중에 곱하면 과대 계산이 된다. 체지방
  20%인 사람이면 체중 기준 약 1.8~2.5 g/kg로, 위 범위 안에 들어온다.
- 범위의 위쪽은 마른 사람이 오래, 세게 감량할 때 쓰는 값이다. 체지방이 넉넉하고 적자가 크지 않으면
  아래쪽으로도 충분하다.
- 단백질로 큰 적자를 메울 수는 없다. 하루 500 kcal 정도의 적자에서도 근육 증가는 멈췄다(근력은
  유지). 적자 크기와 근력 운동 지속이 같이 가야 한다.
- 65세 이상은 평소에도 하루 최소 **1.0~1.2 g/kg**, 운동하거나 아프면 1.2 이상이 전문가 권고다.
  감량 중인 고령자에게는 1.2 g/kg를 하한으로 말한다. 1.6~2.4는 젊은 사람 연구에서 옮겨온 값이다.
- 만성 콩팥병이 있다고 밝힌 사람에게는 이 숫자를 주지 않고 담당 의료진에게 연결한다. KDIGO
  2024는 3~5기에서 0.8 g/kg를 권하고, 진행 위험이 있으면 1.3 g/kg를 넘기지 말라고 한다. 콩팥 질환이
  없는 성인에서는 고단백 식사가 사구체여과율 변화를 만들지 않았다.
