import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@allure.step("Открываем страницу Dynamic ID")
def open_dynamic_id_page(driver):
    driver.get("http://uitestingplayground.com/dynamicid")

@allure.step("Кликаем по кнопке с динамическим ID")
def click_dynamic_button(driver):
    button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
    button.click()

@allure.step("Делаем скриншот страницы")
def take_screenshot(driver, name="screenshot"):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

def test_dynamic_id_button(driver):
    open_dynamic_id_page(driver)
    click_dynamic_button(driver)
    take_screenshot(driver, "После клика")
    assert "dynamicid" in driver.current_url
