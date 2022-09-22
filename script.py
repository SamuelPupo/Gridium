"""
Script that does the data ingestion
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from time import sleep

from datetime import datetime
from pandas import DataFrame
from numpy import array

from os.path import exists
from os import mkdir


def extract(driver: WebDriver, location: str, region: str, country: str) -> None:
    """
    Extract all the information about the location
    :param driver: Webdriver used to extract the data
    :param location: Desired location to extract the information
    :param region: Region to which the location belongs
    :param country: Country to which the region belongs
    """

    country_elem = driver.find_element(By.ID, "country_id")  # Select the input element for the country
    country_elem.send_keys(country)  # Fill the country input
    sleep(2)  # Wait time while webdriver is loading

    region_elem = driver.find_element(By.ID, "region_id")  # Select the input element for the region
    region_elem.send_keys(region)  # Fill the region input
    sleep(2)

    location_elem = driver.find_element(By.ID, "location_filename_part")  # Select the input element for the location
    location_elem.send_keys(location)  # Fill the location input
    sleep(2)

    button = driver.find_element(By.ID, "gobtn")  # Select the search button element
    button.click()  # Click the button to change the page
    sleep(2)

    tides = select(driver)
    save(location, region, country, tides)


def select(driver: WebDriver) -> []:
    """
    Select the information about the low tides that occur after sunrise and before sunset
    :param driver: Webdriver
    """

    elements = driver.find_elements(By.CLASS_NAME, "tide-day")  # Select the classes that have the tides information
    daylight = []  # List of the low tides that occur after sunrise and before sunset
    for element in elements:
        text = element.text.split('\n')
        date = text[0].split(': ')[-1]  # Date of the information
        lows = []  # List of the low tides
        sunrise = 0  # Sunrise time
        sunset = 0  # Sunset time
        for i in range(len(text) - 1):
            if text[i].__contains__("Low"):  # Low tide information
                time = text[i].split(' ')[2:]
                fix = False
                if time[0][:2] == "00":  # The datetime library has a bug that makes impossible to parse the hour 00
                    time[0] = "01" + time[0][2:]
                    fix = True
                time = datetime.strptime("".join(time), "%I:%M%p").time()  # Low tide time
                if fix:  # Fix the hour again
                    time = time.replace(hour=0)
                height = text[i + 2].split(' ')[0]  # Low tide height
                lows.append((time, height))
            
            elif text[i].__contains__("Sunrise"):  # Sunrise information
                sunrise = text[i + 1]
                sunrise = datetime.strptime(sunrise, "%I:%M%p").time()
            
            elif text[i].__contains__("Sunset"):  # Sunset information
                sunset = text[i + 1]
                sunset = datetime.strptime(sunset, "%I:%M%p").time()
                
        for low in lows:
            if sunrise < low[0] < sunset:  # After sunrise and before sunset
                time = low[0].strftime("%I:%M %p")
                height = low[1]
                daylight.append((date, time, height))
                
    return daylight


def save(location: str, region: str, country: str, tides: []) -> None:
    """
    Print the selected low tides information
    :param location: Desired location to analyze the information
    :param region: Region to which the location belongs
    :param country: Country to which the region belongs
    :param tides: Low tides information
    """

    all_tides = []  # The data of all the days
    for tide in tides:
        all_tides.append(tide)
    
    all_tides = array(all_tides)
    dataframe = DataFrame(all_tides, columns=["Date", "Time", "Height (ft.)"])  # Convert data into a dataframe
    
    if not exists("output"):  # Can't find the output directory
        mkdir("output")
    output = "output/" + location + ", " + region + ", " + country + ".csv"
    dataframe.to_csv(output, index=False, encoding="utf8")  # Output file with the tides information
