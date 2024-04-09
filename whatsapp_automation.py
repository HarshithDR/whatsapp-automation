from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

contact_name = input('Enter the name of contact to whoom you want to send message: ')
message_type = input('Do yo want send \n1.message \n2.emoji\n')

def website():
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)
    return()

if message_type == str(1):
    text = input('What do you want to send?\n')
    number = input('How many times you want to send this message: ')
    driver = webdriver.Chrome('C:\\Users\\91911\\chromedriver\\chromedriver.exe')
    website()
    test = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    test.send_keys(contact_name)
    test.send_keys(Keys.RETURN)
    testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
    z = 0
    while True:
        testinput.send_keys(text)
        testinput.send_keys(Keys.RETURN)
        z += 1
        if z == int(number):
            exit(0)
        if z == 100:
            exit(0)

else:
    print('which emoji you want to send?')
    emoji = int(input('Which one do you want to send? \n 1.Toungue emoji \n 2.Eye emoji \n 3.Kiss emoji \n 4.Hearts emoji \n 5.Eye hearts \n'))
    number = int(input('How many times you want to send this message: '))
    driver = webdriver.Chrome('C:\\Users\\91911\\chromedriver\\chromedriver.exe')
    website()
    test = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    test.send_keys(contact_name)
    test.send_keys(Keys.RETURN)
    whatsappemoji = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[1]/div[1]')
    whatsappemoji.click()
    # emojilist = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[3]/span')
    # emojilist.click()
    if emoji == 1:
        z = 0
        while True:
            emoji_1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[7]/div/div/div/span[9]')
            emoji_1.click()
            testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            testinput.send_keys(Keys.RETURN)
            time.sleep(0.2)
            z += 1
            if z == number:
                exit(0)
            if z == 100:
                exit(0)
    if emoji == 2:
        z = 0
        while True:
            emoji_1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[7]/div/div/div/span[1]')
            emoji_1.click()
            testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            testinput.send_keys(Keys.RETURN)
            time.sleep(0.2)
            z += 1
            if z == int(number):
                exit(0)
            if z == 100:
                exit(0)
    if emoji == 3:
        z = 0
        while True:
            emoji_1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[7]/div/div/div/span[8]')
            emoji_1.click()
            testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            testinput.send_keys(Keys.RETURN)
            time.sleep(0.2)
            z += 1
            if z == int(number):
                exit(0)
            if z == 100:
                exit(0)
    if emoji == 4:
        z = 0
        while True:
            whatsappemoji = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[1]/div[1]')
            whatsappemoji.click()
            emojilist = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[3]/span')
            emojilist.click()
            emoji_1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[7]/div/div/div/span[4]')
            emoji_1.click()
            driver.find_element_by_xpath('//span[@data-icon="send"]').click()
            # testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            # testinput.send_keys(Keys.RETURN)
            time.sleep(0.3)
            z += 1
            if z == int(number):
                exit(0)
            if z == 100:
                exit(0)
    if emoji == 5:
        z = 0
        while True:
            emoji_1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[7]/div/div/div/span[3]')
            emoji_1.click()
            testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            testinput.send_keys(Keys.RETURN)
            time.sleep(0.1)
            z += 1
            if z == int(number):
                exit(0)
            if z == 100:
                exit(0)





Print('test')