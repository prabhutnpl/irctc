#login into irctc via chrome browser using python, selenium and webdriver-chromedriver

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
 
driver = webdriver.Chrome("E:/py_project/login/chromedriver_windows.exe")
#launch irctc website
launch_webstie=driver.get('https://www.irctc.co.in/nget/train-search')
#maximize window to get all menu options 
driver.set_window_size(1024, 600)
driver.maximize_window()
#login into into irctc
login = driver.find_element_by_id('loginText').click()
#enter user id and password
irctc_userid='pprabhutnp'
irctc_password='plc685'
#userid
userid = driver.find_element_by_id('userId')
userid.send_keys(Keys.CONTROL, 'a')
userid.send_keys(Keys.BACKSPACE)
userid.send_keys(irctc_userid)
#password
password = driver.find_element_by_id('pwd')
password.send_keys(Keys.CONTROL, 'a')
password.send_keys(Keys.BACKSPACE)
password.send_keys(irctc_password)
time.sleep(8)
#captcha
#captcha = driver.find_element_by_id('nlpAnswer')
#captcha.send_keys('Pehle LIC')
#signin
signin = driver.find_element_by_xpath('//*[@id="login_header_disable"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/button').click()

#######################################################
#input for orgin station

orgin_station='TAMBARAM - TBM'
#select = Select(driver.find_element_by_xpath('//*[@id="origin"]/span/input'))
#select.select_by_visible_text(from_station)
#select.select_by_value('1')
from_input =  driver.find_element_by_xpath('//*[@id="origin"]/span/input')
from_input.send_keys(orgin_station)

#input for destination station

destination_station='PUGALUR - PGR'
tostation_input = driver.find_element_by_xpath('//*[@id="destination"]/span/input')
tostation_input.send_keys(destination_station)

#input for journey date

##############################################################################################################################################################
#input for journey date

journey_date='20-01-2020'

#date0=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]')
#date1 = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar')
#date2=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span')
#date3=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span')
date=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input')
date.send_keys("\n")

#clear the date field and enter the input date values
#ActionChains(driver).move_to_element(date).click().double_click()
#ActionChains(driver).move_to_element(date).click().double_click().send_keys(Keys.BACKSPACE).double_click().send_keys(Keys.BACKSPACE).double_click().send_keys(Keys.BACKSPACE).double_click().send_keys(Keys.BACKSPACE).double_click().send_keys(Keys.BACKSPACE).send_keys(journey_date).perform()

#date = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/button/span[1]')
#WebElement element = driver.findElement(By("#divMain > div > app-main-page > div:nth-child(2) > div > div.row > div > div > div.col-xs-12 > div > app-jp-input > div:nth-child(4) > form > div.form-group.col-lg-12.col-md-12.col-sm-12.ui-float-label > p-calendar > span > input"))
#Actions actions = new Actions(driver);

#actions.moveToElement(element).click().perform();
#journey_date = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/button/span[2]').click()
#placeholderss = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]').click()


#webdriver.ActionChains(driver).move_to_element(journey_date ).click(journey_date ).perform()
#journey_date.send_keys(Keys.CONTROL, 'a')
#journey_date.send_keys(Keys.BACKSPACE)
#journey_date.send_keys(journey_date)





