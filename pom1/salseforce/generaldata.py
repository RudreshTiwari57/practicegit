from configparser import ConfigParser

def data(search,value):
    c = ConfigParser()
    c.read("C:\pom1\salseforce\config.ini")
    return c[search][value]
