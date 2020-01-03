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

time.sleep(6)


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

journey_date='03-01-2020'


date=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input')
date.send_keys(Keys.SPACE)
date.send_keys(Keys.CONTROL, 'a')
date.send_keys(Keys.BACKSPACE)
date.send_keys(journey_date)
date.send_keys("\n")


#to wait for 6 sec so that the advertisements on the page will load fully or else Driver will not find the elements as elements will load after advertisements 
time.sleep(6)

#scrool the window down 300 y-axis so that the Quota select pop-up will display in the hanging mode, or else quota selector will click on advertisements on the page
 
driver.execute_script("window.scrollTo(0, 300)")

#Quota

quota0=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/p-dropdown/div/div[3]/span').click()
quota=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/p-dropdown/div/div[4]/div/ul/li[5]').click()

#select the journey class details



select=Select(driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[4]/div/div[1]/app-train-avl-enq/div[2]/div[1]/div[3]/div[1]/form/select'))

select.select_by_visible_text('Sleeper (SL)')
#list of class
#AC First Class (1A)
#AC 2 Tier (2A)
#AC 3 Tier (3A)
#Sleeper (SL)
#Second Sitting (2S)
#check the avilability

avilability=driver.find_element_by_xpath('//*[@id="check-availability"]').click()



driver.execute_script("window.scrollTo(0, 100)")
#click book now

time.sleep(10)

book_now=driver.find_element_by_xpath('//*[@id="ui-panel-0-content"]/div/div/div/table/tbody/tr/td/div/div[3]/button').click()

time.sleep(10)

#scrool the window down 400 y-axis so that the Quota select pop-up will display in the hanging mode, or else quota selector will click on advertisements on the page
 
driver.execute_script("window.scrollTo(0, 400)")

#passenger details
#passenger_name

person_name='PRABHAKARAN'
passenger_name=driver.find_element_by_xpath('//*[@id="psgn-name"]')
passenger_name.click()
passenger_name.send_keys(person_name)
#passenger age

age='27'
person_age=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[2]/input')
person_age.click()
person_age.send_keys(age)
#passenger gender

selectGender=Select(driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]/select'))
selectGender.select_by_visible_text('Male')

driver.execute_script("window.scrollTo(0, 400)")

#consider for auto upgradtion

auto_upgradtion=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[5]/div/div/label').click()

#wait time to enter the captcha

time.sleep(8)


#payment via BHIM UPI

payment_UPI=driver.find_element_by_xpath('//*[@id="2"]').click()

time.sleep(8)

#click booking

booking=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[6]/div/button[2]').click()

##################################################################

#review booking

time.sleep(8)

driver.execute_script("window.scrollTo(0,800)")

review_booking=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-review-booking/div/div[4]/div/div[2]/div[2]/div[1]/div[6]/div/div/button[2]').click()

time.sleep(15)

 


