# hold-unilateral.md

이 문서는 hold/isometric 종목 진행, unilateral 종목 진행, 입력모드(button vs text) 결정, 무게 재질문 분기 시 읽는다.

> **이 문서는 「편측을 어떻게 진행하는가」이지 「편측인가」가 아니다.**
> 편측 여부는 **선언에서만** 온다 -- `set-table.resolve_unilateral(slot)`이 정본이고,
> program.yaml에 `unilateral` 블록이 없으면 답은 **양측**이다. 아래 절차는 전부
> 그 답이 「편측」으로 나온 뒤에 적용된다.
> 계기(2026-09-11): 선언이 없는 스탠딩 카프레이즈에서 발화가 편측 전환을 주장했다.
> 「아니그거 시티드였는데.. 스탠딩은 양발이야」 -- 115kg에서 양발->한발은
> 다리당 하중 2배다. 산문 키워드(「싱글레그」 등)는 힌트이지 선언이 아니다.
> 상세: reference/set-gates.md "plan-value source".

---

## time-hold exercises (isometric / plank class, owner-confirmed 2026-07-18)

- 타임드 홀드(플랭크/isometric working set, 프렙 드릴, 쿨다운 스트레칭 등 초로
  정해진 홀드)는 "완료되면 알려주세요" + [완료] 버튼이 아니라 press-start
  카운트다운으로 진행한다 (F22/F15, owner 2026-08-14).
- 사용자가 시작할 준비가 되면 "시작" affordance를 제공하고, 시작 탭 순간
  홀드 duration(초)만큼 카운트다운을 발사한다:
  `service/health/set-arm countdown <초> [--label "<이름>"]`
  (range면 상한 사용: "20~30" -> 30). code is SoT: service/health/set-arm.
- 카운트다운은 휴식 타이머와 동일한 채널1 프리미티브 -- 새 홀드 카운트다운은
  직전 카운트다운(휴식/홀드 무관)을 자동 취소한다(오펀 없음). +/- 보정 불필요.
- hold-class 워킹세트가 sets N>1이면 각 세트마다 자기 시작->카운트다운.
- END 도달 후 auto-chain: 다음 종목/세트 안내가 따른다.

## E14 anti-mush (2026-08-09, RC2 residual)

hold-class 슬롯 (program.yaml `progression: hold`, `weight_kg: null`, `rep_range` = SECONDS)에 `sets: N > 1`이면 N 개별 세트, 하나의 완료가 아님:
- 각 세트마다 자기 START 버튼 + END push + `set-add` 행(`set_seq` 1..N).
- N hold를 한 번의 "done" 로그로 뭉치기 절대 금지.
- hold/iso 세트가 마지막 세트가 아니면(continuation) set-add 기록 시 set-arm이 세트 간 휴식을 결정론적으로 arm한다 (카운트다운 + 60/30초 마커 + "✅ {sec}초 휴식 완료" 경과확인 + 세트시작 푸시 -- 워킹세트와 동일). 모델은 hold 세트 완료 후 다음 hold press-start countdown을 곧바로 발사하지 말 것 -- set-add stdout의 `REST_ARMED: <sec>초 (홀드 세트 간 휴식 -- 다음 홀드 시작 전 대기)` 라인이 뜨면 그 세트 간 휴식이 이미 걸린 것이므로, 휴식을 사용자에게 제시하고 휴식이 끝난 뒤(다음 세트 신호 수신 후) 다음 hold set의 press-start를 발사한다. 마지막 hold 세트(transition)는 set-arm stdout이 `REST_ARMED\tNONE`을 내고 세트 간 휴식 없음(홀드 완료 -> 종목/세션 진행). 이 판정은 set-arm이 코드로 결정한다 (code is SoT: service/health/set-arm). 이 세트 간 휴식은 실제 실행 이벤트(set_done)이므로 #22 타이머 발화 게이트 통과 대상이다.
- hold 세트는 elapsed hold SECONDS를 reps 필드에 기록 (현재 스키마에 dedicated hold-duration 컬럼 없음 -- seconds in `reps`, `rep_range`가 seconds인 것과 일치).

