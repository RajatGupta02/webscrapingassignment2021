from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os
import linecache

options= webdriver.ChromeOptions()
options.headless=True

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)

contest_no=input()

int(contest_no)
driver.get("https://codeforces.com/contest/"+contest_no)

os.mkdir(contest_no)
os.chdir(contest_no)

driver.maximize_window()
index=2
while True:
    
    try:
      problem=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[2]/div[6]/table/tbody/tr[{}]/td[1]/a').format(index))
      problem_name=problem.text
      problem.click()
      
      os.mkdir(problem_name)
      
      
      main_element_class=driver.find_element_by_xpath('//*[@id="pageContent"]/div[3]')
      
      S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
      driver.set_window_size(S('Width'),S('Height'))                                                                                                                 
      main_element_class.screenshot(('./{}/problem.png').format(problem_name))
      

      
      listofIO = [el.text for el in driver.find_elements_by_tag_name("pre")]
      
      inp=listofIO[0::2]
      out=listofIO[1::2]
      
      
      i=0
      for listitem in inp:
          with open("./{}/input{}.txt".format(problem_name,i+1), "w") as f:
             f.write('%s' %listitem)
             i+=1
        
      j=0
      for listitem in out:
         with open("./{}/output{}.txt".format(problem_name,j+1), "w") as f:
             f.write('%s' %listitem)
             j+=1
      
      driver.back()
      time.sleep(1)
      index+=1
      
    except :
        break  

    
   

    
    




