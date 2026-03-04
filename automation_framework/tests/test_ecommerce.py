import pytest
import os
from automation_framework.cloud.cloud_upload import upload_report_to_s3
from automation_framework.utils.logger import get_logger
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_product_to_cart(driver):
    logger = get_logger()

    logger.info("Opening website")
    driver.get("https://www.saucedemo.com/")

    home = HomePage(driver)
    logger.info("Logging in")
    home.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    logger.info("Adding product to cart")
    product.add_product_to_cart()

    cart = CartPage(driver)
    product_name = cart.get_cart_product_name()

    logger.info(f"Product in cart: {product_name}")


    assert product_name == "Sauce Labs Backpack"

    #report_file = "../report.html"  # path relative to test execution
 
     # HTML report path (relative to project root)
    report_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report.html")
    
    upload_report_to_s3(report_file, "qa-automation-reports")  