from selenium import webdriver
import time
from creds import word
import random
import urllib.request


from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:\chromedriver.exe')

urlMain = "https://app.fliplearn.com/login"
driver.get(urlMain)
time.sleep(2)
loginID = driver.find_element_by_xpath('//*[@id="Fname"]')
loginID.send_keys("harshgupta9913")
password = driver.find_element_by_xpath('//*[@id="password-lg1"]')
password.send_keys(word)
driver.find_element_by_xpath('//*[@id="login-bg"]/div/div/div/div/div/div/div/div[1]/div/form/div[3]/div/button').click()
time.sleep(7)
# to view all the entries
# for x in range(0,4):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)


for pdfs in driver.find_elements_by_class_name('ng-scope'):
    try:
        downloadLink = pdfs.find_element_by_tag_name('a').get_attribute('href')
        response = urllib.request.urlopen(downloadLink)
        with open(str(1)+"document.pdf", "wb") as f:
            f.write(response.read())
    except NoSuchElementException or AttributeError:
        pass

    # print(pdfs.find_element_by_class_name('assetNameOthers ng-binding').text)

# //*[@id="wall_data"]/div/div[1]/div[3]/div[3]/div/div/div/div/div/div[4]/div[1]/div/div/ul/li[3]/a
# //*[@id="wall_data"]/div/div[1]/div[3]/div[1]/div[2]/div/div/div/div/div[4]/div[1]/div/div/ul/li[3]/a
# //*[@id="wall_data"]/div/div[1]/div[3]/div[2]/div/div/div/div/div/div[4]/div[1]/div/div/ul/li[3]/a

