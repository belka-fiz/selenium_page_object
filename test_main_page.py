from .main_page import MainPage


def test_guest_can_go_to_login_page(browser, browser_name):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
