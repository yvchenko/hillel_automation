"""
docker run -d --name selenium_chrome -p 4347:4444 -p 5900:5900 selenium/standalone-chrome-debug:3.141
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
    command_executor='http://localhost:4090/wd/hub',
    options=options
)
