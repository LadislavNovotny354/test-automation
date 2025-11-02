from pages.home_page import HomePage

def test_013_smoke(driver):
    page = HomePage(driver)
    page.open()
    assert 'Investown' in driver.title
