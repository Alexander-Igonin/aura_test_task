from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_shopping(driver):
    site_amazon = 'https://www.amazon.com/'
    site_bestbuy = 'https://www.bestbuy.com/'
    product_name = 'Samsung Galaxy Buds2'
    wait = WebDriverWait(driver, 10)

    driver.get(site_amazon)
    driver.maximize_window()

    search_field = wait.until(EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox')))
    search_field.click()
    search_field.send_keys(product_name)
    search_field.send_keys(Keys.RETURN)

    choose_color = wait.until(EC.element_to_be_clickable((By.ID, 'p_n_feature_twenty_browse-bin/2972996011')))
    choose_color.click()

    open_menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'a-dropdown-container')))
    open_menu.click()
    options = driver.find_elements(By.CLASS_NAME, 'a-dropdown-item')

    for elem in options:
        if 'Avg. Customer Review' in elem.text:
            elem.click()

    open_product = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, product_name)))
    open_product.click()

    price = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'apexPriceToPay')))
    amazon_price = float(price.text.replace('$', ''))

    # ------------------------------------------------------------------------------------------------------------------

    driver.get(site_bestbuy)

    if 'Select your Country' in driver.title:
        choose_country = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/a[2]/img')))
        choose_country.click()

    close_login = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="widgets-view-email-modal-mount"]/div/div/div[1]/div/div/div/div/button')))
    close_login.click()

    search_field = wait.until(EC.element_to_be_clickable((By.NAME, 'st')))
    search_field.click()
    search_field.send_keys(product_name)
    search_field.send_keys(Keys.RETURN)

    driver.execute_script("window.scrollTo(0, 300)")
    choose_color = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'White')))
    choose_color.click()

    open_menu = Select(driver.find_element(By.ID, 'sort-by-select'))
    open_menu.select_by_value('Customer-Rating')

    open_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sku-title')))
    open_product.click()

    bb_price = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'priceView-customer-price')))
    bb_price = bb_price.text.split('$')
    bestbuy_price = float(bb_price[-1])
    # once script completed the line below should be uncommented.

    assert amazon_price > bestbuy_price
