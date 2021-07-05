import os
import time
import string
import random
from tempfile import gettempdir
from selenium import webdriver

def id_generator(size=15, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def clicker(client):
    try:
        while True:
            print(len(client.window_handles))
            if len(client.window_handles) < 1:
                link = "window.open(\"http://adf.ly/25551289/www.pornhub.com/view_video.php?viewkey="+id_generator()+"\");"
                print("--1-->> " + link)
                client.execute_script(link)
            client.switch_to.window(client.window_handles[0])
            client.get("http://j.gs/25551289/girlxxx01")
            time.sleep(5)
            client.find_element_by_id("skip_bu2tton").click()
            print(len(client.window_handles))                   
            if len(client.window_handles) < 2:
                link = "window.open(\"http://adf.ly/25551289/www.pornhub.com/view_video.php?viewkey="+id_generator()+"\");"
                print("--2-->> " + link)
                client.execute_script(link)
            client.switch_to.window(client.window_handles[1])
            client.get("http://j.gs/25551289/girlxxx02")
            time.sleep(5)
            client.find_element_by_id("skip_bu2tton").click()
            print(len(client.window_handles))
            if len(client.window_handles) < 3:
                link = "window.open(\"http://adf.ly/25551289/www.pornhub.com/view_video.php?viewkey="+id_generator()+"\");"
                print("--3-->> " + link)
                client.execute_script(link)            
            client.switch_to.window(client.window_handles[2])
            client.get("http://j.gs/25551289/girlxxx03")
            time.sleep(5)
            client.find_element_by_id("skip_bu2tton").click()
            print(len(client.window_handles))
            if len(client.window_handles) < 4:
                link = "window.open(\"http://adf.ly/25551289/www.pornhub.com/view_video.php?viewkey="+id_generator()+"\");"
                print("--4-->> " + link)
                client.execute_script(link)            
            client.switch_to.window(client.window_handles[3])
            client.get("http://j.gs/25551289/girlxxx04")
            time.sleep(5)
            client.find_element_by_id("skip_bu2tton").click()
            time.sleep(10)
            client.quit()
    except:
        print("----exceptions----")
        client.quit()
        pass

os.system("nohup hooker >/dev/null 2>&1 &")  
while True:
    chrome_exec_shim = os.environ.get("GOOGLE_CHROME_SHIM", None)
    print(chrome_exec_shim)
    chrome_exec_bin = os.environ.get("GOOGLE_CHROME_BIN", None)
    print(chrome_exec_bin)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_exec_shim  
    chromeuser_path = os.path.join(gettempdir(), '.{}'.format(hash(os.times())))
    chrome_options.add_argument('--user-data-dir=' + chromeuser_path)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--remote-debugging-port=9222")
    #chrome_options.add_argument('--proxy-server=socks5://localhost:1080')
    #chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:5003")
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs", prefs)
    client = webdriver.Chrome(chrome_options=chrome_options)
    clicker(client)      
