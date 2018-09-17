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
10. [License](#license)

## Motivation

>**“I believe esports will rival the biggest traditional sports leagues in terms of future opportunities, and between advertising, ticket sales, licensing, sponsorships and merchandising, there are tremendous growth areas for this nascent industry”**.
>
>–Steve Borenstein, Chairman of Activision Blizzard’s Esports Division and Former CEO of ESPN and NFL Network

Esports is a booming global industry where skilled video gamers play competitively. In the same way that traditional sports have competitions in baseball, basketball, and football, esports encompasses competitions across a variety of video games. Contrary to common perception, esports is not simply a phenomenon occurring in the basements of unemployed twentysomethings; the industry is real, growing globally, and investable. In fact, over 380 million people watch esports worldwide both online and in person. More people watched the 2016 world finals of popular esports game League of Legends (43 million viewers) than the NBA Finals Game 7 that year (31 million viewers). With its fragmented landscape and digital platform, the esports sector holds promise for a multitude of monetization opportunities.

Esports to reach 385 million viewers in 2017: According to Newzoo, an esports market research organization, in 2017, the audience of esports will reach a total of roughly 385 million people globally. Of this figure, 191 million are “esports enthusiasts” and 194 million are “occasional viewers.” The number of enthusiasts is projected to grow by 50% by 2020, totaling 286 million

Similar to how the NFL, NBA, MLB, and NHL follow a franchise model with limited membership in their respective sports, esports in North America seems to be following a similar path. A recent announcement from Riot on their League of Legends title has established a franchise model for the North American league. There will be ten spots, each with the hefty price tag of $10 million to buy in. Activision’s title, Overwatch, is also in the process of franchising. In Europe, esports is likely going to follow a promotion and relegation model, given the region’s familiarity with that sporting system in groups like the UEFA Champions League.

As franchising becomes the dominant model, elite teams and organizations will become revenue-generating machines. However, those without franchise spots will be forced to find revenue in secondary leagues or look to establish themselves in titles that have yet to be franchised. They won’t have access to sizeable revenue sharing deals in places like League of Legends and will have to focus on competing in secondary leagues, which offer far smaller cash prizes and sponsorship opportunities. While this consolidation will certainly be painful initially, I view this as a much-needed step forward for the industry as it continues to grow and prune the market. 

The upcoming year should see esports grow to ~$700 million, a growth of 41% from the previous year and an increase from $325 million in 2015. The 2017 figure does not include betting or fantasy esports numbers. Revenues are projected to reach $1.5 billion by 2020, growing at a CAGR (2015-2020) of 35.6%.





![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Esports%20Growth%202.png)

![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Esports%20Growth%203.jpg)


## Product

The 2018 International Dota 2 World Championships is comprised of two phases, a pre-tournament phase and a main event phase. The pre-tournament phase consists of three separate events; an open qualifier, regional qualifier, and a pre-main event group stage that determines each team’s starting position and bracket during the main event. This pre-tournament phase lasts 2 months starting June 14th and ending on August 20th 2018. The second phase, the main event, is where the top 18 teams from the pre-tournament phase battle it out for the final championship.

The dota-2-predictor makes its main event prediction based of the differences between the two competing team’s average in-game statistics. The main assumption I am making is that teams that perform well in the pre-tournament stages have a higher chance of winning during the main event. These averages are taken from the games they played during the pre-tournament phase. The differences are taken in respect to the "Radiant Team" of that game. The model predicts whether or not the “Radiant Team” will win based off of the differences in various in game statistics.

I chose to limit the training and testing data because I believe that the pre-tournament phase games will be the best indicator of performance in the Main Event games. Other reasons include the fact that many teams are organized specifically for the World championships so team data prior to June 14th for those teams do not exist.



## Usage



## Gathering Data







## Data Preparation

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
# AND matches.start_time <= extract(epoch from timestamp '2018-08-20T07:00:00.000Z')
# AND leagues.tier = 'premium'
# ORDER BY matches.match_id NULLS LAST

The query returned 410 matches. After deleting null values( games that had missing data due to disqualifications or disconnections) there were a total of 390 pre-tournament matches and a total of 31 teams competing for the 18 main event spots. 

I then extracted all 390 match_ids from the query and created a dataframe called “pre_ti_match_ids” that would be used in the cleaning and preparation process.


## Modeling

![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.06.00%20PM.png)

![alt text](https://github.com/jonathanklinn/Dota-2-Predicator/blob/master/Images/Screen%20Shot%202018-09-15%20at%2012.07.32%20PM.png)

![alt text] (


## Results




## Future Work


