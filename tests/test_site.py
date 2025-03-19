
import time #никогда так не делать
from pages.homrpage import HomePage
from pages.product import ProdcutPage



def test_open_s6(browser):

    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProdcutPage(browser)
    product_page.check_title_is('Samsung galaxy s6')
    
def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    #browser.get('https://www.demoblaze.com/index.html')
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_product_count(2)


