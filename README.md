# Gridium Project

## Important

The Google Chrome application should be downloaded and installed: https://www.google.com/chrome/
The ChromeDrive application should be downloaded and installed: https://chromedriver.chromium.org/downloads
The Python language should be downloaded and installed: https://www.python.org/downloads/

## Install and run the project

```bash
$ git clone https://github.com/SamuelPupo/Gridium
$ cd Gridium
$ python -m pip install --upgrade pip && python -m pip install numpy && python -m pip install pandas && python -m pip install selenium
$ python main.py
```

## Python scripts

The "main.py" and "script.py" files contains all the code to execute.
The line 15 of "main.py" should be adapted to the path of the Google Chrome application.
The line 16 of "main.py" should be adapted to the path of the ChromeDriver application

## Requirements

The "requirements.txt" file contains all the libraries required for the project to work properly. 

## Input File

The "input.txt" file should contain all the desired locations one per line with the format: "Location, region, country".

## Output Directory

The "output" directory contains all the information about the low tides after sunrise and before sunset of the input locations.
There is one ".csv" file for each location with the format: "Location, region, country.csv"
