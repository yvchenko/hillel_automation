import os
import time
import pytest

from allure_commons.lifecycle import AllureLifecycle
from allure_commons.model2 import TestResult
from allure_commons import plugin_manager
from allure import attach, attachment_type
from resources.selen import driver


def custom_write_test_case(self, uuid=None):
    test_result = self._pop_item(uuid=uuid, item_type=TestResult)
    if test_result:
        if test_result.parameters:
            adj_parameters = []
            for param in test_result.parameters:
                if param.name != '_pytest_bdd_example':
                    # do not include parameters with "_pytest_bdd_example"
                    adj_parameters.append(param)
            test_result.parameters = adj_parameters

        plugin_manager.hook.report_result(result=test_result)


AllureLifecycle.write_test_case = custom_write_test_case


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def take_screenshot(item, call):
    """
    Takes a screenshot
    """
    # time.sleep(1)
    # attach(
    #     driver.get_screenshot_as_png(),
    #     name='screenshot',
    #     attachment_type=attachment_type.PNG
    # )
# def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))