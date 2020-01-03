from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("E:/py_project/login/chromedriver.exe")
##############################################################################################################################################################
#launch irctc website
launch_webstie=driver.get('https://www.irctc.co.in/nget/train-search')
##############################################################################################################################################################
#maximize window to get all menu options 
driver.set_window_size(1024, 600)
driver.maximize_window()
##############################################################################################################################################################
orgin_station='TAMBARAM - TBM'
from_input =  driver.find_element_by_xpath('//*[@id="origin"]/span/input')
from_input.send_keys(orgin_station)
##############################################################################################################################################################
#input for destination station

destination_station='ARIYALUR - ALU'
tostation_input = driver.find_element_by_xpath('//*[@id="destination"]/span/input')
tostation_input.send_keys(destination_station)
##############################################################################################################################################################
#input for journey date

journey_date='20-08-2019'

date = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input')
#clear the date field and enter the input date values

ActionChains(driver).move_to_element(date).click().double_click().send_keys(Keys.BACKSPACE).double_click().send_keys(Keys.BACKSPACE).double_click().send_keys(Keys.BACKSPACE).double_click().send_keys(Keys.BACKSPACE).double_click().send_keys(Keys.BACKSPACE).send_keys(journey_date).perform()
##############################################################################################################################################################
#select the journey class details

journey_class = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/label').click()

#All_Classes = li[1]
#Anubhuti_Class = li[2]
#AC_First_Class  = li[3]
#Exec._Chair_Car  = li[4]
#AC_2_Tier  = li[5]
#First_Class  = li[6]
#AC_3_Tier  = li[7]
#AC_3_Economy  = li[8]
#AC_Chair_car  = li[9]
#Sleeper  = li[10]
#Second_Sitting  = li[11]
journey_class_name = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/div[4]/div/ul/li[11]').click()

##############################################################################################################################################################
#find the trains
find_trains=driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button').click()

##############################################################################################################################################################

#Quota

time.sleep(8) # sleep time to load all the ads
#to hide all ads by finding the iframe tag and hiding it
all_iframes = driver.find_elements_by_tag_name("iframe")
if len(all_iframes) > 0:
    print("Ad Found\n")
    driver.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)
    print('Total Ads: ' + str(len(all_iframes)))
else:
    print('No frames found')

driver.execute_script("window.scrollTo(0, 60)") 
quota_dropdown = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/p-dropdown/div/div[3]').click()
quota =driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/p-dropdown/div/div[4]/div/ul/li[5]/span').click()

#Check availability
#availability = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[4]/div/div[1]/app-train-avl-enq/div[2]/div[1]/div[3]/div[2]/div').click()

#Train Number
vaigai = 12635
pallavan = 12605

#slider

slider = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[1]/div[1]/div[2]/div[7]/div/p-slider/div/span[2]');
move = ActionChains(driver)
height= slider.size['height']
width=slider.size['width']
print(width)
move.click_and_hold(slider).move_by_offset(100 * 34 / 100, 0).release().perform()


aval = driver.find_element_by_id('check-availability')

print(aval.text)
