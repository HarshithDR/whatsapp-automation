from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys

contact_name = input('Enter the name of contact to whoom you want to send message: ')
message_type = input('Do yo want send \n1.Message \n2.Attachment\n3.Emoji')

def website():
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)
    return()

if message_type == str(1):
    text = input('What do you want to send?\n')
    driver = webdriver.Chrome('C:\\Users\\91911\\chromedriver\\chromedriver.exe')
    website()
    test = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    test.send_keys(contact_name)
    test.send_keys(Keys.RETURN)
    testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
    z = 0
    while True:
        # x = random.randint(1000000000000000, 9999999999999999)
        # testinput.send_keys(text + str(x))
        testinput.send_keys(text)
        testinput.send_keys(Keys.RETURN)
        z += 1
        if z == 10:
            exit(0)

else :
    filepath = input('Enter the correct path of file which you want to send: ')
    driver = webdriver.Chrome('C:\\Users\\91911\\chromedriver\\chromedriver.exe')
    website()
    test = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    test.send_keys(contact_name)
    test.send_keys(Keys.RETURN)
    z=0
    while True:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]").click()
        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)
        time.sleep(1)
        driver.find_element_by_xpath('//span[@data-icon="send"]').click()
        z += 1
        if z == 1:
            exit(0)

