import json
import time
import smtplib
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class dmstagram:
    def __init__(self, username, password, mutedusers):

        self.accounts = {
          "instagramUsername": username,
          "instagramPassword": password,
          "autologin": True,
          "mutedusers": mutedusers,
          "mutereels": False,
        }


        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless=new")
        self.ser = Service(r"C:\Users\Jonah D'Monte\Documents\DMstagram\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.ser, options=self.chrome_options)
        self.driver.get("https://www.instagram.com/direct/inbox/")
        self.username = self.accounts['instagramUsername']
        self.password = self.accounts['instagramPassword']
        self.mutedusers = self.accounts['mutedusers']
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless=new")


    def login(self):
        self.actions = ActionChains(self.driver)
        self.actions.pause(3)  # required for instagram to load properly
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(self.username)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(self.password)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.ENTER)
        self.actions.pause(5)  # required for instagram to load properly
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.ENTER)
        self.actions.pause(2)  # required for instagram to load properly
        self.actions.send_keys(Keys.TAB)
        self.actions.send_keys(Keys.ENTER)
        self.actions.perform()

    def autologin(self):
        if self.accounts["autologin"]:
            self.login()

    def msgcheck(self):
        new_msg_span_class = "_aacl _aaco _aacw _aacx _aad7"
        new_msg_user_span_class = "x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"
        self.driver.refresh()
        time.sleep(6)  # required for instagram to load properly
        users = []
        msgs = []
        spans_arr = self.driver.find_elements(By.TAG_NAME, "span")
        try:
            users = [i.text for i in spans_arr if i.get_attribute('class') == new_msg_user_span_class]
            msgs = [i.text for i in spans_arr if i.get_attribute('class') == new_msg_span_class]
        except:
            self.relogin()
            return [['Checkmsgs error occurred', 'Relogin attempted']]

        filtered = []
        n = 0
        while n < len(users):
            try:
                if not (users[n] in self.accounts["mutedusers"]):
                    # or (msgs[n] == "Sent you a message" and accounts["mutereels"] == True) or (msgs[n] == "Sent a post " and accounts["mutereels"] == True)
                    if msgs[n] == "Sent you a message":
                        filtered.append([users[n], "Reel"])
                    elif msgs[n] == "Sent a post":
                        filtered.append([users[n], "Post"])
                    else:
                        filtered.append([users[n], msgs[n]])
            except:
                self.relogin()
                return [['Checkmsgs error occurred', 'Relogin attempted']]
            n += 1
        return filtered

    def respond(self, user, msg):
        new_msg_user_span_class = "x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"
        self.driver.refresh()
        time.sleep(6)
        spans_arr = self.driver.find_elements(By.TAG_NAME, "span")
        try:
            users = [i for i in spans_arr if i.get_attribute('class') == new_msg_user_span_class]
        except:
            self.relogin()
            return 'Respond error occurred, relogin attempted'

        for i in users:
            if i.text == user:
                try:
                    i.click()
                    time.sleep(3)
                    sender = ActionChains(self.driver)
                    sender.send_keys(msg)
                    sender.send_keys(Keys.ENTER)
                    sender.perform()
                    self.driver.get("https://www.instagram.com/direct/inbox/")
                    return "Response sent!"
                except Exception as e:
                    print("Respond exception. Message still sent, maybe?")
                    print(e)
            else:
                pass



    def relogin(self):
        print("Activating relogin")
        self.driver.quit()
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.instagram.com/direct/inbox/")
        self.login()
        return 'Relogin complete'

