# Python3 + PyTest
import pytest

from appium import webdriver
# Options are available in Python client since v2.6.0
from appium.options.windows import WindowsOptions

def generate_options():
    uwp_options = WindowsOptions()
    # How to get the app ID for Universal Windows Apps (UWP):
    # https://www.securitylearningacademy.com/mod/book/view.php?id=13829&chapterid=678
    uwp_options.app = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'

    classic_options = WindowsOptions()
    classic_options.app = 'C:\\Windows\\System32\\notepad.exe'
    # Make sure arguments are quoted/escaped properly if necessary:
    # https://ss64.com/nt/syntax-esc.html
    classic_options.app_arguments = 'D:\\log.txt'
    classic_options.app_working_dir = 'D:\\'

    use_existing_app_options = WindowsOptions()
    # Active window handles could be retrieved from any compatible UI inspector app:
    # https://docs.microsoft.com/en-us/windows/win32/winauto/inspect-objects
    # or https://accessibilityinsights.io/.
    # Also, it is possible to use the corresponding WinApi calls for this purpose:
    # https://referencesource.microsoft.com/#System/services/monitoring/system/diagnosticts/ProcessManager.cs,db7ac68b7cb40db1
    #
    # This capability could be used to create a workaround for UWP apps startup:
    # https://github.com/microsoft/WinAppDriver/blob/master/Samples/C%23/StickyNotesTest/StickyNotesSession.cs
    use_existing_app_options.app_top_level_window = hex(12345)

    return [uwp_options, classic_options, use_existing_app_options]


@pytest.fixture(params=generate_options())
def driver(request):
    # The default URL is http://127.0.0.1:4723/wd/hub in Appium 1
    drv = webdriver.Remote('http://127.0.0.1:4723', options=request.param)
    yield drv
    drv.quit()


def test_app_source_could_be_retrieved(driver):
    assert len(driver.page_source) > 0