from pages.home_page import HomePage

def test_063_contact_link_present(driver):
    page = HomePage(driver)
    page.open()
    assert 'Kontakt' in driver.page_source or 'kontakt' in driver.page_source.lower()
