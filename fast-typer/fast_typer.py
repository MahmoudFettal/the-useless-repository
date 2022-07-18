"""
    Written by: Mahmoud Fettal
    Date: 18/07/2022

    Description:
    Recently I have been trying to improve my typing speed and I have made some progress
    by reaching the 60 words per minute milestone, but when I saw the scoreboard I found
    a score of 250 words per minute so I decided to beat it XD

    In this python script, I used selenium to create a "bot" to destroy the scoreboard.
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# make sure to download the compatible driver with your browser
# for chrome use the link: https://chromedriver.chromium.org/downloads
# add it in the same folder as the script before runing it
driver = webdriver.Chrome("chromedriver")
driver.get("https://10fastfingers.com/typing-test/english")

# we deny cookies and reload the page
driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline").click()
time.sleep(0.5)
driver.get("https://10fastfingers.com/typing-test/english")
time.sleep(2)

last_text = ""

for _ in range(15):
    # get the text from the element with the id "row1"
    text = driver.find_element(By.ID, "row1").text

    # after finishing the first two lines we must make sure
    # to remove the first line but since the text isn't devided
    # I did this ugly loop :(
    i = 0
    while last_text != "" and i < len(text) and text[:i] in last_text:
        i += 1

    for letter in text[i:]:
        driver.find_element(By.ID, "inputfield").send_keys(letter)
        time.sleep(1 / random.randint(200, 450)) # just having fun with the speed
        # be aware that the limit is 384 words

    driver.find_element(By.ID, "inputfield").send_keys(" ")
    last_text = text
