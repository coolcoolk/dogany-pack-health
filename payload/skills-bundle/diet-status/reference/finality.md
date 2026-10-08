# aggregate finality contract (DGN-669)

- `kit_life.sh agg-day <date>` appends `as_of=` / `last_entry_at=` / `closed=`
  KEY=VALUE lines. `agg-week`: `as_of=` + per-day `[closed]` / `[prov]` suffix.
  `closed=0` = provisional; numbers may still change (late backfill).
- day-close rule (kit derives at read time, never stored):
  closed(D) = now >= max(last_entry(D) + 6h quiet, D+1 12:00 local). late backfill
  re-opens the day automatically.
- marker: any surface showing a PAST date's aggregate with `closed=0` attaches
  `(잠정, HH:MM 기준)` (HH:MM from `as_of`). `closed=1` may render bare or as 확정.
  current-day surfaces (diet card, today's retro) = "so far" views: no marker, never
  claim finality.
- `closed=1` + `meal_cnt=0` = NO RECORDS, not a confirmed fast. never voice 0 kcal /
  fasting day.
- known limit: deletes and date-move-out edits on an already-closed day go undetected
  (tombstone detection = separate ticket).
