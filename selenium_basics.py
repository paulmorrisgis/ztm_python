# Selenium

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

# chrome_browser  # Opens new instance of Chrome
# chrome_browser.maximize_window()  # Opens new instance of Chrome that's maximized

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# assert 'Selenium Easy Demo' in chrome_browser.title  # errors out if isn't true
# print('Selenium Easy Demo' in chrome_browser.title)  # check if text is in title

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))  # Gets button HTML (Show Message)

assert 'Show Message' in chrome_browser.page_source  # check for Show Message in HTML of website

# chrome_browser.find_element_by_css_selector('.btn') Grab by CSS (style)
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()  # Clears any existing text
user_message.send_keys('send this text as input')  # fills out input with text

show_message_button.click()  # Clicks button to send input
output_message = chrome_browser.find_element_by_id('display')
assert 'send this text as input' in output_message.text


# chrome_browser.close()  # Closes current instance. Sometimes need twice.
chrome_browser.quit()  # Quits all sessions
