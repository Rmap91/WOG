from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

Base_URL = 'http://127.0.0.1:5000/'

def test_scores_service():
    driver = webdriver.Chrome()
    driver.get(Base_URL)
    score = driver.find_element(by=By.XPATH, value="/html/body/h1/div/pre").text
    print(score)
    if 1 <= int(score) <= 1000:
        print("True")
    else:
        print("False")

def main_function():
    if test_scores_service() is True:
        sys.exit(0)
    else:
        sys.exit(1)


main_function()