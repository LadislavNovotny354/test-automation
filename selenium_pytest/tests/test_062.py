from pages.home_page import HomePage

def test_062_smoke(driver):
    page = HomePage(driver)
    page.open()
    assert 'Investown' in driver.title
