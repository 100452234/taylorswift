from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sqlparse


# Class to store information about one artist
class InfoArtist:
    def __init__(self, name="", wiki_report=""):
        self.name = name
        self.wiki_report = wiki_report

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_wiki_report(self):
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/')

        search_query = driver.find_element(By.NAME, 'q')
        search_query.send_keys(self.name + ' wikipedia')
        search_query.send_keys(Keys.RETURN)

        wiki_url = driver.find_element(By.CLASS_NAME, 'iUh30').text.replace(' › ', '/')
        driver.get(wiki_url)

        self.wiki_report = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[3]').text

    def get_wiki_report(self):
        return self.wiki_report

    def create_db(self):
        print(self.name)

        sql_code = """CREATE TABLE ARTIST(
  NAME VARCHAR2(50),
  INFO VARCHAR2(500),
  CONSTRAINT PK_ARTIST PRIMARY KEY (NAME)
);

CREATE TABLE CONCERT(
    CITY VARCHAR2(50),
    COUNTRY VARCHAR2(50),
    VENUE VARCHAR2(50),
    TICKET_SOLD INT(5),
    TICKET_AVAILABLE INT(5),
    REVENUE FLOAT(4),
    TOUR_NAME VARCHAR2(50)
);
"""

        # Format and save SQL code to a file
        formatted_sql = sqlparse.format(sql_code)
        with open('my_sql_file.sql', 'w') as sql_file:
            sql_file.write(formatted_sql)

