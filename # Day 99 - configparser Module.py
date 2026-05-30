# Day 99 - configparser Module 
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config["APP"] = {
    "name": "Day99App",
    "version": "1.0",
    "debug": "true"
}
config["USER"] = {
    "name": "PythonLearner",
    "theme": "dark"
}

with open("day99.ini", "w") as f:
    config.write(f)

print("INI file created:", Path("day99.ini").resolve())