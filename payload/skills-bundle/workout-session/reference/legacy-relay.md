# legacy-relay -- un-ledgered session relay rules

Reader: agent. Scope: un-ledgered sessions only (WARG_FLOW=0 or pre-ledger
session). Ledgered sessions (`flow` state exists for the sid): SKILL.md hard
rules govern; nothing here applies.

## cue-as-data
- movement instructions are data. Use the cue + fault already on the
  code-posted row keyboard; send no extra cue message, no improvised replacement prose.
- Delivery failed -> relay the complete numbered cue, fault and completion affordance once.
- Overview card unchanged.
- Run PREP_SET_CMD / PREP_TAP_CMD / RUNG_SET_CMD exactly as emitted: no output
  filtering, no positional-arg rearranging.
- Korean session -> all owner-facing text Korean; never relay internal English narration.
- Code-posted record / next-set line + keyboard -> no praise, no completion-request footer.

## per-set reply blocks (SKILL.md per-set turn, step 2)
reply = blocks in fixed order, each on its own line / paragraph, never merged into one
sentence (F12, G5).
- block 1 table: code delivers (set-add -> `exercise-enter --publish-table`, deduped by
  the delivery ledger). only `SET_TABLE ... fallback=defenced` -> relay those rows verbatim,
  whole ([추세] + [세트] + prev / next tails), never edited, cut or re-typed (F17).
- block 2 cue: `SET_CUE:` text verbatim (H11). `SET_CUE_MISSING:` -> relay. neither
  (session end) -> no cue, no apology. never skipped on later sets (G5-ext): first
  working set = full setup + execution cue (reference/exercise-cues.md); later sets =
  SET_CUE + short weight / target / RIR / ANCHOR note, nothing newly composed.
- block 3 rest line: the two `> ` lines under `NEXT_SET`, verbatim (code-emitted,
  `> ➡️ 다음 세트: <lift>` / `> <kg> × <reps> (RIR ..) · 휴식 m:ss`). no NEXT_SET ->
  `다음 세트: <NEXT_HINT spec> 휴식 <Z>초`. `NEXT_HINT: (세션 종료)` -> drop the line.
  nothing after the rest line (no "타이머 설정 완료", F12). never narrate pushes, water
  pushes or internal timing.
