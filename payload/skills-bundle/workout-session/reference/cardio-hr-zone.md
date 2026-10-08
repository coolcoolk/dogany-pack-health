# cardio-hr-zone.md

이 문서는 라이브 유산소 세그먼트(스테퍼/트레드밀/바이크 등 카디오 블록)에서
카르보넨 공식으로 목표 심박존(target HR zone)을 잡아야 할 때 읽는다. 근력 세트
진행에는 무관 -- 유산소 목표존 요청이 실제로 뜬 시점에만 트리거되는 lazy 경로다.

설계 근거/토론 트레일은 세션 후 처리됨 (배치노트 F1). 여기 담긴 건 실행 메커니즘만.

---

## max_hr = 파생값 (저장 안 함, 재질문 안 함)

나이 구동 정적값 -- 매번 그때그때 계산하는 파생값. 저장/시계열 불필요.

- birth_year는 config store에 이미 있음 (읽기 전용 조회):
  `sqlite3 database/kit_life.db "SELECT value FROM config WHERE key='birth_year';"`
- 공식 (Tanaka): `max_hr = 208 - 0.7 * age_years`, `age_years = 현재연도 - birth_year`.
- 예: birth_year=1995, 2026년 -> age_years=31 -> max_hr = 208 - 0.7*31 = 186.3 bpm.

절대 저장하지 말 것 -- 필요할 때마다 재계산. 온보딩에 넣지 말 것 (온보딩 무변경).

## resting_hr = 시계열값 (lazy 수집, 60일 유효)

훈련 자극에 반응하는 지표라 시계열로 관리 (체중/체지방급). 나이 구동 아님.

### 1. freshness check (질문 전 먼저, 읽기 전용)

metric_log에 최근 60일 내 resting_hr 행이 있는지 먼저 확인한다. metric_log 읽기
전용 CLI 동사는 없으므로 읽기 전용 sqlite 조회를 쓴다 (diet-status D1의 weight_kg
freshness 패턴과 동형):

```bash
sqlite3 database/kit_life.db \
  "SELECT date, value FROM metric_log WHERE metric='resting_hr' ORDER BY date DESC LIMIT 1;"
```

- 행이 있고 60일 이내: 그 값을 조용히 재사용 -- 질문하지 않는다.
- 행이 없거나 60일 초과: 아래 ask 스크립트로 사용자에게 1회만 묻는다.

### 2. ask 스크립트 (세션 중 1회만)

세션 중 딱 1회, 애플워치 **"휴식기 심박수"(Resting Heart Rate)** 위젯의 값을
불러달라고 묻는다. 이 전용 지표(월평균)만 받는다.

- 경고 (오늘 실측 혼동 재발 방지): **"심박수 범위"(Heart Rate Range)** 위젯의
  일간/주간/월간 최저값을 대용치로 쓰지 말 것 -- 그건 더 낮은 다른 숫자이고 안정시
  심박이 아니다. 사용자가 최저값을 불러주면 "휴식기 심박수" 위젯 값으로 다시 확인.
- A9 발명금지: resting_hr 값을 절대 추정/발명/기본채움하지 말 것. 오직 사용자가 말한
  값만 쓴다 -- 미입력이면 목표존 계산을 멈추고 위 질문으로 돌아간다.

### 3. write path (사용자 답 -> metric_log)

값을 받으면 기존 범용 동사로 기록:

```bash
database/kit_life.sh log-metric <YYYY-MM-DD> resting_hr <value>
```

새 kit_life 코드 만들지 말 것 -- 이 동사는 이미 범용이다. kit_life.py/kit_life.sh
수정 금지 (framework-owned).

## Karvonen 목표존 계산 (두 값 확보 후)

```
target_hr = ((max_hr - resting_hr) * intensity_fraction) + resting_hr
```

- intensity_fraction = 카디오 목표별 심박예비율(%HRR) 범위. 지방연소/유산소 베이스
  목표면 표준 0.60-0.75 사용.
- 출력은 단일 정밀값이 아니라 말로 부르는 범위로 (예: "150-160 bpm대"). 오버정밀 금지.

예: max_hr=186, resting_hr=64, intensity 0.60-0.75
-> 하단 (186-64)*0.60+64 = 137, 상단 (186-64)*0.75+64 = 155 -> "137-155 bpm대".

## 스코프 경계 (자동화 금지)

애플워치 API 연동 없음, 스크린샷/OCR 파싱 자동화 없음 -- 사용자가 말로 불러주는 값을
수동 기록하는 것만. 대화형 질문 + log-metric 쓰기 이상의 자동화는 만들지 않는다.

## cross-ref: 킷 workout-log avg_hr (사후 실측)와 상보 관계

이 문서의 목표존은 세트 전 라이브 TARGET(잡아야 할 심박대)이다. 킷 workout-log의
avg_hr 컬럼은 유산소 세션 종료 후 실제 평균 심박을 사후 기록하는 별개 경로다 --
중복 아님, 상보. 목표 vs 실측.
