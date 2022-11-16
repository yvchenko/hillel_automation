import os
import time
import allure

from selen import driver
from datetime import datetime


def take_screenshot():
    """
    Takes a screenshot
    """
    time.sleep(1)
    date_time = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    os.makedirs(os.path.join("screenshots", os.path.dirname(date_time)), exist_ok=True)
    screenshot_path = os.path.join("screenshots", f"{date_time}.png")
    driver.save_screenshot(screenshot_path)
    allure.attach.file(
        screenshot_path,
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )