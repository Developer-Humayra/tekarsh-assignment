""" 
Author : Humayra Khanom
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import random
import string
import time
import os

class AutomationTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.email = f"test_{self._generate_random_string()}@test.com"
        self.password = "TestPassword123!"

    def _generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    def signup_process(self):
        self.driver.get("https://automationexercise.com/login")
        time.sleep(3)
        
        name_field = self.wait.until(EC.presence_of_element_located((By.NAME, "name")))
        name_field.send_keys("Test User")
        time.sleep(1)
        
        email_signup = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
        email_signup.send_keys(self.email)
        time.sleep(1)
        
        signup_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
        signup_button.click()
        time.sleep(3)
        
        title_radio = self.wait.until(EC.presence_of_element_located((By.ID, "id_gender1")))
        title_radio.click()
        
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(self.password)
        
        Select(self.driver.find_element(By.ID, "days")).select_by_value("15")
        Select(self.driver.find_element(By.ID, "months")).select_by_value("6")
        Select(self.driver.find_element(By.ID, "years")).select_by_value("1990")
        
        self.driver.find_element(By.ID, "newsletter").click()
        self.driver.find_element(By.ID, "optin").click()
        
        self.driver.find_element(By.ID, "first_name").send_keys("Test")
        time.sleep(1)
        self.driver.find_element(By.ID, "last_name").send_keys("User")
        time.sleep(1)
        self.driver.find_element(By.ID, "company").send_keys("Test Company")
        time.sleep(1)
        
        self.driver.find_element(By.ID, "address1").send_keys("123 Test Street")
        time.sleep(1)
        self.driver.find_element(By.ID, "address2").send_keys("Apartment 456, Building B")
        time.sleep(1)
        
        country_select = Select(self.driver.find_element(By.ID, "country"))
        country_select.select_by_value("United States")
        time.sleep(1)
        
        self.driver.find_element(By.ID, "state").send_keys("California")
        time.sleep(1)
        self.driver.find_element(By.ID, "city").send_keys("San Francisco")
        time.sleep(1)
        self.driver.find_element(By.ID, "zipcode").send_keys("94105")
        time.sleep(1)
        self.driver.find_element(By.ID, "mobile_number").send_keys("(415) 555-0123")
        time.sleep(3)
        
        create_account_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
        create_account_button.click()
        
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='account-created']")))
        
        time.sleep(3)
        continue_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qa='continue-button']")))
        continue_button.click()

    def select_product(self):
        products_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/products']")))
        products_link.click()
        time.sleep(3)
        
        men_category = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#Men']")))
        time.sleep(2)
        men_category.click()
        
        time.sleep(2)
        
        self.wait.until(EC.visibility_of_element_located((By.ID, "Men")))
        
        jeans_link = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@id='Men']//ul//li/a[contains(text(), 'Jeans')]"
        )))
        jeans_link.click()
        time.sleep(2)
        
        view_product = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[style='color: brown;']")))
        view_product.click()
        time.sleep(2)

    def update_cart(self):
        try:
            quantity = self.wait.until(EC.presence_of_element_located((By.ID, "quantity")))
            quantity.clear()
            quantity.send_keys("2")
            time.sleep(1)
            
            add_to_cart = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cart")))
            add_to_cart.click()
            
            modal = self.wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))
            time.sleep(2)
            
            view_cart = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p a[href='/view_cart']")))
            view_cart.click()
            
            self.wait.until(EC.presence_of_element_located((By.ID, "cart_info_table")))
            time.sleep(2)
            
        except Exception as e:
            raise

    def checkout_process(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "cart_info_table")))
            time.sleep(2)
            
            proceed_checkout = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-default.check_out")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", proceed_checkout)
            time.sleep(1)
            proceed_checkout.click()
            
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='checkout-info']")))
            time.sleep(2)
            
            place_order_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/payment'].btn.btn-default.check_out")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", place_order_btn)
            time.sleep(1)
            place_order_btn.click()
            

            self.wait.until(EC.presence_of_element_located((By.NAME, "name_on_card")))
            time.sleep(1)
            

            self.wait.until(EC.presence_of_element_located((By.NAME, "name_on_card"))).send_keys("Test User")
            self.driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
            self.driver.find_element(By.NAME, "cvc").send_keys("123")
            self.driver.find_element(By.NAME, "expiry_month").send_keys("12")
            self.driver.find_element(By.NAME, "expiry_year").send_keys("2025")
            time.sleep(2)
            
            place_order = self.driver.find_element(By.ID, "submit")
            place_order.click()
            time.sleep(2)

        except Exception as e:
            print(f"Checkout failed: {str(e)}")
            raise

    def contact_us(self):
        self.driver.get("https://automationexercise.com/contact_us")
        
        self.wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Test User")
        self.driver.find_element(By.NAME, "email").send_keys(self.email)
        self.driver.find_element(By.NAME, "subject").send_keys("Test Subject")
        self.driver.find_element(By.NAME, "message").send_keys("This is a test message")
        
        test_file_path = os.path.join(os.getcwd(), "test_file.txt")
        with open(test_file_path, "w") as f:
            f.write("This is a test file for upload")
        
        file_input = self.driver.find_element(By.NAME, "upload_file")
        file_input.send_keys(test_file_path)
        
        submit_button = self.driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        try:
            os.remove(test_file_path)
        except:
            pass

    def run_tests(self):
        try:
            self.signup_process()
            self.select_product()
            self.update_cart()
            self.checkout_process()
            self.contact_us()
        except Exception as e:
            print(f"Test failed with error: {str(e)}")
        finally:
            time.sleep(2)
            self.driver.quit()

if __name__ == "__main__":
    test = AutomationTest()
    test.run_tests()
