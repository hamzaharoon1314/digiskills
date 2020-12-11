from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import  Keys
import time

USERNAME = 'Email fo a person who want to login'
PASSWORD = 'Password fo a person who want to login'

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver\chromedriver.exe")
driver.get("https://lms.digiskills.pk/Login.aspx#0")
driver.maximize_window()

user_input = driver.find_element_by_id('txtStudentId')
user_input.send_keys(USERNAME)


password_input = driver.find_element_by_id('txtNewPassword')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('btnLogin')
login_button.click()
time.sleep(6)
driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_lstCourse_ctrl0_btnCourseWebsite').click()")

driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/section[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]').click()

video1 = driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/section[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/table/tbody/tr[2]/td[1]/a")
driver.execute_script("arguments[0].click();", video1)


check = driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/section[2]/div[2]/div/div/div/div[1]/div/div[1]/span").get_attribute("class")
if check != "fa fa-check-circle text-green":
    time.sleep(40)
if check == "fa fa-check-circle text-green":
   nextvideo = driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/section[2]/div[1]/h1/a")
   driver.execute_script("arguments[0].click();", nextvideo)









