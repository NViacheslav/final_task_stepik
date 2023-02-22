from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPageLocators():
    pass
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_NAME_NT = (By.XPATH, "//div[@id='messages']/div[1]/div[@class='alertinner ']/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_NT = (By.XPATH, "//div[@id='messages']/div[3]/div[@class='alertinner ']/p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")

class BasketPageLocators():
    BASKET = (By.PARTIAL_LINK_TEXT, "basket")
    NT_EMPTY = (By.XPATH, "//p[contains(text(), 'empty')]")
    PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='basket-items']")