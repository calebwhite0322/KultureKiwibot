
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class KultureBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login")
        time.sleep(3)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(3)

    def search_hashtag(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + hashtag)

    def like_photos(self, amount):
        bot = self.bot
        time.sleep(2)
        bot.find_element_by_class_name('v1Nh3').click()

        i = 1
        while i <= amount:
            time.sleep(4)
            bot.find_element_by_class_name('fr66n').click()
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i += 1


    def task_completed(self):
        bot = self.bot
        print("Task Completed")
        bot.get('https://instagram.com/' + self.username)


insta = KultureBot(input("Enter Username: "), input("Enter Password: "))
print("Logging in...")
insta.login()
insta.search_hashtag(input("Enter Target Hashtag: "))
insta.like_photos(float(input("Number of Likes: ")))
insta.task_completed()