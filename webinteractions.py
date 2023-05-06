import json
import time
import smtplib
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

accounts = {
  "instagramUsername": "6476738000",
  "instagramPassword": "Globie123",
  "autologin": True,
  "mutedusers": ["Ahnenerbe Cafe", "OG Gangsters"],
  "mutereels": True,
}

chrome_options = Options()
chrome_options.add_argument("--headless=new")  # remove this line to debug browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/direct/inbox/")
username = accounts['instagramUsername']
password = accounts['instagramPassword']
mutedusers = accounts['mutedusers']


def login():
    actions = ActionChains(driver)
    print("logging in: step 1/3\r", end='', flush=True)
    actions.pause(3)  # required for instagram to load properly
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(username)
    actions.send_keys(Keys.TAB)
    actions.send_keys(password)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    print("logging in: step 2/3\r", end='', flush=True)
    actions.pause(5)  # required for instagram to load properly
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    print("logging in: step 3/3\r", end='', flush=True)
    actions.pause(2)  # required for instagram to load properly
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print("logged in\r", end='', flush=True)


def checkmsgs():
    print("checking messages")
    new_msg_span_class = "_aacl _aaco _aacw _aacx _aad7"
    new_msg_user_span_class = "x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"
    driver.refresh()
    time.sleep(6)  # required for instagram to load properly

    spans_arr = driver.find_elements(By.TAG_NAME, "span")
    users = []
    msgs = []
    print("sorting spans")
    for i in spans_arr:
        if i.get_attribute("class") == new_msg_user_span_class:
            users.append(i.text)

        if i.get_attribute("class") == new_msg_span_class:
            msgs.append(i.text)

    filtered = []
    n = 0
    print("filtering")
    while n < len(users):
        filtered.append([users[n], msgs[n]])
        n += 1
    print("sending")
    return filtered

def exitweb():
    driver.quit()

if accounts["autologin"]:
    login()
