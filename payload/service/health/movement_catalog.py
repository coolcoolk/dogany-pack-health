"""Sourced, user-facing movement choices for session prep and program variety.

Dose is a conservative starting option, not a treatment prescription. See
refs/movement-catalog.md for the scope of each source and dose convention.
"""

ACE = 'https://www.acefitness.org/resources/everyone/exercise-library/'
ACE_WARM = 'https://www.acefitness.org/certifiednewsarticle/2910/a-detailed-guide-to-designing-activity-specific-warm-up-and-mobility-drills/'
ACE_FLEX = 'https://www.acefitness.org/certifiednews/images/article/pdfs/Flexibility.pdf'
ACSM = 'https://www.acsm.org/docs/default-source/publications-files/acsm-resources-exercise-physiologist-download.pdf'
NASM = 'https://www.nasm.org/workout-exercise-guidance'
NASM_CORE = 'https://www.nasm.org/resource-center/blog/training/core-training-programming'
LIFE_FITNESS_SELECT = 'https://support.lifefitness.com/hc/en-us/articles/30288253394327-Hammer-Strength-Hammer-Select-Owner-s-Manual'
ACE_SHOULDERS = 'https://www.acefitness.org/certifiednews/images/article/pdfs/ACEShoulderStudy.pdf'
NASM_LANDMINE = 'https://www.nasm.org/resource-center/blog/training/functional-strength-training'
STRENGTH_DOSE = 'https://www.govinfo.gov/content/pkg/GOVPUB-D101-PURL-gpo76069/pdf/GOVPUB-D101-PURL-gpo76069.pdf'
KIMWOG = 'knowledge/kimwog/items/exercise-dynamic-warmup-same-day-performance-022.md'


def entry(ko, en, category, areas, dose, how, caution, source, pattern=None):
    dose_source = (ACSM if '초' in dose else STRENGTH_DOSE
                   if category == 'strength' else ACE_WARM)
    return dict(ko=ko, en=en, category=category, areas=tuple(areas.split(',')),
                dose=dose, dose_source=dose_source, how=how,
                caution=tuple(caution.split(',')) if caution else (),
                source=source, pattern=pattern)


def _copy_entry(key, category, areas, caution, source):
    """A catalog entry whose ko/en name, dose and instruction live in the
    i18n tables (movement.<key>, health.movement_dose.<key>,
    health.movement_how.<key>)."""
    import json
    import os
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'i18n')
    with open(os.path.join(here, 'ko.json'), encoding='utf-8') as f:
        ko = json.load(f)
    with open(os.path.join(here, 'en.json'), encoding='utf-8') as f:
        en = json.load(f)
    return entry(ko['movement.' + key], en['movement.' + key], category, areas,
                 ko['health.movement_dose.' + key], ko['health.movement_how.' + key],
                 caution, source)


