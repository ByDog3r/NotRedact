from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from json import load

config_user = load(open("src/config.json"))
USER_ID = config_user["TIKTOK_USER"]
PSWD = config_user["TIKTOK_PSWD"]


opts = Options()
opts.add_argument(
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Safari/605.1.15"
)
opts.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opts)
action = ActionChains(driver)

driver.get("https://www.tiktok.com/login/phone-or-email/email")
sleep(3)

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(USER_ID)

password_input = driver.find_element(By.XPATH, '//input[@placeholder="Contraseña"]')
password_input.send_keys(PSWD)
password_input.send_keys(Keys.RETURN)

# Solving captcha manually
sleep(15)

driver.get("https://www.tiktok.com/@" + USER_ID)

followers_button = driver.find_element(By.XPATH, '//span[@data-e2e="following"]')
action.move_to_element(followers_button).click().perform()
sleep(5)


followers = driver.find_elements(By.XPATH, '//button[@data-e2e="follow-button"]')
count = 0
for follower in followers:
    action.move_to_element(follower).click().perform()
    count += 1
    print(f"follow quitado del video {count}")
    sleep(3)
driver.quit()
