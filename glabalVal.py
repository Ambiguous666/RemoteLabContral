from threading import Thread

class globalval:
    temperature = "25"
    humidity = "44"


def set_temeperature(str):
    globalval.temperature = str


def get_temperature():
    return globalval.temperature


def set_humidity(str):
    globalval.humidity = str


def get_humidity():
    return globalval.humidity
