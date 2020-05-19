import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import io

options = Options()
options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = "C:/Users/matth/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(options = options, executable_path = driver_path)

sites = ['https://nflcombineresults.com/nflcombinedata.php?year=2000&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1999&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1998&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1997&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1996&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1995&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1994&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1993&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1992&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1991&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=1990&pos=&college=']

cols = ['Year', 'Name', 'College', 'POS', 'Height (in)', 'Weight (lbs)', 'Wonderlic', '40 Yard', 'Bench Press', 'Vert Leap (in)', 'Broad Jump (in)', 'Shuttle', '3Cone']
df = pd.DataFrame(columns=cols)
for site in sites:
    driver.get(site)

    # time.sleep(1)

    data = driver.find_element_by_xpath('//*[@id="datatable"]/table/tbody')

    trial = []
    for row in data.find_elements_by_xpath(".//tr"):
        trial.append([td.text for td in row.find_elements_by_xpath(".//td")])

    print(trial)
    df2 = pd.DataFrame(trial, columns=cols)
    df = df.append(df2,ignore_index=True)

print(df)
df.to_csv('NFL-Combine-Results_2.csv')

driver = webdriver.Edge(executable_path="/Users/matth/Downloads/edgedriver_win32/msedgedriver.exe")
driver.get("https://www.pro-football-reference.com/draft/2020-combine.htm")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()

data_element = driver.find_element_by_id('csv_combine')
data = data_element.text
trial = io.StringIO(data)
df = pd.read_csv(trial, sep=",")

driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()

data_element = driver.find_element_by_id('csv_combine')
data = data_element.text
trial = io.StringIO(data)
df2 = pd.read_csv(trial, sep=",")
df = df.append(df2, ignore_index=True)

for i in range(0, 19):
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/span').click()
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()
    data_element = driver.find_element_by_id('csv_combine')
    data = data_element.text
    trial = io.StringIO(data)
    df2 = pd.read_csv(trial, sep=",")
    df = df.append(df2)

print(df)
df.to_csv('pro-football-reference_data.csv')

cols = ['Super Bowl Champ', 'AP MVP', 'AP OROTY', 'AP DROTY', 'AP DPOTY', 'Pass Lead', 'Rush Lead', 'Rec Lead']
years = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
         '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019']
year_counter = 0
df = pd.DataFrame(columns=cols)

driver.get("https://www.pro-football-reference.com/years/1990/allpro.htm")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="meta_more_button"]').click()
stats = driver.find_elements_by_tag_name('p')
awards = []
for stat in stats[2:10]:
    awards.append(stat.text)

print(awards)
df.loc[years[year_counter]] = awards

for i in range(0,29):
    year_counter += 1
    driver.find_element_by_xpath('//*[@id="meta"]/div[2]/div/a[2]').click()
    driver.implicitly_wait(5)
    #driver.find_element_by_xpath('//*[@id="meta_more_button"]').click()
    stats = driver.find_elements_by_tag_name('p')
    awards = []
    for stat in stats[2:10]:
        awards.append(stat.text)
    df.loc[years[year_counter]] = awards

print(df)
df.to_csv('nfl_awards.csv')























NFL STATS FROM 1999 TO 1990
driver.get("https://www.pro-football-reference.com/years/1999/draft.htm")
driver.maximize_window()
df = pd.DataFrame()
driver.find_element_by_xpath('//*[@id="all_drafts"]/div[1]/div/ul/li[2]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="all_drafts"]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
data = driver.find_element_by_id('csv_drafts')
data_text = data.text
temp = io.StringIO(data_text)
df2 = pd.read_csv(temp, sep=",")
df = df.append(df2)

for i in range(0,9):
    driver.find_element_by_xpath('//*[@id="meta"]/div[2]/div/a[1]').click()
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_xpath('//*[@id="all_drafts"]/div[1]/div/ul/li[2]/span').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="all_drafts"]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
    except:
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[1]/span').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()
    data = driver.find_element_by_id('csv_drafts')
    data_text = data.text
    temp = io.StringIO(data_text)
    df2 = pd.read_csv(temp, sep=",")
    df = df.append(df2)

df.to_csv('extended_nfl_career_stats.csv')























This was for all colege defensive stats -  it worked for the most part
defense_links = ['https://www.sports-reference.com/cfb/years/2019-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2018-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2017-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2016-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2015-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2014-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2013-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2012-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2011-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2010-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2009-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2008-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2007-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2006-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2005-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2004-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2003-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2002-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2001-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/2000-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/1999-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/1998-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/1997-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/1996-team-defense.html',
                 'https://www.sports-reference.com/cfb/years/1995-team-defense.html'
                 ]

