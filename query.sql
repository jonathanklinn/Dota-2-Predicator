SELECT

tower_damage tower_damage,kills kills,hero_damage hero_damage,gold_per_min gold_per_min,denies denies,deaths deaths,(SELECT SUM(value::text::int) FROM json_each(damage_inflictor_received)) dmg_received,(SELECT SUM(value::text::int) FROM json_each(damage_inflictor)) dmg_dealt,xp_per_min xp_per_min,assists assists,
matches.match_id,
matches.start_time,
((player_matches.player_slot < 128) = matches.radiant_win) win,
player_matches.hero_id,
player_matches.account_id,
leagues.name leaguename
FROM matches
JOIN match_patch using(match_id)
JOIN leagues using(leagueid)
JOIN player_matches using(match_id)
JOIN heroes on heroes.id = player_matches.hero_id
LEFT JOIN notable_players ON notable_players.account_id = player_matches.account_id AND notable_players.locked_until = (SELECT MAX(locked_until) FROM notable_players)
LEFT JOIN teams using(team_id)
WHERE TRUE
AND tower_damage IS NOT NULL AND kills IS NOT NULL AND hero_damage IS NOT NULL AND gold_per_min IS NOT NULL AND denies IS NOT NULL AND deaths IS NOT NULL AND (SELECT SUM(value::text::int) FROM json_each(damage_inflictor_received)) IS NOT NULL AND (SELECT SUM(value::text::int) FROM json_each(damage_inflictor)) IS NOT NULL AND xp_per_min IS NOT NULL AND assists IS NOT NULL
AND (player_matches.account_id = 132851371)
AND matches.start_time >= extract(epoch from timestamp '2015-08-20T07:00:00.000Z')
ORDER BY tower_damage DESC,kills DESC,hero_damage DESC,gold_per_min DESC,denies DESC,deaths DESC,(SELECT SUM(value::text::int) FROM json_each(damage_inflictor_received)) DESC,(SELECT SUM(value::text::int) FROM json_each(damage_inflictor)) DESC,xp_per_min DESC,assists DESC NULLS LAST
