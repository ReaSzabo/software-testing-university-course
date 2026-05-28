import shutil
import tempfile

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless=new')
    options.add_argument('--disable-features=PasswordLeakDetection,PasswordManagerOnboarding,PasswordManager,AutofillServerCommunication')
    options.add_argument('--disable-save-password-bubble')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1280,900')
    profile_dir = tempfile.mkdtemp(prefix="selenium-profile-")
    context.chrome_profile_dir = profile_dir
    options.add_argument(f'--user-data-dir={profile_dir}')
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "autofill.profile_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
        },
    )
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)


def after_scenario(context, scenario):
    try:
        if getattr(context, 'driver', None):
            context.driver.quit()
    except Exception:
        pass
    profile_dir = getattr(context, 'chrome_profile_dir', None)
    if profile_dir:
        shutil.rmtree(profile_dir, ignore_errors=True)
