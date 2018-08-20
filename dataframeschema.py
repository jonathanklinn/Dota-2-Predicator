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
matches_data['radiant_winner'] = 0    # 1= win 0 = lose
