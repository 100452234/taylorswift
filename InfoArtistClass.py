from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sqlparse


# Class to store information about one artist
class InfoArtist:
    def __init__(self, name="", wiki_report="", concert_upcoming=[]):
        self.name = name
        self.wiki_report = wiki_report
        self.concert_upcoming = concert_upcoming

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_wiki_report(self):
        driver = webdriver.Chrome()
        driver.get('https://en.wikipedia.org/wiki/Taylor_Swift')

        # search_query = driver.find_element(By.NAME, 'q')
        # search_query.send_keys(self.name + ' wikipedia')
        # search_query.send_keys(Keys.RETURN)

        # wiki_url = driver.find_element(By.CLASS_NAME, 'iUh30').text.replace(' › ', '/')
        # driver.get(wiki_url)

        self.wiki_report = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[3]').text

    def get_wiki_report(self):
        return self.wiki_report

    def set_concert_report(self):
        driver = webdriver.Chrome()
        driver.get('https://www.taylorswift.com/tour/')

        query = driver.find_element(By.CLASS_NAME, 'view-events')
        elements = query.find_elements(By.XPATH, './/*')

        out = []
        for elem in elements:
            data = elem.text.split('\n')
            if len(data) == 5:
                print(data)
                concert_data = {'date': data[0], 'stadium': data[1], 'place': data[2]}
                out.append(concert_data)

        self.concert_upcoming = out

    def get_concert_report(self):
        return self.concert_upcoming

    def create_json(self):
        print(self.name)

