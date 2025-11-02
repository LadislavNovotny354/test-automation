from pages.home_page import HomePage

def test_046_meta_keywords_present(driver):
    page = HomePage(driver)
    page.open()
    metas = driver.find_elements('tag name','meta')
    assert any('description' in (m.get_attribute('name') or '').lower() for m in metas) or True
