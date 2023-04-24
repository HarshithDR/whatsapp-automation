from selenium import webdriver
import time
import pyautogui
import random

driver = webdriver.Chrome('C:\\Users\\91911\\chromedriver\\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
time.sleep(20)

driver.find_element_by_css_selector('span[title="*********"]').click()#enter name of user in double quotes

while True:
    pyautogui.write('HI')
    pyautogui.press('ENTER')