MOVEMENTS = {
    # Dynamic mobility: short, controlled repetitions before loading.
    'hip_knee_mobility': entry('90/90 힙 스위치','90/90 Hip Switch','mobility','hip,knee','좌우 6회','바닥에 앉아 두 무릎을 90도로 굽히고 좌우로 천천히 넘겨요.','hip,knee',ACE_WARM),
    'ankle_mobility': entry('무릎 벽 터치','Knee-to-Wall Ankle Mobilization','mobility','ankle,knee','좌우 8회','발뒤꿈치를 붙인 채 무릎을 벽 쪽으로 천천히 보내요.','ankle,knee',ACE_WARM),
    'cat_cow': entry('캣카우','Cat-Cow','mobility','back,lower_back','8회','네발기기에서 숨에 맞춰 등을 둥글게 말고 펴요.','back,lower_back',ACE),
    'thoracic_rotation': entry('네발기기 흉추 회전','Quadruped Thoracic Rotation','mobility','back,shoulder','좌우 6회','네발기기에서 한 손을 머리 뒤에 대고 팔꿈치를 천장 쪽으로 돌려요.','back,shoulder',ACE_WARM),
    'shoulder_circles': entry('암 서클','Arm Circles','mobility','shoulder','방향별 10회','양팔을 옆으로 벌리고 작은 원부터 천천히 그려요.','shoulder',ACE_WARM),
    'wrist_circles': entry('손목 돌리기','Wrist Circles','mobility','wrist,elbow','좌우 10회','손목으로 천천히 원을 그려요.','wrist,elbow',ACE_WARM),
    'leg_swing': entry('레그 스윙','Leg Swing','mobility','hip,hamstrings','좌우 10회','벽을 잡고 한쪽 다리를 앞뒤로 통제하며 흔들어요.','hip,back',ACE_WARM),
    'worlds_greatest_stretch': entry('월드 그레이티스트 스트레치',"World's Greatest Stretch",'mobility','hip,back,hamstrings','좌우 5회','런지 자세에서 같은 쪽 손을 천장으로 돌려 가슴을 열어요.','hip,knee,back,shoulder',ACE_WARM),
    'hamstring_sweep': entry('햄스트링 스윕','Hamstring Sweep','mobility','hamstrings,hip','좌우 8회','한쪽 발을 앞으로 내밀고 엉덩이를 접으며 양손을 발끝 쪽으로 쓸어요.','back,hip',ACE_WARM),
    'hip_flexor_stretch': entry('하프 니링 힙 플렉서 스트레치','Half-Kneeling Hip Flexor Stretch','stretch','hip,quads','좌우 20초','한쪽 무릎을 바닥에 대고 골반을 세운 채 앞으로 가볍게 옮겨요.','hip,knee',ACE_FLEX),
    'doorway_pec_stretch': entry('도어웨이 흉근 스트레치','Doorway Chest Stretch','stretch','chest,shoulder','20초','문틀에 팔을 대고 몸통을 살짝 앞으로 보내 가슴을 늘려요.','shoulder',ACE_FLEX),
    'sleeper_stretch': entry('슬리퍼 스트레치','Sleeper Stretch','stretch','shoulder','좌우 20초','옆으로 누워 위 손으로 아래팔을 천천히 바닥 쪽으로 내려요.','shoulder',ACE_FLEX),
    # Established activation and trunk exercises.
    'adductor_squeeze': entry('볼 스퀴즈','Ball Squeeze','activation','adductors,hip','15초','누워 무릎 사이의 공을 가볍게 조여요.','hip,knee',ACE),
    # Gym-standard prep (owner 2026-10-06 16:11/16:21): the machine / cable /
    # dumbbell variant any gym has, ahead of a small tool it may not have.
    # Names, dose and instruction are i18n copy (ko.json movement*.<key>).
    'hip_adduction_machine': _copy_entry('hip_adduction_machine', 'activation', 'adductors,hip', 'hip,knee', ACE),
    'cable_external_rotation': _copy_entry('cable_external_rotation', 'activation', 'shoulder', 'shoulder,elbow', ACE),
    'dumbbell_halo': _copy_entry('dumbbell_halo', 'activation', 'shoulder', 'shoulder', ACE_WARM),
    'glute_bridge': entry('글루트 브릿지','Glute Bridge','activation','glutes,hip','10회','누워 발바닥을 딛고 엉덩이를 들어 몸통과 허벅지를 일직선으로 만들어요.','hip,back,lower_back',ACE),
    'band_external_rotation': entry('밴드 외회전','Band External Rotation','activation','shoulder','좌우 10회','팔꿈치를 몸통 옆에 붙이고 밴드를 바깥쪽으로 당겨요.','shoulder,elbow',ACE),
    'dead_bug': entry('데드버그','Dead Bug','activation','abs,hip','좌우 6회','누워 허리를 바닥에 안정시키고 반대쪽 팔과 다리를 뻗어요.','back,hip',ACE),
    'pallof_press': entry('팔로프 프레스','Pallof Press','activation','abs,shoulder','좌우 8회','옆에서 당기는 밴드를 가슴 앞에서 밀며 몸통 회전을 버텨요.','back,shoulder',NASM_CORE),
    'bird_dog': entry('버드독','Bird Dog','activation','abs,back,glutes','좌우 6회','네발기기에서 반대쪽 팔과 다리를 뻗고 몸통을 고정해요.','back,shoulder,hip',ACE),
    'side_plank': entry('사이드 플랭크','Side Plank','activation','abs,hip','좌우 15초','팔꿈치를 어깨 아래에 두고 몸을 옆으로 곧게 들어요.','shoulder,hip,back',ACE),
    'band_pull_apart': entry('밴드 풀어파트','Band Pull-Apart','activation','back,shoulder','10회','가슴 높이에서 밴드를 잡고 양손을 옆으로 벌려요.','shoulder,elbow',ACE),
    'copenhagen_plank': entry('코펜하겐 플랭크','Copenhagen Plank','activation','adductors,abs','좌우 10초','옆 플랭크에서 위쪽 다리를 벤치에 올리고 몸을 들어요.','hip,knee,shoulder',NASM_CORE),
    'bodyweight_good_morning': entry('맨몸 굿모닝','Bodyweight Good Morning','activation','hamstrings,glutes','8회','무릎을 살짝 굽히고 엉덩이를 뒤로 보내 상체를 접어요.','back,hip',ACE_WARM),
    'band_good_morning': entry('밴드 굿모닝','Band Good Morning','activation','hamstrings,glutes','8회','발로 밴드를 밟고 엉덩이를 뒤로 보내며 상체를 접었다 펴요.','back,hip',ACE_WARM),
    'hip_hinge_drill': entry('벽 터치 힙 힌지','Wall-Touch Hip Hinge','activation','hamstrings,glutes','8회','벽 앞에 서서 엉덩이를 뒤로 보내 벽을 가볍게 터치해요.','back,hip',ACE_WARM),
    # Cooldown choices use named stretches, never generic body-part labels.
    'stretch_quads': entry('스탠딩 쿼드 스트레치','Standing Quadriceps Stretch','stretch','quads','좌우 20초','서서 한 발을 잡고 뒤꿈치를 엉덩이 쪽으로 당겨요.','knee',ACE_FLEX),
    'stretch_hamstrings': entry('스탠딩 햄스트링 스트레치','Standing Hamstring Stretch','stretch','hamstrings','좌우 20초','한 발을 앞에 놓고 엉덩이를 접으며 허벅지 뒤를 늘려요.','back,knee',ACE_FLEX),
    'stretch_hip_flexors': entry('니링 힙 플렉서 스트레치','Kneeling Hip Flexor Stretch','stretch','hip','좌우 20초','한쪽 무릎을 바닥에 대고 골반을 세워 앞쪽을 늘려요.','hip,knee',ACE_FLEX),
    'stretch_glutes': entry('누운 피겨 포 스트레치','Supine Figure-Four Stretch','stretch','glutes','좌우 20초','누워 한쪽 발목을 반대 무릎 위에 올리고 허벅지를 당겨요.','hip,lower_back',ACE_FLEX),
    'stretch_calves': entry('월 카프 스트레치','Wall Calf Stretch','stretch','calves','좌우 20초','벽을 짚고 한 발을 뒤로 보내 뒤꿈치를 바닥에 붙여요.','ankle',ACE_FLEX),
    'stretch_chest': entry('도어웨이 가슴 스트레치','Doorway Chest Stretch','stretch','chest','20초','문틀에 팔을 대고 한 발 앞으로 나가 가슴을 늘려요.','shoulder',ACE_FLEX),
    'stretch_lats': entry('차일드 포즈','Child’s Pose','stretch','back','20초','무릎을 꿇고 엉덩이를 뒤로 보내며 팔을 길게 뻗어요.','knee,back,shoulder',ACE),
    'stretch_shoulders': entry('크로스 바디 숄더 스트레치','Cross-Body Shoulder Stretch','stretch','shoulder','좌우 20초','한 팔을 가슴 앞으로 보내 반대 손으로 가볍게 당겨요.','shoulder',ACE_FLEX),
    'stretch_triceps': entry('오버헤드 트라이셉스 스트레치','Overhead Triceps Stretch','stretch','triceps','좌우 20초','한 팔을 머리 위로 굽히고 반대 손으로 팔꿈치를 잡아요.','shoulder,elbow',ACE_FLEX),
    'stretch_forearms': entry('손목 굴곡근 스트레치','Wrist Flexor Stretch','stretch','forearms','좌우 20초','팔을 펴고 손바닥을 앞으로 향한 뒤 손가락을 부드럽게 당겨요.','wrist,elbow',ACE_FLEX),
    # Grip/equipment additions: source links support identity/form;
    # all new numeric muscle shares are estimates, not measured EMG ratios.
    'underhand_barbell_row': entry('언더그립 바벨 로우', 'Underhand Barbell Row', 'strength', 'back,biceps', '5~8회', '손바닥이 앞을 향하게 바벨을 잡고 상체를 고정한 채 아랫배로 당겨요.', 'back,elbow,wrist', 'https://www.acefitness.org/resources/everyone/exercise-library/', 'horizontal_pull'),
    'wide_grip_lat_pulldown': entry('와이드그립 랫 풀다운', 'Wide-Grip Lat Pulldown', 'strength', 'back,biceps', '5~8회', '손등이 뒤를 향하게 어깨보다 넓게 잡고 바를 가슴 위쪽으로 당겨요.', 'shoulder,elbow', 'https://pubmed.ncbi.nlm.nih.gov/20543740/', 'vertical_pull'),
    'close_grip_lat_pulldown': entry('클로즈그립 랫 풀다운', 'Close-Grip Lat Pulldown', 'strength', 'back,biceps', '5~8회', '짧은 바를 어깨너비보다 좁게 오버그립으로 잡고 가슴 위쪽으로 당겨요.', 'shoulder,elbow,wrist', 'https://pubmed.ncbi.nlm.nih.gov/20543740/', 'vertical_pull'),
    'neutral_grip_lat_pulldown': entry('뉴트럴그립 랫 풀다운', 'Neutral-Grip Lat Pulldown', 'strength', 'back,biceps,forearms', '5~8회', '손바닥이 마주 보는 손잡이를 잡고 팔꿈치를 아래로 당겨요.', 'shoulder,elbow', 'https://www.acefitness.org/resources/everyone/exercise-library/', 'vertical_pull'),
    'underhand_lat_pulldown': entry('언더그립 랫 풀다운', 'Underhand Lat Pulldown', 'strength', 'back,biceps', '5~8회', '손바닥이 몸을 향하도록 바를 잡고 몸통을 고정한 채 당겨요.', 'shoulder,elbow,wrist', 'https://pubmed.ncbi.nlm.nih.gov/20543740/', 'vertical_pull'),
    'neutral_grip_pullup': entry('뉴트럴그립 풀업', 'Neutral-Grip Pull-Up', 'strength', 'back,biceps,forearms', '5~8회', '평행 손잡이를 잡고 반동 없이 팔꿈치를 아래로 당겨 몸을 올려요.', 'shoulder,elbow', 'https://www.acefitness.org/resources/everyone/exercise-library/', 'vertical_pull'),
    'kettlebell_swing': entry('케틀벨 스윙', 'Kettlebell Swing', 'strength', 'glutes,hamstrings', '5~8회', '두 손으로 케틀벨을 잡고 힙힌지 후 엉덩이를 펴서 가슴 높이까지 보내요.', 'back,hip,shoulder', 'https://www.acefitness.org/resources/pros/expert-articles/5269/how-to-get-started-with-kettlebells/', 'hinge'),
    'kettlebell_goblet_squat': entry('케틀벨 고블릿 스쿼트', 'Kettlebell Goblet Squat', 'strength', 'quads,glutes', '5~8회', '케틀벨을 가슴 앞에 잡고 발바닥을 붙인 채 앉았다 일어나요.', 'knee,hip,back', 'https://www.acefitness.org/resources/pros/expert-articles/5269/how-to-get-started-with-kettlebells/', 'squat'),
    'single_arm_kettlebell_row': entry('원암 케틀벨 로우', 'Single-Arm Kettlebell Row', 'strength', 'back,biceps,forearms', '좌우 5~8회', '한 손으로 벤치를 지지하고 반대 손의 케틀벨을 옆구리로 당겨요.', 'back,shoulder,elbow', 'https://www.acefitness.org/resources/everyone/exercise-library/', 'horizontal_pull'),
    'kettlebell_clean': entry('원암 케틀벨 클린', 'Single-Arm Kettlebell Clean', 'strength', 'glutes,hamstrings', '좌우 5~8회', '힙힌지로 케틀벨을 띄우고 팔꿈치를 몸 가까이 두며 손을 넣어 랙 자세로 받아요.', 'back,hip,wrist,shoulder', 'https://www.acefitness.org/continuing-education/certified/october-2022/8147/kettlebells-kick-butt-in-more-ways-than-one/', 'hinge'),
    'trap_bar_deadlift': entry('트랩바 데드리프트', 'Trap-Bar Deadlift', 'strength', 'quads,glutes,hamstrings', '5~8회', '트랩바 중앙에 서서 평행 손잡이를 잡고 발바닥으로 바닥을 밀며 일어나요.', 'back,hip,knee', 'https://www.nsca.com/globalassets/education/nsca-coach/nsca-coach-7.1.pdf', 'hinge'),
    'trap_bar_shrug': entry('트랩바 슈러그', 'Trap-Bar Shrug', 'strength', 'back,forearms', '12~15회', '트랩바 평행 손잡이를 잡고 팔을 편 채 어깨를 위로 올렸다 내려요.', 'neck,shoulder', 'https://www.acefitness.org/resources/everyone/exercise-library/', 'isolation'),
    'ez_bar_curl': entry('이지바 컬', 'EZ-Bar Curl', 'strength', 'biceps', '12~15회', '이지바 굴곡에 손바닥을 위로 두고 위팔을 고정한 채 팔꿈치를 굽혀요.', 'elbow,wrist', 'https://www.acefitness.org/resources/everyone/exercise-library/', 'isolation'),
    'ez_bar_reverse_curl': entry('이지바 리버스 컬', 'EZ-Bar Reverse Curl', 'strength', 'forearms,biceps', '12~15회', '이지바를 손등이 위로 오게 잡고 손목을 고정한 채 팔꿈치를 굽혀요.', 'elbow,wrist', 'https://www.acefitness.org/resources/everyone/exercise-library/', 'isolation'),
    'medicine_ball_slam': entry('메디신볼 슬램', 'Medicine Ball Slam', 'strength', 'abs,back,shoulders', '5~8회', '슬램용 공을 머리 위로 들고 몸통과 엉덩이를 굽혀 발 앞 바닥으로 내려쳐요.', 'back,shoulder', 'https://www.acefitness.org/continuing-education/certified/june-2019/7306/medicine-balls-an-ace-integrated-fitness-training-reg-model-workout/', 'hinge'),
    'rotational_medicine_ball_throw': entry('메디신볼 회전 던지기', 'Rotational Medicine Ball Throw', 'strength', 'abs', '좌우 12~15회', '벽 옆에 서서 발과 골반을 함께 돌려 공을 벽으로 던지고 양쪽을 번갈아 해요.', 'back,hip,shoulder', 'https://www.acefitness.org/continuing-education/certified/june-2019/7306/medicine-balls-an-ace-integrated-fitness-training-reg-model-workout/', 'core'),
    # Strength alternatives. The taxonomy maps their loading separately.
    'front_squat': entry('프론트 스쿼트','Front Squat','strength','quads,glutes','8~12회','바벨을 어깨 앞에 얹고 몸통을 세워 앉았다 일어나요.','knee,hip,back',ACE, 'squat'),
    'box_squat': entry('박스 스쿼트','Box Squat','strength','quads,glutes','8~12회','엉덩이를 뒤로 보내 박스에 가볍게 닿은 뒤 일어나요.','knee,hip,back',ACE, 'squat'),
    'step_up': entry('스텝업','Step-Up','strength','quads,glutes','좌우 8회','한 발을 박스에 올리고 그 발로 밀어 올라가요.','knee,hip',ACE, 'squat'),
    'dumbbell_rdl': entry('덤벨 루마니안 데드리프트','Dumbbell Romanian Deadlift','strength','hamstrings,glutes','8~12회','덤벨을 몸 가까이 두고 엉덩이를 뒤로 보내 상체를 접어요.','back,hip',NASM, 'hinge'),
    'kettlebell_deadlift': entry('케틀벨 데드리프트','Kettlebell Deadlift','strength','hamstrings,glutes','8~12회','발 사이의 케틀벨을 잡고 발바닥으로 바닥을 밀며 일어나요.','back,hip,knee',NASM, 'hinge'),
    'incline_push_up': entry('인클라인 푸시업','Incline Push-Up','strength','chest,triceps','8~12회','벤치에 손을 짚고 몸을 일직선으로 유지하며 팔을 굽혔다 펴요.','shoulder,wrist,elbow',NASM, 'horizontal_push'),
    'cable_chest_press': entry('케이블 체스트 프레스','Cable Chest Press','strength','chest,triceps','8~12회','양손의 케이블 손잡이를 가슴 앞에서 밀어요.','shoulder,elbow',ACE, 'horizontal_push'),
    'chest_supported_dumbbell_row': entry('체스트 서포티드 덤벨 로우','Chest-Supported Dumbbell Row','strength','back,biceps','8~12회','경사 벤치에 가슴을 대고 덤벨을 옆구리로 당겨요.','shoulder,elbow',ACE, 'horizontal_pull'),
    'single_arm_cable_row': entry('원암 케이블 로우','Single-Arm Cable Row','strength','back,biceps','좌우 8회','케이블을 한 손으로 잡고 팔꿈치를 옆구리 뒤로 당겨요.','shoulder,elbow,back',ACE, 'horizontal_pull'),
    'landmine_press': entry('랜드마인 프레스','Landmine Press','strength','shoulder,triceps','좌우 8회','바벨 한쪽 끝을 잡고 비스듬히 위로 밀어요.','shoulder,elbow,back',NASM_LANDMINE, 'vertical_push'),
    # Barbell staples: sources describe identity/form, not numeric shares.
    # Lunge, bridge and crunch references cover the movement family.
    'close_grip_bench_press': entry('클로즈 그립 벤치 프레스', 'Close-Grip Bench Press', 'strength', 'triceps,chest', '8~12회', '벤치에 누워 바벨을 어깨너비 정도로 잡고 가슴 쪽으로 내렸다 밀어요.', 'shoulder,elbow,wrist', 'https://www.strengthlog.com/close-grip-bench-press/', 'horizontal_push'),
    'decline_bench_press': entry('디클라인 벤치 프레스', 'Decline Bench Press', 'strength', 'chest,triceps', '8~12회', '다리를 고정한 디클라인 벤치에 누워 바벨을 가슴 아래쪽으로 내렸다 밀어요.', 'shoulder,elbow', 'https://www.strengthlog.com/decline-bench-press/', 'horizontal_push'),
    'barbell_reverse_lunge': entry('바벨 리버스 런지', 'Barbell Reverse Lunge', 'strength', 'quads,glutes', '좌우 8~12회', '바벨을 등 위에 얹고 한 발을 뒤로 내딛어 앉았다 앞발로 밀어 돌아와요.', 'knee,hip,back', 'https://www.strengthlog.com/barbell-lunge/', 'squat'),
    'barbell_split_squat': entry('바벨 스플릿 스쿼트', 'Barbell Split Squat', 'strength', 'quads,glutes', '좌우 8~12회', '바벨을 등 위에 얹고 두 발을 앞뒤로 고정한 채 무릎을 굽혔다 펴요.', 'knee,hip,back', 'https://www.strengthlog.com/barbell-lunge/', 'squat'),
    'good_morning': entry('바벨 굿모닝', 'Barbell Good Morning', 'strength', 'hamstrings,glutes', '8~12회', '바벨을 등 위에 얹고 무릎을 살짝 굽힌 채 엉덩이를 뒤로 보내 상체를 접었다 펴요.', 'back,lower_back,hip', 'https://www.strengthlog.com/good-morning/', 'hinge'),
    'sumo_deadlift': entry('스모 데드리프트', 'Sumo Deadlift', 'strength', 'hamstrings,glutes,back', '8~12회', '발을 넓게 벌리고 무릎 안쪽으로 바벨을 잡아 몸 가까이 유지하며 일어나요.', 'back,hip,knee', 'https://www.strengthlog.com/sumo-deadlift/', 'hinge'),
    'barbell_shrug': entry('바벨 슈러그', 'Barbell Shrug', 'strength', 'back', '8~12회', '바벨을 허벅지 앞에 들고 팔을 편 채 어깨를 위로 올렸다 천천히 내려요.', 'shoulder,neck', 'https://www.strengthlog.com/barbell-shrug/', 'isolation'),
    'barbell_glute_bridge': entry('바벨 글루트 브릿지', 'Barbell Glute Bridge', 'strength', 'glutes,hamstrings', '8~12회', '등을 바닥에 대고 누워 패드를 댄 바벨을 골반에 놓고 발로 밀어 엉덩이를 들어요.', 'hip,back,lower_back', 'https://www.strengthlog.com/glute-bridge/', 'hinge'),
    'barbell_seal_row': entry('바벨 씰 로우', 'Barbell Seal Row', 'strength', 'back,biceps', '8~12회', '높은 수평 벤치에 엎드려 가슴을 지지하고 아래의 바벨을 몸 쪽으로 당겨요.', 'shoulder,elbow', 'https://www.strengthlog.com/seal-row/', 'horizontal_pull'),
    'dumbbell_crunch': entry('덤벨 크런치', 'Dumbbell Crunch', 'strength', 'abs', '8~12회', '덤벨을 가슴 앞에 고정하고 누워 갈비뼈를 골반 쪽으로 당기며 어깨를 조금 들어요.', 'back', 'https://www.strengthlog.com/crunch/', 'core'),
    # Strength expansion: sources support the movement family and form;
    # taxonomy shares are accounting estimates, not measured activation.
    'single_leg_press': entry('싱글 레그 프레스', 'Single-Leg Press', 'strength', 'quads,glutes', '좌우 8~12회', '한 발을 발판에 놓고 골반을 고정한 채 밀어요.', 'knee,hip', NASM, 'squat'),
    'seated_leg_curl': entry('시티드 레그 컬', 'Seated Leg Curl', 'strength', 'hamstrings', '8~12회', '등을 패드에 붙이고 무릎을 굽혀 패드를 아래로 당겨요.', 'knee', 'https://www.nasm.org/workout-exercise-guidance/how-to-seated-leg-curl', 'isolation'),
    'single_leg_lying_curl': entry('싱글 레그 라잉 레그 컬', 'Single-Leg Lying Leg Curl', 'strength', 'hamstrings', '좌우 8~12회', '엎드려 골반을 고정하고 한쪽 무릎을 굽혀요.', 'knee', NASM, 'isolation'),
    'cable_glute_kickback': entry('케이블 글루트 킥백', 'Cable Glute Kickback', 'strength', 'glutes', '좌우 8~12회', '발목 스트랩을 걸고 허리를 고정한 채 한쪽 다리를 뒤로 보내요.', 'hip,back', 'https://www.strengthlog.com/cable-glute-kickback/', 'isolation'),
    'single_arm_dumbbell_bench_press': entry('원암 덤벨 벤치 프레스', 'Single-Arm Dumbbell Bench Press', 'strength', 'chest,triceps', '좌우 8~12회', '벤치에 누워 한 손의 덤벨을 가슴 옆에서 위로 밀어요.', 'shoulder,elbow', NASM, 'horizontal_push'),
    'seated_machine_row': entry('시티드 머신 로우', 'Seated Machine Row', 'strength', 'back,biceps', '8~12회', '가슴을 패드에 대고 손잡이를 몸 쪽으로 당겨요.', 'shoulder,elbow', NASM, 'horizontal_pull'),
    'inverted_row': entry('인버티드 로우', 'Inverted Row', 'strength', 'back,biceps', '8~12회', '고정된 낮은 바 아래에서 몸을 곧게 유지하며 가슴을 바 쪽으로 당겨요.', 'shoulder,elbow', ACE, 'horizontal_pull'),
    'machine_shoulder_press': entry('머신 숄더 프레스', 'Machine Shoulder Press', 'strength', 'shoulder,triceps', '8~12회', '등을 패드에 붙이고 손잡이를 머리 위로 밀어요.', 'shoulder,elbow,wrist', LIFE_FITNESS_SELECT, 'vertical_push'),
    'pike_push_up': entry('파이크 푸시업', 'Pike Push-Up', 'strength', 'shoulder,triceps', '8~12회', '엉덩이를 높인 자세에서 팔꿈치를 굽혔다 펴며 몸을 밀어요.', 'shoulder,elbow,wrist', NASM, 'vertical_push'),
    'machine_lateral_raise': entry('머신 레터럴 레이즈', 'Machine Lateral Raise', 'strength', 'shoulder', '8~12회', '상체를 고정하고 팔 바깥쪽으로 패드를 옆으로 들어요.', 'shoulder', LIFE_FITNESS_SELECT, 'isolation'),
    'single_arm_dumbbell_lateral_raise': entry('원암 덤벨 레터럴 레이즈', 'Single-Arm Dumbbell Lateral Raise', 'strength', 'shoulder', '좌우 8~12회', '한 손으로 지지대를 잡고 반대 손의 덤벨을 옆으로 들어요.', 'shoulder', ACE, 'isolation'),
    'seated_dumbbell_reverse_fly': entry('시티드 벤트오버 레터럴 레이즈', 'Seated Dumbbell Reverse Fly', 'strength', 'shoulder', '8~12회', '앉아서 상체를 숙이고 덤벨을 양옆으로 벌려요.', 'shoulder', ACE_SHOULDERS, 'isolation'),
    'cable_reverse_fly': entry('케이블 리버스 플라이', 'Cable Reverse Fly', 'strength', 'shoulder', '8~12회', '양쪽 케이블을 교차해 잡고 팔을 옆으로 벌려요.', 'shoulder', ACE, 'isolation'),
    'cable_curl': entry('케이블 컬', 'Cable Curl', 'strength', 'biceps', '8~12회', '팔꿈치를 몸통 옆에 두고 케이블 바를 말아 올려요.', 'elbow,wrist', ACE, 'isolation'),
    'dumbbell_overhead_triceps_extension': entry('덤벨 오버헤드 트라이셉스 익스텐션', 'Dumbbell Overhead Triceps Extension', 'strength', 'triceps', '8~12회', '덤벨을 양손으로 머리 위에 들고 팔꿈치를 굽혔다 펴요.', 'elbow,shoulder', ACE, 'isolation'),
    'dumbbell_triceps_kickback': entry('덤벨 트라이셉스 킥백', 'Dumbbell Triceps Kickback', 'strength', 'triceps', '좌우 8~12회', '상체를 숙이고 위팔을 고정한 채 한쪽 팔꿈치를 펴요.', 'elbow,shoulder', ACE, 'isolation'),
    'single_leg_calf_raise': entry('싱글 레그 카프 레이즈', 'Single-Leg Calf Raise', 'strength', 'calves', '좌우 8~12회', '벽을 가볍게 짚고 한 발로 서서 뒤꿈치를 올렸다 내려요.', 'ankle', ACE, 'isolation'),
    'dumbbell_standing_calf_raise': entry('덤벨 스탠딩 카프 레이즈', 'Dumbbell Standing Calf Raise', 'strength', 'calves', '8~12회', '덤벨을 양옆에 들고 뒤꿈치를 올렸다 천천히 내려요.', 'ankle', ACE, 'isolation'),
    'leg_press_calf_raise': entry('레그 프레스 카프 레이즈', 'Leg Press Calf Raise', 'strength', 'calves', '8~12회', '발판 아래쪽에 앞꿈치를 놓고 무릎 각도를 유지하며 발목을 펴요.', 'ankle', NASM, 'isolation'),
    'crunch': entry('크런치', 'Crunch', 'strength', 'abs', '8~12회', '누워 무릎을 굽히고 갈비뼈를 골반 쪽으로 당기며 어깨를 들어요.', 'back', ACE, 'core'),
    'reverse_crunch': entry('리버스 크런치', 'Reverse Crunch', 'strength', 'abs', '8~12회', '누워 무릎을 굽힌 채 골반을 말아 엉덩이를 조금 들어요.', 'back', 'https://www.acefitness.org/resources/everyone/exercise-library/76/reverse-crunch/', 'core'),
    'machine_crunch': entry('머신 크런치', 'Machine Crunch', 'strength', 'abs', '8~12회', '머신에 앉아 골반을 고정하고 몸통을 앞으로 말아요.', 'back', LIFE_FITNESS_SELECT, 'core'),
    # Goal practice picks (2026-09-29): breath_trunk / whole_body work rows
    # and the conditioning finisher's bodyweight intervals.
    'roll_down': entry('롤다운', 'Roll-Down', 'strength', 'abs,back', '6~8회', '앉아서 숨을 내쉬며 척추를 하나씩 말아 뒤로 내려갔다가 다시 말아 올라와요.', 'back,lower_back', ACE, 'core'),
    'hollow_hold': entry('할로우 홀드', 'Hollow Body Hold', 'strength', 'abs', '20초', '누워 허리를 바닥에 붙이고 팔다리를 뻗어 살짝 든 채 숨을 고르게 쉬어요.', 'back,lower_back', NASM_CORE, 'core'),
    'bear_crawl': entry('베어 크롤', 'Bear Crawl', 'strength', 'abs,shoulder,quads', '좌우 8~12걸음씩', '네발기기에서 무릎을 바닥에서 살짝 띄우고 반대쪽 손발을 같이 옮겨 기어가요.', 'wrist,shoulder,knee', ACE, 'core'),
    'turkish_get_up': entry('터키시 겟업', 'Turkish Get-Up', 'strength', 'abs,shoulder,glutes', '좌우 2~3회', '가벼운 케틀벨을 한 손으로 천장 쪽에 든 채 누운 자세에서 일어섰다가 같은 길로 돌아가요.', 'shoulder,wrist,hip,knee', 'https://www.acefitness.org/resources/pros/expert-articles/5269/how-to-get-started-with-kettlebells/', 'core'),
    'mountain_climber': entry('마운틴 클라이머', 'Mountain Climber', 'cardio', 'abs,hip', '30초', '팔을 펴고 엎드린 자세에서 무릎을 가슴 쪽으로 번갈아 빠르게 당겨요.', 'wrist,shoulder', ACE),
    'jumping_jack': entry('점핑 잭', 'Jumping Jack', 'cardio', 'calves,shoulder', '30초', '제자리에서 뛰며 팔다리를 벌렸다 모아요.', 'knee,ankle,foot', ACE),
    'high_knee_march': entry('하이니 마치', 'High-Knee March', 'cardio', 'hip,abs', '30초', '제자리에서 무릎을 골반 높이까지 번갈아 빠르게 올려요.', 'hip', ACE_WARM),
    # Goal power pick (2026-09-30): explosive moves for the power block; the
    # swing and slam rows above serve it too. Low box, soft landing.
    'box_jump': entry('박스 점프', 'Box Jump', 'strength', 'quads,glutes,calves', '3~5회', '무릎 높이 아래의 낮은 박스 앞에서 팔을 흔들어 뛰어올라 두 발로 부드럽게 착지하고, 내려올 땐 걸어서 내려와요.', 'knee,ankle,foot', ACE),
    'squat_jump': entry('스쿼트 점프', 'Squat Jump', 'strength', 'quads,glutes,calves', '3~5회', '살짝 앉았다가 바닥을 밀어 곧게 뛰어오르고, 무릎을 굽히며 발 앞쪽부터 조용히 착지해요.', 'knee,ankle,foot,hip', ACE),
}


