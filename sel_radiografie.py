import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def accesare_radiografie_mail():
    driver = webdriver.Edge()
    driver.get('https://mail.yahoo.com/d/folders/50')
    driver.maximize_window()

    # insert username and Enter
    elem = driver.find_element(by=By.CLASS_NAME, value='input-group')
    elemuser = elem.find_element(by=By.NAME, value='username')
    elemuser.send_keys('stefan.nosca')
    elemuser.send_keys(Keys.RETURN)
    driver.implicitly_wait(0.5)

    # insert password and Enter
    elemp = driver.find_element(by=By.ID, value='password-challenge')
    elempass = elemp.find_element(by=By.ID, value='password-container')
    elempassinput = elemp.find_element(by=By.ID, value='login-passwd')
    elempassinput.send_keys('mail.yahoo.com')
    elempassinput.send_keys(Keys.RETURN)



# dr = webdriver.Edge()
# accesare_radiografie_mail(dr)