## HOLD 타이머 발사 시 완료 버튼 필수 (2026-08-17, dead-air 금지)

hold 카운트다운(`set-arm countdown <초> --label ...`)을 발사하는 메시지에는
반드시 같은 메시지에 완료/다음 `[[OPTIONS]]` 버튼을 붙인다.

- 이유: 카운트다운이 끝나도 bridge는 자동 모델 turn을 깨우지 않는다(CountdownDriver
  auto-wake = 프레임워크 레인, 미구현). 버튼이 없으면 타이머 종료 후 흐름이 dead-air.
- 형식: 타이머 발사 메시지 마지막에 번호목록 `1. 완료 / 다음` + `[[OPTIONS]]` 마커.
- 적용: 모든 set-arm countdown 발사 -- hold 워킹세트, 쿨다운 스트레칭, 매트프렙 홀드.
- 미적용: 워킹세트 사이 REST 타이머 자체(세트 기록으로 자동 진행, dead-air 없음). 단, 워킹세트 REST 완료 푸시(set-arm)의 "✅ {sec}초 휴식 완료" 경과 확인 라인은 이제 **hold 세트 사이(continuation)에도 동일 적용**된다 (#23) -- 예전 "hold 세트엔 적용 안 함"은 폐기. 단 마지막 hold 세트(transition)에는 세트 간 휴식 자체가 없으므로 이 라인도 없다.
- 버튼 탭 or "다음"/"완료" 텍스트 수신 -> 다음 세트/드릴 진행.

## hold-class 다음버튼 강제 (2026-08-10, F19/F33 부분 착지)

set-add로 hold-class 슬롯 기록 시 set-arm이 hold-class로 판정(`progression: hold` AND `weight_kg: null` -- 무게있는 'hold'(백스쿼트/인클라인바벨프레스 등 무진행 의미)는 제외)하고 두 가지 결정론적 발사:
1. hold END 푸시 텍스트에 `👉 다음으로 진행하려면 '<label>'라고 보내주세요` 자가진행 안내 자동 부착 (푸시엔 인라인버튼 불가 -- 사용자가 종료 푸시만 보고도 진행 행동경로를 갖게 함). `<label>`은 position-correct 버튼 라벨(아래 3방향 분기).
2. set-add stdout에 `HOLD_NEXT: <label>` 라인 재노출. 라벨 값은 고정 "다음"이나 raw spec이 아니라 아래 position-correct 라벨이다:
   - 같은 종목의 hold 세트가 더 남아 있음 -> `다음 세트`
   - 종목/단계 완료, 다음으로 진행 -> `다음(진행)`
   - 세션 종료 -> `완료`
   (set-arm의 `hold_next_label()` 결정론 산출; NEXT_HINT 라인은 별도로 "다음:" 채팅 라인에 사용)

   **D3 정정 (2026-08-24, H17 정합).** 이 항목은 「이 신호가 뜨면 다음 인세션 응답에 탭 가능한 `[[OPTIONS]]` 블록을 반드시 렌더할 것」이라고 적혀 있었다. 후보가 하나뿐인데 메뉴를 내는 것은 H17이 폐기한 동작이다 -- 브릿지 분류기가 `>= 2`에서만 돌기 때문에 버튼이 붙지도 않고 "선택: 1. 다음(진행)" 글자만 남아 사용자가 멈춘다. `HOLD_NEXT`는 다음 동작의 **이름**일 뿐이고, 수행 명령은 `AUTO_ADVANCE: <라벨>`이다 -- 그게 뜨면 같은 turn에 **바로 실행**한다. `[[OPTIONS]]`는 진짜 후보 2개 이상일 때만. (`HOLD_NEXT`가 여전히 필요한 자리는 위 1번 -- 푸시엔 인라인 버튼이 안 붙으므로 라벨을 문장으로 알려야 한다.) SKILL.md H17 절이 SoT.

잔여(미착지 -- 스펙만): 푸시에 인라인 "다음" 버튼 근본해결 = DGN-594/프레임워크 seam(bridge push inline-keyboard) -- 도메인 스크립트 범위 밖.

## unilateral exercises: hold vs non-hold (owner-confirmed 2026-07-18)

- HOLD type (isometric unilateral): 각 쪽 한 번씩, WEAKER SIDE FIRST.
  두 쪽은 **자동 체인**으로 이어진다 -- 좌 타이머 완료 버튼이 곧바로 우 타이머를 발사하고,
  우 타이머 완료가 기록+다음 진행. 중간 "시작" 스텝 없음. (아래 "편측 홀드 자동 체인" 절,
  그리고 `set-arm hold-chain`. 옛 "두 번의 별도 START tap" 규칙은 폐기.)
- NON-HOLD type (불가리안 스플릿 스쿼트, 싱글레그 프레스 등): 두 다리 사이 휴식 없음.
  약한쪽/강한쪽으로 별도 큐 쪼개기 금지 -- 포맷 = "두 다리 다 하고 한 번 기록" (세트결과 입력 1회가 양다리 커버).
  휴식 타이머는 양다리 모두 완료 후에만 작동 (세트 사이, 다리 사이 아님).
- 두 클래스 혼동 금지: hold = 좌 -> 우 **자동 체인**(아래 참조, 버튼 1개씩); non-hold = 단일 combined cue, 종목 중 휴식 없음.

## 편측 홀드 자동 체인 -- 중간 "시작" 스텝 금지 (확정, 재확인)

규칙: 왼쪽 홀드 타이머가 끝나면 타이머의 버튼이 곧바로 다음(오른쪽) 타이머를 트리거하고,
오른쪽 홀드 타이머가 끝나면 그 종목을 완료하고 다음 종목으로 넘어간다.
정정: 타이머에서 시작을 누르면 바로 다음 행동으로 이어간다. 중간 스텝을 끼우지 않는다.

**폐기된 옛 규칙**: "좌 완료 -> 우 START 버튼 (두 번의 별도 START tap)". 더 이상 쓰지 말 것.

**현재 규칙 -- 3비트, 그 사이에 아무 스텝도 없음:**
1. 왼쪽 홀드 타이머 발사
2. 왼쪽 타이머 완료 시 붙어 있는 **그 버튼 하나가 곧바로 오른쪽 타이머를 발사**한다.
   "이제 오른쪽 갑니다 [시작]" 같은 안내 스텝을 끼우지 말 것 (완료 -> 다음 직결).
3. 오른쪽 타이머 완료 버튼 -> 해당 종목 **기록 완료** -> 다음 종목/세트로 진행.

**모델이 직접 큐를 짜지 말 것 -- 결정론 캐리어를 호출한다:**

```
service/health/set-arm hold-chain <session_id> <exercise_name> <set_seq> \
    --seconds <초|범위> --trigger start [--sides left,right] [--label "<이름>"]
```

- 이 한 번의 호출이 (a) 첫 쪽 카운트다운 발사 + (b) 완료 버튼 arm + (c) `[[IDRILL:<id>]]`
  마커 출력까지 전부 한다. 마커를 **verbatim으로 응답에 실으면** 그 메시지에 버튼이 렌더된다.
- 그 버튼 탭 = 모델 턴 0. 브릿지가 다음 링크를 직접 실행해 **오른쪽 타이머를 즉시 발사**하고
  다음 버튼을 푸시로 보낸다. 모델은 중간에 아무것도 하지 않는다.
- 마지막 쪽 버튼 = `set-add` 발사(홀드 초를 reps에 기록) + 세트표 갱신 + 다음 안내.
  프로그램 슬롯이 아닌 프렙/스트레칭 드릴이면 기록 없이 종료만 한다.
- `--sides` 순서 = **근력 약한 쪽 먼저**(아래 F26). 기본값 `left,right`.
- `--trigger`는 #22 인텔 가드: 실제 실행 신호(start/ready/set_done)에서만 타이머가 걸린다.
  "~하자/~할게" 같은 계획 발화로는 어떤 링크도 타이머를 못 건다.
- 모델이 별도로 `[[OPTIONS]]` 완료/전환 버튼을 미리 렌더하지 말 것 (버튼 중복 = 08-20 5.5 사고).
  버튼의 단일 소스는 이 체인이다.
- code is SoT: `service/health/set-arm` (`run_hold_chain` / `build_hold_chain_payload`).

**한쪽만 하는 홀드**(양측 아님, 예: 플랭크/월싯)는 체인이 아니라 기존 단일
`set-arm countdown <초>` 경로 그대로.

## F26: 부상 축 != 약축 (F26)

부상 축(injury side)과 근력 약한 축(strength-weak side)은 별개의 두 축 -- 각각 따로 확인.
- 순서 기준(먼저 하는 쪽) = "근력 약한 쪽 먼저"(WEAKER-STRENGTH side first). 부상 축이 순서를 정하는 게 아님.
- 부상 축은 순서 결정 요인이 아님 -- ROM/통증을 주의하며 매칭하는 대상. 해당 쪽 세트는 통증/가동범위를 살피며 진행.
- 오안내 예: 우측=부상 축, 좌측=근력 약한 축이었는데 "약한 쪽 먼저"를 부상 축(우측)으로 잘못 해석해 우측 먼저 안내 -- 근력 약한 좌측이 먼저였어야 함.
- 저장된 좌우 사실(어느 쪽이 부상 축, 어느 쪽이 근력 약한 축)을 즉석 큐 산출 시 반드시 분리 참조 -- 두 축을 각각 조회해서 적용.

## 입력모드: button vs text (owner-confirmed 2026-07-18)

- warmup sets + ramp-up sets (rungs, setup included): one done tap, posted by code (set-arm
  rung arm, `marker=arm-rung-next`, row_keyboard). never author one
  (reference/set-recording.md).
- working sets: in-place reps -> RIR drilldown (IDRILL). code delivers the keyboard; the
  `[[IDRILL:<id>]]` line is never put in a reply (reference/set-recording.md). numeric
  TEXT (kg / reps / RIR) stays open as fallback; both converge on set-add. the old F17
  two-message `[[OPTIONS]]` narration is retired.
  [정정 2026-09-26: this line used to say "echo set-add's `IDRILL_MARKER:` line verbatim so
  the bridge renders the keyboard" and "warmup = OPTIONS button only". both were retired
  by A1-KEYBOARD 2026-08-25 (code delivery) and RUNG ARM 2026-08-21.]

## 무게 재질문 분기 (owner-confirmed 2026-07-31, C7/C9/C10)

[정정 2026-09-26: the two request lines below are TEXT-path wording only -- a turn that
carries a code keyboard gets no request line at all (owner 2026-08-25 06:48,
reference/set-recording.md).]

- FIXED-weight case (prescribed weight에서 세트 수행): reps/RIR만 요청. 무게 재질문 금지 -- 에이전트가 이미 처방.
  오너는 실제 무게가 처방과 다를 때만 weight를 자발적으로 보고(unprompted).
  완료 요청 문구: `"완료 후 횟수-RIR 알려주세요"`.
- OPEN-weight case (이 세트의 무게가 오너 자유선택, 미결정): 완료 요청에 무게 포함 필수.
  완료 요청 문구: `"완료 후 무게-횟수-RIR 알려주세요"`.
- separator 통일 (2026-08-01, C9/C10): 모든 완료 요청 문구는 DASH(`-`) 사용, slash(`/`) 금지.
  예: `"횟수-RIR"` (fixed) / `"무게-횟수-RIR"` (open).
