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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv xuk3077 x1oa3qoh x1nhvcw1
# x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv xuk3077 x1oa3qoh x1nhvcw1
# _aacl _aaco _aacu _aacx _aad6 _aade
class dmstagram:
    def __init__(self, username, password, mutedusers):

        self.accounts = {
          "instagramUsername": username,
          "instagramPassword": password,
          "autologin": True,
          "mutedusers": mutedusers,
          "mutereels": False,
        }

        self.new_msg_span_class = "x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"
        #
        self.new_msg_user_span_class = "x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"
        #
        self.read_msg_span_class = "_aacl _aaco _aacu _aacy _aad7"
        self.read_msg_user_span_class = "x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"
        self.chrome_options = Options()
        #self.chrome_options.add_argument("--headless=new")
        self.ser = Service(r"C:\Users\Jonah D'Monte\Documents\DMstagram\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.ser, options=self.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.instagram.com/direct/inbox/")
        self.username = self.accounts['instagramUsername']
        self.password = self.accounts['instagramPassword']
        self.mutedusers = self.accounts['mutedusers']
        self.msg_spans_arr = []



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
        print(self.driver.current_url)

    def autologin(self):
        if self.accounts["autologin"]:
            self.login()
    def refresh_span_tags(self):
        if self.driver.current_url ==  "https://www.instagram.com/direct/inbox/":
            self.driver.refresh()
        else:
            self.driver.get("https://www.instagram.com/direct/inbox/")
        time.sleep(10)

        refresh_users = [i for i in self.driver.find_elements(By.TAG_NAME, "span") if i.text == "Millia Rage"]
        refresh_msgs = [i for i in self.driver.find_elements(By.TAG_NAME, "span") if i.text == "test"]

        print(refresh_users)
        print(refresh_msgs)
        self.new_msg_user_span_class = refresh_users[0].get_attribute("class")
        self.new_msg_span_class = refresh_msgs[0].get_attribute("class")

    def refresh_msg_spans_arr(self):
        new_msg_span_class = "_aacl _aaco _aacw _aacx _aad7"
        new_msg_span_class = "x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"
        new_msg_user_span_class = "x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"
        new_msg_user_span_class = "x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"
        read_msg_span_class = "_aacl _aaco _aacu _aacy _aad7"
        read_msg_user_span_class = "x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"
        self.refresh_span_tags()
        span_filters = [self.new_msg_span_class, self.new_msg_user_span_class, self.read_msg_span_class, self.read_msg_user_span_class]

        self.msg_spans_arr = [i for i in self.driver.find_elements(By.TAG_NAME, "span") if i.get_attribute("class") in span_filters]


    def msgcheck(self):
        self.refresh_msg_spans_arr()
        users = []
        msgs = []

        try:
            users = [i.text for i in self.msg_spans_arr if i.get_attribute('class') == self.new_msg_user_span_class]
            msgs = [i.text for i in  self.msg_spans_arr if i.get_attribute('class') == self.new_msg_span_class]
        except:
            self.relogin()
            return [['Checkmsgs error occurred', 'Relogin attempted']]

        filtered = []
        n = 0
        print("users")
        print(users)
        print("msgs")
        print(msgs)

        while n < len(users):
            try:
                if not (users[n] in self.accounts["mutedusers"]):
                    # or (msgs[n] == "Sent you a message" and accounts["mutereels"] == True) or (msgs[n] == "Sent a post " and accounts["mutereels"] == True)
                    if msgs[n] == "Sent you a message":
                        filtered.append([users[n], "Sent you a reel"]) # todo implement reel downloading
                    elif msgs[n] == "Sent a post":
                        filtered.append([users[n], "Sent you a post"]) # todo implement post embedding
                    else:
                        filtered.append([users[n], msgs[n]])
            except:
                self.relogin()
                return [['Checkmsgs error occurred', 'Relogin attempted']]
            n += 1
        return filtered

    def respond(self, user, msg, attachments=None):
        self.refresh_msg_spans_arr()

        try:
            users = [i for i in self.msg_spans_arr if i.get_attribute('class') == self.new_msg_user_span_class or i.get_attribute('class') == self.read_msg_user_span_class]
        except:
            self.relogin()
            return 'Respond error occurred, relogin attempted'

        for i in users:
            if i.text == user:
                try:
                    i.click()
                    time.sleep(3)
                    print(self.driver.page_source)
                    print("\n\n\n\n")
                    sender = ActionChains(self.driver)
                    sender.send_keys(msg)
                    sender.send_keys(Keys.ENTER)
                    print(self.driver.page_source)
                    if attachments:
                        pass # todo implement attachment sending
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


