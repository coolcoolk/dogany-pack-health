# 종목 자세 애니메이션 -- 제작 레퍼런스 시트 (v0 scaffold, 2026-07-20)

목적: 도가니 제품용 모션그래픽 애니메이션(자체 제작 = 저작권 소유). 2번 루트
(코드/리깅 기반, Rive 우선). 이 시트는 애니메이터(사람/디자이너)가 종목별
정확한 폼 각도를 잡을 때 쓰는 작업 대장.

## 규칙
- target file: service/health/gifs/<snake_case_name>.gif (program.yaml slot의
  `gif` 필드가 이 경로를 가리킴).
- ref source: 정확한 폼 레퍼런스. free-exercise-db(퍼블릭 도메인) 시작/끝 컷 또는
  신뢰할 영상. GymVisual 계열 GIF는 AI/제작 입력 금지(라이선스).
- start/end angle: 시작·끝 자세 주요 관절 각도(무릎/엉덩이/어깨/팔꿈치). 레퍼런스
  보고 채운다. 안전 각도(예: 브이스쿼트 무릎 90도 캡)는 반드시 반영.
- status: TODO(미착수) / REF(레퍼런스 확보) / RIGGED / ANIMATED / EXPORTED / DONE.

## 안전 각도 제약 (program.yaml safety_note에서 온 것 -- 애니에도 반영 필수)
- v_squat: 무릎 굴곡 90도 초과 금지(깊이 제한). injury_knee.
- single_leg_extension / leg_curl: 싱글레그(한 다리씩), 약한 쪽 먼저.
- overhead_press: 헤비 오버헤드 주의(injury_shoulder). 중립 궤적.
- tricep_pushdown: 로프/스트랩 손잡이.

## 종목 대장 (22종)

| snake_case | 표시명 | target gif | ref source (candidate) | status |
|---|---|---|---|---|
| incline_dumbbell_press | 인클라인 덤벨 프레스 | incline_dumbbell_press.gif | free-exercise-db: Incline_Dumbbell_Press (verify) | TODO |
| v_squat | 브이스쿼트 | v_squat.gif | 영상(무릎 90도 캡 반영) | TODO |
| chest_press_machine | 체스트 프레스(머신) | chest_press_machine.gif | free-exercise-db (verify) | TODO |
| single_leg_extension | 싱글레그 익스텐션 | single_leg_extension.gif | free-exercise-db: Leg_Extensions (싱글레그로 변형) | TODO |
| cable_fly | 케이블 플라이 | cable_fly.gif | free-exercise-db: Cable_Crossover / Dumbbell_Flyes (verify) | TODO |
| tricep_pushdown_rope | 삼두 푸시다운(로프) | tricep_pushdown_rope.gif | free-exercise-db (verify) | TODO |
| deadlift | 데드리프트 | deadlift.gif | 영상 | TODO |
| pullup | 풀업(친업) | pullup.gif | free-exercise-db (verify) | TODO |
| barbell_row | 바벨 로우 | barbell_row.gif | free-exercise-db (verify) | TODO |
| leg_curl | 시티드 레그 컬(싱글레그) | leg_curl.gif | free-exercise-db (싱글레그 변형) | TODO |
| face_pull | 페이스 풀 | face_pull.gif | free-exercise-db (verify) | TODO |
| bicep_curl | 이두 컬 | bicep_curl.gif | free-exercise-db (verify) | TODO |
| overhead_press | 오버헤드 프레스(OHP) | overhead_press.gif | 영상(어깨 중립 궤적) | TODO |
| incline_barbell_press | 인클라인 바벨 프레스 | incline_barbell_press.gif | free-exercise-db (verify) | TODO |
| tricep_overhead_extension | 삼두 오버헤드 익스텐션 | tricep_overhead_extension.gif | free-exercise-db (verify) | TODO |
| pendlay_row | 펜들레이 로우 | pendlay_row.gif | 영상 | TODO |
| rdl | RDL(루마니안 데드) | rdl.gif | 영상(힙힌지) | TODO |
| bulgarian_split_squat | 불가리안 스플릿 스쿼트 | bulgarian_split_squat.gif | 영상 | TODO |
| chest_supported_t_bar_row | 체스트 서포트 T바 로우 | chest_supported_t_bar_row.gif | free-exercise-db (verify) | TODO |
| chinup | 친업(언더그립) | chinup.gif | free-exercise-db (verify) | TODO |
| hammer_curl | 해머 컬 | hammer_curl.gif | free-exercise-db (verify) | TODO |
| incline_dumbbell_curl | 인클라인 덤벨 컬 | incline_dumbbell_curl.gif | free-exercise-db (verify) | TODO |

## 프로토타입 우선순위
1. incline_dumbbell_press (앞A slot1) -- 이거 하나로 리그+애니+export 파이프라인
   검증. 시간/퀄리티 감 잡은 뒤 나머지 21종 확장.
