from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

browser.get("http://localhost:3000/login")

login = browser.find_element(by=By.NAME, value="login")
password = browser.find_element(by=By.NAME, value="password")
submit = browser.find_element(by=By.NAME, value="loginSubmit")

login.send_keys("random_user")
password.send_keys("")

submit.click()

try:
    print("Test-case #1 - logging in with invalid credentials")
    assert "Wrong credentials" in browser.find_element(
        by=By.ID, value="mainHelpBlock").text
    print("Caught the \"Wrong credentials\"")
except Exception as err:
    print("Did not catch the \"Wrong credentials\"")

login.clear()
login.send_keys("tissue_12")
password.send_keys("QWESZXCqweszxc123!")

submit.click()

def is_loaded(driver):
    if browser.find_element(by=By.NAME, value="postNewWorkBtn"):
        return True

try:
    print("Test-case #2 - logging in with valid credentials")
    WebDriverWait(browser, timeout=5).until(is_loaded)
    assert "Home — Fanfiction-Project" in browser.title
    print("Successfully logged in and navigated to the home page")
except Exception as err:
    print("Did not get navigated to the home page")

toggle = browser.find_element(by=By.ID, value="menuDropdown")

toggle.click()

logout = browser.find_element(by=By.ID, value="logoutBtn")

logout.click()

try:
    print("Test-case #3 - logging out")
    assert "tissue_12" not in (browser.find_elements(by=By.CLASS_NAME, value="container")[0].text)
    print("Successfully logged out")
except Exception as err:
    print(err)
    print("Did not log out")

browser.close()
