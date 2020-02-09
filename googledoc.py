from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('headless')
options.add_argument('window-size=1200x600')
#options.add_argument("--lang=en-GB");
#options.add_argument("start-maximized"); 
#options.add_argument("disable-infobars"); 
options.add_argument("--disable-extensions"); 
options.add_argument("--disable-gpu"); 
#options.add_argument("--disable-dev-shm-usage"); 
options.add_argument("--no-sandbox");
driver = webdriver.Chrome(chrome_options=options)  # Optional argument, if not specified will search path.

driver.get('https://drive.google.com/file/d/1uuDkF4j4H1AI1ot88XdqzwMdvAPhxKN8/view')
path="//*"
#python_menu=driver.find_element_by_xpath(path)
#print(python_menu)
time.sleep(120)
path='/html/body/div[5]/div[2]/div[4]/div[4]/div[1]/div[5]/div[1]'
path="//div[@aria-label='Downloaden']"
print(driver.page_source)
python_menu=driver.find_element_by_xpath(path)
print(python_menu)
python_menu.click()
Whandles = driver.window_handles
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
xpath="//a[@id='uc-download-link']"
python_menu=driver.find_element_by_xpath(xpath)
print(python_menu)
python_menu.click()
