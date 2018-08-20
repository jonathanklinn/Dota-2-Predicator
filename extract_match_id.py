import pandas as pd
import numpy as np
import requests
import bs4 import BeautifulSoup



def get_match_id(team_1,team_2, match_ids):
    try:
        url='http://www.datdota.com/matchfinder/classic?team-a=' + team_1 + '&team-b=' + team_2 +'&patch=7.19&patch=7.18&patch=7.17&patch=7.16&patch=7.15&patch=7.14&patch=7.13&patch=7.12&patch=7.11&patch=7.10&patch=7.09&patch=7.08&patch=7.07&patch=7.06&patch=7.05&patch=7.04&patch=7.03&patch=7.02&patch=7.01&patch=7.00&patch=6.88&after=20%2F08%2F2015&before=20%2F08%2F2018&duration=0%3B200&duration-value-from=0&duration-value-to=200&valve-event=does-not-matter&threshold=1'


    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find(class_ ='table table-striped table-bordered table-hover data-table')

    for row in table.find_all('tr')[2:]:
            col = row.find_all('td')
            temp_id = col[1].text.strip()
            print(temp_id)
            temp_df = {'match_id': temp_id}
            match_ids = match_ids.append(temp_df, ignore_index=True)

    return match_ids
        except:
            return match_ids

dict1 = {'match_id': [np.nan]}
match_ids = pd.DataFrame(dict1)

# match_ids = getMatchIds(team_a, team_b, match_ids)

team_ids = pd.read_csv("data/match_info_data.csv")

# print(team_ids)

for i in range(0, len(team_ids)):
    for x in range (i + 1, len(team_ids)):
        team_a = team_ids.loc[i, 'Team_ID']
        team_b = team_ids.loc[x, 'Team_ID']
        match_ids = getMatchIds(str(team_a), str(team_b), match_ids)

match_ids = match_ids.dropna(how ='all')
print(match_ids)

match_ids.to_csv("data/match_ids.csv", index = False)
