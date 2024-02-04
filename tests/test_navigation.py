def test_open_home_page(demoblaze):
    demoblaze.navbar.home_button.click()
    assert "demoblaze.com/index.html" in demoblaze.browser.current_url

def test_open_contact_page(demoblaze):
    demoblaze.navbar.contact_button.click()
    assert demoblaze.contact_page.is_open


def test_open_about_us_page(demoblaze):
    demoblaze.navbar.about_us_button.click()
    assert demoblaze.about_us.is_open



def test_open_cart_page(demoblaze):
    demoblaze.navbar.cart_button.click()
    assert "demoblaze.com/cart.html" in demoblaze.browser.current_url


def test_open_login_page(demoblaze):
    demoblaze.navbar.login_button.click()
    assert demoblaze.login_page.is_open


def test_open_signup_page(demoblaze):
    demoblaze.navbar.signup_button.click()
    assert demoblaze.sign_up.is_open
