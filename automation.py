from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
# print(chrome_browser)
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
print('Selenium Easy' in chrome_browser.title)


button = chrome_browser.find_element_by_class_name('btn-default')
print(button.get_attribute('innerHTML'))
assert  'Selenium Easy' in chrome_browser.title
assert  'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM POWERRRRRRRRRRRRRRRRRRRRR')
button.click()
outmsg = chrome_browser.find_element_by_id('display')
assert  'I AM POWERRRRRRRRRRRRRRRRRRRRR' in outmsg.text
css = chrome_browser.find_element_by_css_selector('#get-input >.btn')
print(css)
#chrome_browser.close()
chrome_browser.quit()