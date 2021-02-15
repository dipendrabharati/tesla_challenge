class CreateAccountPage:
    # Create Account Page
    textbox_first_name_id = 'form-input-first_name'  # id is the textbox_field_name_locator
    textbox_last_name_id = 'form-input-last_name'
    textbox_email_id = 'form-input-email'
    textbox_password_id = 'form-input-password'
    checkbox_agree_to_terms_xpath = '//label[@for="agree-with-privacy-and-terms"]'
    button_create_account_submit_id = 'form-submit-continue'
    iframe_captcha_css = 'iframe[role=presentation]'
    checkbox_captcha_xpath = '//span[@aria-checked="true"][@id="recaptcha-anchor"]'

    button_tesla_account_xpath = '//a[contains(text(), "Tesla Account")]'
    button_create_account_id = 'form-button-create'

    # constructor: __init__, driver will be passed from the actual test case
    # constructor is automatically invoked at the time of object creation
    def __init__(self, driver):
        self.driver = driver

    # username is received from  the actual test case
    def setFirstName(self, first_name):
        self.driver.find_element_by_id(self.textbox_first_name_id).clear()
        self.driver.find_element_by_id(self.textbox_first_name_id).send_keys(first_name)

    def setLastName(self, last_name):
        self.driver.find_element_by_id(self.textbox_last_name_id).clear()
        self.driver.find_element_by_id(self.textbox_last_name_id).send_keys(last_name)

    def setEmail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def selectAgreeToTerms(self):
        self.driver.find_element_by_xpath(self.checkbox_agree_to_terms_xpath).click()

    def clickOnCaptcha(self):
        self.driver.find_element_by_css_selector(self.iframe_captcha_css).click()

    def setIframe(self):
        return self.driver.find_element_by_css_selector(self.iframe_captcha_css)

    def clickCreateAccountSubmit(self):
        self.driver.find_element_by_id(self.button_create_account_submit_id).click()

    # for  teslaAccount button and createAccount button, not belonging to Create Account Page though
    def clickTeslaAccount(self):
        self.driver.find_element_by_xpath(self.button_tesla_account_xpath).click()

    def clickCreateAccount(self):
        self.driver.find_element_by_id(self.button_create_account_id).click()


