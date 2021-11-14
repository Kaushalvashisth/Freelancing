import time
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': r'D:\Downloads\test',
         "download.prompt_for_download": False, }
options.add_experimental_option('prefs', prefs)

#additional for no detection
#user_agent=""
options.headless = False
#options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("user-data-dir=C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\User Data")


def download(path, x_cord, y_cord, i,link):
    a_path = path[0:len(path)-5]

    driver = webdriver.Chrome(
        executable_path="chromedriver.exe", chrome_options=options)
    driver.get(link)

    time.sleep(random.randint(4, 6))
    action = ActionChains(driver)
    action.move_by_offset(x_cord, y_cord).perform()
    time.sleep(random.randint(1, 3))

    download_a_tag = driver.find_element_by_xpath(a_path)
    ActionChains(driver).move_to_element(download_a_tag).click().perform()

    # if i==2 || i==5 || i ==7 || i ==10:
    #     driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(random.randint(1, 3))
    driver.quit()

dnlink1= 'https://chartink.com/dashboard/66914'
dnlink2= 'https://chartink.com/dashboard/68754'

path_li = [
    "/html/body/div/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[4]/a/span"]
x_cord_li = [290]
ycord_li = [380]
if __name__ == "__main__":
    while True:

        for i in range(len(path_li)):
            download(path_li[i], x_cord_li[i], ycord_li[i], i,dnlink1)
            download(path_li[i], x_cord_li[i], ycord_li[i], i,dnlink2)
        time.sleep(5)


