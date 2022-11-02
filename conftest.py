
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options


@pytest.fixture(autouse=True)
def setup(request):
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-blink-features=AutomationControlled')
    browser = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver', chrome_options=options)
    wait = WebDriverWait(browser, 20)
    browser.get("https://www.yatra.com/")
    browser.maximize_window()
    request.cls.browser = browser
    request.cls.wait = wait
    yield
    browser.close()
