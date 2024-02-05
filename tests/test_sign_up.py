import time
import pytest
from api.user_api import UserApi


@pytest.mark.parametrize('login,password', [
    ("Kamilla", "admin123"), 
    ("Matvei", "pass1")
])
def test_sign_up_success(demoblaze, login, password):
    demoblaze.navbar.open_signup()
    demoblaze.sign_up.fill_signup(f"{login}{time.time()}", password)
    assert "Sign up successful." in demoblaze.alert.text

@pytest.mark.parametrize('login,password', [
    ("Kamilla", "admin123"),
])
def test_sign_up_fail_existing_user(demoblaze, login, password):
    UserApi.create_user(login, password)
    demoblaze.navbar.open_signup()
    demoblaze.sign_up.fill_signup(f"{login}", password)
    assert "This user already exist." in demoblaze.alert.text

