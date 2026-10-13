-- health_taxonomy_seed.sql -- pack_health owned taxonomy DATA.
--
-- WHAT THIS IS
--   The 370 rows of muscle / exercise classification that used to be INSERTed
--   by dogany-lifekit payload/database/schema.sql at every fresh mint. The
--   TABLES still belong to the kit (they are FK targets and kit_life's schema
--   owns their DDL); the ROWS are pack_health product knowledge and belong
--   to this pack. An instance that never trains no longer receives them.
--
-- WHY EVERY STATEMENT IS "INSERT OR IGNORE"
--   All 11 tables carry a NATURAL primary key (verified, no implicit-rowid
--   table in the set), so a PK collision is an exact identity match. OR IGNORE
--   therefore means: a row already present is left EXACTLY as it is, including
--   any edit the user made on top of it. This file can never clobber a user's
--   own taxonomy. It can only add rows that are absent.
--
-- ORDER IS LOAD-BEARING
--   muscle_label.node REFERENCES muscle_node(node) and muscle_node.parent
--   REFERENCES muscle_node(node) (self). The statement order below is the
--   schema.sql source order, which is already topologically valid; the runner
--   (health_taxonomy_seed.py) additionally runs PRAGMA foreign_key_check on
--   every touched table inside the transaction and rolls back on any violation.
--   The muscle TREE (muscle_node, then muscle_label) comes FIRST, before any
--   map row (2026-09-30, kit 063). 063 binds exercise_muscle_map.muscle /
--   exercise_subregion_map.subregion to muscle_node by trigger on every
--   connection, and exempts only a completely EMPTY muscle_node. Maps first
--   rode that exemption on a fresh mint; with the tree first, every map row
--   is checked against the tree as it lands.
--
-- DO NOT hand-edit to add product knowledge. Every row below is one of three
-- things: a MOVE of a row schema.sql used to insert (byte-for-byte apart from
-- the OR IGNORE conflict clause -- that is what makes the parity proof
-- possible); for the ax_exercise block, DERIVED BY RULE from rows already in
-- this file; or, inside the @@CATALOG-2026-09-26 block at the very end,
-- GENERATED from exercise_catalog.py (the reviewed catalog expansion: bench
-- press, leg press, push-up, plank, lunges and the other staples the planner
-- could never offer). To change that block, edit exercise_catalog.py and
-- re-emit it (`exercise_catalog.py --emit-sql`); a test holds them identical.
--
-- @@OWNING_AGENT@@ -- THE ONE TOKEN IN THIS FILE (2026-09-14)
--   ax_projection_rule and ax_exercise both carry `owning_agent`, the column
--   that tells two crew members apart on the shared kit_life.db. This file used
--   to write a hard-coded legacy slug into all nine rule
--   rows. The runner substitutes the token for the slug THIS instance resolves
--   (health_taxonomy_seed.py: --owning-agent > LIFEKIT_OWNING_AGENT >
--   .instance.conf DOGANY_AGENT_NAME), and degrades to the legacy slug, out
--   loud, on a pre-049 DB whose CHECK still refuses anything else.
--   The token is substituted BEFORE the SQL guard runs, so a guard failure is
--   read on the statement that will actually execute.
--
-- Runner: health_taxonomy_seed.py (dry-run by default; --apply to write).

-- muscle_node (47 rows)
INSERT OR IGNORE INTO muscle_node VALUES('arms',NULL,'group',3,NULL);
INSERT OR IGNORE INTO muscle_node VALUES('legs',NULL,'group',4,NULL);
INSERT OR IGNORE INTO muscle_node VALUES('core',NULL,'group',5,NULL);
INSERT OR IGNORE INTO muscle_node VALUES('chest',NULL,'muscle',0,'chest');
INSERT OR IGNORE INTO muscle_node VALUES('back',NULL,'muscle',1,'back');
INSERT OR IGNORE INTO muscle_node VALUES('shoulders',NULL,'muscle',2,'shoulders');
INSERT OR IGNORE INTO muscle_node VALUES('biceps','arms','muscle',306,'biceps');
INSERT OR IGNORE INTO muscle_node VALUES('forearms','arms','muscle',307,'forearms');
INSERT OR IGNORE INTO muscle_node VALUES('triceps','arms','muscle',308,'triceps');
INSERT OR IGNORE INTO muscle_node VALUES('calves','legs','muscle',409,'calves');
INSERT OR IGNORE INTO muscle_node VALUES('glutes','legs','muscle',410,'glutes');
INSERT OR IGNORE INTO muscle_node VALUES('hamstrings','legs','muscle',411,'hamstrings');
INSERT OR IGNORE INTO muscle_node VALUES('quads','legs','muscle',412,'quads');
INSERT OR IGNORE INTO muscle_node VALUES('abs','core','muscle',513,'abs');
INSERT OR IGNORE INTO muscle_node VALUES('abs_lower','abs','subregion',0,'abs_lower');
INSERT OR IGNORE INTO muscle_node VALUES('adductors','legs','subregion',1,'adductors');
INSERT OR IGNORE INTO muscle_node VALUES('back_erectors','back','subregion',2,'back');
INSERT OR IGNORE INTO muscle_node VALUES('back_lats','back','subregion',3,'back');
INSERT OR IGNORE INTO muscle_node VALUES('back_upper','back','subregion',4,'back');
INSERT OR IGNORE INTO muscle_node VALUES('biceps_distal','biceps','subregion',5,'biceps');
INSERT OR IGNORE INTO muscle_node VALUES('biceps_prox','biceps','subregion',6,'biceps');
INSERT OR IGNORE INTO muscle_node VALUES('calf_gastroc','calves','subregion',7,'calves');
INSERT OR IGNORE INTO muscle_node VALUES('calf_soleus','calves','subregion',8,'calves');
INSERT OR IGNORE INTO muscle_node VALUES('chest_lower','chest','subregion',9,'chest');
INSERT OR IGNORE INTO muscle_node VALUES('chest_mid','chest','subregion',10,'chest');
INSERT OR IGNORE INTO muscle_node VALUES('chest_upper','chest','subregion',11,'chest');
INSERT OR IGNORE INTO muscle_node VALUES('front_delt','shoulders','subregion',12,'front_delt');
INSERT OR IGNORE INTO muscle_node VALUES('glute_max','glutes','subregion',13,'glutes');
INSERT OR IGNORE INTO muscle_node VALUES('glute_med','glutes','subregion',14,'glutes');
INSERT OR IGNORE INTO muscle_node VALUES('rear_delt','shoulders','subregion',15,'rear_delt');
INSERT OR IGNORE INTO muscle_node VALUES('side_delt','shoulders','subregion',16,'side_delt');
INSERT OR IGNORE INTO muscle_node VALUES('triceps_lat_med','triceps','subregion',17,'triceps');
INSERT OR IGNORE INTO muscle_node VALUES('triceps_long','triceps','subregion',18,'triceps');
INSERT OR IGNORE INTO muscle_node VALUES('rotator_cuff','shoulders','subregion',19,'rotator_cuff');
INSERT OR IGNORE INTO muscle_node VALUES('obliques','abs','subregion',20,'obliques');
INSERT OR IGNORE INTO muscle_node VALUES('brachialis','biceps','subregion',21,'biceps');
INSERT OR IGNORE INTO muscle_node VALUES('brachioradialis','forearms','subregion',22,'forearms');
INSERT OR IGNORE INTO muscle_node VALUES('hip_flexors','legs','subregion',23,'hip_flexors');
INSERT OR IGNORE INTO muscle_node VALUES('tibialis_anterior','legs','subregion',24,'tibialis_anterior');
INSERT OR IGNORE INTO muscle_node VALUES('serratus','chest','subregion',25,'chest');
INSERT OR IGNORE INTO muscle_node VALUES('forearm_flexors','forearms','subregion',26,'forearms');
INSERT OR IGNORE INTO muscle_node VALUES('forearm_extensors','forearms','subregion',27,'forearms');
INSERT OR IGNORE INTO muscle_node VALUES('rect_fem','quads','subregion',28,'quads');
INSERT OR IGNORE INTO muscle_node VALUES('vast_lat','quads','subregion',29,'quads');
INSERT OR IGNORE INTO muscle_node VALUES('vast_med','quads','subregion',30,'quads');
INSERT OR IGNORE INTO muscle_node VALUES('hams_lateral','hamstrings','subregion',31,'hamstrings');
INSERT OR IGNORE INTO muscle_node VALUES('hams_medial','hamstrings','subregion',32,'hamstrings');

