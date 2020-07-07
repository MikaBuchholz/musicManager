import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
import time
import os
import shutil
import glob

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.170"}
driver = webdriver.Firefox()

class get_file:
    def __init__(self, link, download_folder, dest_folder):
        self.link = link
        self.download_folder = download_folder
        self.dest_folder = dest_folder

       
    def var_setup(self):
        download_link = "https://ontiva.com/en"
        page = requests.get(download_link, headers=headers)
        driver.get(download_link)

    def link_input_field(self, driver):
        time.sleep(1)
        link_field = driver.find_element_by_id("convertform-video_link-selectized")
        link_field.send_keys(self.link)

    def start_now_button_presser(self, driver):
        start_button = driver.find_element_by_class_name("btn")
        start_button.click()

    def select_audio(self, driver):
        audio_button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div[2]/ul/li[2]/a")
        audio_button.click()

    def download_button_clicker(self, driver):
        time.sleep(11)
        download_button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[4]/td[4]/a")
        download_button.click()

        time.sleep(2)
        Controller().press(Key.down)

        time.sleep(1)
        Controller().press(Key.enter)

    def file_move(self):
        time.sleep(5)
        path = self.download_folder
        os.chdir(path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        destination = self.dest_folder
        dest = shutil.move(files[-1], destination)

    def start_function(self):
            self.var_setup()
            self.link_input_field(driver)
            self.start_now_button_presser(driver)
            self.select_audio(driver)
            self.download_button_clicker(driver)
            self.file_move()



