import os

from behave import fixture, use_fixture
from selenium.webdriver import Chrome

from django.behave_fixtures import django_test_case, django_test_runner

os.environ["DJANGO_SETTINGS_MODULE"] = "test_project.settings"

def before_all(context):
    use_fixture(django_test_runner, context)
    use_fixture(browser_chrome, context)

def before_scenario(context, scenario):
    use_fixture(django_test_case, context)

@fixture
def browser_chrome(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.browser = Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()
