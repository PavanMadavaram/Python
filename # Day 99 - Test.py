# Day 99 - Test
import configparser

c = configparser.ConfigParser()
c.read_dict({"A": {"x": "1"}})
print("Day 99 test:", c.getint("A", "x") == 1)
print("Day 99 test ok")