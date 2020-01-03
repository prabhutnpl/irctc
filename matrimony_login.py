import time

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import [TheNameOfTheExceptionClass]


binary = FirefoxBinary('D:/ProgramFiles/MozillaFirefox/firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get('https://www.tamilmatrimony.com')

#login =driver.find_element_by_xpath('//*[@id="open_loginpp"]').click()

#username =driver.find_element_by_css('html body#close center div#loginpopup.loginoverlay div.loginpopup form div.paddt5.txt-left input#ID.hp-txtBox')

#username.send_keys('M5468781')


#password =driver.find_element_by_xpath('//*[@id="PASSWORD"]').click()

#password.send_keys('ahaniniyal')

time.sleep(60)

next =driver.find_element_by_xpath('/html/body/center/div/div/div/div/div[3]/div/div/ul/div[1]/li[4]/div/div[1]/a').click()
time.sleep(10)
profile =driver.find_element_by_xpath('//*[@id="smartignore_2"]').click()

nextt=driver.find_element_by_xpath('//*[@id="NxtPro"]').click()

