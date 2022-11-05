from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("C:\BDD2\BDDBehavePOM\ConfigurationData\config.ini")
    return config.get(section, Key)