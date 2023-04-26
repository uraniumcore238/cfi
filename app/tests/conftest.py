import allure
import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from app.utilities import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser_ver", action="store", default="109.0")
    parser.addoption("--headless", action="store", default=False)
    parser.addoption("--remote", action="store", default=False)
    parser.addoption("--hub", action="store", default="localhost")


@pytest.fixture(scope='module')
def config(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browser_ver")
    hub = request.config.getoption("--hub")
    headless = bool(request.config.getoption("--headless"))
    remote = bool(request.config.getoption("--remote"))
    return {"remote": remote,
            "version": version,
            "browser": browser,
            "headless": headless,
            "hub": hub}


def get_chrome_options(config):
    options = ChromeOptions()
    options.headless = config["headless"]
    if config['headless']:
        options.add_argument("--window-size=1920,1080")
    return options


def get_firefox_options(config):
    options = FirefoxOptions()
    options.headless = config["headless"]
    return options


def create_remote_driver(config):
    if config["browser"] == "chrome":
        # download_path = Path(tests.__file__).parent.parent.joinpath('Downloads')
        prefs = {
            'profile.default_content_settings.popups': 0,
            'download.default_directory': '/home/selenium/Downloads',
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': False,
            'plugins.always_open_pdf_externally': True,
            'plugins.plugins_disabled': ['Chrome PDF Viewer']
        }
        # os.makedirs(download_path, exist_ok=True)
        options = get_chrome_options(config)
        options.add_experimental_option("prefs", prefs)

    else:
        options = get_firefox_options(config)
    capabilities = {
        "browserName": config["browser"],
        "browserVersion": config["version"],
        "selenoid:options": {
        "sessionTimeout": "30m",
        "enableVNC": True,
        "enableVideo": False
        # "screenResolution": "1920x1080x24"
        }
    }
    options.capabilities.update(capabilities)
    return webdriver.Remote(command_executor="http://localhost:9515/wd/hub", options=options)


def create_local_driver(config):
    driver = None
    if config["browser"] == "chrome":
        # download_path = str(Path(tests.__file__).parent.parent.joinpath('download'))
        prefs = {
            # 'download.default_directory': download_path,
              'download.prompt_for_download': False,
             'download.directory_upgrade': True,
            'safebrowsing.enabled': True
        }
        # os.makedirs(download_path, exist_ok=True)
        prefs["profile.default_content_settings.popups"] = 0
        options = get_chrome_options(config)
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif config["browser"] == "firefox":
        options = get_firefox_options(config)
        driver = webdriver.Firefox(service=Service(ChromeDriverManager().install()), options=options)
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            web_driver = item.funcargs['wd']
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print("Couldn't make a screenshot: {}".format(e))


@pytest.fixture(scope="class")
def wd(config):
    if config["remote"] is True:
        driver = create_remote_driver(config)
        driver.maximize_window()
    else:
        driver = create_local_driver(config)
        driver.maximize_window()
    yield driver
    with allure.step('Close the driver'):
        attach.add_html(driver)
        attach.add_logs(driver)
        driver.quit()
