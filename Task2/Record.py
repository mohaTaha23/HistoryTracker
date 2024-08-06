from App import App
import datetime


def makedate(date):
    try:
        year, month, day = date.split("-")
        return datetime.datetime(int(year), int(month), int(day))
    except:
        return None
    pass


class Record:

    def __init__(self, app_name, environment, version, date, developer):
        self.app_name = app_name
        self.environment = environment
        self.version = version
        self.date = date
        self.developer = developer
        self.app = App(app_name, version)

    def info(self):
        return f"{self.app_name},{self.environment},{self.version},{self.date},{self.developer}"
