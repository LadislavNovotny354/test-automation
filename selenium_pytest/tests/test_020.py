from pages.home_page import HomePage

def test_020_smoke(driver):
    page = HomePage(driver)
    page.open()
    assert 'Investown' in driver.title