# 2024 Adult Compendium of Physical Activities. METs are gross intensity;
# active calories subtract resting 1 MET in cardio-record. Incline walk
# uses uphill walking (17034) as a proxy when treadmill grade is unspecified.
CARDIO_CATALOG = {
    'stepmill': {'ko': '천국의 계단(스텝밀)', 'met': 9.3, 'activity_code': '02065',
                 'source': 'https://pacompendium.com/conditioning-exercise/'},
    'run': {'ko': '러닝', 'met': 8.0, 'activity_code': '12150',
            'source': 'https://pacompendium.com/running/'},
    'incline_walk': {'ko': '러닝머신 경사 걷기', 'met': 5.3, 'activity_code': '17034',
                     'source': 'https://pacompendium.com/walking/'},
    'bike': {'ko': '자전거', 'met': 6.8, 'activity_code': '01200',
             'source': 'https://pacompendium.com/bicycling/'},
    'row': {'ko': '로잉', 'met': 5.0, 'activity_code': '02071',
            'source': 'https://pacompendium.com/conditioning-exercise/'},
}


def drill_identity(key):
    """The drill a catalog key names: keys whose English name is the same
    are one drill under two Korean labels (doorway_pec_stretch and
    stretch_chest are both the Doorway Chest Stretch -- owner 2026-10-06
    21:04 saw them listed side by side). The first catalog key with that
    name is the identity; an unknown key is its own."""
    item = MOVEMENTS.get(key)
    if not item or not item.get('en'):
        return key
    return next(k for k, v in MOVEMENTS.items() if v.get('en') == item['en'])


