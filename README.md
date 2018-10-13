# Dota 2 World Championship Main Event Match Predictor 
A Machine Learning Approach to Predicting the Results of Professional ESports Tournament

## Table of Contents
1. [Motivation](#motivation)
2. [Product](#product)
3. [Usage](#usage)
4. [Gathering Data](#gathering-data)
5. [Data Preparation](#data-preparation)
6. [Modeling](#modeling)
7. [Results](#prediction-results)
8. [Future Work](#future-work)
9. [References](#references)

## Motivation

>**“I believe esports will rival the biggest traditional sports leagues in terms of future opportunities, and between advertising, ticket sales, licensing, sponsorships and merchandising, there are tremendous growth areas for this nascent industry”**.
>
>–Steve Borenstein, Chairman of Activision Blizzard’s Esports Division and Former CEO of ESPN and NFL Network

Esports is currently the fastest growing digital entertainment platform. In the same way that traditional sports have competitions, in basketball, football, and baseball, esports encompasses competitions across a variety of video games. Contrary to common perception, esports is not simply a phenomenon occurring in the basements of unemployed twentysomethings; the industry is real, growing rapidly, and readily investable. Over 380 million people watch esports worldwide both online and in person. More people watched the 2016 world finals of League of Legends (43 million viewers) than the NBA Finals Game 7 that year (31 million viewers). The esports sector holds promise for a multitude of monetization opportunities.

Similar to how the NFL, NHL, MLB, and NBA follow a franchise model , esports in North America seems to be following a similar path. As franchising becomes the dominant model, elite teams and organizations will become revenue-generating machines. However, those without franchise spots will be forced to find revenue in secondary markets and this is where I believe industries industries built around data analytics, predictions, esports gambling, will thrive. 


### Market Segments of E-Sports

![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Esports%20Growth%202.png)



### Popularity Growth of E-Sports Gambling

![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Esports%20Growth%203.jpg)


## Product

The 2018 International Dota 2 World Championships is comprised of two phases, a pre-tournament phase and a main event phase. The pre-tournament phase consists of three separate events; an open qualifier, regional qualifier, and a pre-main event group stage that determines each team’s starting position and bracket during the main event. This pre-tournament phase lasts 2 months starting June 14th and ending on August 20th 2018. The second phase, the main event, is where the top 18 teams from the pre-tournament phase battle it out for the final championship.

The dota-2-predictor makes its main event prediction based of the differences between the two competing team’s average in-game statistics. The main assumption I am making is that teams that perform well in the pre-tournament stages have a higher chance of winning during the main event. These averages are taken from the games they played during the pre-tournament phase. The differences are taken in respect to the "Radiant Team" of that game. The model predicts whether or not the “Radiant Team” will win based off of the differences in various in game statistics.

I chose to limit the training and testing data because I believe that the pre-tournament phase games will be the best indicator of performance in the Main Event games. Other reasons include the fact that many teams are organized specifically for the World championships so team data prior to June 14th for those teams do not exist.


## Usage

Clone this repository with the command
```
git clone https://github.com/jonathanklinn/Dota-2-Predictor
```
The repository has the following structure. GitHub scraping and cleaning are located in data_cleaning_functions.py.  Modeling and analysis are located in model a Model\ Analysis.ipynb
```
.
├── Images
│   ├── Esports\ Growth\ 1.jpg
│   ├── Esports\ Growth\ 2.png
├── Pre\ Tournament\ Base\ Models
│   ├── Data\ Cleaning\ Test.ipynb
│   ├── Model\ Analysis.ipynb
│   ├── README.md
│   ├── data
│   │   ├── full_data.csv
│   │   ├── match_ids.csv
│   │   ├── matchup_data.csv
│   │   ├── pre_ti_matches.csv
│   │   ├── team_averages.csv
│   │   └── tournament_matches.csv
│   ├── data_cleaning_functions.py
│   ├── model_functions.py
│   └── steam_api_key.txt
├── README.md
├── Tournament\ Prediction\ Models
│   ├── README.md
│   ├── TI\ Predictions\ Using\ Gradient\ Boosting.ipynb
│   ├── data
│   │   ├── full_data.csv
│   │   ├── match_ids.csv
│   │   ├── matchup_data.csv
│   │   ├── pre_ti_matches.csv
│   │   ├── team_averages.csv
│   │   ├── ti_full_data.csv
│   │   ├── ti_match_ids.csv
│   │   ├── ti_matchup_data.csv
│   │   ├── ti_team_averages.csv
│   │   └── tournament_matches.csv
│   ├── data_cleaning_functions.py
│   └── model_functions.py
└── steam_api_key.txt

```
In order to use data_cleaning_functions.py you will need to register for your own private steam_api_key. The last 3 digits of mine have been asterisked out for privacy and security reasons. You can find how to get your own api key here https://steamcommunity.com/dev


## Gathering Data

Using opendota.com query function. I used the following SQL query to gather all games pre-tournament matches played from June 14th 2018 to August 20th 2018:

```SELECT
matches.match_id,
matches.start_time,
((player_matches.player_slot < 128) = matches.radiant_win) win,
player_matches.hero_id,
player_matches.account_id,
leagues.name leaguename
FROM matches
JOIN match_patch using(match_id)
JOIN leagues using(leagueid)
JOIN player_matches using(match_id)
JOIN heroes on heroes.id = player_matches.hero_id
LEFT JOIN notable_players
ON notable_players.account_id = player_matches.account_id
AND notable_players.locked_until = (SELECT MAX(locked_until)
FROM notable_players)
LEFT JOIN teams using(team_id)
WHERE TRUE
AND matches.start_time >= extract(epoch from timestamp '2018-06-20T07:00:00.000Z')
AND matches.start_time <= extract(epoch from timestamp '2018-08-20T07:00:00.000Z')
AND leagues.tier = 'premium'
ORDER BY matches.match_id NULLS LAST
```
The query returned 410 matches. After deleting null values( games that had missing data due to disqualifications or disconnections) there were a total of 390 pre-tournament matches and a total of 31 teams competing for the 18 main event spots. 

I then extracted all 390 match_ids from the query and created a dataframe called “pre_ti_match_ids” that would be used in the cleaning and preparation process.

## Data Preparation

The dataframe consisting of the match ids were then processed using a data cleaning pipeline using the functions in "data_cleaning_functions.py. 

This is a quick outline of the steps taken to create the final dataframe used for modeling

  1. Intialize the dota2api by using a personal steam api key
  2. Call the dota2api for individual match data by looping through each match_id from "pre_ti_match_ids" dataframe
  3. Find team averages for each team by using the pivot function
  4. Find the differences in team averages between competeing teams for each match. Include a binary variable called "radiant_winner"
  
 The final dataframe should look something like this:
 ![alt text](https://github.com/jonathanklinn/Dota-2-Predictor/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.09.58%20PM.png)




## Modeling

To train my model, I tried four different hard classifier algorithims using sci-kit learn. Logistic Regression, KNN, Random Forest, and Gradient Boosting. I used accuracy is my performance metric.

Of the four tested, Gradient Boosting had the highest cross validation accuracy rating. After performing a grid search for the best possible parameters I had the following results:

![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.06.00%20PM.png)

The following are the feature importances:

![alt text](https://github.com/jonathanklinn/Dota-2-Predictor/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.06.49%20PM.png)

The results show that hero damage was the most influential in the construction of the GDBC model.

The following are partial dependency plots:
![alt text](https://github.com/jonathanklinn/Dota-2-Predictor/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.07.17%20PM.png)

You can see here how drastic the change is when looking at hero damage.


##  Prediction Results

After finding the best fit model for the pre-toruanment results. I applied the same model and same parameters but this time using the Main Event game results as my target. The targets consisted of the final 38 games played during the "Main Event" phase of the tournament.

These were my results:

![alt text](https://github.com/jonathanklinn/Dota-2-Predictor/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.11.20%20PM.png)

Surprisngly, there was a higher accuracy rating in predicting the 38 games. This is probably due to the fact that the data set was much smaller. 

My model predicted that Team OG would beat out PSG.LGD in the World Championship Finals. The final series ended up with a 5 game series where Team OG beat out PSG.LGD 3-2.  

Since my model used data from the pre-tournament matches it is inherently flawed because it does not take into account data from the Main Event. MY model would have predicted that OG would have won every single game in the 5 game series regardless of how they had performed during the week. This is something thatva rolling average could fix and is mentioned in my future work section


## Future Work

I believe that my model could be further improved if I used rolling averages instead of static averages to predict game outcomes. I also believe that adding in individual player data instead of team data would make my model more robust seeing how many teams change players during the competitive season. I also plan on implementing a web app where you can input two teams and a prediction will be generated.

## References

'Report: Esports To Grow Substantially And Near Billion-Dollar Revenues In 2018'
https://www.forbes.com/sites/mattperez/2018/02/21/report-esports-to-grow-substantially-and-near-a-billion-dollar-revenues-in-2018/#40cc893b2b01

'Complete Guide to Parameter Tuning in Gradient Boosting (GBM) in Python'
https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/


## Tech Stack

<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="250">

<img src="https://kaggle2.blob.core.windows.net/competitions/kaggle/3428/media/scikit-learn-logo.png" width="250">
<img src="https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Logo_of_NumPy.svg/1200px-Logo_of_NumPy.svg.png" width="250">
<img src="https://pandas.pydata.org/_static/pandas_logo.png" width="250">



