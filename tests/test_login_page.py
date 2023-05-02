from pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


def test_login_page(browser, browser_name):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
