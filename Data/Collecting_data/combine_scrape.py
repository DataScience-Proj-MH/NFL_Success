import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import io

options = Options()
options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = "C:/Users/matth/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("https://www.pro-football-reference.com/draft/2020-combine.htm")
driver.maximize_window()
driver.implicitly_wait(5)

df = pd.DataFrame()

driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()
data = driver.find_element_by_id('csv_combine')
data_text = data.text
trial = io.StringIO(data_text)
df2 = pd.read_csv(trial, sep=",")
df = df.append(df2, ignore_index=True)

for i in range(0,20):
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/span').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="all_combine"]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()
    except:
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div/ul/li[1]/span').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div/ul/li[1]/div/ul/li[4]/button').click()
    data = driver.find_element_by_id('csv_combine')
    data_text = data.text
    trial = io.StringIO(data_text)
    df2 = pd.read_csv(trial, sep=",")
    df = df.append(df2, ignore_index=True)

df.to_csv('first_try.csv')