import dota2api
import pprint
import pandas as pd
import numpy as np

api= dota2api.Initialise("B335AEF628EF2F2D2DC5A94BA4A02ED9")

match_data= pd.read_csv("data/match_ids.csv")


pd.set_option('display.expand_frame_repr', False)


matches_data['Radiant'] = ''
matches_data['Dire'] = ''

matches_data['radiant_assists'] = 0
matches_data['radiant_barracks'] = 0
matches_data['radiant_denies'] = 0
matches_data['radiant_gpm'] = 0
matches_data['radiant_healing'] = 0
matches_data['radiant_hero_damage'] = 0
matches_data['radiant_kills'] = 0
matches_data['radiant_last_hits'] = 0
matches_data['radiant_total_levels'] = 0
matches_data['radiant_tower_damage'] = 0
matches_data['radiant_tower_status'] = 0
matches_data['radiant_xpm'] = 0

matches_data['dire_assists'] = 0
matches_data['dire_barracks'] = 0
matches_data['dire_denies'] = 0
matches_data['dire_gpm'] = 0
matches_data['dire_healing'] = 0
matches_data['dire_hero_damage'] = 0
matches_data['dire_kills'] = 0
matches_data['dire_last_hits'] = 0
matches_data['dire_total_levels'] = 0
matches_data['dire_tower_damage'] = 0
matches_data['dire_tower_status'] = 0
matches_data['dire_xpm'] = 0

matches_data['first_blood'] = 0
matches_data['match_duration'] = 0
matches_data['radiant_winner'] = 0

for i in range(0, len(matches_data)): 
    # MATCH
    first_blood          = 0
    match_duration       = 0
    match_winner         = 0

# RADIANT
    radiant_assists      = 0
    radiant_denies       = 0
    radiant_gpm          = 0
    radiant_healing      = 0
    radiant_hero_damage  = 0
    radiant_kills        = 0
    radiant_last_hits    = 0
    radiant_name         = ""
    radiant_total_levels = 0
    radiant_tower_damage = 0
    radiant_xpm          = 0 #26905 xp for 25
    radiant_barracks     = 0

# DIRE
    dire_assists         = 0
    dire_denies          = 0
    dire_gpm             = 0
    dire_healing         = 0
    dire_hero_damage     = 0
    dire_kills           = 0
    dire_last_hits       = 0
    dire_name            = ""
    dire_total_levels    = 0
    dire_tower_damage    = 0
    dire_xpm             = 0
    dire_barracks        = 0

current_match = matches_data['match_id'][i]
print(current_match)
    try:
        match = api.get_match_details(match_id = current_match)

    for x in range(0, 5):
            radiant_assists      += match['players'][x]['assists']
            radiant_denies       += match['players'][x]['denies']
            radiant_gpm          += match['players'][x]['gold_per_min']
            radiant_healing      += match['players'][x]['hero_healing']
            radiant_hero_damage  += match['players'][x]['hero_damage']
            radiant_kills        += match['players'][x]['kills']
            radiant_last_hits    += match['players'][x]['last_hits']
            radiant_total_levels += match['players'][x]['level']
            radiant_tower_damage += match['players'][x]['tower_damage']
            radiant_xpm          += match['players'][x]['xp_per_min']

radiant_barracks = match['barracks_status_radiant']
        radiant_name = match['radiant_name']
        radiant_tower_status = match['tower_status_radiant']

matches_data.loc[i, 'radiant_assists'] = radiant_assists
        matches_data.loc[i, 'radiant_barracks'] = radiant_barracks
        matches_data.loc[i, 'radiant_denies'] = radiant_denies
        matches_data.loc[i, 'radiant_gpm'] = radiant_gpm
        matches_data.loc[i, 'radiant_healing'] = radiant_healing
        matches_data.loc[i, 'radiant_hero_damage'] = radiant_hero_damage
        matches_data.loc[i, 'radiant_kills'] = radiant_kills
        matches_data.loc[i, 'radiant_last_hits'] = radiant_last_hits
        matches_data.loc[i, 'Radiant'] = radiant_name
        matches_data.loc[i, 'radiant_total_levels'] = radiant_total_levels
        matches_data.loc[i, 'radiant_tower_status'] = radiant_tower_status
        matches_data.loc[i, 'radiant_tower_damage'] = radiant_tower_damage
        matches_data.loc[i, 'radiant_xpm'] = radiant_xpm

for x in range(5, 10):
            dire_assists      += match['players'][x]['assists']
            dire_denies       += match['players'][x]['denies']
            dire_gpm          += match['players'][x]['gold_per_min']
            dire_healing      += match['players'][x]['hero_healing']
            dire_hero_damage  += match['players'][x]['hero_damage']
            dire_kills        += match['players'][x]['kills']
            dire_last_hits    += match['players'][x]['last_hits']
            dire_total_levels += match['players'][x]['level']
            dire_tower_damage += match['players'][x]['tower_damage']
            dire_xpm          += match['players'][x]['xp_per_min']

dire_barracks = match['barracks_status_dire']
dire_name = match['dire_name']
dire_tower_status = match['tower_status_dire']

matches_data.loc[i, 'dire_assists'] = dire_assists
matches_data.loc[i, 'dire_barracks'] = dire_barracks
matches_data.loc[i, 'dire_denies'] = dire_denies
matches_data.loc[i, 'dire_gpm'] = dire_gpm
matches_data.loc[i, 'dire_healing'] = dire_healing
matches_data.loc[i, 'dire_hero_damage'] = dire_hero_damage
matches_data.loc[i, 'dire_kills'] = dire_kills
matches_data.loc[i, 'dire_last_hits'] = dire_last_hits
matches_data.loc[i, 'Dire'] = dire_name
matches_data.loc[i, 'dire_total_levels'] = dire_total_levels
matches_data.loc[i, 'dire_tower_damage'] = dire_tower_damage
matches_data.loc[i, 'dire_tower_status'] = dire_tower_status
matches_data.loc[i, 'dire_xpm'] = dire_xpm

first_blood= match['first_blood_time']
        match_duration       = match['duration']
        if (match['radiant_win'] == True):
            match_winner = 1
        else:
            match_winner = 0

matches_data.loc[i, 'first_blood'] = first_blood
        matches_data.loc[i, 'match_duration'] = match_duration
        matches_data.loc[i, 'radiant_winner'] = match_winner
    except:
        print("Could not find data for ",  current_match)

pprint.pprint(matches_data.head(10))
matches_data.to_csv("data/full_data.csv", index=False)