-- muscle_label (94 rows)
INSERT OR IGNORE INTO muscle_label VALUES('arms','ko','long','팔');
INSERT OR IGNORE INTO muscle_label VALUES('arms','ko','short','팔');
INSERT OR IGNORE INTO muscle_label VALUES('legs','ko','long','다리');
INSERT OR IGNORE INTO muscle_label VALUES('legs','ko','short','다리');
INSERT OR IGNORE INTO muscle_label VALUES('core','ko','long','코어');
INSERT OR IGNORE INTO muscle_label VALUES('core','ko','short','코어');
INSERT OR IGNORE INTO muscle_label VALUES('chest','ko','long','가슴');
INSERT OR IGNORE INTO muscle_label VALUES('chest','ko','short','가슴');
INSERT OR IGNORE INTO muscle_label VALUES('back','ko','long','등');
INSERT OR IGNORE INTO muscle_label VALUES('back','ko','short','등');
INSERT OR IGNORE INTO muscle_label VALUES('shoulders','ko','long','어깨');
INSERT OR IGNORE INTO muscle_label VALUES('shoulders','ko','short','어깨');
INSERT OR IGNORE INTO muscle_label VALUES('biceps','ko','long','이두');
INSERT OR IGNORE INTO muscle_label VALUES('biceps','ko','short','이두');
INSERT OR IGNORE INTO muscle_label VALUES('triceps','ko','long','삼두');
INSERT OR IGNORE INTO muscle_label VALUES('triceps','ko','short','삼두');
INSERT OR IGNORE INTO muscle_label VALUES('forearms','ko','long','전완');
INSERT OR IGNORE INTO muscle_label VALUES('forearms','ko','short','전완');
INSERT OR IGNORE INTO muscle_label VALUES('quads','ko','long','대퇴사두');
INSERT OR IGNORE INTO muscle_label VALUES('quads','ko','short','사두');
INSERT OR IGNORE INTO muscle_label VALUES('hamstrings','ko','long','햄스트링');
INSERT OR IGNORE INTO muscle_label VALUES('hamstrings','ko','short','햄스');
INSERT OR IGNORE INTO muscle_label VALUES('glutes','ko','long','둔근');
INSERT OR IGNORE INTO muscle_label VALUES('glutes','ko','short','둔근');
INSERT OR IGNORE INTO muscle_label VALUES('calves','ko','long','종아리');
INSERT OR IGNORE INTO muscle_label VALUES('calves','ko','short','종아리');
INSERT OR IGNORE INTO muscle_label VALUES('abs','ko','long','복직근');
INSERT OR IGNORE INTO muscle_label VALUES('abs','ko','short','복근');
INSERT OR IGNORE INTO muscle_label VALUES('abs_lower','ko','long','하복부');
INSERT OR IGNORE INTO muscle_label VALUES('abs_lower','ko','short','하복');
INSERT OR IGNORE INTO muscle_label VALUES('adductors','ko','long','내전근');
INSERT OR IGNORE INTO muscle_label VALUES('adductors','ko','short','내전근');
INSERT OR IGNORE INTO muscle_label VALUES('back_erectors','ko','short','척추');
INSERT OR IGNORE INTO muscle_label VALUES('back_lats','ko','long','광배근');
INSERT OR IGNORE INTO muscle_label VALUES('back_lats','ko','short','광배');
INSERT OR IGNORE INTO muscle_label VALUES('back_upper','ko','short','승모');
INSERT OR IGNORE INTO muscle_label VALUES('biceps_distal','ko','long','이두근 하부');
INSERT OR IGNORE INTO muscle_label VALUES('biceps_distal','ko','short','이두하');
INSERT OR IGNORE INTO muscle_label VALUES('biceps_prox','ko','long','이두근 상부');
INSERT OR IGNORE INTO muscle_label VALUES('biceps_prox','ko','short','이두상');
INSERT OR IGNORE INTO muscle_label VALUES('calf_gastroc','ko','long','비복근');
INSERT OR IGNORE INTO muscle_label VALUES('calf_gastroc','ko','short','비복');
INSERT OR IGNORE INTO muscle_label VALUES('calf_soleus','ko','long','가자미근');
INSERT OR IGNORE INTO muscle_label VALUES('calf_soleus','ko','short','가자미');
INSERT OR IGNORE INTO muscle_label VALUES('chest_lower','ko','long','하부 대흉근');
INSERT OR IGNORE INTO muscle_label VALUES('chest_lower','ko','short','하흉');
INSERT OR IGNORE INTO muscle_label VALUES('chest_mid','ko','long','중부 대흉근');
INSERT OR IGNORE INTO muscle_label VALUES('chest_mid','ko','short','중흉');
INSERT OR IGNORE INTO muscle_label VALUES('chest_upper','ko','long','상부 대흉근');
INSERT OR IGNORE INTO muscle_label VALUES('chest_upper','ko','short','상흉');
INSERT OR IGNORE INTO muscle_label VALUES('front_delt','ko','long','전면 삼각근');
INSERT OR IGNORE INTO muscle_label VALUES('front_delt','ko','short','앞삼각');
INSERT OR IGNORE INTO muscle_label VALUES('glute_max','ko','long','대둔근');
INSERT OR IGNORE INTO muscle_label VALUES('glute_max','ko','short','대둔');
INSERT OR IGNORE INTO muscle_label VALUES('glute_med','ko','long','중둔근');
INSERT OR IGNORE INTO muscle_label VALUES('glute_med','ko','short','중둔');
INSERT OR IGNORE INTO muscle_label VALUES('rear_delt','ko','long','후면 삼각근');
INSERT OR IGNORE INTO muscle_label VALUES('rear_delt','ko','short','뒷삼각');
INSERT OR IGNORE INTO muscle_label VALUES('side_delt','ko','long','측면 삼각근');
INSERT OR IGNORE INTO muscle_label VALUES('side_delt','ko','short','옆삼각');
INSERT OR IGNORE INTO muscle_label VALUES('triceps_lat_med','ko','long','삼두 외측두·내측두');
INSERT OR IGNORE INTO muscle_label VALUES('triceps_lat_med','ko','short','외측두');
INSERT OR IGNORE INTO muscle_label VALUES('triceps_long','ko','long','삼두 장두');
INSERT OR IGNORE INTO muscle_label VALUES('triceps_long','ko','short','장두');
INSERT OR IGNORE INTO muscle_label VALUES('rotator_cuff','ko','long','회전근개');
INSERT OR IGNORE INTO muscle_label VALUES('rotator_cuff','ko','short','회전근개');
INSERT OR IGNORE INTO muscle_label VALUES('obliques','ko','long','복사근');
INSERT OR IGNORE INTO muscle_label VALUES('obliques','ko','short','복사근');
INSERT OR IGNORE INTO muscle_label VALUES('brachialis','ko','long','상완근');
INSERT OR IGNORE INTO muscle_label VALUES('brachialis','ko','short','상완근');
INSERT OR IGNORE INTO muscle_label VALUES('brachioradialis','ko','long','상완요골근');
INSERT OR IGNORE INTO muscle_label VALUES('brachioradialis','ko','short','상완요골');
INSERT OR IGNORE INTO muscle_label VALUES('hip_flexors','ko','long','장요근');
INSERT OR IGNORE INTO muscle_label VALUES('hip_flexors','ko','short','장요근');
INSERT OR IGNORE INTO muscle_label VALUES('tibialis_anterior','ko','long','전경골근');
INSERT OR IGNORE INTO muscle_label VALUES('tibialis_anterior','ko','short','정강이');
INSERT OR IGNORE INTO muscle_label VALUES('serratus','ko','long','전거근');
INSERT OR IGNORE INTO muscle_label VALUES('serratus','ko','short','전거근');
INSERT OR IGNORE INTO muscle_label VALUES('forearm_flexors','ko','long','전완 굴곡근');
INSERT OR IGNORE INTO muscle_label VALUES('forearm_flexors','ko','short','전완굴곡');
INSERT OR IGNORE INTO muscle_label VALUES('forearm_extensors','ko','long','전완 신전근');
INSERT OR IGNORE INTO muscle_label VALUES('forearm_extensors','ko','short','전완신전');
INSERT OR IGNORE INTO muscle_label VALUES('rect_fem','ko','long','대퇴직근');
INSERT OR IGNORE INTO muscle_label VALUES('rect_fem','ko','short','대퇴직근');
INSERT OR IGNORE INTO muscle_label VALUES('vast_lat','ko','long','외측광근');
INSERT OR IGNORE INTO muscle_label VALUES('vast_lat','ko','short','외측광근');
INSERT OR IGNORE INTO muscle_label VALUES('vast_med','ko','long','내측광근');
INSERT OR IGNORE INTO muscle_label VALUES('vast_med','ko','short','내측광근');
INSERT OR IGNORE INTO muscle_label VALUES('hams_lateral','ko','long','대퇴이두근');
INSERT OR IGNORE INTO muscle_label VALUES('hams_lateral','ko','short','외측 햄스');
INSERT OR IGNORE INTO muscle_label VALUES('hams_medial','ko','long','반건·반막양근');
INSERT OR IGNORE INTO muscle_label VALUES('hams_medial','ko','short','내측 햄스');
INSERT OR IGNORE INTO muscle_label VALUES('back_upper','ko','long','승모근');
INSERT OR IGNORE INTO muscle_label VALUES('back_erectors','ko','long','척추기립근');

