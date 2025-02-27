import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--driver")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")  # Ensures fully headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")  # Avoids loading user data
        options.add_argument("--incognito")  # Ensures no user-data-dir
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("-headless")
        options.add_argument("-private")  # Ensures no user data is stored
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")  # Avoids loading user data
        options.add_argument("--inprivate")  # Ensures no user data
        service = EdgeService()
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()


@pytest.mark.selenium
def test_homepage_title(driver):
    driver.get("http://localhost:8865")

    # Wait until the title contains "HubbleDS"
    WebDriverWait(driver, 60).until(EC.title_contains("HubbleDS"))

    assert "HubbleDS" in driver.title


@pytest.mark.selenium
def test_jump_to_stage_one(driver):
    driver.get("http://localhost:8865")

    # Wait until the button is visible and clickable
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "btn-jump-to-stage-1"))
    )

    # Click the button
    button.click()

    # Wait for the URL to change
    WebDriverWait(driver, 60).until(EC.url_changes("http://localhost:8865/"))

    # Verify that clicking the button triggered the expected behavior
    assert "01-spectra-&-velocity" in driver.current_url
