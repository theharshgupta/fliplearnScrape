from selenium import webdriver
import time
driver = webdriver.Chrome('C:\chromedriver.exe')

urlMain = "https://app.fliplearn.com/login"
driver.get(urlMain)
time.sleep(2)
loginID = driver.find_element_by_xpath('//*[@id="Fname"]')
loginID.send_keys("harshgupta9913")
password = driver.find_element_by_xpath('//*[@id="password-lg1"]')
password.send_keys("harshgupta9913")
driver.find_element_by_xpath('//*[@id="login-bg"]/div/div/div/div/div/div/div/div[1]/div/form/div[3]/div/button').click()
time.sleep(2)
for x in range(0,4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)


for pdfs in driver.find_element_by_class_name('col-md-3 col-sm-4 ng-scope').find_elements_by_class_name('assetNameOthers ng-binding'):
    print(pdfs)






