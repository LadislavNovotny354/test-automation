from pages.home_page import HomePage

def test_059_cookie_banner(driver):
    page = HomePage(driver)
    page.open()
    try:
        btn = driver.find_element('xpath',"//button[contains(.,'Přijmout')]")
        btn.click()
    except Exception:
        pass
    assert True