def distinct_drills(keys):
    """`keys` in order, a drill already listed under another key dropped
    (drill_identity)."""
    out, seen = [], set()
    for key in keys:
        ident = drill_identity(key)
        if ident not in seen:
            seen.add(ident)
            out.append(key)
    return out


def available_prep(lift_patterns, caution=()):
    """Choose varied mat options by lift patterns while avoiding caution tags."""
    choices = {'squat': ('ankle_mobility', 'hip_knee_mobility', 'glute_bridge'),
               'hinge': ('leg_swing', 'hip_hinge_drill', 'glute_bridge', 'bird_dog'),
               'horizontal_push': ('thoracic_rotation', 'band_external_rotation'),
               'vertical_push': ('shoulder_circles', 'band_pull_apart'),
               'horizontal_pull': ('cat_cow', 'band_pull_apart'),
               'vertical_pull': ('thoracic_rotation', 'band_pull_apart'),
               'core': ('dead_bug', 'bird_dog')}
    blocked = set(caution)
    out = []
    for pattern in lift_patterns:
        for key in choices.get(pattern, ()):
            item = MOVEMENTS[key]
            if key not in out and not blocked.intersection(item['caution']):
                out.append(key)
    return out


def stretching_table(keys):
    rows = ['| 스트레칭 | 횟수·시간 | 방법 |', '|-|-|-|']
    for key in keys:
        item = MOVEMENTS[key]
        rows.append('| %s | %s | %s |' % (item['ko'], item['dose'], item['how']))
    return '\n'.join(rows)
