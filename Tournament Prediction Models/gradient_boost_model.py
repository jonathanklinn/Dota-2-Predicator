import pprint
import pandas as pd
import numpy as np


from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.metrics import log_loss, make_scorer
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV


matchup_data = pd.read_csv("data/matchup_data.csv")

x_data = matchup_data[['diff_assists', 'diff_denies', 'diff_first_blood', 'diff_gpm', 'diff_healing', 'diff_hero_damage', 'diff_kills', 'diff_last_hits', 'diff_match_duration', 'diff_total_levels', 'diff_tower_damage', 'diff_xpm']]
y_data = matchup_data.radiant_winner

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.33, random_state = 14)
gbc = GradientBoostingClassifier(n_estimators=10000,learning_rate= .01,max_depth= 10, random_state=14)
gbc.fit(x_train, y_train)
prediction = dict()
prediction['Gradient Boost'] = gbc.predict(x_test)

print(f"log loss = {log_loss(y_test, gbc.predict_proba(x_test)[:, 1])}")
print(f"accuracy = {gbc.score(x_test, y_test)}")