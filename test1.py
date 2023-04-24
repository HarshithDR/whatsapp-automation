from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

driver = webdriver.Chrome('C:\\Users\\91911\\chromedriver\\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
time.sleep(20)

am = driver.find_element_by_css_selector('span[title="*********"]').click()#enter name of user in double quotes

# testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div/span")
z=0
while True:
    # Hx = random.randint(1000000000000000, 9999999999999999)
    # testinput.send(img)
    # testinput.send_keys('hiii')
    # testinput.send_keys(Keys.RETURN)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[1]/div[1]/button[2]/span').click()
    # driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[10]/div/div/div/span[1]').click()
    # time.sleep(0.1)
    # driver.find_element_by_xpath('//span[@data-icon="send"]').click()

    pyautogui.write('HI', interval=0.25)
    pyautogui.press('ENTER')
    time.sleep(0.1)
    z+=1
    if z == 1:
        exit(0)