# 도메인 화법 레지스터 (F11, owner 2026-09-18) + 어휘 3층 (F1)

Read when: about to plain-speak or gloss a domain word, the user uses or asks about
RIR / sub-muscle names / tempo, or an experience answer of 2+ years lands. Applies to
every sentence the MODEL composes in this pack (consult, design, session chat). Single
home; AGENT-CONSULT and workout-session reference/vocabulary.md point here.

## two axes, never derived from each other

```
경력        -> 프로그램 구조 (분할/전신, 볼륨, 회복 간격)   -- consumer: program-plan experience/split
어휘·지표   -> 화법 깊이 (RIR, 하위 부위명, 템포)           -- consumer: every model sentence
```

low correlation ("2년 했는데 RIR 모름" is most common). experience answer never raises
the register; a register raise never changes structure. origin: rehearsal 2, owner
verbatim *"rir이런 거랑 세부근육 다루는 중급자인지 이런겅 언제 분기가 갈리냐"*.

## raise rules

- default = plain speech for a new user ("2개쯤 남기고 멈추기", "등 전체").
- raise trigger, either:
  1. user uses the term FIRST as an information carrier ("RIR 2로 갈게" -> RIR on;
     "광배" -> back splits into 광배 / 기립근 / 승모). ASKING its meaning ("RIR이 뭐야?")
     is not adoption: answer via the `service/health/ui_labels.py` gloss, no raise.
  2. the record needs the precision (e.g. a lift stalled 3 weeks at one weight): ask
     ONCE, offering the raise.
- one-way: no lowering, not across sessions either.
- first use of a raised term carries exactly ONE teaching line; bare after that.
- "2년+" experience is NOT a raise: it earns one lifetime offer 「RIR로 말씀드려도
  될까요?」. declined or unanswered -> never again; accepted = trigger 1.

persistence: config `vocab_register` (kit_life.sh config-set; merge-only comma list
like consult_modules, no delete path). items `rir` / `tempo` / `submuscle:<group>`
(group = muscle_node top key, e.g. back) / `rir_offered` (latch: the 2+ offer went
out, written that turn whatever the answer). write in the trigger turn. key absent =
all plain.

sub-muscle granularity rides the same switch; vocabulary = taxonomy subregion layer
(muscle_node back -> back_lats / back_erectors / back_traps, user labels 광배 / 기립근 /
승모). judging machinery (volume audit, rx) already runs per sub-muscle regardless --
register gates what is SAID, never what is computed.

boundary (b9d0080 regression, do not repeat): model-composed speech only. tool strings
(set-table header, NEXT_HINT, confirms) = verbatim echo, labels owned by
`service/health/ui_labels.py`; never rewrite them for register. deterministic-surface
level gating (ui_gate, 2026-08-24 ticket) not landed (needs kit migration): an
unraised user still SEES RIR on the set table. known residue; if asked, gloss (gloss
!= raise).

## 어휘 3층 -- reach of the plain-speech rule (F1, owner rejected twice 2026-09-18)

owner rejected "분할" rewritten as "쪼갠다/갈래" twice. plain-speech exists to keep
INTERNAL machine words out of the user's ear, not to erase words the user owns.

```
내부 기계어     라더/스테이지 id/파일명/config 키/G-코드   -> 절대 발화 금지 (기존 "라더" 금지와 같은 층)
정밀 도구어     RIR · 하위 부위명(광배/기립근/승모) · 템포  -> 레지스터 승급 후에만. 기본은 풀어 말한다
도메인 공용어   분할 · 전신 · 후면사슬 · 데드리프트 · 종목명 -> 항상 그대로. 평이화 금지
```

same ruling already in tree twice: workout-session (real lift names are never touched,
only coined compounds) and ui_labels.py U1c ("플라이는 실제 운동 어휘라 남는다;
프리프레스가 조어다"). before plainifying ANY word, place it in a tier first; plainifying
a domain word deletes information and gets rejected.
