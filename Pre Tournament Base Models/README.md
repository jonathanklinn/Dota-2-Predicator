# Dota-2-Predicator
Model for predicting the winner of a Dota 2 game.
extract_team_id reads through CSV file downloaded from OPenDota.com and returns a list of unique team_ids along with team names
extract_match_id reads through out put of extract_team_id and looks for matches where teams played each other.
dataschema is a pipeline that creates the dataframe I want listing All matches and their aggregate team performance including win and loss.

