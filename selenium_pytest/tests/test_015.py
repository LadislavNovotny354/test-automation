from pages.home_page import HomePage

def test_015_offers_page_has_heading(driver):
    page = HomePage(driver)
    page.open()
    page.go_to_offers()
    assert driver.find_element('tag name','h1').text != ''
