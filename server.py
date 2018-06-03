import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def isElementExist(client,element):
    try:
        client.find_element_by_xpath(element)
        return True
    except:
        return False

def waitElement(client,element):
    while not isElementExist(client,element):
        time.sleep(2)

def loginc9():
    try:
        chrome_exec_shim = os.environ.get("GOOGLE_CHROME_SHIM", None)
        chromedriver_path = os.environ.get("CHROMEDRIVER_PATH", None)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_exec_shim
        client = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver_path)
        client.set_window_size(1366, 768)
        print("*********************************1*********************************")
        client.get("https://c9.io/login")
        waitElement(client,"//button[@type='submit']")
        client.find_element_by_id("id-username").clear()
        client.find_element_by_id("id-username").send_keys("user")
        client.find_element_by_id("id-password").clear()
        client.find_element_by_id("id-password").send_keys("password")
        client.find_element_by_xpath("//button[@type='submit']").click()
        print("*********************************2*********************************")
        mainwindow = client.current_window_handle
        client.execute_script('''window.open("about:blank", "_blank");''')
        time.sleep(2)
        client.switch_to_window(client.window_handles[1])
        print("*********************************3*********************************")
        client.get("https://codeanywhere.com/login")
        waitElement(client,"//button[@type='submit']")
        client.find_element_by_id("login-email").clear()
        client.find_element_by_id("login-email").send_keys("user@gmail.com")
        client.find_element_by_id("login-password").clear()
        client.find_element_by_id("login-password").send_keys("password")
        client.find_element_by_xpath("//button[@type='submit']").click()
        print("*********************************4*********************************")
        client.switch_to_window(mainwindow)    
        waitElement(client,"//a[@href='https://ide.c9.io/user/app']")
        client.find_element_by_xpath("//a[@href='https://ide.c9.io/user/app']").click()
        time.sleep(1500)
        client.get("https://appid.herokuapp.com")
        time.sleep(300)
        client.quit()
        return True
    except:
        return False
        
os.system("nohup gost -L socks+ws://:$PORT >/dev/null 2>&1 &")    

while True:
    if not loginc9():
        continue
    time.sleep(600)