-- exercise_muscle_map (53 rows)
INSERT OR IGNORE INTO exercise_muscle_map VALUES('back_squat','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('back_squat','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bicep_curl','biceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bulgarian_split_squat','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bulgarian_split_squat','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_crunch','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_fly','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_lateral_raise','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('chest_press_machine','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('chest_press_machine','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('chest_supported_t_bar_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('chest_supported_t_bar_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('chinup','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('chinup','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('deadlift','back','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('deadlift','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('deadlift','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('face_pull','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('hammer_curl','biceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('hammer_curl','forearms','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_barbell_press','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_barbell_press','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_barbell_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_dumbbell_curl','biceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_dumbbell_press','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_dumbbell_press','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_dumbbell_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('lat_pulldown','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('lat_pulldown','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('leg_curl','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('leg_raise','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('overhead_press','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('overhead_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('overhead_press_smith_seated','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('overhead_press_smith_seated','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('pendlay_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('pendlay_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('preacher_curl','biceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('pullup','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('pullup','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('rdl','back','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('rdl','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('rdl','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('reverse_pecdec','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('seated_calf_raise','calves','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_leg_extension','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('standing_calf_raise','calves','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('tricep_overhead_extension','triceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('tricep_pushdown_rope','triceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('v_squat','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('v_squat','quads','primary');

-- exercise_subregion_map (132 rows)
INSERT OR IGNORE INTO exercise_subregion_map VALUES('back_squat','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('back_squat','glute_max',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('back_squat','glute_med',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('back_squat','rect_fem',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('back_squat','vast_lat',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('back_squat','vast_med',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_row','back_erectors',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_row','back_lats',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_row','back_upper',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_row','biceps_distal',0.125,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_row','biceps_prox',0.125,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_row','brachialis',0.25,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bicep_curl','biceps_distal',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bicep_curl','biceps_prox',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bicep_curl','brachialis',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bulgarian_split_squat','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bulgarian_split_squat','glute_max',0.65,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bulgarian_split_squat','glute_med',0.35,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bulgarian_split_squat','rect_fem',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bulgarian_split_squat','vast_lat',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bulgarian_split_squat','vast_med',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_crunch','abs',0.6,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_crunch','abs_lower',0.25,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_crunch','obliques',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_fly','chest_lower',0.25,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_fly','chest_mid',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_fly','chest_upper',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_lateral_raise','front_delt',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_lateral_raise','rotator_cuff',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_lateral_raise','side_delt',0.8,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_press_machine','chest_lower',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_press_machine','chest_mid',0.5,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_press_machine','chest_upper',0.25,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_press_machine','serratus',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_press_machine','triceps_lat_med',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_press_machine','triceps_long',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_supported_t_bar_row','back_lats',0.5,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_supported_t_bar_row','back_upper',0.5,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_supported_t_bar_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_supported_t_bar_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chinup','back_lats',0.7,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chinup','back_upper',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chinup','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chinup','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('deadlift','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('deadlift','back_erectors',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('deadlift','back_lats',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('deadlift','back_upper',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('deadlift','glute_max',0.8,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('deadlift','glute_med',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('deadlift','hams_lateral',0.55,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('deadlift','hams_medial',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('face_pull','rear_delt',0.6,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('face_pull','rotator_cuff',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hammer_curl','biceps_distal',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hammer_curl','biceps_prox',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hammer_curl','brachialis',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hammer_curl','brachioradialis',0.35,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hammer_curl','forearm_extensors',0.05,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hammer_curl','forearm_flexors',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_barbell_press','chest_lower',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_barbell_press','chest_mid',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_barbell_press','chest_upper',0.5,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_barbell_press','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_barbell_press','serratus',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_barbell_press','triceps_lat_med',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_barbell_press','triceps_long',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_curl','biceps_distal',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_curl','biceps_prox',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_curl','brachialis',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_press','chest_lower',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_press','chest_mid',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_press','chest_upper',0.5,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_press','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_press','serratus',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_press','triceps_lat_med',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_dumbbell_press','triceps_long',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_curl','hams_lateral',0.35,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_curl','hams_medial',0.65,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_raise','abs',0.25,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_raise','abs_lower',0.6,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_raise','obliques',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('overhead_press','front_delt',0.65,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('overhead_press','side_delt',0.35,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('overhead_press','triceps_lat_med',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('overhead_press','triceps_long',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('overhead_press_smith_seated','front_delt',0.65,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('overhead_press_smith_seated','side_delt',0.35,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('overhead_press_smith_seated','triceps_lat_med',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('overhead_press_smith_seated','triceps_long',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pendlay_row','back_erectors',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pendlay_row','back_lats',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pendlay_row','back_upper',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pendlay_row','biceps_distal',0.125,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pendlay_row','biceps_prox',0.125,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pendlay_row','brachialis',0.25,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('preacher_curl','biceps_distal',0.5,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('preacher_curl','biceps_prox',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('preacher_curl','brachialis',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pullup','back_lats',0.7,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pullup','back_upper',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pullup','biceps_distal',0.125,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pullup','biceps_prox',0.125,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pullup','brachialis',0.25,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rdl','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rdl','back_erectors',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rdl','back_lats',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rdl','back_upper',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rdl','glute_max',0.8,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rdl','glute_med',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rdl','hams_lateral',0.55,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rdl','hams_medial',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('reverse_pecdec','rear_delt',0.8,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('reverse_pecdec','rotator_cuff',0.2,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_calf_raise','calf_gastroc',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_calf_raise','calf_soleus',0.85,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_extension','rect_fem',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_extension','vast_lat',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_extension','vast_med',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('standing_calf_raise','calf_gastroc',0.7,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('standing_calf_raise','calf_soleus',0.3,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('tibialis_raise','tibialis_anterior',1.0,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('tricep_overhead_extension','triceps_lat_med',0.4000000000000000222,'B');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('tricep_overhead_extension','triceps_long',0.5999999999999999778,'B');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('tricep_pushdown_rope','triceps_lat_med',0.65,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('tricep_pushdown_rope','triceps_long',0.35,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('v_squat','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('v_squat','glute_max',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('v_squat','glute_med',0.1,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('v_squat','rect_fem',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('v_squat','vast_lat',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('v_squat','vast_med',0.4,'C');

-- Missing lat-pulldown detail: neutral accounting split, not EMG ratios.
INSERT OR IGNORE INTO exercise_subregion_map VALUES('lat_pulldown','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('lat_pulldown','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('lat_pulldown','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('lat_pulldown','biceps_prox',0.25,'even');

-- exercise_movement_grip (31 rows)
INSERT OR IGNORE INTO exercise_movement_grip VALUES('back_squat','squat','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('barbell_row','pull_compound','barbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('bicep_curl','curl','barbell','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('bulgarian_split_squat','split_squat','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('cable_crunch','crunch','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('cable_fly','fly_isolation','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('cable_lateral_raise','lateral_raise','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('chest_press_machine','flat_press_machine','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('chest_supported_t_bar_row','pull_compound','t_bar','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('chinup','pull_compound','bodyweight_assist','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('deadlift','hip_hinge_deadlift','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('face_pull','rear_delt_isolation','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('hammer_curl','curl','dumbbell','neutral');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('incline_barbell_press','incline_press','barbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('incline_dumbbell_curl','curl','dumbbell','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('incline_dumbbell_press','incline_press','dumbbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('lat_pulldown','pull_compound','cable','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('leg_curl','leg_curl','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('overhead_press','overhead_press','barbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('overhead_press_smith_seated','overhead_press','smith_machine','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('pendlay_row','pull_compound','barbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('preacher_curl','curl','ez_bar','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('pullup','pull_compound','bodyweight_assist','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('rdl','hip_hinge_deadlift','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('reverse_pecdec','rear_delt_isolation','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('seated_calf_raise','calf_raise','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_leg_extension','leg_extension','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('standing_calf_raise','calf_raise','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('tricep_overhead_extension','tricep_isolation','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('tricep_pushdown_rope','tricep_isolation','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('v_squat','squat','v_squat_machine',NULL);

-- exercise_fatigue_cost (34 rows)
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('back_squat','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('barbell_row','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('bicep_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('bulgarian_split_squat','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('cable_crunch','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('cable_fly','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('cable_lateral_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('chest_press_machine','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('chest_supported_t_bar_row','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('chinup','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('deadlift','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('face_pull','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('hammer_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('incline_barbell_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('incline_dumbbell_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('incline_dumbbell_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('lat_pulldown','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('leg_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('leg_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('overhead_press','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('overhead_press_smith_seated','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('pendlay_row','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('preacher_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('pullup','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('rdl','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('reverse_pecdec','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('seated_calf_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_leg_extension','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('smith_seated_calf_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('standing_calf_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('tricep_overhead_extension','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('tricep_pushdown_rope','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('v_squat','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('wall_sit','low','explicit');

-- exercise_pattern (34 rows)
INSERT OR IGNORE INTO exercise_pattern VALUES('back_squat','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('barbell_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('bicep_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('bulgarian_split_squat','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('cable_crunch','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('cable_fly','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('cable_lateral_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('chest_press_machine','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('chest_supported_t_bar_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('chinup','vertical_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('deadlift','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('face_pull','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('hammer_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('incline_barbell_press','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('incline_dumbbell_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('incline_dumbbell_press','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('lat_pulldown','vertical_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('leg_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('leg_raise','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('overhead_press','vertical_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('overhead_press_smith_seated','vertical_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('pendlay_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('preacher_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('pullup','vertical_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('rdl','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('reverse_pecdec','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('seated_calf_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_leg_extension','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('smith_seated_calf_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('standing_calf_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('tricep_overhead_extension','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('tricep_pushdown_rope','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('v_squat','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('wall_sit','squat');

-- movement_muscle_base (25 rows)
INSERT OR IGNORE INTO movement_muscle_base VALUES('calf_raise','calves','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('crunch','abs','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('curl','biceps','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('flat_press_machine','chest','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('flat_press_machine','triceps','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('fly_isolation','chest','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('hip_hinge_deadlift','back','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('hip_hinge_deadlift','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('hip_hinge_deadlift','hamstrings','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('incline_press','chest','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('incline_press','shoulders','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('incline_press','triceps','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('lateral_raise','shoulders','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('leg_curl','hamstrings','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('leg_extension','quads','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('overhead_press','shoulders','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('overhead_press','triceps','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('pull_compound','back','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('pull_compound','biceps','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('rear_delt_isolation','shoulders','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('split_squat','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('split_squat','quads','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('squat','glutes','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('squat','quads','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('tricep_isolation','triceps','primary');

-- grip_muscle_delta (1 rows)
INSERT OR IGNORE INTO grip_muscle_delta VALUES('neutral','forearms','secondary','hammer_curl (confirmed exercise_muscle row, 2026-07-24 mapping)');

-- grip_vocab (5 rows)
INSERT OR IGNORE INTO grip_vocab VALUES('close','inside-shoulder; lower-lat/mid-back + more biceps on pull; differentiates at subregion, not coarse muscle');
INSERT OR IGNORE INTO grip_vocab VALUES('neutral','palms-facing (hammer); brachioradialis + forearms co-emphasis');
INSERT OR IGNORE INTO grip_vocab VALUES('pronated','overhand (palms away/down); brachioradialis + wrist-extensor emphasis on pulls');
INSERT OR IGNORE INTO grip_vocab VALUES('supinated','underhand (palms toward you); peak biceps; default curl/chin grip');
INSERT OR IGNORE INTO grip_vocab VALUES('wide','wider-than-shoulder; upper/outer-lat emphasis on pulldown; differentiates at subregion, not coarse muscle');

-- ax_projection_rule (9 rows)
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZAYAH000000000000000001',@@OWNING_AGENT@@,'F6_empty_bar_ramp',10,'compound','freeweight',NULL,NULL,NULL,NULL,'empty_bar_ramp','{"warmup":"empty_bar","then":"ramp"}','active','2026-08-09T00:00:00Z');
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZAYAH000000000000000002',@@OWNING_AGENT@@,'F10_injury_drill',20,NULL,NULL,NULL,NULL,NULL,1,'injury_drill_include','{"source":"ax_tag:injury_profile"}','active','2026-08-09T00:00:00Z');
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZAYAH000000000000000003',@@OWNING_AGENT@@,'F15_grip_order_defer',30,NULL,NULL,NULL,NULL,NULL,NULL,'order_defer','{"when_tag_group":"muscle","tag_in":["forearm","grip"]}','active','2026-08-09T00:00:00Z');
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZAYAH000000000000000004',@@OWNING_AGENT@@,'F16_isolation_tut',40,'isolation',NULL,NULL,NULL,NULL,NULL,'tut_progression','{"prefer_measure":["tempo","hold_sec"]}','active','2026-08-09T00:00:00Z');
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZAYAH000000000000000005',@@OWNING_AGENT@@,'CABLE_dual_specify',50,NULL,'cable',NULL,'dual',NULL,NULL,'cable_line_specify','{"require":"which_line"}','active','2026-08-09T00:00:00Z');
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZAYAH000000000000000006',@@OWNING_AGENT@@,'PLATE_projection',60,NULL,NULL,'plate_loaded',NULL,NULL,NULL,'plate_projection','{"source":"ax_machine.available_plates"}','active','2026-08-09T00:00:00Z');
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZAYAH000000000000000007',@@OWNING_AGENT@@,'F17_lattice_round',70,NULL,'machine',NULL,NULL,NULL,NULL,'lattice_round','{"source":"ax_machine.lattice_base,lattice_step"}','active','2026-08-09T00:00:00Z');
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZRUL00000000000CABLE01',@@OWNING_AGENT@@,'CABLE_lattice_round',68,NULL,'cable',NULL,NULL,NULL,NULL,'lattice_round','{"source":"ax_machine.lattice_base,lattice_step"}','active','2026-08-10T00:00:00Z');
INSERT OR IGNORE INTO ax_projection_rule VALUES('01KZRUL0000000000FREEWT01',@@OWNING_AGENT@@,'FREEWEIGHT_lattice_round',72,NULL,'freeweight',NULL,NULL,NULL,NULL,'lattice_round','{"source":"owner_freeweight_grid_2026-08-10","freeweight_grid":{"deadlift":{"type":"standard","base":0.0,"coarse_step":5.0},"back_squat":{"type":"standard","base":0.0,"coarse_step":5.0},"rdl":{"type":"standard","base":0.0,"coarse_step":5.0},"barbell_row":{"type":"standard","base":0.0,"coarse_step":5.0,"working_step":2.5},"overhead_press":{"type":"standard","base":0.0,"coarse_step":5.0,"working_step":2.5},"incline_barbell_press":{"type":"standard","base":0.0,"coarse_step":5.0,"working_step":2.5},"pendlay_row":{"type":"standard","base":0.0,"coarse_step":5.0,"working_step":2.5},"incline_dumbbell_press":{"type":"even","base":0.0,"coarse_step":2.0},"incline_dumbbell_curl":{"type":"even","base":0.0,"coarse_step":2.0},"bulgarian_split_squat":{"type":"even","base":0.0,"coarse_step":2.0}}}','active','2026-08-10T00:00:00Z');

-- ---------------------------------------------------------------------------
-- ax_exercise (16 rows) -- THE MOVEMENT/LOAD CLASS OF A LIFT.
--
-- WHY THIS BLOCK IS NEW AND EVERYTHING ABOVE IT IS A MOVE (2026-09-14)
--   ax_exercise was never seeded by anything, by anyone. The fresh-mint
--   simulation of 2026-09-13 measured it holding 0 rows with NO WRITER
--   ANYWHERE in a finished install, while its eleven sibling tables were full.
--   The consequence is the pack's single worst silent failure:
--   ax_engine.exercise_class() reads ONLY this table, so is_free_weight_compound
--   is False for every lift, is_plate_loaded is False for every lift,
--   plate_cue_line returns '', and set-table prints a completely normal-looking
--   card with no empty-bar rung, no ramp taper and no plate cue --
--   `RAMP_DECISION decision=none reason=not_ramp_class rungs=0` on the machine
--   rail and nothing at all on the owner's. The owner meets it in his first
--   session as "왜 원판 안 알려줘?".
--
-- SEED, NOT A FALLBACK. The alternative repair was to let exercise_class() fall
--   back to exercise_movement_grip (equipment='barbell' -> compound/freeweight).
--   Rejected: movement_grip can answer 2 of this table's 12 columns and none of
--   measure / tempo / hold_sec / machine_ref / status; ax_exercise is an FK
--   target (ax_exercise_tag.exercise_ref, ax_projection_slot.exercise_ref) and a
--   derived row cannot be referenced; and a fallback would make an empty catalog
--   INVISIBLE FOREVER, which is the exact defect class the audit exists about.
--   A miss is instead NAMED -- ax_engine._announce_class_miss_once emits
--   AX-EXERCISE-UNCLASSIFIED once per lift when movement_grip knows a name this
--   table does not.
--
-- DERIVED BY RULE, NOT HAND-AUTHORED. Every row is computed from two tables
--   already in this file, so there is no second opinion to drift:
--     load_type  <- exercise_movement_grip.equipment
--                   barbell|dumbbell|ez_bar|t_bar -> 'freeweight'
--                   bodyweight_assist             -> 'bodyweight'
--     movement   <- exercise_pattern.pattern
--                   'isolation' -> 'isolation', everything else -> 'compound'
--     measure    <- 'reps' for all 16 (none of them is a hold or a tempo lift;
--                   wall_sit, the one hold in exercise_pattern, has no
--                   movement_grip row and so is not seeded -- see below).
--
-- WHY ONLY 16 OF THE 31 LIFTS. The kit's own DDL decides this, not a judgement:
--     CHECK (load_type NOT IN ('machine','cable') OR machine_ref IS NOT NULL)
--   A machine or cable lift CANNOT have a row without an ax_machine row, and an
--   ax_machine row is a specific machine in a specific gym (ax_machine.gym_id ->
--   place). That is instance data this pack must never invent. Those 15 lifts
--   are registered JIT, at the machine, by ax-jit -- and every one of them is
--   is_plate_loaded=False either way, so the plate-cue path loses nothing.
--   The 16 seeded here are exactly the bar-and-bell half: the half the cue is
--   about.
--
-- IDEMPOTENT ON TWO KEYS, not one. Unlike the eleven tables above, ax_exercise's
--   primary key is a ULID, not the natural key -- so OR IGNORE alone would let a
--   second row for the same exercise_name land beside a JIT-registered one, and
--   exercise_class()'s `LIMIT 1` would then pick arbitrarily between them. Each
--   statement therefore carries its own natural-key guard, WHERE NOT EXISTS on
--   exercise_name: a lift the instance already classified is left exactly as the
--   instance classified it. This is the one statement shape in this file that is
--   not `VALUES(...)`; health_taxonomy_seed.SQL_GUARD allows it explicitly and
--   still refuses everything that is not an INSERT into an allowlisted table.
-- ---------------------------------------------------------------------------
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000001',@@OWNING_AGENT@@,'back_squat','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='back_squat');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000002',@@OWNING_AGENT@@,'barbell_row','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='barbell_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000003',@@OWNING_AGENT@@,'bicep_curl','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='bicep_curl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000004',@@OWNING_AGENT@@,'bulgarian_split_squat','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='bulgarian_split_squat');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000005',@@OWNING_AGENT@@,'chest_supported_t_bar_row','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='chest_supported_t_bar_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000006',@@OWNING_AGENT@@,'chinup','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='chinup');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000007',@@OWNING_AGENT@@,'deadlift','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='deadlift');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000008',@@OWNING_AGENT@@,'hammer_curl','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='hammer_curl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000009',@@OWNING_AGENT@@,'incline_barbell_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='incline_barbell_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000010',@@OWNING_AGENT@@,'incline_dumbbell_curl','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='incline_dumbbell_curl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000011',@@OWNING_AGENT@@,'incline_dumbbell_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='incline_dumbbell_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000012',@@OWNING_AGENT@@,'overhead_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='overhead_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000013',@@OWNING_AGENT@@,'pendlay_row','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='pendlay_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000014',@@OWNING_AGENT@@,'preacher_curl','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='preacher_curl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000015',@@OWNING_AGENT@@,'pullup','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='pullup');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000016',@@OWNING_AGENT@@,'rdl','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-14T00:00:00Z','2026-09-14T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='rdl');

-- ---------------------------------------------------------------------------
-- CATALOG EXPANSION (2026-09-26) -- GENERATED, NOT HAND-EDITED.
--
-- The planner offers only lifts with a muscle map (E9), and the moved rows had
-- no flat bench, leg press, push-up, plank or lunge. Each lift below passed the
-- creation gate in exercise_catalog.py (movement + equipment, pattern, muscle
-- map, subregion split, stabilizer roles, fatigue cost, rep class); this block
-- is that table rendered to rows. It also closes two lifts that already had a
-- pattern + fatigue row but no map (smith_seated_calf_raise, wall_sit).
-- Stabilizer roles are NOT rows yet (kit CHECK: role primary|secondary); they
-- live in exercise_catalog.py until the fatigue spec's P1 tag seed.
-- ax_exercise rows follow the block above's rule, with 'bodyweight' added to
-- the seedable class and HOLD movements (plank, wall_sit) excluded: a hold
-- needs a hold_sec nobody measured.
-- ---------------------------------------------------------------------------
-- @@KIT056-TAGS BEGIN -- stabilizer / laterality tags, row-for-row the same as
-- kit_life 056_muscle_fatigue.sql section D4 (same vocabulary ulids, same
-- exercise pairs, same conditions), so a fresh mint seeded here and a live DB
-- migrated by 056 hold the same tags.  The kit read model (muscle-state)
-- credits a `stabilizes` node one fixed tier; a tag only lands on an
-- exercise that is registered in ax_exercise.  Vocabulary rows are keyed on
-- (tag_group, value), junction rows on (exercise, tag) -- the ulid PK is not
-- the identity, so each statement carries its own NOT EXISTS guard (the
-- ax_exercise shape).  Requires kit_life >= 2.28.0 (056 adds nothing to these
-- two tables; they exist since the ax axis, but the node rotator_cuff above
-- is what makes those tags non-dangling).
INSERT OR IGNORE INTO ax_tag SELECT '01KZ056TAG0STAB0000000ERE',@@OWNING_AGENT@@,'stabilizes','back_erectors','056 draft (spec A2.4)','active','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_tag WHERE tag_group='stabilizes' AND value='back_erectors') AND EXISTS (SELECT 1 FROM muscle_node WHERE node='back_erectors') AND EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name IN ('back_squat','barbell_row','deadlift','pendlay_row','rdl'));
INSERT OR IGNORE INTO ax_tag SELECT '01KZ056TAG0STAB0000000FFL',@@OWNING_AGENT@@,'stabilizes','forearm_flexors','056 draft (spec A2.4)','active','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_tag WHERE tag_group='stabilizes' AND value='forearm_flexors') AND EXISTS (SELECT 1 FROM muscle_node WHERE node='forearm_flexors') AND EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name IN ('barbell_row','chinup','deadlift','lat_pulldown','pendlay_row','pullup','rdl'));
INSERT OR IGNORE INTO ax_tag SELECT '01KZ056TAG0STAB0000000ADD',@@OWNING_AGENT@@,'stabilizes','adductors','056 draft (spec A2.4)','active','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_tag WHERE tag_group='stabilizes' AND value='adductors') AND EXISTS (SELECT 1 FROM muscle_node WHERE node='adductors') AND EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name IN ('back_squat','bulgarian_split_squat','deadlift','rdl','single_leg_deadlift'));
INSERT OR IGNORE INTO ax_tag SELECT '01KZ056TAG0STAB0000000RDT',@@OWNING_AGENT@@,'stabilizes','rear_delt','056 draft (spec A2.4)','active','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_tag WHERE tag_group='stabilizes' AND value='rear_delt') AND EXISTS (SELECT 1 FROM muscle_node WHERE node='rear_delt') AND EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name IN ('barbell_row','pendlay_row'));
INSERT OR IGNORE INTO ax_tag SELECT '01KZ056TAG0STAB0000000ABS',@@OWNING_AGENT@@,'stabilizes','abs','056 draft (spec A2.4)','active','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_tag WHERE tag_group='stabilizes' AND value='abs') AND EXISTS (SELECT 1 FROM muscle_node WHERE node='abs') AND EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name IN ('back_squat','overhead_press'));
INSERT OR IGNORE INTO ax_tag SELECT '01KZ056TAG0STAB0000000GMD',@@OWNING_AGENT@@,'stabilizes','glute_med','056 draft (spec A2.4)','active','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_tag WHERE tag_group='stabilizes' AND value='glute_med') AND EXISTS (SELECT 1 FROM muscle_node WHERE node='glute_med') AND EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name IN ('bulgarian_split_squat','single_leg_deadlift'));
INSERT OR IGNORE INTO ax_tag SELECT '01KZ056TAG0STAB0000000RTC',@@OWNING_AGENT@@,'stabilizes','rotator_cuff','056 draft (spec A2.4)','active','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_tag WHERE tag_group='stabilizes' AND value='rotator_cuff') AND EXISTS (SELECT 1 FROM muscle_node WHERE node='rotator_cuff') AND EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name IN ('face_pull','incline_barbell_press','incline_dumbbell_press','overhead_press','reverse_pec_deck_fly','reverse_pecdec'));
INSERT OR IGNORE INTO ax_tag SELECT '01KZ056TAG0LATR0000000UNI',@@OWNING_AGENT@@,'laterality','unilateral','056 draft (spec A2.4)','active','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_tag WHERE tag_group='laterality' AND value='unilateral') AND EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name IN ('bulgarian_split_squat','single_leg_deadlift','single_leg_extension'));
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='back_erectors' AND tg.status='active' WHERE e.exercise_name='deadlift' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='forearm_flexors' AND tg.status='active' WHERE e.exercise_name='deadlift' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='adductors' AND tg.status='active' WHERE e.exercise_name='deadlift' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='back_erectors' AND tg.status='active' WHERE e.exercise_name='rdl' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='forearm_flexors' AND tg.status='active' WHERE e.exercise_name='rdl' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='adductors' AND tg.status='active' WHERE e.exercise_name='rdl' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='back_erectors' AND tg.status='active' WHERE e.exercise_name='barbell_row' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='forearm_flexors' AND tg.status='active' WHERE e.exercise_name='barbell_row' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='rear_delt' AND tg.status='active' WHERE e.exercise_name='barbell_row' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='back_erectors' AND tg.status='active' WHERE e.exercise_name='pendlay_row' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='forearm_flexors' AND tg.status='active' WHERE e.exercise_name='pendlay_row' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='rear_delt' AND tg.status='active' WHERE e.exercise_name='pendlay_row' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='back_erectors' AND tg.status='active' WHERE e.exercise_name='back_squat' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='abs' AND tg.status='active' WHERE e.exercise_name='back_squat' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='adductors' AND tg.status='active' WHERE e.exercise_name='back_squat' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='glute_med' AND tg.status='active' WHERE e.exercise_name='bulgarian_split_squat' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='adductors' AND tg.status='active' WHERE e.exercise_name='bulgarian_split_squat' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='glute_med' AND tg.status='active' WHERE e.exercise_name='single_leg_deadlift' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='adductors' AND tg.status='active' WHERE e.exercise_name='single_leg_deadlift' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='abs' AND tg.status='active' WHERE e.exercise_name='overhead_press' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='rotator_cuff' AND tg.status='active' WHERE e.exercise_name='overhead_press' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='rotator_cuff' AND tg.status='active' WHERE e.exercise_name='incline_barbell_press' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='rotator_cuff' AND tg.status='active' WHERE e.exercise_name='incline_dumbbell_press' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='forearm_flexors' AND tg.status='active' WHERE e.exercise_name='chinup' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='forearm_flexors' AND tg.status='active' WHERE e.exercise_name='pullup' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='forearm_flexors' AND tg.status='active' WHERE e.exercise_name='lat_pulldown' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='rotator_cuff' AND tg.status='active' WHERE e.exercise_name='face_pull' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='rotator_cuff' AND tg.status='active' WHERE e.exercise_name='reverse_pec_deck_fly' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='stabilizes' AND tg.value='rotator_cuff' AND tg.status='active' WHERE e.exercise_name='reverse_pecdec' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='laterality' AND tg.value='unilateral' AND tg.status='active' WHERE e.exercise_name='bulgarian_split_squat' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='laterality' AND tg.value='unilateral' AND tg.status='active' WHERE e.exercise_name='single_leg_deadlift' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
INSERT OR IGNORE INTO ax_exercise_tag SELECT '01KZ056XT' || upper(hex(randomblob(9))),e.owning_agent,e.ulid,tg.ulid,'2026-09-26T00:00:00Z' FROM ax_exercise e JOIN ax_tag tg ON tg.tag_group='laterality' AND tg.value='unilateral' AND tg.status='active' WHERE e.exercise_name='single_leg_extension' AND NOT EXISTS (SELECT 1 FROM ax_exercise_tag x WHERE x.exercise_ref=e.ulid AND x.tag_ref=tg.ulid);
-- @@KIT056-TAGS END

-- @@CATALOG-2026-09-26 BEGIN (generated: exercise_catalog.py --emit-sql)
-- exercise_muscle_map (+158 rows)
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_glute_bridge','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_glute_bridge','hamstrings','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_reverse_lunge','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_reverse_lunge','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_seal_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_seal_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_shrug','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_split_squat','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('barbell_split_squat','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bear_crawl','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bear_crawl','quads','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bear_crawl','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bench_press','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bench_press','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bench_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bodyweight_lunge','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('bodyweight_lunge','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('box_squat','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('box_squat','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_chest_press','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_chest_press','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_chest_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_curl','biceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_glute_kickback','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('cable_reverse_fly','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('chest_supported_dumbbell_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('chest_supported_dumbbell_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('close_grip_bench_press','chest','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('close_grip_bench_press','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('close_grip_bench_press','triceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('close_grip_lat_pulldown','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('close_grip_lat_pulldown','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('crunch','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('decline_bench_press','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('decline_bench_press','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('decline_bench_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dip','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dip','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dip','triceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_bench_press','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_bench_press','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_bench_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_crunch','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_curl','biceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_lateral_raise','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_overhead_triceps_extension','triceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_rdl','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_rdl','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_shoulder_press','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_shoulder_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_standing_calf_raise','calves','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('dumbbell_triceps_kickback','triceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('ez_bar_curl','biceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('ez_bar_reverse_curl','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('ez_bar_reverse_curl','forearms','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('front_squat','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('front_squat','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('goblet_squat','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('goblet_squat','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('good_morning','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('good_morning','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('hip_abduction_machine','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('hip_thrust','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('hip_thrust','hamstrings','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('hollow_hold','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_push_up','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_push_up','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('incline_push_up','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('inverted_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('inverted_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('kettlebell_clean','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('kettlebell_clean','hamstrings','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('kettlebell_deadlift','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('kettlebell_deadlift','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('kettlebell_goblet_squat','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('kettlebell_goblet_squat','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('kettlebell_swing','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('kettlebell_swing','hamstrings','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('landmine_press','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('landmine_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('leg_extension','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('leg_press','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('leg_press','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('leg_press_calf_raise','calves','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('lying_triceps_extension','triceps','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('machine_crunch','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('machine_lateral_raise','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('machine_shoulder_press','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('machine_shoulder_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('medicine_ball_slam','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('medicine_ball_slam','back','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('medicine_ball_slam','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('neutral_grip_lat_pulldown','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('neutral_grip_lat_pulldown','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('neutral_grip_lat_pulldown','forearms','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('neutral_grip_pullup','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('neutral_grip_pullup','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('neutral_grip_pullup','forearms','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('pec_deck_fly','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('pike_push_up','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('pike_push_up','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('plank','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('push_up','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('push_up','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('push_up','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('reverse_crunch','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('reverse_lunge','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('reverse_lunge','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('roll_down','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('rotational_medicine_ball_throw','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('seated_cable_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('seated_cable_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('seated_dumbbell_reverse_fly','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('seated_leg_curl','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('seated_machine_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('seated_machine_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('side_plank','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_cable_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_cable_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_dumbbell_bench_press','chest','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_dumbbell_bench_press','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_dumbbell_bench_press','triceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_dumbbell_lateral_raise','shoulders','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_kettlebell_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_kettlebell_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_arm_kettlebell_row','forearms','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_leg_calf_raise','calves','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_leg_lying_curl','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_leg_press','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_leg_press','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_leg_rdl','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('single_leg_rdl','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('smith_seated_calf_raise','calves','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('step_up','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('step_up','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('sumo_deadlift','back','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('sumo_deadlift','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('sumo_deadlift','hamstrings','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('trap_bar_deadlift','forearms','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('trap_bar_deadlift','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('trap_bar_deadlift','hamstrings','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('trap_bar_deadlift','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('trap_bar_shrug','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('trap_bar_shrug','forearms','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('turkish_get_up','abs','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('turkish_get_up','glutes','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('turkish_get_up','shoulders','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('underhand_barbell_row','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('underhand_barbell_row','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('underhand_lat_pulldown','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('underhand_lat_pulldown','biceps','secondary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('walking_lunge','glutes','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('walking_lunge','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('wall_sit','quads','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('wide_grip_lat_pulldown','back','primary');
INSERT OR IGNORE INTO exercise_muscle_map VALUES('wide_grip_lat_pulldown','biceps','secondary');
-- exercise_subregion_map (+294 rows)
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_glute_bridge','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_glute_bridge','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_glute_bridge','hamstrings',0.5,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_reverse_lunge','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_reverse_lunge','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_reverse_lunge','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_reverse_lunge','rect_fem',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_reverse_lunge','vast_lat',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_reverse_lunge','vast_med',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_seal_row','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_seal_row','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_seal_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_seal_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_shrug','back_lats',0.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_shrug','back_upper',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_split_squat','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_split_squat','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_split_squat','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_split_squat','rect_fem',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_split_squat','vast_lat',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('barbell_split_squat','vast_med',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bear_crawl','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bear_crawl','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bear_crawl','quads',0.5,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bench_press','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bench_press','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bench_press','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bench_press','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bench_press','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bench_press','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bodyweight_lunge','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bodyweight_lunge','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bodyweight_lunge','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('bodyweight_lunge','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('box_squat','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('box_squat','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('box_squat','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('box_squat','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_chest_press','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_chest_press','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_chest_press','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_chest_press','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_chest_press','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_chest_press','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_curl','biceps_distal',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_curl','biceps_prox',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_glute_kickback','glute_max',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('cable_reverse_fly','rear_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_supported_dumbbell_row','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_supported_dumbbell_row','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_supported_dumbbell_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('chest_supported_dumbbell_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_bench_press','chest_lower',0.165,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_bench_press','chest_mid',0.165,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_bench_press','chest_upper',0.17,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_bench_press','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_bench_press','triceps_lat_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_bench_press','triceps_long',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_lat_pulldown','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_lat_pulldown','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_lat_pulldown','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('close_grip_lat_pulldown','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('crunch','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('decline_bench_press','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('decline_bench_press','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('decline_bench_press','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('decline_bench_press','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('decline_bench_press','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('decline_bench_press','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dip','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dip','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dip','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dip','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dip','triceps_lat_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dip','triceps_long',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_bench_press','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_bench_press','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_bench_press','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_bench_press','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_bench_press','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_bench_press','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_crunch','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_curl','biceps_distal',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_curl','biceps_prox',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_lateral_raise','side_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_overhead_triceps_extension','triceps_lat_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_overhead_triceps_extension','triceps_long',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_rdl','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_rdl','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_rdl','hamstrings',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_row','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_row','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_shoulder_press','front_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_shoulder_press','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_shoulder_press','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_standing_calf_raise','calf_gastroc',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_standing_calf_raise','calf_soleus',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_triceps_kickback','triceps_lat_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('dumbbell_triceps_kickback','triceps_long',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('ez_bar_curl','biceps_distal',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('ez_bar_curl','biceps_prox',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('ez_bar_reverse_curl','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('ez_bar_reverse_curl','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('ez_bar_reverse_curl','brachioradialis',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('ez_bar_reverse_curl','forearm_extensors',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('front_squat','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('front_squat','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('front_squat','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('front_squat','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('goblet_squat','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('goblet_squat','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('goblet_squat','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('goblet_squat','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('good_morning','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('good_morning','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('good_morning','hams_lateral',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('good_morning','hams_medial',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hip_abduction_machine','glute_med',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hip_thrust','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hip_thrust','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hip_thrust','hamstrings',0.5,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('hollow_hold','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_push_up','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_push_up','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_push_up','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_push_up','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_push_up','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('incline_push_up','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('inverted_row','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('inverted_row','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('inverted_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('inverted_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_clean','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_clean','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_clean','hamstrings',0.5,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_deadlift','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_deadlift','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_deadlift','hamstrings',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_goblet_squat','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_goblet_squat','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_goblet_squat','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_goblet_squat','rect_fem',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_goblet_squat','vast_lat',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_goblet_squat','vast_med',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_swing','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_swing','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('kettlebell_swing','hamstrings',0.5,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('landmine_press','front_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('landmine_press','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('landmine_press','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_extension','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_press','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_press','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_press','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_press','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_press_calf_raise','calf_gastroc',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('leg_press_calf_raise','calf_soleus',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('lying_triceps_extension','triceps_lat_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('lying_triceps_extension','triceps_long',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('machine_crunch','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('machine_lateral_raise','side_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('machine_shoulder_press','front_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('machine_shoulder_press','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('machine_shoulder_press','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('medicine_ball_slam','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('medicine_ball_slam','back_lats',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('medicine_ball_slam','back_upper',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('medicine_ball_slam','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_lat_pulldown','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_lat_pulldown','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_lat_pulldown','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_lat_pulldown','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_lat_pulldown','brachioradialis',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_lat_pulldown','forearm_flexors',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_pullup','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_pullup','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_pullup','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_pullup','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_pullup','brachioradialis',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('neutral_grip_pullup','forearm_flexors',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pec_deck_fly','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pec_deck_fly','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pec_deck_fly','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pike_push_up','front_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pike_push_up','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('pike_push_up','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('plank','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('push_up','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('push_up','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('push_up','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('push_up','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('push_up','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('push_up','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('reverse_crunch','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('reverse_lunge','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('reverse_lunge','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('reverse_lunge','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('reverse_lunge','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('roll_down','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('rotational_medicine_ball_throw','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_cable_row','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_cable_row','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_cable_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_cable_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_dumbbell_reverse_fly','rear_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_leg_curl','hams_lateral',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_leg_curl','hams_medial',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_machine_row','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_machine_row','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_machine_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('seated_machine_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('side_plank','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_cable_row','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_cable_row','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_cable_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_cable_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_dumbbell_bench_press','chest_lower',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_dumbbell_bench_press','chest_mid',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_dumbbell_bench_press','chest_upper',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_dumbbell_bench_press','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_dumbbell_bench_press','triceps_lat_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_dumbbell_bench_press','triceps_long',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_dumbbell_lateral_raise','side_delt',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_kettlebell_row','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_kettlebell_row','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_kettlebell_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_kettlebell_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_kettlebell_row','brachioradialis',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_arm_kettlebell_row','forearm_flexors',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_calf_raise','calf_gastroc',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_calf_raise','calf_soleus',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_lying_curl','hams_lateral',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_lying_curl','hams_medial',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_press','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_press','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_press','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_press','rect_fem',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_press','vast_lat',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_press','vast_med',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_rdl','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_rdl','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('single_leg_rdl','hamstrings',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('smith_seated_calf_raise','calf_gastroc',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('smith_seated_calf_raise','calf_soleus',0.85,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('step_up','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('step_up','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('step_up','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('step_up','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('sumo_deadlift','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('sumo_deadlift','back_erectors',0.17,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('sumo_deadlift','back_lats',0.165,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('sumo_deadlift','back_upper',0.165,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('sumo_deadlift','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('sumo_deadlift','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('sumo_deadlift','hams_lateral',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('sumo_deadlift','hams_medial',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_deadlift','brachioradialis',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_deadlift','forearm_flexors',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_deadlift','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_deadlift','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_deadlift','hamstrings',0.5,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_deadlift','rect_fem',0.34,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_deadlift','vast_lat',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_deadlift','vast_med',0.33,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_shrug','back_lats',0.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_shrug','back_upper',1.0,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_shrug','brachioradialis',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('trap_bar_shrug','forearm_flexors',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('turkish_get_up','abs',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('turkish_get_up','front_delt',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('turkish_get_up','glute_max',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('turkish_get_up','glute_med',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_barbell_row','back_erectors',0.15,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_barbell_row','back_lats',0.45,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_barbell_row','back_upper',0.4,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_barbell_row','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_barbell_row','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_lat_pulldown','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_lat_pulldown','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_lat_pulldown','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('underhand_lat_pulldown','biceps_prox',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('walking_lunge','adductors',0.5,'functional');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('walking_lunge','glute_max',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('walking_lunge','glute_med',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('walking_lunge','quads',1.0,'group');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('wall_sit','rect_fem',0.15,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('wall_sit','vast_lat',0.45,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('wall_sit','vast_med',0.4,'C');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('wide_grip_lat_pulldown','back_lats',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('wide_grip_lat_pulldown','back_upper',0.5,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('wide_grip_lat_pulldown','biceps_distal',0.25,'even');
INSERT OR IGNORE INTO exercise_subregion_map VALUES('wide_grip_lat_pulldown','biceps_prox',0.25,'even');
-- exercise_movement_grip (+86 rows)
INSERT OR IGNORE INTO exercise_movement_grip VALUES('barbell_glute_bridge','hip_thrust','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('barbell_reverse_lunge','split_squat','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('barbell_seal_row','pull_compound','barbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('barbell_shrug','shrug','barbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('barbell_split_squat','split_squat','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('bear_crawl','crawl','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('bench_press','flat_press','barbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('bodyweight_lunge','split_squat','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('box_squat','squat','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('cable_chest_press','flat_press','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('cable_curl','curl','cable','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('cable_glute_kickback','glute_extension','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('cable_reverse_fly','rear_delt_isolation','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('chest_supported_dumbbell_row','pull_compound','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('close_grip_bench_press','close_grip_press','barbell','close');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('close_grip_lat_pulldown','pull_compound','cable','close');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('crunch','crunch','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('decline_bench_press','flat_press','barbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dip','dip','bodyweight_assist',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_bench_press','flat_press','dumbbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_crunch','crunch','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_curl','curl','dumbbell','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_lateral_raise','lateral_raise','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_overhead_triceps_extension','tricep_isolation','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_rdl','hinge_bilateral','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_row','pull_compound','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_shoulder_press','overhead_press','dumbbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_standing_calf_raise','calf_raise','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('dumbbell_triceps_kickback','tricep_isolation','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('ez_bar_curl','curl','ez_bar','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('ez_bar_reverse_curl','reverse_curl','ez_bar','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('front_squat','squat','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('goblet_squat','squat','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('good_morning','hinge_bilateral','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('hip_abduction_machine','hip_abduction','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('hip_thrust','hip_thrust','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('hollow_hold','plank','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('incline_push_up','flat_press','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('inverted_row','pull_compound','bodyweight_assist','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('kettlebell_clean','kettlebell_clean','kettlebell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('kettlebell_deadlift','hinge_bilateral','kettlebell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('kettlebell_goblet_squat','squat','kettlebell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('kettlebell_swing','kettlebell_swing','kettlebell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('landmine_press','overhead_press','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('leg_extension','leg_extension','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('leg_press','squat','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('leg_press_calf_raise','calf_raise','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('lying_triceps_extension','tricep_isolation','ez_bar','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('machine_crunch','crunch','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('machine_lateral_raise','lateral_raise','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('machine_shoulder_press','overhead_press','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('medicine_ball_slam','ball_slam','medicine_ball',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('neutral_grip_lat_pulldown','pull_compound','cable','neutral');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('neutral_grip_pullup','pull_compound','bodyweight_assist','neutral');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('pec_deck_fly','fly_isolation','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('pike_push_up','overhead_press','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('plank','plank','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('push_up','flat_press','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('reverse_crunch','crunch','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('reverse_lunge','split_squat','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('roll_down','crunch','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('rotational_medicine_ball_throw','ball_rotation','medicine_ball',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('seated_cable_row','pull_compound','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('seated_dumbbell_reverse_fly','rear_delt_isolation','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('seated_leg_curl','leg_curl','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('seated_machine_row','pull_compound','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('side_plank','plank','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_arm_cable_row','pull_compound','cable',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_arm_dumbbell_bench_press','flat_press','dumbbell','pronated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_arm_dumbbell_lateral_raise','lateral_raise','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_arm_kettlebell_row','pull_compound','kettlebell','neutral');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_leg_calf_raise','calf_raise','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_leg_lying_curl','leg_curl','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_leg_press','squat','machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('single_leg_rdl','single_leg_hinge','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('smith_seated_calf_raise','calf_raise','smith_machine',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('step_up','split_squat','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('sumo_deadlift','hip_hinge_deadlift','barbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('trap_bar_deadlift','trap_bar_hinge','trap_bar','neutral');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('trap_bar_shrug','shrug','trap_bar','neutral');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('turkish_get_up','get_up','kettlebell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('underhand_barbell_row','pull_compound','barbell','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('underhand_lat_pulldown','pull_compound','cable','supinated');
INSERT OR IGNORE INTO exercise_movement_grip VALUES('walking_lunge','split_squat','dumbbell',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('wall_sit','wall_sit','bodyweight',NULL);
INSERT OR IGNORE INTO exercise_movement_grip VALUES('wide_grip_lat_pulldown','pull_compound','cable','wide');
-- exercise_fatigue_cost (+84 rows)
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('barbell_glute_bridge','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('barbell_reverse_lunge','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('barbell_seal_row','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('barbell_shrug','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('barbell_split_squat','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('bear_crawl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('bench_press','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('bodyweight_lunge','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('box_squat','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('cable_chest_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('cable_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('cable_glute_kickback','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('cable_reverse_fly','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('chest_supported_dumbbell_row','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('close_grip_bench_press','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('close_grip_lat_pulldown','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('crunch','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('decline_bench_press','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dip','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_bench_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_crunch','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_lateral_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_overhead_triceps_extension','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_rdl','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_row','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_shoulder_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_standing_calf_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('dumbbell_triceps_kickback','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('ez_bar_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('ez_bar_reverse_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('front_squat','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('goblet_squat','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('good_morning','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('hip_abduction_machine','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('hip_thrust','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('hollow_hold','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('incline_push_up','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('inverted_row','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('kettlebell_clean','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('kettlebell_deadlift','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('kettlebell_goblet_squat','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('kettlebell_swing','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('landmine_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('leg_extension','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('leg_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('leg_press_calf_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('lying_triceps_extension','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('machine_crunch','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('machine_lateral_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('machine_shoulder_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('medicine_ball_slam','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('neutral_grip_lat_pulldown','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('neutral_grip_pullup','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('pec_deck_fly','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('pike_push_up','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('plank','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('push_up','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('reverse_crunch','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('reverse_lunge','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('roll_down','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('rotational_medicine_ball_throw','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('seated_cable_row','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('seated_dumbbell_reverse_fly','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('seated_leg_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('seated_machine_row','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('side_plank','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_arm_cable_row','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_arm_dumbbell_bench_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_arm_dumbbell_lateral_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_arm_kettlebell_row','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_leg_calf_raise','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_leg_lying_curl','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_leg_press','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('single_leg_rdl','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('step_up','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('sumo_deadlift','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('trap_bar_deadlift','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('trap_bar_shrug','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('turkish_get_up','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('underhand_barbell_row','high','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('underhand_lat_pulldown','low','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('walking_lunge','med','explicit');
INSERT OR IGNORE INTO exercise_fatigue_cost VALUES('wide_grip_lat_pulldown','low','explicit');
-- exercise_pattern (+84 rows)
INSERT OR IGNORE INTO exercise_pattern VALUES('barbell_glute_bridge','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('barbell_reverse_lunge','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('barbell_seal_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('barbell_shrug','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('barbell_split_squat','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('bear_crawl','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('bench_press','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('bodyweight_lunge','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('box_squat','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('cable_chest_press','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('cable_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('cable_glute_kickback','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('cable_reverse_fly','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('chest_supported_dumbbell_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('close_grip_bench_press','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('close_grip_lat_pulldown','vertical_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('crunch','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('decline_bench_press','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('dip','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_bench_press','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_crunch','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_lateral_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_overhead_triceps_extension','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_rdl','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_shoulder_press','vertical_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_standing_calf_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('dumbbell_triceps_kickback','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('ez_bar_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('ez_bar_reverse_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('front_squat','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('goblet_squat','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('good_morning','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('hip_abduction_machine','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('hip_thrust','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('hollow_hold','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('incline_push_up','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('inverted_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('kettlebell_clean','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('kettlebell_deadlift','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('kettlebell_goblet_squat','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('kettlebell_swing','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('landmine_press','vertical_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('leg_extension','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('leg_press','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('leg_press_calf_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('lying_triceps_extension','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('machine_crunch','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('machine_lateral_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('machine_shoulder_press','vertical_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('medicine_ball_slam','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('neutral_grip_lat_pulldown','vertical_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('neutral_grip_pullup','vertical_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('pec_deck_fly','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('pike_push_up','vertical_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('plank','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('push_up','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('reverse_crunch','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('reverse_lunge','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('roll_down','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('rotational_medicine_ball_throw','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('seated_cable_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('seated_dumbbell_reverse_fly','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('seated_leg_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('seated_machine_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('side_plank','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_arm_cable_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_arm_dumbbell_bench_press','horizontal_push');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_arm_dumbbell_lateral_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_arm_kettlebell_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_leg_calf_raise','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_leg_lying_curl','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_leg_press','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('single_leg_rdl','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('step_up','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('sumo_deadlift','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('trap_bar_deadlift','hinge');
INSERT OR IGNORE INTO exercise_pattern VALUES('trap_bar_shrug','isolation');
INSERT OR IGNORE INTO exercise_pattern VALUES('turkish_get_up','core');
INSERT OR IGNORE INTO exercise_pattern VALUES('underhand_barbell_row','horizontal_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('underhand_lat_pulldown','vertical_pull');
INSERT OR IGNORE INTO exercise_pattern VALUES('walking_lunge','squat');
INSERT OR IGNORE INTO exercise_pattern VALUES('wide_grip_lat_pulldown','vertical_pull');
-- movement_muscle_base (+39 rows)
INSERT OR IGNORE INTO movement_muscle_base VALUES('ball_rotation','abs','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('ball_slam','abs','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('ball_slam','back','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('ball_slam','shoulders','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('close_grip_press','chest','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('close_grip_press','shoulders','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('close_grip_press','triceps','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('crawl','abs','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('crawl','quads','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('crawl','shoulders','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('dip','chest','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('dip','shoulders','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('dip','triceps','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('flat_press','chest','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('flat_press','shoulders','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('flat_press','triceps','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('get_up','abs','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('get_up','glutes','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('get_up','shoulders','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('glute_extension','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('hinge_bilateral','glutes','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('hinge_bilateral','hamstrings','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('hip_abduction','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('hip_thrust','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('hip_thrust','hamstrings','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('kettlebell_clean','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('kettlebell_clean','hamstrings','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('kettlebell_swing','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('kettlebell_swing','hamstrings','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('plank','abs','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('reverse_curl','biceps','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('reverse_curl','forearms','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('shrug','back','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('single_leg_hinge','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('single_leg_hinge','hamstrings','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('trap_bar_hinge','glutes','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('trap_bar_hinge','hamstrings','secondary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('trap_bar_hinge','quads','primary');
INSERT OR IGNORE INTO movement_muscle_base VALUES('wall_sit','quads','primary');
-- ax_exercise (+59 rows, same derivation rule as above)
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000051',@@OWNING_AGENT@@,'barbell_glute_bridge','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='barbell_glute_bridge');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000052',@@OWNING_AGENT@@,'barbell_reverse_lunge','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='barbell_reverse_lunge');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000053',@@OWNING_AGENT@@,'barbell_seal_row','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='barbell_seal_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000054',@@OWNING_AGENT@@,'barbell_shrug','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='barbell_shrug');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000055',@@OWNING_AGENT@@,'barbell_split_squat','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='barbell_split_squat');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000073',@@OWNING_AGENT@@,'bear_crawl','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='bear_crawl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000017',@@OWNING_AGENT@@,'bench_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='bench_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000018',@@OWNING_AGENT@@,'bodyweight_lunge','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='bodyweight_lunge');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000032',@@OWNING_AGENT@@,'box_squat','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='box_squat');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000033',@@OWNING_AGENT@@,'chest_supported_dumbbell_row','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='chest_supported_dumbbell_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000056',@@OWNING_AGENT@@,'close_grip_bench_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='close_grip_bench_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000040',@@OWNING_AGENT@@,'crunch','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='crunch');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000057',@@OWNING_AGENT@@,'decline_bench_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='decline_bench_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000019',@@OWNING_AGENT@@,'dip','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dip');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000020',@@OWNING_AGENT@@,'dumbbell_bench_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_bench_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000058',@@OWNING_AGENT@@,'dumbbell_crunch','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_crunch');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000021',@@OWNING_AGENT@@,'dumbbell_curl','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_curl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000022',@@OWNING_AGENT@@,'dumbbell_lateral_raise','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_lateral_raise');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000041',@@OWNING_AGENT@@,'dumbbell_overhead_triceps_extension','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_overhead_triceps_extension');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000034',@@OWNING_AGENT@@,'dumbbell_rdl','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_rdl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000023',@@OWNING_AGENT@@,'dumbbell_row','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000024',@@OWNING_AGENT@@,'dumbbell_shoulder_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_shoulder_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000042',@@OWNING_AGENT@@,'dumbbell_standing_calf_raise','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_standing_calf_raise');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000043',@@OWNING_AGENT@@,'dumbbell_triceps_kickback','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='dumbbell_triceps_kickback');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000061',@@OWNING_AGENT@@,'ez_bar_curl','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='ez_bar_curl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000062',@@OWNING_AGENT@@,'ez_bar_reverse_curl','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='ez_bar_reverse_curl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000035',@@OWNING_AGENT@@,'front_squat','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='front_squat');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000025',@@OWNING_AGENT@@,'goblet_squat','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='goblet_squat');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000059',@@OWNING_AGENT@@,'good_morning','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='good_morning');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000026',@@OWNING_AGENT@@,'hip_thrust','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='hip_thrust');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000036',@@OWNING_AGENT@@,'incline_push_up','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='incline_push_up');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000044',@@OWNING_AGENT@@,'inverted_row','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='inverted_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000063',@@OWNING_AGENT@@,'kettlebell_clean','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='kettlebell_clean');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000037',@@OWNING_AGENT@@,'kettlebell_deadlift','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='kettlebell_deadlift');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000064',@@OWNING_AGENT@@,'kettlebell_goblet_squat','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='kettlebell_goblet_squat');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000065',@@OWNING_AGENT@@,'kettlebell_swing','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='kettlebell_swing');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000038',@@OWNING_AGENT@@,'landmine_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='landmine_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000027',@@OWNING_AGENT@@,'lying_triceps_extension','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='lying_triceps_extension');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000066',@@OWNING_AGENT@@,'medicine_ball_slam','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='medicine_ball_slam');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000067',@@OWNING_AGENT@@,'neutral_grip_pullup','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='neutral_grip_pullup');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000045',@@OWNING_AGENT@@,'pike_push_up','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='pike_push_up');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000028',@@OWNING_AGENT@@,'push_up','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='push_up');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000046',@@OWNING_AGENT@@,'reverse_crunch','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='reverse_crunch');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000029',@@OWNING_AGENT@@,'reverse_lunge','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='reverse_lunge');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000074',@@OWNING_AGENT@@,'roll_down','compound','reps','bodyweight','3030',NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='roll_down');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000068',@@OWNING_AGENT@@,'rotational_medicine_ball_throw','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='rotational_medicine_ball_throw');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000047',@@OWNING_AGENT@@,'seated_dumbbell_reverse_fly','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='seated_dumbbell_reverse_fly');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000048',@@OWNING_AGENT@@,'single_arm_dumbbell_bench_press','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='single_arm_dumbbell_bench_press');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000049',@@OWNING_AGENT@@,'single_arm_dumbbell_lateral_raise','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='single_arm_dumbbell_lateral_raise');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000069',@@OWNING_AGENT@@,'single_arm_kettlebell_row','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='single_arm_kettlebell_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000050',@@OWNING_AGENT@@,'single_leg_calf_raise','isolation','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='single_leg_calf_raise');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000030',@@OWNING_AGENT@@,'single_leg_rdl','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='single_leg_rdl');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000039',@@OWNING_AGENT@@,'step_up','compound','reps','bodyweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='step_up');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000060',@@OWNING_AGENT@@,'sumo_deadlift','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='sumo_deadlift');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000070',@@OWNING_AGENT@@,'trap_bar_deadlift','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='trap_bar_deadlift');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000071',@@OWNING_AGENT@@,'trap_bar_shrug','isolation','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='trap_bar_shrug');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000075',@@OWNING_AGENT@@,'turkish_get_up','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='turkish_get_up');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000072',@@OWNING_AGENT@@,'underhand_barbell_row','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='underhand_barbell_row');
INSERT OR IGNORE INTO ax_exercise SELECT '01KZAXEX000000000000000031',@@OWNING_AGENT@@,'walking_lunge','compound','reps','freeweight',NULL,NULL,NULL,'active','2026-09-26T00:00:00Z','2026-09-26T00:00:00Z' WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name='walking_lunge');
-- @@CATALOG-2026-09-26 END
