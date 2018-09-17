# Dota 2 World Championship Main Event Match Predictor 
A Machine Learning Approach to Predicting the Results of Professional ESports Tournament

## Table of Contents
1. [Motivation](#motivation)
2. [Product](#product)
3. [Usage](#usage)
4. [Gathering Data](#gathering-and-cleaning-data)
5. [Data Preparation](#data-preparation)
6. [Modeling](#modeling)
7. [Results](#results)
8. [Future Work](#future-work)
9. [References](#references)

## Motivation

>**“I believe esports will rival the biggest traditional sports leagues in terms of future opportunities, and between advertising, ticket sales, licensing, sponsorships and merchandising, there are tremendous growth areas for this nascent industry”**.
>
>–Steve Borenstein, Chairman of Activision Blizzard’s Esports Division and Former CEO of ESPN and NFL Network

Esports is currently the fastest growing . In the same way that traditional sports have competitions in baseball, basketball, and football, esports encompasses competitions across a variety of video games. Contrary to common perception, esports is not simply a phenomenon occurring in the basements of unemployed twentysomethings; the industry is real, growing globally, and investable. In fact, over 380 million people watch esports worldwide both online and in person. More people watched the 2016 world finals of popular esports game League of Legends (43 million viewers) than the NBA Finals Game 7 that year (31 million viewers). With its fragmented landscape and digital platform, the esports sector holds promise for a multitude of monetization opportunities.

Esports to reach 385 million viewers in 2017: According to Newzoo, an esports market research organization, in 2017, the audience of esports will reach a total of roughly 385 million people globally. Of this figure, 191 million are “esports enthusiasts” and 194 million are “occasional viewers.” The number of enthusiasts is projected to grow by 50% by 2020, totaling 286 million

Similar to how the NFL, NBA, MLB, and NHL follow a franchise model with limited membership in their respective sports, esports in North America seems to be following a similar path. A recent announcement from Riot on their League of Legends title has established a franchise model for the North American league. 

As franchising becomes the dominant model, elite teams and organizations will become revenue-generating machines. However, those without franchise spots will be forced to find revenue in secondary 







![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Esports%20Growth%202.png)

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
The repository has the following structure. GitHub scraping and cleaning are located in data_cleaning_functions.py.  Code and analysis are located in model a Model\ Analysis.ipynb
```
├── Pre\ Tournament\ Base\ Models
│   ├── Data\ Cleaning\ Test.ipynb
│   ├── Model\ Analysis.ipynb
│   ├── README.md
│   ├── __pycache__
│   │   ├── data_cleaning_functions.cpython-36.pyc
│   │   ├── dota2_predictor_functions.cpython-36.pyc
│   │   ├── extract_match_data.cpython-36.pyc
│   │   └── model_functions.cpython-36.pyc
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
└── steam_api_key.txt

```

## Gathering Data

Using opendota.com query function. I used the following SQL query to gather all games pre-tournament matches played from June 14th 2018 to August 20th 2018:

SELECT
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

The query returned 410 matches. After deleting null values( games that had missing data due to disqualifications or disconnections) there were a total of 390 pre-tournament matches and a total of 31 teams competing for the 18 main event spots. 

I then extracted all 390 match_ids from the query and created a dataframe called “pre_ti_match_ids” that would be used in the cleaning and preparation process.

## Data Preparation

The dataframe consisting of the match ids were then processed using a data cleaning pipeline using the functions in "data_cleaning_functions.py. 

This is a quick outline of the steps taken to create the final dataframe used for modeling

  1. Intialize the dota2api by using a personal steam api key
  2. Call the dota2api for individual match data by looping through each match_id from "pre_ti_match_ids" dataframe
  3. Find team averages for each team by using the pivot function
  4. Find the differences in team averages between competeing teams for each match. Include a binary variable called "Radiant        Win"
  
 The final dataframe should look something like this:
 ![alt text](https://github.com/jonathanklinn/Dota-2-Predictor/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.09.58%20PM.png)




## Modeling

To train my model, I tried four different hard classifier algorithims using sci-kit learn. Logistic Regression, KNN, Random Forest, and Gradient Boosting. I used accuracy is my performance metric.

Of the four tested, Gradient Boosting had the highest cross validation accuracy rating. After performing a grid search for the best possible parameters I had the following results:

![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.06.00%20PM.png)

The following are the feature importances:
![alt text](https://github.com/jonathanklinn/Dota-2-Predictor/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.06.49%20PM.png)

The results show that hero damage had the most influence and predictive power when using GDBC.

The following are partial dependency plots:
![alt text](https://github.com/jonathanklinn/Dota-2-Predictor/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.07.17%20PM.png)

You can see here how drastic the change is when looking at hero damage.


## Results

After finding the best fit model for the pre-toruanment results. I applied the same model and same parameters but this time using the Main Event game results as my target. The targets consisted of the final 38 games played during the "Main Event" phase of the tournament.

These were my results:

![alt text](https://github.com/jonathanklinn/Dota-2-Predictor/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.11.20%20PM.png)

Surprisngly, there was a higher accuracy rating in predicting the 38 games. This is probably due to the fact that the data set was much smaller. 

My model correctly predicted that Team OG would beat out PSG.LGD even though the match up was neck to neck and ended in a 5 game series.


## Future Work

I believe that my model could be further improved if I used rolling averages instead of static averages to predict game outcomes. I also believe that adding in individual player data instead of team data would make my model more robust seeing how many teams change players during the competitive season. I also plan on implementing a web app where you can input two teams and a prediction will be generated.

## References




