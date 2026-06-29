from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Test si le formulaire de login fonctionne correctement avec Selenium
def test_should_login_with_selenium():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5000/")

    driver.find_element(By.NAME, "email").send_keys("john@simplylift.co")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "Welcome" in driver.page_source

    driver.quit()


# Test si le message d'erreur s'affiche correctement lorsque l'email est incorrect
def test_should_show_error_message_with_selenium():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5000/")

    driver.find_element(By.NAME, "email").send_keys("invalid@email.com")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "Registration Portal" in driver.page_source

    driver.quit()
