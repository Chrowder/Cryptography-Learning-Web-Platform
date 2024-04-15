import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time

with open('test_text/text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

with open('test_text/text_shift_5.txt', 'r', encoding='utf-8') as file:
    text_shift_5 = file.read()




def test_shift_encrypt_5():


    # 设置 WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 打开网页
    driver.get("http://127.0.0.1:5000/shift_cipher")

    # 找到输入框并输入文本
    input_key = driver.find_element(By.ID, "key")
    input_key.send_keys(5)

    input = driver.find_element(By.ID, "srcText")
    input.send_keys(text)

    # 找到按钮并点击
    button_element = driver.find_element(By.ID, "encryptButton")
    button_element.click()

    # 获取结果
    result = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "resultLabel"), "Encrypted message")
    )
    result_element = driver.find_element(By.ID, "resultText")
    result_text = result_element.get_attribute('value')

    # 断言结果是否符合预期
    assert result_text == text_shift_5




def test_shift_decrypt_5():
    # 设置 WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 打开网页
    driver.get("http://127.0.0.1:5000/shift_cipher")

    # 找到输入框并输入文本
    input_key = driver.find_element(By.ID, "key")
    input_key.send_keys(5)

    input = driver.find_element(By.ID, "srcText")
    input.send_keys(text_shift_5)

    # 找到按钮并点击
    button_element = driver.find_element(By.ID, "decryptButton")
    button_element.click()

    # 获取结果
    result = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "resultLabel"), "Decrypted message")
    )
    result_element = driver.find_element(By.ID, "resultText")
    result_text = result_element.get_attribute('value')

    # 断言结果是否符合预期
    assert result_text == text


def test_shift_brute_decrypt_5():
    # 设置 WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 打开网页
    driver.get("http://127.0.0.1:5000/shift_cipher")

    # 找到输入框并输入文本

    input = driver.find_element(By.ID, "srcText")
    input.send_keys(text_shift_5)

    # 找到按钮并点击
    button_element = driver.find_element(By.ID, "decryptWithoutKeyButton")
    button_element.click()

    # 获取结果
    result = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "resultLabel"), "Decrypted message without key.")
    )
    result_element = driver.find_element(By.ID, "resultText")
    result_text = result_element.get_attribute('value')

    # 断言结果是否符合预期
    assert result_text == text