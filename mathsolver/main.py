import constants
import time
import sympy as sp
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Путь к хром-драйверу указывается на каждом локальном компьютере отдельно
chrome_driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

def convert_degree(text):
    return text.replace("^", "").replace("e", "")


driver.get(constants.url)
time.sleep(constants.sleep_time)
soup = BeautifulSoup(driver.page_source, "lxml")
object = soup.find("span", {"class": "katex-html"})
button = driver.find_element(By.ID, "id__204")
button.click()
time.sleep(5)
way = soup.find("div", {"class": "Steps_sectionTitle__WYFvr steps-title"})
way_text = way.get_text()
math_text = soup.find("div", {"class": "Step_stepExpression__99EXI Step_stepStart__TFXZC"})
math_text_div = math_text.find("div", {"class": "hidden"})
rendered_math = math_text_div.get_text()
converted_math = convert_degree(rendered_math)
print(way_text, converted_math)
driver.close()
