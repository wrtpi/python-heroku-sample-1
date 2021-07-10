import os
import time
import string
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def id_generator(size=11, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def clicker(client):
    try:
        while True:
            #if len(client.window_handles) < 1:
            #    link = "window.open(\"https://www.youtube.com/watch?v="+id_generator()+"\");"
            #    client.execute_script(link)
            #client.switch_to.window(client.window_handles[0])
            client.get("https://www.gaily.ga")
            #WebDriverWait(client, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='showSkip']/a[@class='skip']"))).click()
            #time.sleep(5)
            #client.delete_all_cookies()
            print("----opening----")
            time.sleep(60000)
    except:
        print("----exceptions----")
        client.quit()
        pass

os.system("nohup portmap >/dev/null 2>&1 &") 

while True:
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    client = webdriver.Firefox(options=firefox_options)
    client.set_window_size(1366, 768)
    clicker(client)      
