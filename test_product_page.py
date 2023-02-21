from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest

@pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    browser.get(link)
    page = ProductPage(browser, link)
    code = BasePage(browser, link)
    page.open()
    page.add_to_basket_button()
    code.solve_quiz_and_get_code()
    page.name_should_be_same()
    page.price_should_be_same()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_to_basket_button()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()
  
@pytest.mark.skip  
def test_message_disappeared_after_adding_product_to_basket(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_to_basket_button()
    page.should_be_disappeared_success_message()
