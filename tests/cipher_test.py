import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time

text = """
For a recap of how substitution ciphers work, see here.

   The Simple substitution cipher is one of the simplest ciphers, simple enough that it can usually be broken with pen and paper in a few minutes. On this page we will focus on automatic cryptanalysis of substitution ciphers, i.e. writing programs to solve these ciphers for us.

   The substitution cipher is more complicated than the Caesar and Affine ciphers. In those cases, the number of keys were 25 and 311 respectively. This allowed a brute force solution of trying all possible keys. The number of keys possible with the substitution cipher is much higher, around 2^88 possible keys. This means we cannot tests them all, we have to 'search' for good keys.

   We will be using a 'hill-climbing' algorithm to find the correct key. For this approach, we need a way of determining how similar a piece of text is to english text. This is called rating the 'fitness' of the text. A piece of text very similar to english will get a high score (a high fitness), while a jumble of random characters will get a low score (a low fitness). For this we will use a fitness measure based on quadgram statistics. For a guide on how to generate quadgram statistics, and some MyCipher code for rating the fitness of text, see this tutorial. This method works by first determining the statistics of english text, then calculating the probability that the ciphertext comes from the same distribution. An incorrectly deciphered (i.e. using the wrong key) message will probably contain sequences e.g. 'QKPC' which are very rare in normal english. In this way we can rank different decryption keys, the decryption key we want is the one that produces deciphered text with the highest likelyhood.
"""

text_shift_5 = """
Ktw f wjhfu tk mtb xzgxynyzynts hnumjwx btwp, xjj mjwj.

   Ymj Xnruqj xzgxynyzynts hnumjw nx tsj tk ymj xnruqjxy hnumjwx, xnruqj jstzlm ymfy ny hfs zxzfqqd gj gwtpjs bnym ujs fsi ufujw ns f kjb rnszyjx. Ts ymnx uflj bj bnqq kthzx ts fzytrfynh hwduyfsfqdxnx tk xzgxynyzynts hnumjwx, n.j. bwnynsl uwtlwfrx yt xtqaj ymjxj hnumjwx ktw zx.

   Ymj xzgxynyzynts hnumjw nx rtwj htruqnhfyji ymfs ymj Hfjxfw fsi Fkknsj hnumjwx. Ns ymtxj hfxjx, ymj szrgjw tk pjdx bjwj 25 fsi 311 wjxujhynajqd. Ymnx fqqtbji f gwzyj ktwhj xtqzynts tk ywdnsl fqq utxxngqj pjdx. Ymj szrgjw tk pjdx utxxngqj bnym ymj xzgxynyzynts hnumjw nx rzhm mnlmjw, fwtzsi 2^88 utxxngqj pjdx. Ymnx rjfsx bj hfssty yjxyx ymjr fqq, bj mfaj yt 'xjfwhm' ktw ltti pjdx.

   Bj bnqq gj zxnsl f 'mnqq-hqnrgnsl' fqltwnymr yt knsi ymj htwwjhy pjd. Ktw ymnx fuuwtfhm, bj sjji f bfd tk ijyjwrnsnsl mtb xnrnqfw f unjhj tk yjcy nx yt jslqnxm yjcy. Ymnx nx hfqqji wfynsl ymj 'knysjxx' tk ymj yjcy. F unjhj tk yjcy ajwd xnrnqfw yt jslqnxm bnqq ljy f mnlm xhtwj (f mnlm knysjxx), bmnqj f ozrgqj tk wfsitr hmfwfhyjwx bnqq ljy f qtb xhtwj (f qtb knysjxx). Ktw ymnx bj bnqq zxj f knysjxx rjfxzwj gfxji ts vzfilwfr xyfynxynhx. Ktw f lznij ts mtb yt ljsjwfyj vzfilwfr xyfynxynhx, fsi xtrj RdHnumjw htij ktw wfynsl ymj knysjxx tk yjcy, xjj ymnx yzytwnfq. Ymnx rjymti btwpx gd knwxy ijyjwrnsnsl ymj xyfynxynhx tk jslqnxm yjcy, ymjs hfqhzqfynsl ymj uwtgfgnqnyd ymfy ymj hnumjwyjcy htrjx kwtr ymj xfrj inxywngzynts. Fs nshtwwjhyqd ijhnumjwji (n.j. zxnsl ymj bwtsl pjd) rjxxflj bnqq uwtgfgqd htsyfns xjvzjshjx j.l. 'VPUH' bmnhm fwj ajwd wfwj ns stwrfq jslqnxm. Ns ymnx bfd bj hfs wfsp inkkjwjsy ijhwduynts pjdx, ymj ijhwduynts pjd bj bfsy nx ymj tsj ymfy uwtizhjx ijhnumjwji yjcy bnym ymj mnlmjxy qnpjqdmtti.
"""


def test_shift_encrypt_5():


    # 设置 WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 打开网页
    driver.get("http://127.0.0.1:5000")

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
    driver.get("http://127.0.0.1:5000")

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
    driver.get("http://127.0.0.1:5000")

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