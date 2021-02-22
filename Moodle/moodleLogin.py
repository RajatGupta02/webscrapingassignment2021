from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import linecache
PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
try:
    form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )
except:
    driver.quit()

userid= driver.find_element_by_id("username")
userid.send_keys(input())

passid=driver.find_element_by_id("password")
print("Please enter your password: ")
passid.send_keys(input())

driver.find_element_by_name("valuepkg3").clear()
captcha=driver.find_element_by_name("valuepkg3")

logintext = driver.find_element_by_id("login").text


if "add" in logintext:
    add_index= logintext.index("add")
    tosolve=logintext[add_index+4:-38]
    splitarr= tosolve.split("+")
    for i in range(0, len(splitarr)): 
        splitarr[i] = int(splitarr[i])
    
    captcha.send_keys(splitarr[0]+splitarr[1])


elif "subtract" in logintext:
    sub_index= logintext.index("subtract")
    tosolve=logintext[sub_index+9:-38]
    splitarr= tosolve.split("-")
    for i in range(0, len(splitarr)): 
        splitarr[i] = int(splitarr[i])
    
    captcha.send_keys(splitarr[0]-splitarr[1])


elif "first value" in logintext:
    first_index= logintext.index("first value")
    tosolve=logintext[first_index+12:-38]
    splitarr= tosolve.split(",")
    for i in range(0, len(splitarr)): 
        splitarr[i] = int(splitarr[i])
    
    captcha.send_keys(splitarr[0])       


elif "second value" in logintext:
    second_index= logintext.index("second value")
    tosolve=logintext[second_index+13:-38]
    splitarr= tosolve.split(",")
    for i in range(0, len(splitarr)): 
        splitarr[i] = int(splitarr[i])
    
    captcha.send_keys(splitarr[1])       

button=driver.find_element_by_id("loginbtn")
button.click()

print("Login Successful!")




