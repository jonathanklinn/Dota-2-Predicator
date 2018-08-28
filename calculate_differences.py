import pprint
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score , confusion_matrix

pd.set_option('display.expand_frame_repr', False)

team_data = pd.read_csv("data/team_averages.csv")
matches_data = pd.read_csv("data/full_data.csv")
matchup_data = matches_data[['match_id', 'Radiant', 'Dire', 'radiant_winner']]

matchup_data['diff_assists'] = 0
matchup_data['diff_denies'] = 0
matchup_data['diff_first_blood'] = 0
matchup_data['diff_gpm'] = 0
matchup_data['diff_healing'] = 0
matchup_data['diff_hero_damage'] = 0
matchup_data['diff_kills'] = 0
matchup_data['diff_last_hits'] = 0
matchup_data['diff_match_duration'] = 0
matchup_data['diff_total_levels'] = 0
matchup_data['diff_tower_damage'] = 0
matchup_data['diff_xpm'] = 0

def find_team_difference(team1, team2, i):
    team_map = {'Evil Geniuses' : 0, 'Fnatic' : 1, 'Invictus Gaming' : 2, 'Mineski': 3, ' Newbee' : 4, 'OG': 5, 'OpTic Gaming': 6 ,'PSG.LGD': 7 ,'TNC Predator': 8 ,'Team Liquid': 9,'Team Secret': 10 ,'Team Serenity': 11 ,'VGJ Storm': 12 ,'VGJ Thunder: 13 ,'Vici Gaming': 14 ,'Virtus.pro':15 ,'Winstrike': 16 ,'paiN Gaming': 17 , }

    team1_ix = team_map[team1]
    team2_ix = team_map[team2]

matchup_data.loc[i, 'diff_assists'] = team_data.loc[team1_ix, 'assists'] - team_data.loc[team2_ix, 'assists']
    matchup_data.loc[i, 'diff_denies'] = team_data.loc[team1_ix, 'denies'] - team_data.loc[team2_ix, 'denies']
    matchup_data.loc[i, 'diff_first_blood'] = team_data.loc[team1_ix, 'first_blood'] - team_data.loc[team2_ix, 'first_blood']
    matchup_data.loc[i, 'diff_gpm'] = team_data.loc[team1_ix, 'gpm'] - team_data.loc[team2_ix, 'gpm']
    matchup_data.loc[i, 'diff_healing'] = team_data.loc[team1_ix, 'healing'] - team_data.loc[team2_ix, 'healing']'':  ,
    matchup_data.loc[i, 'diff_hero_damage'] = team_data.loc[team1_ix, 'hero_damage'] - team_data.loc[team2_ix, 'hero_damage']
    matchup_data.loc[i, 'diff_kills'] = team_data.loc[team1_ix, 'kills'] - team_data.loc[team2_ix, 'kills']
    matchup_data.loc[i, 'diff_last_hits'] = team_data.loc[team1_ix, 'last_hits'] - team_data.loc[team2_ix, 'last_hits']
    matchup_data.loc[i, 'diff_match_duration'] = team_data.loc[team1_ix, 'match_duration'] - team_data.loc[team2_ix, 'match_duration']
    matchup_data.loc[i, 'diff_total_levels'] = team_data.loc[team1_ix, 'total_levels'] - team_data.loc[team2_ix, 'total_levels']
    matchup_data.loc[i, 'diff_tower_damage'] = team_data.loc[team1_ix, 'tower_damage'] - team_data.loc[team2_ix, 'tower_damage']
    matchup_data.loc[i, 'diff_xpm'] = team_data.loc[team1_ix, 'xpm'] - team_data.loc[team2_ix, 'xpm']

for x in range(0, len(matchup_data)):
    print(x, " of ", len(matchup_data))
    try:
        find_team_difference(matchup_data.loc[x,'Radiant'], matchup_data.loc[x, 'Dire'], x)
    except:
        print("Not able to find ", x)

matchup_data.to_csv("data/matchup_data.csv", index = False)
