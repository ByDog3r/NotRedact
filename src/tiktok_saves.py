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
sleep(5)

saved_item = driver.find_element(
    By.XPATH, '//*[contains(@class, "css-1wncxfu-PFavorite")]'
)
action.move_to_element(saved_item).click().perform()
sleep(3)

saved_items = driver.find_elements(By.XPATH, '//div[@data-e2e="favorites-item-list"]')

video = saved_items[0].find_element(By.XPATH, ".//a")
action.move_to_element(video).click().perform()
sleep(5)

count = 0
while True:
    try:
        like_button = driver.find_element(
            By.XPATH, '//strong[@data-e2e="undefined-count"]'
        )
        action.move_to_element(like_button).click().perform()
        count += 1
        print(f"Save quitado del video {count}")
        sleep(0.5)

        next_video = driver.find_element(By.XPATH, '//button[@data-e2e="arrow-right"]')
        action.move_to_element(next_video).click().perform()
        sleep(2)
        # sleep(random.uniform(3, 7))

    except Exception as e:
        print("No más videos o error:", e)
        break

driver.quit()
