import random
import string
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from customLogger import LogGen
from CreateAccountPage import CreateAccountPage


class Test_001_CreateAccount:  # Test_number_page
    baseURL = 'https://www.tesla.com'
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*******************Test_001_CreateAccount****************************")
        self.logger.info("*******************Verifying Home Page Title*************************")
        self.driver = setup
        self.driver.get(self.baseURL)  # accessing the website homepage
        home_title = self.driver.title  # Getting the title

        if home_title == 'Electric Cars, Solar & Clean Energy | Tesla':  # Verification of title
            assert True
            self.driver.close()
            self.logger.info("*****************Home page title test is passed**********************")
        else:
            self.driver.save_screenshot("test_homePageTitle.png")
            self.logger.info("*****************Home page title test is failed***********************")
            self.driver.close()
            assert False

    def test_signInPageTitle(self, setup):
        self.logger.info("**********************Verifying Sign in Page title*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.ca = CreateAccountPage(self.driver)
        self.ca.clickTeslaAccount()
        time.sleep(2)

        sign_in_title = self.driver.title
        if sign_in_title == 'Tesla SSO - Sign In':
            self.driver.close()
            self.logger.info("***********************Sign in Page title is passed***********************")
            assert True
        else:
            self.driver.save_screenshot("test_signInPageTitle.png")
            self.driver.close
            self.logger.info("***********************Sign in Page title is failed**********************")
            assert False

    def test_createAccountPage(self, setup):
        self.logger.info("**************************Verifying Create Account Test************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.ca = CreateAccountPage(self.driver)
        self.ca.clickTeslaAccount()
        time.sleep(2)

        self.ca.clickCreateAccount()
        self.ca.setFirstName('Dipendra')
        self.ca.setLastName('Bharati')
        self.email = random_generator() + '@gmail.com'
        self.ca.setEmail(self.email)
        self.ca.setPassword('abcdefg123#*&')
        self.ca.selectAgreeToTerms()

        # wait for captcha to be appear,
        time.sleep(2)

        self.ca.clickOnCaptcha()
        self.driver.switch_to.frame(self.ca.setIframe())
        # Solve the captcha within 120 seconds
        wait = WebDriverWait(self.driver, 120)
        try:
            wait.until(ec.presence_of_element_located((By.XPATH, self.ca.checkbox_captcha_xpath)))
        except TimeoutException:
            self.logger.info("*********************Failed to solve captcha in the expected time***************")
        else:
            self.logger.info("*********************Captcha solved successfully, proceeding to click!********************")
            self.driver.switch_to.parent_frame()
            self.ca.clickCreateAccountSubmit()

        # wait for the page to load
        time.sleep(2)
        ac_title = self.driver.title  # Getting title after account creation

        if ac_title == 'Tesla Account | Tesla':
            self.driver.close()
            self.logger.info("*************************Create Acccount Test is passed*************************")
            assert True
        else:
            self.driver.save_screenshot(".\\test_createAccount.png")
            self.driver.close()
            self.logger.info("*************************Create Account Test is failed***************************")
            assert False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))