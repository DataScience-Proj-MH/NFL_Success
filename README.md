# Data Science Player Draft Round Estimator
* Created a tool that estimates in which round a player will be selected through analyzing their college and combine statistics
* Scraped over a thousand current NFL players from websites using selenium and beautiful soup
* Engineered features to find which college/combine statistics best determine a players likelihood to fall in a specific round

## Code and Resources Used
**Python Version:** 3.5 
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, beautifulsoup

## Web Scraping
By navigating to data/collecting_data you will find the web scrapers we used in order to collect 65 features from profootballreference.com. The features we scraped that included college statistics were:
* College Games Played	
* College Receptions	
* College Recieving Yards	
* College Recieving Average	
* College Receiving Touch Downs	
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
