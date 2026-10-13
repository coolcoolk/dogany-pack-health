# code-post contract (read at session start)

- code posts and your prose never contradict (owner 2026-10-10). a code value you judge
  wrong (target, rung, timer, row) is CHANGED through a verb so code re-posts it:
  `set-arm <sid> <ex> <seq> --ov-weight <kg> --ov-reason "..."` (target),
  `set-reclass <sid> <ex> <seq> --to ramp|working` (a warm-up logged as working or the
  reverse -- one verb, never set-undo + set-add), `set-undo` (a row that should not
  exist). never write "무시하세요" about a machine post; the contradiction carrier
  (`[MACHINE-CONTRADICTION]`) flags it on the next turn.
- no load history: relay `CALIBRATION_RAMP_SAY` / `LOAD_ESTIMATE_SAY` (empty bar or the
  lightest weight first; a transferred ramp target is a TARGET, never the working
  weight). never "편한 무게로 해 보세요". a set the owner reports below the band with no
  RIR is a warm-up rung: `RIR_ASK` -> the RIR ask (buttons 0 · 1 · 2 · 3 · 4+), run the
  correction it names. while no working weight exists, `CALIBRATION_NEXT` is the gate's
  answer (never "오늘 몇 kg?"): relay `CALIBRATION_NEXT_SAY`; the owner's next "60-5" is a
  done warm-up set -- log it with set-add as reported.
- input asks are code copy. no keyboard on screen -> relay `TEXT_ASK_SAY:` verbatim
  ("몇 회 하셨어요? 이번 세트 RIR은요? (예: 10회 RIR 2)") and a `RIR_EXPLAINER:` line, when
  printed, directly under it (`RIR_ASK_TEXT:` likewise). never invent an input format
  ("'회수-여유' 형식으로 (예: 6-2)" -- owner 12:56 "회수여유는 뭐냐"). the RIR ask on a
  warm-up is code-posted buttons (`RIR_ASK_KEYBOARD`, the same RIR ask as a working set,
  owner 2026-10-10 18:49); a tap arrives as its label ("2") -> run the RIR_ASK command
  with the RIR the KEYBOARD line maps it to.
- `OWNER_LINES posted=code` -> the record line, load sentence, RIR-floor note, next-set
  lines (and on a free session's last listed lift, the lift wrap-up) are on the owner's
  screen. the reply repeats none of them; no reply is owed unless the owner asked.
- record the owner's report as reported. the weight they just lifted is never passed back
  as `--ov-weight` (set-add drops the echo: `OV_ECHO_DROPPED`); the code's next load
  (a step-down after a set below the rep floor) stands. you disagree -> `set-arm --ov-weight
  <kg> --ov-reason "<한국어 한 줄>"`, never "표의 x10은 현실과 안 맞아요".
- `--ov-reason` is owner-facing Korean; never "owner" / "엔진" / "판정" in owner copy.
