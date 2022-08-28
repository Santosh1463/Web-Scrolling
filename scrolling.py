from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path=r'C:\Users\santo\chromedriver.exe')
driver.get("https://en.wikipedia.org/wiki/India")
driver.maximize_window()
#driver.execute_script("window.scrollBy(0,2000)","")
#element = driver.find_element("xpath", '/html/body/div[3]/div[3]/div[5]/div[1]/h2[4]/span')
#driver.execute_script("arguments[0].scrollIntoView()",element)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(4)