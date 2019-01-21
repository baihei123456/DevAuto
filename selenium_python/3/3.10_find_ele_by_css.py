# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from selenium import webdriver


if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    driver.get("http://www.python.org")

    # 通过正确css
    ele = driver.find_element_by_css_selector("#fieldset >input[@id='id-search-field']")
    print(ele)

    # 给错误css，看下定位到的结果是什么
    ele = driver.find_element_by_css_selector("search-field_error")
    print(ele)

    driver.quit()