df = pd.DataFrame()
for link in defense_links:
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get(link)
    driver.maximize_window()
    table_data = driver.find_element_by_xpath('//*[@id="defense"]/tbody')
    almost_links = table_data.find_elements_by_tag_name('a')
    print(almost_links)
    schools = []
    for almost in almost_links:
        schools.append(almost.get_attribute("href"))
    for school in schools:
        driver.get(school)
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 1000)")
        try:
            driver.find_element_by_xpath('//*[@id="all_defense_and_fumbles"]/div[1]/div/ul/li[2]/span').click()
            driver.implicitly_wait(20)
            driver.find_element_by_xpath('//*[@id="all_defense_and_fumbles"]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
        except Exception as e:
            driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[5]/div[1]/div/ul/li[1]/span').click()
            driver.implicitly_wait(5)
            driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[5]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()
        defense_stats = driver.find_element_by_id('csv_defense_and_fumbles')
        df_text = defense_stats.text
        temp = io.StringIO(df_text)
        df2 = pd.read_csv(temp, sep=",")
        df = df.append(df2)

df.to_csv('College_defense.csv')
print(df)

























## RECEIVING
df = pd.DataFrame()
driver.get("https://www.sports-reference.com/cfb/years/2019-receiving.html")
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
passing_stats = driver.find_element_by_id('csv_receiving')
ps_text = passing_stats.text
temp = io.StringIO(ps_text)
df2 = pd.read_csv(temp, sep=",")
df = df.append(df2)

for i in range(0,25):
    driver.find_element_by_xpath('//*[@id="meta"]/div/div/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/span').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
    passing_stats = driver.find_element_by_id('csv_receiving')
    ps_text = passing_stats.text
    temp = io.StringIO(ps_text)
    df2 = pd.read_csv(temp, sep=",")
    df = df.append(df2)

df.to_csv('College_stats_receiving.csv')


## RUSHING
df = pd.DataFrame()
driver.get("https://www.sports-reference.com/cfb/years/2019-rushing.html")
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
passing_stats = driver.find_element_by_id('csv_rushing')
ps_text = passing_stats.text
temp = io.StringIO(ps_text)
df2 = pd.read_csv(temp, sep=",")
df = df.append(df2)

for i in range(0,25):
    driver.find_element_by_xpath('//*[@id="meta"]/div/div/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/span').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
    passing_stats = driver.find_element_by_id('csv_rushing')
    ps_text = passing_stats.text
    temp = io.StringIO(ps_text)
    df2 = pd.read_csv(temp, sep=",")
    df = df.append(df2)

df.to_csv('College_stats_rushing.csv')

# PASSING

df = pd.DataFrame()
driver.get("https://www.sports-reference.com/cfb/years/2019-passing.html")
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
passing_stats = driver.find_element_by_id('csv_passing')
ps_text = passing_stats.text
temp = io.StringIO(ps_text)
df2 = pd.read_csv(temp, sep=",")
df = df.append(df2)

for i in range(0,25):
    driver.find_element_by_xpath('//*[@id="meta"]/div/div/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/span').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
    passing_stats = driver.find_element_by_id('csv_passing')
    ps_text = passing_stats.text
    temp = io.StringIO(ps_text)
    df2 = pd.read_csv(temp, sep=",")
    df = df.append(df2)

df.to_csv('College_stats_passing.csv')



driver.get("https://www.pro-football-reference.com/years/2000/draft.htm")
test = driver.find_elements_by_tag_name("a")
links = []
for t in test:
    links.append(str(t.get_attribute("href")))

cstats = []
print(links)
for link in links:
    if link.__contains__("cfb"):
        cstats.append(link)
cstats.pop(0)
print(cstats)

names = []
df = pd.DataFrame()
for link in cstats:
    driver.get(link)
    try:

        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/span').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
        collegestats = driver.find_element_by_id('csv_defense')
        cs = collegestats.text
        temp = io.StringIO(cs)
        df2 = pd.read_csv(temp, sep=",")
        df = df.append(df2)
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[2]/span').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[2]/div/ul/li[4]/button')
        collegestats = driver.find_element_by_id('csv_scoring')
        cs = collegestats.text
        temp = io.StringIO(cs)
        df2 = pd.read_csv(temp, sep=",")
        df = df.append(df2)
        names.append(driver.find_element_by_xpath('//*[@id="meta"]/div/h1').text)
    except:
        continue

for link in links:
    print(link)
    if check in link:
        print("YES")

    driver.find_element_by_link_text(t.text).click()
    print(t.id)
    driver.execute_script("window.history.go(-1)")








































sites_1 = ["https://www.pro-football-reference.com/years/2002/draft.htm",
           "https://www.pro-football-reference.com/years/2003/draft.htm",
           "https://www.pro-football-reference.com/years/2005/draft.htm",
           "https://www.pro-football-reference.com/years/2006/draft.htm",
           "https://www.pro-football-reference.com/years/2007/draft.htm",
           "https://www.pro-football-reference.com/years/2009/draft.htm",
           "https://www.pro-football-reference.com/years/2010/draft.htm",
           "https://www.pro-football-reference.com/years/2011/draft.htm",
           "https://www.pro-football-reference.com/years/2012/draft.htm",
           "https://www.pro-football-reference.com/years/2015/draft.htm",
           "https://www.pro-football-reference.com/years/2018/draft.htm",
           "https://www.pro-football-reference.com/years/2019/draft.htm",
         ]
