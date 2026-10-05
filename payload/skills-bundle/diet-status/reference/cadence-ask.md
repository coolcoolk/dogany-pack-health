# measurement cadence ask (read when log-metric prints CADENCE-ASK, or before a planned measurement)

cadence = USER field. module recommends, user picks, kit stores. this skill writes body
metrics back, so the ask happens here.

- `log-metric` may append:
  `CADENCE-ASK<TAB><metric><TAB><hours><TAB><domain><TAB><owner><TAB><why>`.
  only while that metric's cadence is unconfirmed. no line -> say NOTHING about cadence.
- HARD GATE: render the question ONLY if `<owner>` == your slug. otherwise record the
  value, say nothing about cadence, no "owner will ask later" promise (cannot back a
  claim about when a peer raises it; same as meal-capture no-time-claim). kit already
  suppresses the line for non-owners, so normally: no line -> silence. health pack on a
  health-owning instance: slugs normally agree. check the line, do not assume.
- fires + yours -> ask ONCE, carrying the guideline. never bare, never a promise:
  "체성분은 보통 주 1회 정도 봅니다(그보다 잦으면 수분 변동에 묻힙니다). 어떻게 하실래요?"
- answer -> `kit_life.sh freshness-set <metric> <daily|weekly|biweekly|monthly|hours>`.
  whatever they pick is right; guideline is not a default to push.
- ask-once is structural: after freshness-set the kit stops emitting CADENCE-ASK. never
  re-raise. they change their mind -> run freshness-set again.
- optional pre-check: `kit_life.sh freshness-touch <metric>` ->
  `<metric><TAB>confirmed|ask|silent<TAB><hours><TAB><domain|-><TAB><owner|-><TAB><why|->`.
  `silent` = no guideline -> do not invent one, do not ask. touch is a READ verb and
  reports `ask` to every caller; same owner gate applies.
- diet macros are fixed daily by the module. never ask about diet cadence.
- staleness is not raised here; retro-reflection reports stale metrics.
