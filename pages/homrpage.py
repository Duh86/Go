from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.demoblaze.com/index.html')

    def click_galaxy_s6(self):
            galaxy_s6 = self.browser.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
            galaxy_s6.click()


    def click_monitor(self):
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_product_count(self, count):
        title_monitors = self.browser.find_elements(By.CLASS_NAME, 'hrefch')
        assert len(title_monitors) == count
