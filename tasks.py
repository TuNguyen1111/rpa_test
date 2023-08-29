from RPA.Browser.Selenium import Selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url, maximized=True)


def search_for(term):
    input_field = "css:input"
    browser_lib.input_text(input_field, term)
    browser_lib.press_keys(input_field, "ENTER")


def store_screenshot(filename):
    browser_lib.screenshot(filename=filename)


# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website("https://www.nytimes.com/")
        button_ele = '//*[@id="complianceOverlay"]/div/button'
        button = browser_lib.find_element(button_ele)
        button.click()
        button_2 = browser_lib.find_element("//*[@id='app']/div[2]/div[2]/header/section[1]/div[1]/div[2]/button")
        button_2.click()
        # search_for("python")
        store_screenshot("output/screenshot1.png")
    finally:
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()