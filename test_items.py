import pytest
import time
from selenium import webdriver


def test_succeed(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    #time.sleep(30)
    btn = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert btn == 1, "Кнопка не найдена."
