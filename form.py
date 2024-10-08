from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import os

# Initialize the driver as a global variable
driver = None

def initialize_driver():
    """ Initialize the Firefox WebDriver and return the driver instance """
    global driver
    options = Options()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0")
    driver = webdriver.Firefox(options=options)
    return driver
    

def form_interaction(f_rentals_address_list,f_rentals_price_list,f_rentals_properties_list,f_rentals_link_list):
    global driver
    driver.get(os.getenv("FORM_LINK"))

    address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prop = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit =  driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
 
    # Interact with the form
    address.send_keys(f_rentals_address_list)
    price.send_keys(f_rentals_price_list)
    prop.send_keys(f_rentals_properties_list)
    link.send_keys(f_rentals_link_list)
    submit.send_keys(Keys.RETURN)
    

def form_quit():
    global driver
    # # Close the driver
    if driver:
        driver.quit()
        driver = None

