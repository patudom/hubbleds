import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function")
def selenium(selenium, request):
    browser = request.config.getoption("--driver")
    options = None

    if browser == "firefox":
        options = FirefoxOptions()
    # elif browser == "chrome":
    #     options = ChromeOptions()
    # elif browser == "edge":
    #     options = EdgeOptions()

    if options:
        options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.mark.selenium
def test_homepage_title(selenium):
    selenium.get("http://localhost:8865")  # Change this to your web app URL

    WebDriverWait(selenium, 10).until(EC.title_contains("HubbleDS"))
    assert "HubbleDS" in selenium.title


@pytest.mark.selenium
def test_click_demo_button(selenium):
    selenium.get("http://localhost:8865")  # Open your test page

    # Wait until the button is visible and clickable
    button = WebDriverWait(selenium, 10).until(
        EC.element_to_be_clickable((By.ID, "btn-jump-to-stage-1"))
    )

    # Click the button
    button.click()

    # Wait for the URL to change
    WebDriverWait(selenium, 10).until(EC.url_changes("http://localhost:8865"))

    # Optionally, verify that clicking the button triggered the expected behavior
    assert (
        "01-spectra-&-velocity" in selenium.current_url
    )  # Update based on what the button does
