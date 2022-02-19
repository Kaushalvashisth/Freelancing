import time
import random
#import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import datetime 

def chromeSettings():
    options = webdriver.ChromeOptions()
    
    #add ur user agent 
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    
    #to make chrome invisible
    options.headless = True
    
    options.add_argument(f'user-agent={user_agent}')
    
    options.add_argument("--test-type");
    options.add_argument("--no-first-run");
    options.add_argument("--no-default-browser-check");
    options.add_argument("--start-maximized");
    
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    # add path to chrome user data 
    options.add_argument("user-data-dir=C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\User Data")
    return options

def renameFile():
    #path 
    PATH=os.getcwd()+"\\stock_data"
    current_time = datetime.datetime.today().strftime('%Y-%m-%d__%H-%M-%S')
    timestr=current_time+".csv"
    
    for filename in os.listdir(PATH):
        if filename.startswith("NIFTY"):
            org_fp = os.path.join(PATH, filename)
            # rename of file
            new_fp = os.path.join(PATH, "OptionChain_"+timestr)
            os.rename(org_fp, new_fp)
    
def login_once(login_link):
    
    options=chromeSettings()   
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    driver.get(login_link)
    
    #driver.get_screenshot_as_file("login.png") 
    
    # login 
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys('your email for icharts')
    
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys('your password for icharts')
                           
    driver.find_element_by_name("submit").click()
    
#    driver.get_screenshot_as_file("after_login2222.png")
    
def getNiftyPrices(driver):
    niftyPrice=driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/span[2]/span[1]/div/span[2]/span[1]").text
    niftyPrice_chg=driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/span[2]/span[1]/div/span[2]/span[3]").text
    niftyPrice_chg_per=driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/span[2]/span[1]/div/span[2]/span[4]/b").text
#    lot_size=driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/span[2]/span[3]/b").text
    
    print("Nifty Price :",niftyPrice,"\n")
    print("Nifty Price change:",niftyPrice_chg,"\n")
    print("Nifty Price change percentage:",niftyPrice_chg_per,"\n")
#    print(lot_size,"\n")

def getBankNiftyPrices(driver):
    Bank_niftyPrice=driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/span[2]/span[1]/div/span[2]/span[1]").text
    Bank_niftyPrice_chg=driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/span[2]/span[1]/div/span[2]/span[3]").text
    Bank_niftyPrice_chg_per=driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/span[2]/span[1]/div/span[2]/span[4]/b").text
#    lot_size=driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/span[2]/span[3]/b").text
    
    print("Bank Nifty Price :",Bank_niftyPrice,"\n")
    print("Bank Nifty Price change:",Bank_niftyPrice_chg,"\n")
    print("Bank Nifty Price change percentage:",Bank_niftyPrice_chg_per,"\n")
#    print(lot_size,"\n")
    
def download(a_path,download_link):
    options=chromeSettings()
    
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options) 
    # download address
    downloadpath=os.getcwd()+"\\stock_data"
    params={'behavior':'allow', 'downloadPath':downloadpath}
    driver.execute_cdp_cmd('Page.setDownloadBehavior',params)
    
    action = ActionChains(driver)
    time.sleep(random.randint(4, 6))
    
    #sleep
    #driver.get_screenshot_as_file("login.png")    
    #driver.implicitly_wait(10)


    # go to download link 
    driver.implicitly_wait(10)    
    driver.get(download_link)    
    
    #driver.implicitly_wait(10)
    #driver.get_screenshot_as_file("after_login2222.png")
    
    #downloading nifty csv
    download_a_tag = driver.find_element(By.XPATH,a_path)
    print(download_a_tag,"\n")
    action.move_to_element(download_a_tag).click().perform()
    
    #GET nifty prices 
    print("\n\t\t NIFTY CSV DOWNLODED\n")
    getNiftyPrices(driver)
    
    driver.implicitly_wait(10) 
    
    #go to bank nifty 
    dropdown=Select(driver.find_element_by_id("optSymbol"))
    dropdown.select_by_visible_text("BANKNIFTY")
    driver.implicitly_wait(100)
    driver.get_screenshot_as_file("bank.png")
    #downoad bank nifty csv
    
#    driver.implicitly_wait(10) 
#    download_a_tag2 = driver.find_element(By.XPATH,a_path)
#    print(download_a_tag2,"\n")
#    action.move_to_element(download_a_tag2).click().perform()
    
    driver.implicitly_wait(10) 
#    print("\n\t\t BANK NIFTY CSV DOWNLODED\n")
    print("\n\t\t BANK NIFTY DATA \n")
    #GET bank nifty prices
    getBankNiftyPrices(driver)
    driver.get_screenshot_as_file("bank2.png")
        
    
    time.sleep(random.randint(1, 3))
    driver.quit()

# links and paths
login_link='https://options.icharts.in/opt/login.php'
download_link='https://options.icharts.in/opt/OptionChain.php'
path='/html/body/div[1]/form/div[1]/span[1]/div[1]/div/button[2]'


if __name__ == "__main__":
    
    login_once(login_link)
    
    while True:
        download(path,download_link)
        time.sleep(5)


