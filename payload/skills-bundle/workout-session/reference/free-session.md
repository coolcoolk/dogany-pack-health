# free session detail (read when session-open --free is in play)

The free open serves what a planned open
serves, by code: install lane (keyboards), 표3 pin + lineup card, CARE, mat prep and
cooldown for today's lifts. Pass EVERY lift the owner named in `--exercises`, in their
words (`--exercises 데드리프트,클린`): a bare gym lift with only implement-qualified
siblings (클린 vs 원암 케틀벨 클린) is the barbell lift and the open registers it
(`REGISTERED` line). Any other missing lift: `--register <name>=<sibling>@<implement>:<표시 이름>`;
never refused. `LINEUP` names the open's lifts: one the owner named is not in it ->
`exercise-enter <sid> <owner's word>` that same turn (resolves or registers it).
The session's lift list is not the session: an owner-named lift mid-session (catalog
or registered) is appended with `exercise-enter <sid> <name>` and recorded with set-add,
never kept as a note. A swing / kettlebell clean / slam is dosed by reps. Interval rounds
the owner asks for: `session-post interval <sid> --name .. --work .. --rest .. --rounds ..`
(one countdown for the block; say it does not cue each round). "집갈래" -> close-out:
cooldown offered once (skippable), then the card; minutes are open -> close or the
onboarded watch's workout, kcal asked by hand only when `WATCH` says not onboarded;
never `workout-upd` the minutes after the card.

