import pprint
import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

matches_data_radiant = pd.read_csv("data/full_data.csv")
matches_data_radiant.insert(3, 'is_radiant', 1)

matches_data_dire = pd.read_csv("data/full_data.csv")
matches_data_dire.insert(3, 'is_radiant', 0)

del matches_data_radiant['Dire']
del matches_data_radiant['dire_assists']
del matches_data_radiant['dire_barracks']
del matches_data_radiant['dire_denies']
del matches_data_radiant['dire_gpm']
del matches_data_radiant['dire_healing']
del matches_data_radiant['dire_hero_damage']
del matches_data_radiant['dire_kills']
del matches_data_radiant['dire_last_hits']
del matches_data_radiant['dire_total_levels']
del matches_data_radiant['dire_tower_damage']
del matches_data_radiant['dire_tower_status']
del matches_data_radiant['dire_xpm']

del matches_data_dire['Radiant']
del matches_data_dire['radiant_assists']
del matches_data_dire['radiant_barracks']
del matches_data_dire['radiant_denies']
del matches_data_dire['radiant_gpm']
del matches_data_dire['radiant_healing']
del matches_data_dire['radiant_hero_damage']
del matches_data_dire['radiant_kills']
del matches_data_dire['radiant_last_hits']
del matches_data_dire['radiant_total_levels']
del matches_data_dire['radiant_tower_damage']
del matches_data_dire['radiant_tower_status']
del matches_data_dire['radiant_xpm']

matches_data_radiant = matches_data_radiant.rename(columns = {'Radiant' : 'team', 'radiant_assists' : 'assists', 'radiant_barracks' : 'barracks', 'radiant_denies' : 'denies', 'radiant_gpm' : 'gpm', 'radiant_healing' : 'healing', 'radiant_hero_damage' : 'hero_damage','radiant_kills' : 'kills', 'radiant_last_hits' : 'last_hits', 'radiant_total_levels' : 'total_levels', 'radiant_tower_damage' : 'tower_damage', 'radiant_tower_status' : 'tower_status', 'radiant_xpm' : 'xpm'})

matches_data_dire = matches_data_dire.rename(columns = {'Dire' : 'team', 'dire_assists' : 'assists', 'dire_barracks' : 'barracks', 'dire_denies' : 'denies', 'dire_gpm' : 'gpm', 'dire_healing' : 'healing', 'dire_hero_damage' : 'hero_damage','dire_kills' : 'kills', 'dire_last_hits' : 'last_hits', 'dire_total_levels' : 'total_levels', 'dire_tower_damage' : 'tower_damage', 'dire_tower_status' : 'tower_status', 'dire_xpm' : 'xpm'})

matches_data_both = pd.concat([matches_data_radiant, matches_data_dire])

matches_pivot = matches_data_both.pivot_table(index = ['team'], margins = True , aggfunc = np.mean)

del matches_pivot['match_id']
del matches_pivot['barracks']
del matches_pivot['tower_status']

matches_pivot = matches_pivot.drop(['All'])

# pprint.pprint(matches_pivot)

matches_pivot.to_csv("data/team_averages.csv")
