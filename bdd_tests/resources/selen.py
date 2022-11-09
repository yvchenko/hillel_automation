"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug:3.141
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""
#
# import time
#
# from selenium import webdriver
# import subprocess
#
# from selenium.webdriver.common.by import By
#
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-ssl-errors=yes')
# options.add_argument('--ignore-certificate-errors')
#
# port = 4347
#
# try:
#     subprocess.run(f"docker run -d --name selenium_chrome -p"
#                    f" {port}:4444 -v "
#                    f"/dev/shm:/dev/shm selenium/standalone-chrome-debug:3.141",
#                    shell=True, check=True)
#     time.sleep(5)
#     print("docker started")
#     driver = webdriver.Remote(
#             command_executor=f'http://localhost:{port}/wd/hub',
#             options=options)
#
#     # driver.get("https://google.com")
#     # print("google opened")
#     # element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/img")
#     # print(element.get_attribute("src"))
#     driver.quit()
# except subprocess.CalledProcessError:
#     print("not started")
# finally:
#     subprocess.run("docker rm --force selenium_chrome", shell=True, check=True)
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    options=options
)
