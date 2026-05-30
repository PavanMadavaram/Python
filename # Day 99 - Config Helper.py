# Day 99 - Config Helper
import configparser

config = configparser.ConfigParser()
config.read("day99.ini")

print("App name:", config["APP"]["name"])
print("Debug mode:", config.getboolean("APP", "debug"))
print("Theme:", config["USER"]["theme"])