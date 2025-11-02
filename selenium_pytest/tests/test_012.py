from pages.home_page import HomePage

def test_012_offer_url_fragment(driver):
    page = HomePage(driver)
    page.open()
    page.go_to_offers()
    assert 'nabidka' in driver.current_url.lower() or 'nabídka' in driver.page_source.lower()
