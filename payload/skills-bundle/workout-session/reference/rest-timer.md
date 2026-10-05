# rest-timer.md

이 문서는 팁 라이드 판단, 오너 직전 폼지적 MANDATORY 카브아웃, dash 포맷 확인, 격려/마지막세트 타이밍, 75s/150s 스키매틱 참조 시 읽는다.

---

## 팁 선택 원칙 (selective discipline)

휴식 중 팁/동기부여 알림은 매 세트마다 넣지 말 것(over-notify = 무시됨).
- 자세 교정 포인트, 마지막 세트 동기부여 등 정말 필요할 때만 선별 배분.
- 대부분의 휴식은 "세트 시작" 알림만.
- 마지막은 "다음 세트 시작" 알림.

### 팁 라이드 결정 규칙 -- 언제 --tip / --tip60 을 넘기는가 (SPEC 5.10, owner 2026-08-20)

**캔 팁(default-on) 폐지.** #36의 "여유 있으면 기본으로 팁 1개를 태운다"는 규칙은
라이브 피드백(팁 과다 발화, 07:24)으로 **폐기**됐다. 근거 없이 매 휴식마다
문구를 만들어 태우니, 2번째 워킹세트에 "첫 렙 폼이 세트 전체를 좌우" 같은 셋업
팁이 오발했다. 코드 쪽 캔 문구 뱅크(set-arm DEFAULT_TIPS)도 **삭제**됐다.

팁은 **숨기는 게 아니라 프론트라인**이다(5.12: 팁은 접이식에 넣지 않는다). 다만
**근거가 있을 때만** 나간다:

- **기본값은 bare 마커.** `--tip`을 안 넘기면 `⏱ 30초 전`만 나간다. 그게 정상이고,
  대부분의 휴식이 여기 해당한다. "휴식이 기니까 뭐라도 한 줄" = 금지.
- `--tip`을 넘기는 경우는 **실제 근거가 있을 때뿐**, 둘 중 하나:
  (1) **오너 직전제기 포인트** -- 사용자가 이번 세션 직전 세트/메시지에서 JUST RAISED
      하거나 물어본 폼 포인트 (아래 MANDATORY 카브아웃, 여전히 필수).
  (2) **이번 세션에서 실제로 관측된 구체적 폼 이슈** -- 사용자가 말했거나 기록에서
      드러난 것. 일반론·교과서 큐를 지어내는 것은 근거가 아니다.
  둘 다 없으면 `--tip` 없이 arm 한다.
- **매 카운트다운마다 설교 금지.** 한 휴식에 팁은 최대 1개. 30s와 60s 양쪽에
  겹쳐 태우지 않는다.
- `--tip60`은 거의 쓰지 않는다. 물 알림은 **코드가 소유**(15분 케이던스,
  WATER_LINES, 저빈도·비설교)하므로 모델이 물 문구를 따로 지어 태우지 말 것 --
  중복 물팁의 원인이었다.
- 짧은 휴식(대략 45초 이하)·transition(마지막 세트, before-marker 억제)·hold-only
  arm은 bare 마커/억제 그대로.
- 팁을 태울 때의 문구는 F13 완전문장 + 그 이유를 담아 (결과-바꾸는 구체 디테일,
  generic 큐 아님).

## MANDATORY 카브아웃 (owner-confirmed 2026-07-31, C22)

형식: TIP placement (2차 목표, selective for GENERIC tips, MANDATORY carve-out for owner-just-raised points)

- CARVE-OUT (mandatory, not a judgment call): 오너가 이번 세션 직전 세트/메시지에서 JUST RAISED OR ASKED ABOUT한 폼 교정 포인트는 다음 세트의 remaining 30 마커(및 해당 시 remaining 60 마커)에 MUST ride.
  - 선택 사항이 아님, 과다알림 이유로 건너뛰지 말 것.
  - 이는 해당 포인트에만 "required"로 승격되는 것 -- generic tip의 selective 규칙은 유지.

