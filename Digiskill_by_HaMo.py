from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import  Keys
import time
import os, sys
print("Learning Management System", "Automation", "By Hamza Haroon")
print("Downlaod from Github:", "http://bit.ly/Digiskills-Auto", "By Mr.HaaMoo")
print("Source code Available on Github")
print("---------------START PROGRAM---------------")
print("---------------PUT (chromedriver.exe) IN (C:\)---------------")


USERNAME = input('Enter username:')
PASSWORD = input("Enter Password:")
CourseNo = int(input("Enter Course No.(1 or 2)"))
tot = int(input("Enter Total Videos:"))
totvid = tot
Course = CourseNo

if getattr(sys, 'frozen', False):
	chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
	driver = webdriver.Chrome(chromedriver_path)
else:
	driver = webdriver.Chrome()


driver.get("https://lms.digiskills.pk/Login.aspx#0")
driver.maximize_window()

user_input = driver.find_element_by_id('txtStudentId')
user_input.send_keys(USERNAME)


password_input = driver.find_element_by_id('txtNewPassword')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('btnLogin')
login_button.click()

if Course == 1:
    driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_lstCourse_ctrl0_btnCourseWebsite').click()")
else:
    driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_lstCourse_ctrl1_btnCourseWebsite').click()")

driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/section[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]').click()

video1 = driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/section[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/table/tbody/tr[2]/td[1]/a")
driver.execute_script("arguments[0].click();", video1)

while totvid>=1:
    check = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_lblcompletion']").get_attribute("class")
    print(check, "True")
    green = "fa fa-check-circle text-green"
    if check == green:
        print("Green True")
        print("---------------NEXT VIDEO---------------")
        nextvideo = driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbtnNextLessonTop")
        driver.execute_script("arguments[0].click();", nextvideo)
    else:
        print("Green False")
        print("---------------WAIT FOR GREEN TICK---------------")
        time.sleep(40)
        print("---------------NEXT VIDEO---------------")
        nextvideo = driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbtnNextLessonTop")
        driver.execute_script("arguments[0].click();", nextvideo)
    time.sleep(5)
    totvid=totvid-1


print("---------------Automation Completed---------------")
time.sleep(5)
driver.quit()
