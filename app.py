#USAGE python app.py -u [@USERNAME] -p [PASSWORD]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required=True,
	help="your twitter username")
ap.add_argument("-p", "--password", required=True,
    help="your twitter password")
ap.add_argument("-k", "--keyword", required=True,
    help="your twitter keywords, Posts to like")
args = vars(ap.parse_args())    

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(30)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twiter.com/search?q='+hashtag+'&src=typd')
        time.sleep(10)
        for i in range(0,1):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(10)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com'+link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(30)

selorm = TwitterBot(args["username"], args["password"])
selorm.login()
selorm.like_tweet(args["username"])
