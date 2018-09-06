import dota2api
import pandas as pd
import numpy as np


api= dota2api.Initialise("B335AEF628EF2F2D2DC5A94BA4A02ED9")

#CSV file was taken from https://www.opendota.com/ Using the SQL query function using the following SQL Query:
# use ctrl + '/' to uncomment SQL query if you want to use it

# SELECT
# matches.match_id,
# matches.start_time,
# ((player_matches.player_slot < 128) = matches.radiant_win) win,
# player_matches.hero_id,
# player_matches.account_id,
# leagues.name leaguename
# FROM matches
# JOIN match_patch using(match_id)
# JOIN leagues using(leagueid)
# JOIN player_matches using(match_id)
# JOIN heroes on heroes.id = player_matches.hero_id
# LEFT JOIN notable_players ON notable_players.account_id = player_matches.account_id AND notable_players.locked_until = (SELECT MAX(locked_until) FROM notable_players)
# LEFT JOIN teams using(team_id)
# WHERE TRUE
# AND matches.start_time >= extract(epoch from timestamp '2018-06-20T07:00:00.000Z')
# AND matches.start_time <= extract(epoch from timestamp '2018-08-20T07:00:00.000Z')
# AND leagues.tier = 'premium'
# ORDER BY matches.match_id NULLS LAST


# All functions that end with path are indicate that the file path to the csv file needs to be inserted as a string.

# this function creates a match_ids.csv file using the raw data from the query
def load_csv(csv_path): # parameter is the csv file path as a string
    df=pd.read_csv(csv_path)
    df=df.drop_duplicates('match_id')#drops duplicate match ids because players can be in the same match.
    df.drop(df.iloc[:,1:6], inplace=True, axis=1)# remove unused columns
    df.to_csv("data/match_ids.csv", index = False)# create a new dataframe "match_ids.csv"


# this function uses the match ids in "match_ids.csv" and does and api call. It then puts that data into a dataframe I have named "full_data.csv"
def extract_match_data(match_ids_path):   # parameter is the csv file path as a string
    matches_data= pd.read_csv("data/match_ids.csv")
    matches_data['Radiant'] = ''
    matches_data['Dire'] = ''

    matches_data['radiant_assists'] = 0  # Here I am creating individual columns for the new dataframe
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
        # MATCH   Fills
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
        radiant_xpm          = 0
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
            match = api.get_match_details(match_id = current_match) # uses the dota2api to query each match.
            for x in range(0, 5):# cycles through the first 5 players of each match (radiant team) and aggregates their in game stats to create team statistics
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

            for x in range(5, 10): # cycles through the last 5 players (dire team) and aggregates their in-game stats to create team statistics.
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



    matches_data=matches_data.dropna()
    matches_data=matches_data.reset_index(drop=True)


    print(matches_data)

    matches_data.to_csv("data/full_data.csv", index=False)
# This function takes in the csv file path as a string and drops any rows with missing values and reindex's the data frame. You made need to use this when there are teams that no longer exist in the database
def drop_na(full_data_path):
    df=pd.read_csv(full_data_path)
    df=df.dropna()
    df=df.reset_index(drop=True)
    df.to_csv(full_data_path, index=False)

# This function takes in the full_data csv from the "extract match data function" and creates a dataframe listing all teams and their average performance over specificed time period.
def find_team_avg(full_data_path):  # parameter is the csv file path as a string
    matches_data_radiant = pd.read_csv(full_data_path) # creates a radiant team data frame
    matches_data_radiant.insert(3, 'is_radiant', 1)

    matches_data_dire = pd.read_csv(full_data_path) # creates a dire team data frame
    matches_data_dire.insert(3, 'is_radiant', 0)

    del matches_data_radiant['Dire'] # removes Dire Team data from the Radiant dataframe
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

    del matches_data_dire['Radiant'] # removes Radiant Team data from the Dire dataframe
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
    
    # renames the columns for the data frames, adds the two frames together and gives finds the averages of all the matches

    matches_data_radiant = matches_data_radiant.rename(columns = {'Radiant' : 'team', 'radiant_assists' : 'assists', 'radiant_barracks' : 'barracks', 'radiant_denies' : 'denies', 'radiant_gpm' : 'gpm', 'radiant_healing' : 'healing', 'radiant_hero_damage' : 'hero_damage','radiant_kills' : 'kills', 'radiant_last_hits' : 'last_hits', 'radiant_total_levels' : 'total_levels', 'radiant_tower_damage' : 'tower_damage', 'radiant_tower_status' : 'tower_status', 'radiant_xpm' : 'xpm'})

    matches_data_dire = matches_data_dire.rename(columns = {'Dire' : 'team', 'dire_assists' : 'assists', 'dire_barracks' : 'barracks', 'dire_denies' : 'denies', 'dire_gpm' : 'gpm', 'dire_healing' : 'healing', 'dire_hero_damage' : 'hero_damage','dire_kills' : 'kills', 'dire_last_hits' : 'last_hits', 'dire_total_levels' : 'total_levels', 'dire_tower_damage' : 'tower_damage', 'dire_tower_status' : 'tower_status', 'dire_xpm' : 'xpm'})

    matches_data_both = pd.concat([matches_data_radiant, matches_data_dire])

    matches_pivot = matches_data_both.pivot_table(index = ['team'], margins = True , aggfunc = np.mean)

    del matches_pivot['match_id']
    del matches_pivot['barracks']
    del matches_pivot['tower_status']

    matches_pivot = matches_pivot.drop(['All'])


    matches_pivot.to_csv("data/team_averages.csv")

# This function take both team_average.csv from find_team_avg function and and full_data from extract_match_data functio
# It then outputs a dataframe that shows the difference in average staatistics IN RESPECT to the Radiant team_map
# the function the outputs our final data frame to be used in the modeling process called "matchup_data"
def calculate_team_differences(team_averages_path,full_data_path):  # parameters are both csv file path as a string
    team_data = pd.read_csv(team_averages_path)
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
    # this Inner function takes uses a dictionary that is mapped from the team_averages.csv. It lists every team that will be used in that time period
    # it then subtracts the team averages IN RESPECT TO THE RADIANT team
    # Example:  A negative 25 score in "diff_last hits" column would indicate that the Dire team had 25 MORE last hits than the radiant team
    def find_team_difference(team1, team2, i):
        team_map = {'20 min afk les' : 0, 'Alliance' : 1, 'Espada' : 2, 'Evil Geniuses': 3, 'Fnatic' : 4, 'Invictus Gaming': 5, 'Kaipi': 6 ,'LeftOneTV': 7 ,'MEGA-LADA E-sports': 8 ,'Mineski': 9,'New Guys':10 ,'Newbee': 11,'No Bounty Hunter': 12 ,'OG': 13 ,'OpTic Gaming': 14 ,'PSG.LGD':15 ,'TNC Predator': 16 ,'Team Empire': 17,'Team Liquid': 18,'Team Secret': 19,'Team Serenity':20 ,'Team Singularity':21 ,'The Final Tribe':22 ,'VGJ Storm':23 ,'VGJ Thunder':24 ,'Vega Squadron':25,'Vici Gaming':26,'Virtus.pro':27,'Wind and Rain':28, 'Winstrike':29, 'paiN Gaming':30, '•':31}
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
            print("Not able to find ", x)

    matchup_data.to_csv("data/matchup_data.csv", index = False)
