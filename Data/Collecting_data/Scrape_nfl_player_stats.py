from selenium.webdriver import Chrome
import pandas as pd

#load chrome driver
webdriver = 'C:/Users/Hneva/OneDrive/Desktop/ChromeDriver/chromedriver.exe'
driver = Chrome(webdriver)

#list of all the websites to be scraped
URL = ['https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2000&year_max=2000&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2001&year_max=2001&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2002&year_max=2002&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2003&year_max=2003&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2004&year_max=2004&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2005&year_max=2005&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2006&year_max=2006&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2007&year_max=2007&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2008&year_max=2008&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2009&year_max=2009&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2010&year_max=2010&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2011&year_max=2011&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2012&year_max=2012&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2013&year_max=2013&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2014&year_max=2014&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2015&year_max=2015&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2016&year_max=2016&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2017&year_max=2017&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2018&year_max=2018&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ,
       'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=2019&year_max=2019&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&conference=any&show=p&order_by=default' ]
      
#creating column headings for each feature that is being scraped
cols = ['Year' , 'Rnd' , 'Pick' , 'Player' , 'Pos' , 'DrAge' , 'Tm' , 'From' , 'To' , 'AP1' , 'PB' , 'St' , 'CarAV' , 'G' , 'GS' , 'QBrec' , 'Cmp' , 'PassAtt' , 'PassYds' , 'PassTD' , 'Int' , 'RushAtt' , 'RushYds' , 'RushTD' , 'RecRec' , 'RecYds' , 'RecTD' , 'College' , 'College Stats']
rows = [] 
player_stats_df = pd.DataFrame(columns = cols)

for link in URL: #loop through all URL's
    driver.get(link)
    data = driver.find_element_by_xpath('//*[@id="results"]/tbody') #isolate table 
    
    
    for x in data.find_elements_by_xpath('.//tr'): #isolate row
       rows.append([td.text for td in x.find_elements_by_xpath(".//td")]) #isolate specific stats
       
temp_df = pd.DataFrame(rows ,columns=cols) #merge dataframes together
player_stats_df = player_stats_df.append(temp_df , ignore_index=True) 

#export to csv
player_stats_df.to_csv(r'C:\Users\Hneva\OneDrive\Desktop\AI Club Workshops\nfl_player_stats.csv' , index = True)