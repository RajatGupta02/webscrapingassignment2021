from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os
import sys
import linecache

options= webdriver.ChromeOptions()
options.headless=True

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)

x=int(sys.argv[1])
driver.get("https://codeforces.com/contests")
time.sleep(2)

contest_index=2



while contest_index <= x+1:
   contest=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[1]/div[2]/div[1]/div[6]/table/tbody/tr[{}]/td[1]/a[1]').format(contest_index))

   contest_data=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[1]/div[2]/div[1]/div[6]/table/tbody/tr[{}]/td[1]').format(contest_index)).text
   
   enter_index=contest_data.index("Enter")
   contest_name=contest_data[0:enter_index-1]
   os.mkdir('./{}'.format(contest_name))
   
   contest.click()
   time.sleep(1)

   index=2
   while True:
    
    try:
      problem=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[2]/div[6]/table/tbody/tr[{}]/td[1]/a').format(index))
      problem_name=problem.text
      problem.click()
      time.sleep(2)
      
      os.mkdir('./{}/{}'.format(contest_name, problem_name))
      
      
      main_element_class=driver.find_element_by_xpath('//*[@id="pageContent"]/div[3]')
      
      S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
      driver.set_window_size(S('Width'),S('Height'))                                                                                                                 
      main_element_class.screenshot(('./{}/{}/problem.png').format(contest_name,problem_name))
      

      
      listofIO = [el.text for el in driver.find_elements_by_tag_name("pre")]
      
      inp=listofIO[0::2]
      out=listofIO[1::2]
      
      
      i=0
      for listitem in inp:
          with open("./{}/{}/input{}.txt".format(contest_name,problem_name,i+1), "w") as f:
             f.write('%s' %listitem)
             i+=1
        
      j=0
      for listitem in out:
         with open("./{}/{}/output{}.txt".format(contest_name,problem_name,j+1), "w") as f:
             f.write('%s' %listitem)
             j+=1
      
      driver.back()
      time.sleep(1)
      index+=1
      
    except :
        break
   contest_index+=1
   driver.back()

print("Successfully fetched contests")
