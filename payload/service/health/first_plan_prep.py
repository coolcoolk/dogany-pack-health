"""Pack defaults for first-program preparation drills."""
PREP_DOSES = {
    'adductor_squeeze': (15, 'seconds', '무릎 사이 폼롤러를 가볍게 조이고 15초 유지하세요.'),
    'ankle_mobility': (10, 'reps', '발뒤꿈치를 바닥에 둔 채 무릎을 발끝 방향으로 천천히 보내세요.'),
    'shoulder_circles': (10, 'reps', '어깨를 천천히 크게 돌리세요.'),
    'band_external_rotation': (12, 'reps', '팔꿈치를 몸통에 붙이고 밴드를 바깥으로 당기세요.'),
    'dead_bug': (10, 'reps', '허리를 바닥에 붙이고 반대쪽 팔과 다리를 천천히 뻗으세요.'),
    'hip_knee_mobility': (10, 'reps', '고관절과 무릎을 통증 없는 범위에서 천천히 움직이세요.'),
    'glute_bridge': (12, 'reps', '발바닥을 짚고 엉덩이를 들어 몸통을 곧게 만드세요.'),
    'cat_cow': (10, 'reps', '네발기기에서 등을 천천히 둥글게 말았다 펴세요.'),
    'thoracic_rotation': (10, 'reps', '네발기기에서 한 손을 머리 뒤에 두고 가슴을 옆으로 돌리세요.'),
    'wrist_circles': (10, 'reps', '손목을 통증 없는 범위에서 천천히 돌리세요.'),
    'pallof_press': (10, 'reps', '밴드를 가슴 앞에서 밀고 몸통이 돌아가지 않게 버티세요.'),
    'bird_dog': (10, 'reps', '네발기기에서 반대쪽 팔과 다리를 뻗고 몸통을 고정하세요.'),
    'side_plank': (20, 'seconds', '팔꿈치를 어깨 아래에 두고 옆으로 몸통을 곧게 버티세요.'),
    'stretch_quads': (20, 'seconds', '서서 발목을 잡고 허벅지 앞을 부드럽게 늘리세요.'),
    'stretch_hamstrings': (20, 'seconds', '무릎을 잠그지 않고 허벅지 뒤가 당길 만큼 숙이세요.'),
    'stretch_hip_flexors': (20, 'seconds', '한 발을 앞으로 내딛고 뒤쪽 고관절 앞을 늘리세요.'),
    'stretch_glutes': (20, 'seconds', '앉아서 한쪽 다리를 반대쪽 위에 올리고 엉덩이를 늘리세요.'),
    'stretch_calves': (20, 'seconds', '벽을 짚고 뒤쪽 발뒤꿈치를 바닥에 눌러 종아리를 늘리세요.'),
    'stretch_chest': (20, 'seconds', '문틀에 팔을 대고 가슴을 부드럽게 앞으로 보내세요.'),
    'stretch_lats': (20, 'seconds', '팔을 머리 위로 뻗고 몸통 옆을 길게 늘리세요.'),
    'stretch_shoulders': (20, 'seconds', '한 팔을 가슴 앞으로 가져와 어깨 뒤를 늘리세요.'),
    'stretch_triceps': (20, 'seconds', '한 팔을 머리 뒤로 접고 팔 뒤쪽을 늘리세요.'),
    'stretch_forearms': (20, 'seconds', '팔을 펴고 손가락을 부드럽게 당겨 아래팔을 늘리세요.'),
}


# New catalog movements share the same provenance gate as the original list.
# Their published dose and instruction are the pack's first-plan defaults.
import re as _re
from movement_catalog import MOVEMENTS as _MOVEMENTS
for _key, _item in _MOVEMENTS.items():
    if (_item['category'] not in ('mobility', 'activation', 'stretch')
            and _key not in ('roll_down', 'bear_crawl')):
        continue
    _dose = _item['dose']
    _amount = int(_re.search(r'\d+', _dose).group())
    PREP_DOSES[_key] = (_amount,
                        'seconds' if '초' in _dose else 'reps',
                        _item['how'])
