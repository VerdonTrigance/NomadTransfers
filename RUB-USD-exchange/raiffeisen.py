from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def get_rate():
    url = "https://www.raiffeisen.ru/currency_rates"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        timeout = 3
        selector = "#content-container > div:nth-child(4) > div > div > div:nth-child(2) > span > div:nth-child(2) > div > div:nth-child(1) > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > p"
        WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        html = driver.page_source
        soup = BeautifulSoup(html, "html5lib")
        reverse_rate = soup.select_one(selector).text
        rate = 1 / reverse_rate
        print(rate)
    except:
        driver.quit()

    return rate


get_rate()
