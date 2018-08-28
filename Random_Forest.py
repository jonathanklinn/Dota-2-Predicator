import pprint
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import log_loss, make_scorer
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV


matchup_data = pd.read_csv("data/matchup_data.csv")

x_data = matchup_data[['diff_assists', 'diff_denies', 'diff_first_blood', 'diff_gpm', 'diff_healing', 'diff_hero_damage', 'diff_kills', 'diff_last_hits', 'diff_match_duration', 'diff_total_levels', 'diff_tower_damage', 'diff_xpm']]
y_data = matchup_data.radiant_winner

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.33, random_state = 12)
rf = RandomForestClassifier(n_estimators=1000,max_features='auto',random_state=0)
rf.fit(x_train, y_train)
prediction = dict()
prediction['RandomForest'] = rf.predict(x_test)

print(f"log loss = {log_loss(y_test, rf.predict_proba(x_test)[:, 1])}")
print(f"accuracy = {rf.score(x_test, y_test)}")

conf_mat_logist = confusion_matrix(y_test, prediction['Logistic'])
print('Logist \r', conf_mat_logist)
