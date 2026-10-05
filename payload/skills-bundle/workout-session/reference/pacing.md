# multi-item delivery pacing + session wrap (read when a list of 3+ items, a proposal bundle, or the session end is coming)

## list-then-step-through (F23, generalises F1 routine table + F2 mat prep list)
- 3+ items: short overview list once (names, one per line), then one item at a time:
  item -> user reaction / done -> next.
- 1-2 items: no overview, go one by one.
- ONE decision question per message (owner: the problem is questions packed into one
  message, not their total; sessions run linear). overview = view only. give the anchor
  (first item), preview "N more", reveal the next only after each answer. never cut items
  to reduce questions.
- same rule for every owner-approval bundle (workout-program injury-lifecycle
  first-occurrence / pattern-spread candidates). no separate convention.
- "next" inside a sequence = the next item of the SAME bundle (2026-08-27: finishing mat
  drill 1 re-armed a working slot). stray working-slot arm already sent -> retract in text
  ("방금 뜬 세팅 안내는 무시해 주세요, 제때 다시 안내할게요").
- "N remaining" always names its unit (2026-08-27: "(남은 6개)" beside "총 20회" read as
  reps). say "이 뒤로 드릴 6개".

overview rendering (session-start enumerations, e.g. mat prep overview): inside a
triple-backtick fence, monospaced, space-aligned columns, no dash / em-dash separators.
short ack / intro above the fence.

overview labelling (G4):
- count atomic steps from stretch-matrix; a composite block ("풀/힌지 프렙") is a section
  header, not one item. item count = atomic steps.
- same drill both sides -> one line "스탠딩 햄스트링 스트레칭 (좌우)"; side order handled in
  the step. real alternating circuit rounds (카사크 스쿼트 1R/2R) keep their items.
- no bundle names (H1, 2026-08-24): never call several drills by one name, never coin
  one. "어깨 트리오" is retired and does not exist. 와이레이즈 / 시티드 어라운드 더 월드 /
  헤일로 (U1d/U1e/U1f) are separate drills, guided and closed one by one ("셋 다 끝났어요"
  banned). the name was removed from data because a surviving name gets used.

drill implement / weight = data only (H2; a kettlebell drill was cued with a nonexistent
plate weight "이전에 쓰시던 6kg"):
- source = prep.yaml `implement` / `load_kg`, already rendered into the drill text
  (`(케틀벨)` / `(케틀벨 6kg)`). none in text -> say no implement / no weight. never borrow
  from a similar drill, never estimate, never "가벼운 걸로".
- no provenance phrases ("이전에 쓰시던" / "지난번에 쓰신" / "평소 쓰시는") without a record.
- user states a weight -> write it to `load_kg`; until then keep silent about it.
- detail: reference/warmup-stretch.md.

## compound step auto-split (F5 / F11, every surface and modality)
one step bundling 2+ distinct actions -> split: each action gets its own message, own
done button, own checklist row. applies to mat prep, slot prep (W rows), warmup / ramp,
shoulder mobility, the start checklist table, the closing phase. sister of F23 (F23 =
rhythm across items; this = split within an item).

## session end
1. `pain.py recent` (pain-triage skill; `--days 1` for today). open events -> pain-triage
   phase 2 before the wrap. never defer to another day.
2. closing items (pain check, cooldown stretches, retro items): 3+ -> overview then one
   by one; 1-2 -> one by one. timed holds use the press-start countdown
   (reference/timers.md). overview never replaces one-by-one.
3. `session-closeout` stdout: the closeout card (owner 2026-10-02, lineup shape:
   `🏁 <split> 종료 · 분 · kcal`, `[v]`/`[ ]` rows with weight · sets · volume, `[갱신]`
   only when a lift beat its last session, `[부위별 부하]`, and the fatigue tail folded
   into its LAST line -- `회복 늦은 곳: <부위> · <언제>`) + one confirmation line under it
   if an exercise was created mid-session. relay the card as one code block, as-is; add
   no question and no summary of your own ("맞으면 그대로 둘게요": no answer = confirmed).
   spec: reference/progress-tables.md (4).
4. wrap + calorie card AUTO-posted (#46, owner 2026-08-19) on session end, including early
   end / skip ("시간없어 생략", "오늘 여기까지", "마무리하자"). skipping is not skipping the
   wrap; card covers what was done so far.
   - content: lifts / sets done, duration, kcal burned, pain / anomaly notes + calorie /
     diet card. label = rotation CODE verbatim.
   - watch ask first (#46-ext, owner 2026-08-21 16:08), exactly once: "오늘 운동 워치 기록
     있으면 공유해주세요, 없으면 추정할게요." shared -> use its measured kcal / duration;
     none / "없다" -> estimate at once, never re-ask. watch kcal = ACTIVE only (total
     double-counts resting burn in the day balance; kit workout-log rule). total may go in
     note as "총 Xkcal".
   - After actual cardio, use `service/health/cardio-record <modality> <minutes>
     --date <date> --db <kit db> --kit <kit_life.sh>`. The HealthKit ingest row
     wins when present; otherwise the command reads the latest measured
     bodyweight and writes an active-kcal MET estimate via the kit workout
     facade. The diet card reads that workout kcal through `agg-day`.
