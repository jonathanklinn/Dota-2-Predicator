import dota 2 api
import pprint
import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

api = dota2api.Initialise("STEAM_API_KEY")

matches_data = pd.read_csv("data\3yearmatchid.csv", encoding = "ISO-8859-1")

dict_info = {'Team_ID': [np.nan], 'Team_name': [np.nan]}
match_info = pd.DataFrame(dict_info)

for i in range(0, len(matches_data)): #
    try:
        current_match = matches_data['Match ID'][i]
        print(current_match)
        match = api.get_match_details(match_id = current_match)

        try:
            radiant_current = match['radiant_team_id']
        except:
            radiant_current = ""

try:
            radiant_name = match['radiant_name']
        except:
            radiant_name = ""

temp_info1 = {'Team_ID': radiant_current, 'Team_name': radiant_name}
        match_info = match_info.append(temp_info1, ignore_index=True)

try:
            dire_current = match['dire_team_id']
        except:
            dire_current = ""

try:
            dire_name = match['dire_name']
        except:
            dire_name = ""

temp_info2 = {'Team_ID': dire_current, 'Team_name': dire_name}
        match_info = match_info.append(temp_info2, ignore_index=True)

except:
        print("Something went wrong")

match_info = match_info.dropna()
match_info_nodups = match_info.drop_duplicates()
match_info_nodups.to_csv("data\\match_info_data.csv", index=False)
