"""
Main script that leads all the process
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

from os.path import exists

from script import extract


GOOGLE_CHROME_BIN = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path of the Google Chrome application
CHROMEDRIVER_PATH = "C:/Users/samue/Downloads/chromedriver.exe"  # Path of the Chromedriver application

URL = "https://www.tide-forecast.com/"  # URL Homepage


def webdriver() -> WebDriver:
    """
    Open the Chrome webdriver
    """

    service = Service(CHROMEDRIVER_PATH)

    options = Options()  # Browser options
    options.add_argument('--headless')  # Launch browser without UI (headless)
    options.binary_location = GOOGLE_CHROME_BIN

    driver = Chrome(service=service, options=options)  # Chrome webdriver
    driver.get(URL)
    return driver


def main() -> int:
    """
    Read the input locations and call the method that extracts all the information
    """

    if not exists("input.txt"):
        print("Missing file: 'input.txt'")  # Can't find the input file
        return 1

    print("Process running. Please wait...\n")

    driver = webdriver()

    file = open("input.txt")  # Input file with the locations
    lines = file.readlines()  # All the input lines
    for line in lines:
        line = [lin.strip() for lin in line.replace('\n', '').split(',')]

        try:
            location = line[0]
            region = line[1]
            country = line[2]
            extract(driver, location, region, country)

            print("Finished: " + location + ", " + region + ", " + country)

        except Exception:
            print("\nSomething went wrong!\n")
            driver.close()
            return 1

    driver.close()  # Close the webdriver
    return 0


if __name__ == '__main__':
    print("\nProcess started...\n")
    main()
    print("\nProcess ended.\n")
