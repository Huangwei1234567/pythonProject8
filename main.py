#coding=utf-8
from appium import webdriver
from appium.webdriver.common.appiumby import By
import time
desired_caps={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.dajia.view.wcy",
  "appActivity": "com.dajia.view.login.ui.LoginActivity",
  "noReset":True,
  'automationName':'Appium'
}
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
time.sleep(3)
driver.find_element(By.ID,'com.dajia.view.wcy:id/user_name').send_keys('asdasd')
time.sleep(3)
driver.quit()