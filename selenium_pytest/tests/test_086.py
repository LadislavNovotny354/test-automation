from pages.home_page import HomePage

def test_086_login_link_visible(driver):
    page = HomePage(driver)
    page.open()
    page.open_login()
    assert 'Přihl' in driver.page_source or 'Prihl' in driver.page_source or 'login' in driver.current_url.lower()
