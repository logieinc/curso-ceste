import configparser

config = configparser.ConfigParser(allow_no_value=True)
config.read("01_allow_no_value.ini")

print(config["mysqld"]["user"])
print(config["mysqld"]["skip-bdb"])