TIP-PENDING MARKER WRITE-ORDER (M6, DGN-801, 2026-08-12): When a C22 tip is
raised (owner just raised a form point that will ride the next set's 30s/60s
marker), the model MUST write `files/program/.tip-pending` holding the active sid
BEFORE sending the tip response -- no marker-absent window may open mid-stream for
the fast-path to miss the pending tip. Clear the marker on tip-consume (owner
acknowledges/replies), OR when the next set is logged, OR on the next successful
non-tip in-session turn -- whichever comes first. The fast-path handler reads this
marker read-only (step2) and FALLBACKs if it names the active sid; the model is
the sole WRITER of this marker.

## dash-is-separator 포맷 규칙 (2026-07-22, owner formatting fix)

- dash는 tag와 tip 사이의 SEPARATOR이며 tag 자체의 일부가 아니다.
- 팁 탄다 -> 포맷: `<tag> — <tip text>`
- 팁 안 탄다 -> bare tag 단독 전송, trailing dash 전부 삭제 -- 내용 없는 dangling dash 금지.

## 60초 전 마커 팁 규칙

remaining 60 marker: water reminder (only when due) + 가치있을 때만 한 줄 격려.
- 팁 탐: `⏱ 60초 전 — <line>`
- 팁 없음: bare `⏱ 60초 전`, dash 없음 (2026-07-22 owner formatting fix).
- 오너 직전제기 교정 포인트도 upcoming set에 적용되면 여기 mandatory ride.

## 30초 전 마커 팁 규칙

remaining 30 marker: 폼 교정 팁 with its reason (결과-바꾸는 디테일, generic 큐 아님).
- generic tip은 선택적 (worthwhile할 때만; no tip -> bare `⏱ 30초 전`, dash 없음).
- 오너 직전제기 포인트 = required, never drop for selectivity.
- 포맷: `⏱ 30초 전 — <tip>`

## F13 큐 문장 형식 (owner 2026-08-14)

마커/큐 텍스트(팁, --tip, --tip60, 물 알림 등)는 완전한 한국어 지시 문장으로 쓴다 -- 전보식 단편(예: "물 한 모금") 금지, 완전한 문장(예: "물 한 모금 하세요")으로. 물 알림 문구는 코드가 이미 완전문장으로 발사한다(code SoT: service/health/set-arm). 모델이 --tip/--tip60로 넘기는 큐도 동일하게 완전문장으로 작성할 것.

## 마지막 세트 식별 및 타이밍

마지막 세트(set_seq >= prescribed sets) -> TRANSITION: single set-start alert only, no before-markers.
- "prescribed sets" = TODAY's rx-calc prescription (calc_rx exercises[].sets, already fatigue-trimmed), NOT program.yaml static slot count.
- 이 판정은 set-arm이 코드로 결정 (set-arm enforces; code is SoT: service/health/set-arm).
- 마지막 워킹세트 기록 시 `--no-arm`, 수동 set-start 억제 금지 -- F15 interim workaround는 OBSOLETE.

## 마커 스케줄 (요지 -- 상세 emit은 코드)

푸시 스케줄(60초 전 / 30초 전 마커 + 종료 세트-시작 알림)은 **set-arm이 자동 생성**한다. 모델은 set-arm 1회 호출 + 필요시 `--tip`/`--tip60`(팁 내용=판단, 위 규칙)만 전달 -- 명령/포맷을 직접 타이핑하지 않는다. 전체 emit 포맷/tag/schedule = code SoT: `service/health/set-arm` (2026-08-01, C12 ILLUSTRATION-ONLY 예시는 코드로 이관).

- **F13 cap**: before-marker는 60초 전 / 30초 전 둘만. 휴식이 아무리 길어도 120초 전 / 90초 전은 SUPPRESSED.
- **모델 chat reply 포맷** (HOT chat discipline과 동일): `다음 세트: <종목> <무게> RIR <n>. 휴식 <Z>초` (Z = designated rest). **F12 (2026-08-14): "타이머 설정 완료"/"타이머 설정했어요" 알림은 붙이지 않는다 -- 라이브 카운트다운 자체가 신호다.** rest-line 뒤에 아무것도 붙이지 않는다.
