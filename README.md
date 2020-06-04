# Data Science Player Success Predictor
* Created a tool that estimates in whether a player will become a pro-bowl caliber prospect based off of college statistics and combine results
* Scraped over a thousand current NFL players from websites using selenium and beautiful soup
* Engineered features to find which college/combine statistics best determine a players likelihood to become a pro-bowler

## Code and Resources Used
**Python Version:** 3.5  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, beatiful soup
## Web Scraping
By navigating to data/collecting_data you will find the web scrapers we used in order to collect 65 features from profootballreference.com. The features we scraped that included college statistics were:
* College Games Played	
* College Receptions	
* College Receiver Yards	
* College Receiver Average	
* College Receiver Touch Downs	
* College Rushing Attempts	
* College Rushing Yards	
* College Rushing Average	
* College Rushing Touch Downs	
* College Scrimage Plays	
* College Scrimage Yards	
* College Scrimage Average	
* College Scrimage Touch Downs		
* College Passing Completions	
* College Passing Attempts	
* College Passing Percentage	
* College Passing Yards	
* College Passing Y/A	
* College Passing AY/A	
* College Passing Touch Downs	
* College Passing Interceptions	
* College Passing Rate

The features we scraped that included combine statistics were:
* Position
* School	
* Weight	
* 40 Yard Time 
* Vertical	
* Bench	
* Broad Jump	
* 3Cone	
* Shuttle	
* Team
*Round	
*Pick	
*Year

## Data Cleaning
After scraping the data, we cleaned the data so that it was usable for our model.

*	Parsed the players name to remove unnecessary characters
*	Split Round, Year, and Pick into unique features 
*	Removed players who were never drafted
* Removed players who did not have a record of college statistics	 
*	Merged various years of a player's college statistics and combine results to fit in a single row
*	Merged a players NFL statistics with their college and combine statistics 
*	Transformed founded date into age of company 

## EDA
Our main concern was the different statistical significance a feature would have on a given position. To account for this, we split our data analysis we seperated the players by position; Quarterback, running back / full back , wide receiver, and tight end. We looked at the correlation between various features in relation to pro-bowls to find most influential features. Our explaoratory data analysis in more detail is linked below as well as a quick snipper of our data analysis.

[Quarterback Data Analysis](https://github.com/DataScience-Proj-MH/NFL_Success/blob/master/Quarterback%20analysis.ipynb) <br>
![40 Yard chart](images/40yd.png) <br>
[Tight End Data Analysis](https://github.com/DataScience-Proj-MH/NFL_Success/blob/master/TE_analysis.ipynb) <br>
![40 Yard chart](images/graphh.png)
[Wide Receiver Data Analysis](google.com) <br>
[Running Back Data Analysis](google.com) <br>
