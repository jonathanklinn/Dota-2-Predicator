import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix





matchup_data = pd.read_csv("data/matchup_data.csv")

x_data = matchup_data[['diff_assists', 'diff_denies', 'diff_first_blood', 'diff_gpm', 'diff_healing', 'diff_hero_damage', 'diff_kills', 'diff_last_hits', 'diff_match_duration', 'diff_total_levels', 'diff_tower_damage', 'diff_xpm']]
y_data = matchup_data.radiant_winner

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.33, random_state = 14)
model = LogisticRegression()
model.fit(x_train, y_train)
prediction = dict()
prediction['Logistic'] = model.predict(x_test)

print('Log: ',accuracy_score(y_test, prediction['Logistic']))
print(model.coef_)

conf_mat_logist = confusion_matrix(y_test, prediction['Logistic'])
print('Logist \r', conf_mat_logist)