sites_2 = ["https://www.pro-football-reference.com/years/2004/draft.htm",
           "https://www.pro-football-reference.com/years/2008/draft.htm",
           "https://www.pro-football-reference.com/years/2013/draft.htm",
           "https://www.pro-football-reference.com/years/2014/draft.htm",
           "https://www.pro-football-reference.com/years/2016/draft.htm",
           "https://www.pro-football-reference.com/years/2017/draft.htm",
           ]

df = pd.DataFrame()
for site in sites_2:
    driver = webdriver.Chrome(options = options, executable_path = driver_path)
    driver.get(site)
    driver.maximize_window()
    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[1]/span').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()
    draft_elements = driver.find_element_by_id('csv_drafts')
    draft = draft_elements.text
    temp = io.StringIO(draft)
    df2 = pd.read_csv(temp, sep=",")
    df = df.append(df2)

temp = pd.read_csv('Nfl-career-stats.csv')
temp = temp.append(df, ignore_index=True)
temp.to_csv('Nfl-career-stats-final.csv')
THIS WORKS FOR ALL SITES IN SITE 1 PLUS 00 AND 01
driver = webdriver.Chrome(options = options, executable_path = driver_path)
driver.get("https://www.pro-football-reference.com/years/2000/draft.htm")
driver.find_element_by_xpath('//*[@id="all_drafts"]/div[1]/div/ul/li[2]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="all_drafts"]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()

draft_elements = driver.find_element_by_id('csv_drafts')
draft = draft_elements.text
temp = io.StringIO(draft)
df = pd.read_csv(temp, sep=",")
print(df)

driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get("https://www.pro-football-reference.com/years/2001/draft.htm")
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[1]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()

draft_elements = driver.find_element_by_id('csv_drafts')
draft = draft_elements.text
temp = io.StringIO(draft)
df2 = pd.read_csv(temp, sep=",")
df = df.append(df2)
for site in sites_1:
    driver = webdriver.Chrome(options = options, executable_path = driver_path)
    driver.get(site)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="all_drafts"]/div[1]/div/ul/li[2]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="all_drafts"]/div[1]/div/ul/li[2]/div/ul/li[4]').click()

    draft_elements = driver.find_element_by_id('csv_drafts')
    draft = draft_elements.text
    temp = io.StringIO(draft)
    df2 = pd.read_csv(temp, sep=",")
    df = df.append(df2)



df.to_csv('Nfl-career-stats.csv')









driver = webdriver.Edge(executable_path="/Users/matth/Downloads/edgedriver_win32/msedgedriver.exe")
sites = ['https://nflcombineresults.com/nflcombinedata.php?year=2000&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2001&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2002&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2003&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2004&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2005&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2006&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2007&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2008&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2009&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2010&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2011&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2012&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2013&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2014&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2015&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2016&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2017&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2018&pos=&college=',
                  'https://nflcombineresults.com/nflcombinedata.php?year=2019&pos=&college=',]

cols = ['Year', 'Name', 'College', 'POS', 'Height (in)', 'Weight (lbs)', 'Wonderlic', '40 Yard', 'Bench Press', 'Vert Leap (in)', 'Broad Jump (in)', 'Shuttle', '3Cone']
df = pd.DataFrame(columns=cols)
for site in sites:
    driver.get(site)

    # time.sleep(1)

    data = driver.find_element_by_xpath('//*[@id="datatable"]/table/tbody')

    trial = []
    for row in data.find_elements_by_xpath(".//tr"):
        trial.append([td.text for td in row.find_elements_by_xpath(".//td")])

    # print(trial)
    df2 = pd.DataFrame(trial, columns=cols)
    df = df.append(df2,ignore_index=True)

print(df)
df.to_csv('NFL-Combine-Results.csv')

driver = webdriver.Edge(executable_path="/Users/matth/Downloads/edgedriver_win32/msedgedriver.exe")
driver.get("https://www.pro-football-reference.com/draft/2020-combine.htm")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()

data_element = driver.find_element_by_id('csv_combine')
data = data_element.text
trial = io.StringIO(data)
df = pd.read_csv(trial, sep=",")

driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()

data_element = driver.find_element_by_id('csv_combine')
data = data_element.text
trial = io.StringIO(data)
df2 = pd.read_csv(trial, sep=",")
df = df.append(df2, ignore_index=True)

for i in range(0, 19):
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/span').click()
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()
    data_element = driver.find_element_by_id('csv_combine')
    data = data_element.text
    trial = io.StringIO(data)
    df2 = pd.read_csv(trial, sep=",")
    df = df.append(df2)

print(df)
df.to_csv('pro-football-reference_data.csv')