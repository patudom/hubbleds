import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


# @pytest.fixture(scope="function")
# def selenium(selenium, request):
#     browser = request.config.getoption("--driver")
#     options = None
#
#     if browser == "firefox":
#         options = FirefoxOptions()
#     elif browser == "chrome":
#         options = ChromeOptions()
#     elif browser == "edge":
#         options = EdgeOptions()
#
#     if options is not None:
#         options.add_argument("--headless")
#
#     driver = webdriver.Firefox(options=options)
#     yield driver
#     driver.quit()


@pytest.mark.selenium
def test_homepage_title(selenium):
    selenium.get("http://localhost:8865")

    WebDriverWait(selenium, 10).until(EC.title_contains("HubbleDS"))
    assert "HubbleDS" in selenium.title


@pytest.mark.selenium
def test_jump_to_stage_one(selenium):
    selenium.get("http://localhost:8865")

    # Wait until the button is visible and clickable
    button = WebDriverWait(selenium, 10).until(
        EC.element_to_be_clickable((By.ID, "btn-jump-to-stage-1"))
    )

    # Click the button
    button.click()

    # Wait for the URL to change
    WebDriverWait(selenium, 10).until(EC.url_changes("http://localhost:8865"))

    # Verify that clicking the button triggered the expected behavior
    assert "01-spectra-&-velocity" in selenium.current_url
