import pandas as pd
import numpy as np



import matplotlib.pyplot as plt
plt.style.use('ggplot')


from pandas.plotting import scatter_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import r2_score, log_loss
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.metrics import log_loss, make_scorer

from sklearn.pipeline import Pipeline
from regression_tools.dftransformers import (
    ColumnSelector, Identity,
    FeatureUnion, MapFeature,
    StandardScaler)


matchup_data = pd.read_csv("data/matchup_data.csv")

X = matchup_data[['diff_assists', 'diff_denies', 'diff_first_blood', 'diff_gpm', 'diff_healing', 'diff_hero_damage', 'diff_kills', 'diff_last_hits', 'diff_match_duration', 'diff_total_levels', 'diff_tower_damage', 'diff_xpm']]
#X = matchup_data[['diff_assists', 'diff_denies','diff_gpm', 'diff_healing', 'diff_hero_damage', 'diff_kills', 'diff_last_hits', 'diff_total_levels', 'diff_tower_damage', 'diff_xpm']]
y = matchup_data.radiant_winner

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 1)



def crossVal(estimators, X_train, y_train, k=5):
    kf = KFold(n_splits = k, shuffle=True)
    splits = kf.split(X_train, y_train)
    scores = []

    for train_index, test_index in splits:
        score = []
        for estimator in estimators:
            X_train_fold, X_test_fold = X_train.values[train_index], X_train.values[test_index]
            y_train_fold, y_test_fold = y_train.values[train_index], y_train.values[test_index]
            estimator.fit(X_train_fold, y_train_fold)
            train_predicted = estimator.predict(X_train_fold)
            test_predicted = estimator.predict(X_test_fold)
            score.append(accuracy_score(y_test_fold, test_predicted))
        scores.append(score)
    return np.array(scores)
