# lattice-jit.md

이 문서는 calc_rx가 needs_lattice 플래그를 반환했을 때 읽는다 (loading 마킹된 이산하중 기구인데 격자 미등록/불완전한 슬롯).

---

## JIT 기구 격자 등록 (F17, 2026-08-07)

결정론 강제점: 처방 산출(calc_rx) 결과에 `needs_lattice`가 비어있지 않으면, 그 슬롯의 처방 무게를 최종/권위값으로 제시하지 말 것. 그 무게는 기계가 실제로 못 올릴 수 있는 raw 값이다.

대신 그 자리에서 JIT로 딱 필요한 필드만 오너에게 질의:
- 그 기구의 최소 무게(base)와 한 칸 증가폭(step) [필요 시 격자 유형].
- 그 기구 하나만, 그 순간에. bulk 체크리스트 금지("작게 시작" 금지).

## 질의 문구 (오너 대면 언어, 내부어 노출 금지 규율)

"격자/lattice" 같은 내부어 대신 도메인 언어로:
- 예: "이 기계 최소 무게 몇 kg부터, 한 칸 올리면 몇 kg씩 늘어요?"

## 저장 명령

오너 답을 받으면:
```
service/health/lattice-set <slot> --type <even|stack|standard> --base <b> --step <s>
```
저장 후 calc_rx가 자동 스냅, 재질의 없음.

## 미등록 상태로 진행 시

미등록 상태로 진행해야 하면 그 무게는 provisional로 명시 (확정 아님).

## 근거 및 스코프

F17 오처방 원천차단. "프롬프트 판단 -> 데이터+룰+코드 강제" (미등록 기구엔 추정 처방 금지, forcing-point).
interim/씸: 이건 program.yaml inline 격자 위 interim JIT다. gym-스코프 기구 레지스트리 + 사영 엔진 프리미티브는 후속 프레임워크 랜딩(AX 3층 / DGN-387 확장). cross-ref: design notes `2026-08-07-ax-exercise-attribute-model.md`.

lattice 술어(rx-calc:414) = code enforces; code is SoT: service/health/rx-calc.
