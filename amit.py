
import random
import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pynput.mouse import Button, Controller

Vip = Controller
from pynput.keyboard import Key, Controller
import os
# arram=[18,22,12]
arram = [2, 1, 9, 16]
jl = 6
i = 1
howmanyvideos = arram[jl]
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_extension("app.crx")
# Change chrome driver path accordingly
chrome_driver = "A:\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

# driver.get(
#      "https://www.appliedaicourse.com/lecture/11/applied-machine-learning-online-course/2811/find-elements-common-in-two-lists/1/module-1-fundamentals-of-programming")

# for i in [21, 28, 24, 21, 19, 13, 18, 25, 8, 15, 10, 11, 5, 10, 25, 8, 27, 19, 14, 12]:
keyboard = Controller()
keyboard.press(Key.cmd_l)
keyboard.press("3")
keyboard.release(Key.cmd_l)
keyboard.release("3")
# try:
while True:
    try:
        while True:
            # ]]]
            mouse = Vip()
            keyboard.press(Key.ctrl_r)
            keyboard.press("1")
            keyboard.release(Key.ctrl_r)
            keyboard.release("1")

            try:
                iframe = driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/iframe')
            except:
                iframe = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div[3]/div[2]/div[1]/div[1]/div/div/iframe')
            driver.switch_to.frame(iframe)
            time.sleep(1)
            # while True:
            try:
                driver.find_element(By.XPATH, '/html/body/video').click()
            except:
                # if reload == 1:
                #     break
                # else:
                # reload = reload + 1
                keyboard.press(Key.ctrl_l)
                keyboard.press("r")
                keyboard.release("r")
                keyboard.release(Key.cmd_l)
                driver.find_element(By.XPATH, '/html/body/video').click()
            time.sleep(3)
            driver.switch_to.default_content()
            driver.find_element(By.CSS_SELECTOR,
                                '#movie_player > div > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(6)').click()
            mouse.position = (1455, 178)

            keyboard = Controller()


            def press_release_char(char):
                keyboard.press(char)
                keyboard.release(char)


            press_release_char(str(']'))
            time.sleep(random.randint(2, 5))
            press_release_char(str(']'))

            # time.sleep(((i * 60) / 1.4) + 20)

            e = driver.find_element(By.CLASS_NAME,
                                    'ytp-time-duration')
            totalTime = (e.get_attribute("innerHTML"))
            b = totalTime.split(":")

            time.sleep(1)
            keyboard.press(Key.cmd_l)
            keyboard.press("3")
            keyboard.release(Key.cmd_l)
            keyboard.release("3")

            while True:
                m = driver.find_element(By.CLASS_NAME,
                                        'ytp-time-current')
                currentTime = (m.get_attribute("innerHTML"))
                a = currentTime.split(":")
                if len(a) < len(b):
                    a.insert(0, "00")

                if int(a[0]) == int(b[0]):
                    if int(a[1]) == int(b[1]):
                        if len(a) == 3:
                            if int(a[2]) == int(b[2]):
                                break
                        else:
                            break

                time.sleep(15)

            keyboard.press(Key.cmd_l)
            keyboard.press("3")
            keyboard.release(Key.cmd_l)
            keyboard.release("3")
            time.sleep(2)

            keyboard.press(Key.esc)
            keyboard.release(Key.esc)

            keyboard.press(Key.ctrl_l)
            keyboard.press("2")
            keyboard.release("2")
            keyboard.release(Key.ctrl_l)

            mouse.position = (474, 782)
            time.sleep(1)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time.sleep(20)

            # change above time

            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(7)

            keyboard.press(Key.ctrl_l)
            keyboard.press(Key.shift)
            keyboard.press("h")
            keyboard.release("h")
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl_l)

            time.sleep(1)
            mouse.position = (973, 763)
            time.sleep(1)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time.sleep(1)
            mouse.position = (459, 339)
            time.sleep(1)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time.sleep(1)
            mouse.position = (1112, 556)
            time.sleep(1)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time.sleep(1)
            mouse.position = (874, 775)
            time.sleep(1)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time.sleep(1)
            mouse.position = (962, 155)
            time.sleep(1)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time.sleep(1)
            mouse.position = (568, 243)
            time.sleep(1)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time.sleep(1)
            mouse.position = (932, 568)
            time.sleep(1)
            mouse.press(Button.left)
            mouse.release(Button.left)
            # while True:
            try:
                m1 = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div[3]/div[1]/div[1]/h1')
            except:
                m1 = driver.find_element(By.XPATH,
                                         '/ html / body / div[3] / div[3] / div[1] / div[1] / h1')

            videoname = m1.get_attribute("innerHTML")
            print(type(videoname))
            print(jl)
            videoname = str(jl + 1) + "." + str(i + 1) + " - " + videoname
            videoname = list(videoname)
            an1 = [':', '/', '\ ', '?', '"', '*', '<', '>', '|']
            ki = 0
            while ki < len(an1):
                if an1[ki] in videoname:
                    videoname.remove(an1[ki])
                    continue
                ki = ki + 1
            j = ''
            for itt in videoname:
                j = j + itt

            old_name = "A:\Module 10\AA\screen-capture.webm"

            new_name = "A:\Module 10\AA\ " + j + ".webm"
            os.rename(old_name, new_name)

            i = i + 1
            if i >= howmanyvideos:
                if jl == len(arram) - 1:
                    break
                else:
                    jl = jl + 1
                    i = 0
                    howmanyvideos = arram[jl]

            # button = WebDriverWait(driver, (i*60)+10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            #                                                                       '#movie_player > div > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(7)')))
            # button.click()
            # try:
            #     driver.find_element(By.CSS_SELECTOR,
            #                         '#movie_player > div > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(7)').click()
            # except:
            #     driver.find_element(By.CSS_SELECTOR,
            #                         '#movie_player > div > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(7)').click()

            driver.find_element(By.ID, 'nextLectureURL').click()

        # driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[4]/button').click()
        # driver.find_element(By.XPATH, '/html/body/div/div/div[27]/div[2]/div[2]/button[2]').click()
        # body = driver.find_element(By.TAG_NAME, "body")
        # body.send_keys(Keys.CONTROL + 't')
        # driver.get("chrome-extension://hniebljpgcogalllopnjokppmgbhaden/index.html#/")
        # alert = Alert(driver)
        # driver.find_element(By.CSS_SELECTOR,
        #                     "#root > div:nth-child(4) > div.container.css-1is9h6g > div.css-90rmsm > div > main > div > div:nth-child(1) > button").click()
        # time.sleep(2)
        # driver.find_element(By.CSS_SELECTOR,
        #                     "#root > div:nth-child(4) > div.container.css-1is9h6g > div:nth-child(7) > div > main > div > div:nth-child(4) > button").click()
        # time.sleep(2)
        # driver.find_element(By.CSS_SELECTOR, "#root > div:nth-child(4) > div.css-2vcgdh > button").click()
        # print(alert.text)
        # # driver.find_element(By.CLASS_NAME, "css-131yo1y").click()
        #
        # time.sleep(7)
        # driver.find_element(By.XPATH, '//*[@id="shakaVid"]').click()
        # driver.switch_to.frame(5)
        # driver.find_element(By.XPATH, '//*[@id="embedBox"]/div/iframe').click()
        # time.sleep(5)
        # driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("naveen90.v@gmail.com")
        # driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("naWIN@90")
        # driver.find_element(By.XPATH, '//*[@id="movie_player"]/div/div[28]/div[2]/div[2]/button[4]').click()
        # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[1]/div/div/div/form/button').click()
        # driver.quit()

    except:
        driver.find_element(By.ID, 'nextLectureURL').click()
        i = i + 1
        if i >= howmanyvideos:
            if jl == len(arram) - 1:
                break
            else:
                jl = jl + 1
                i = 0
                howmanyvideos = arram[jl]

# except:
#     print(prim)
#     mouse = Vip()
#     keyboard.press(Key.ctrl_l)
#     keyboard.press("2")
#     keyboard.release("2")
#     keyboard.release(Key.ctrl_l)
#     time.sleep(1)
#
#     mouse.position = (973, 763)
#     time.sleep(1)
#     mouse.press(Button.left)
#     mouse.release(Button.left)
