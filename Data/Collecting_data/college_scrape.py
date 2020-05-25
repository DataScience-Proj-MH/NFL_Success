import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import io

options = Options()
options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = "C:/Users/matth/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=driver_path)
player = pd.read_csv('csv/second.csv')


years = ['2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007',
         '2006', '2005', '2004', '2003', '2002', '2001', '2000']

driver.get('https://www.pro-football-reference.com/draft/2020-combine.htm')
driver.maximize_window()
driver.implicitly_wait(5)

df = pd.DataFrame()

for year in years:
    player_names = player.loc[player['Year'] == int(year), 'Player']
    i = 1
    i_values = []

    while True:
        lookup = '//*[@id="combine"]/tbody/tr[' + str(i) + ']/th/a'
        try:
            temp = driver.find_element_by_xpath(lookup).text
        except:
            if i < 350:
                i += 1
                continue
            break
        if player_names.str.contains(temp).any():
            i_values.append(i)
        i += 1
    for i_curr in i_values:
        lookup_2 = '//*[@id="combine"]/tbody/tr[' + str(i_curr) + ']/td[3]/a'
        element = driver.find_element_by_xpath(lookup_2)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element = driver.find_element_by_xpath(lookup_2).click()
        driver.implicitly_wait(5)
        try:
            driver.find_element_by_xpath('//*[@id="all_rushing"]/div[1]/div/ul/li[2]/span').click()
            driver.implicitly_wait(5)
            driver.find_element_by_xpath('//*[@id="all_rushing"]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
            table = driver.find_element_by_id('csv_rushing')
        except:
            try:
                driver.find_element_by_xpath('//*[@id="all_receiving"]/div[1]/div/ul/li[2]/span').click()
                driver.implicitly_wait(5)
                driver.find_element_by_xpath('//*[@id="all_receiving"]/div[1]/div/ul/li[2]/div/ul/li[4]/button').click()
                table = driver.find_element_by_id('csv_receiving')
            except:
                try:
                    print(driver.find_element_by_xpath('//*[@id="meta"]/div/h1').text + ': NO STATS')
                except:
                    print('NO STATS AT: ' + driver.current_url)
                driver.back()
                driver.implicitly_wait(20)
                continue
        table_text = table.text
        temp_str = io.StringIO(table_text)
        df2 = pd.read_csv(temp_str, sep=",")
        df2.iloc[0, df2.columns.get_loc('Unnamed: 0')] = driver.find_element_by_xpath('//*[@id="meta"]/div/h1').text
        df = df.append(df2)
        driver.back()
        driver.implicitly_wait(20)
    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/a')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').click()
    time.sleep(2)



print(df)
df.to_csv("college2.csv")