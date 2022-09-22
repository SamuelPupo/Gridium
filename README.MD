# Gridium Project

## Install and run the project

```bash
$ git clone https://github.com/arnel-sanchez/IA-Sim-Com
$ cd SamuelPW_Gridium
$ python -m pip install --upgrade pip && python -m pip install numpy && python -m pip install pandas && python -m pip install selenium
$ python main.py
```

## Requirements

The "requirements.txt" file contains all the library required for the project works properly.

## Input File

The "input.txt" file should contains all the desired locations one for line with the format: "Location, Region, Country".

Example:
Half Moon Bay, California, United States
Huntington Beach, California, United States
Providence, Rhode Island, United States
Wrightsville Beach, North Carolina, United States

## Output Directory

The "output" directory contains all the information of the low tides after sunrise and before sunset of the gived input locations.
There is one ".csv" file for every location with the format: "Location, Region, Country.csv"
