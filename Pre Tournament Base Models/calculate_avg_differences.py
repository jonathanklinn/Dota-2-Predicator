
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
    team_map = {'20 min afk les' : 0, 'ALPHA Red' : 1, 'Alliance' : 2, 'BOOM ID': 3, 'Battle Arena Elites' : 4, 'BlinkPool': 5, 'Double Dimension': 6 ,'Entity Gaming': 7 ,'Espada': 8 ,'LeftOneTV': 9,'Fnatic': 10 ,'ForTheDream': 11 ,'GangSquad': 12 ,'Immortals': 13 ,'Infamous': 14 ,'Invictus Gaming':15 ,'Kaipi': 16 ,'Kingdra': 17,' LGD.Forever Young': 18,'LeftOneTV': 19,'MEGA-LADA E-sports':20 ,'Midas Club':21 ,'Mineski':22 ,'New Guys':23 ,'Newbee':24 ,'No Bounty Hunter':25,'OG':26 ,'OpTic Gaming':27 ,'PSG.LGD':28 ,'SG e-sports team': 29 ,'Sterling Global Dragons': 30,'TNC Predator': 31 ,'TNC Tigers':32 ,'Team Empire':33 ,'Team Kinguin': 34 ,'Team Leviathan': 35 ,'Team Liquid':36  ,'Team Secret': 37 ,'Team Serenity': 38 ,'Team Singularity':39  ,'Team. Spirit':40  ,'The Final Tribe':41  ,'Thunder Predator':42  ,'Torus Gaming':43  ,'VGJ Storm':44  ,'VGJ Thunder':45  ,'Vega Squadron':46  ,'Vici Gaming':47  ,'Virtus.pro':48  ,'Wind and Rain':49  ,'Winstrike': 50 ,'compLexity Gaming':51  ,'jsut a squad':52  ,'paiN Gaming':53}
    team1_ix = team_map[team1]
    team2_ix = team_map[team2]

    matchup_data.loc[i, 'diff_assists'] = team_data.loc[team1_ix, 'assists'] - team_data.loc[team2_ix, 'assists']
    matchup_data.loc[i, 'diff_denies'] = team_data.loc[team1_ix, 'denies'] - team_data.loc[team2_ix, 'denies']
    matchup_data.loc[i, 'diff_first_blood'] = team_data.loc[team1_ix, 'first_blood'] - team_data.loc[team2_ix, 'first_blood']
    matchup_data.loc[i, 'diff_gpm'] = team_data.loc[team1_ix, 'gpm'] - team_data.loc[team2_ix, 'gpm']
    matchup_data.loc[i, 'diff_healing'] = team_data.loc[team1_ix, 'healing'] - team_data.loc[team2_ix, 'healing']
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
        print("Could not find match ", x)

matchup_data.to_csv("data/matchup_data.csv", index = False)
