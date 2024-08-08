class App:
    def __init__(self, name, version, environment):
        self.name = name
        self.version = version
        self.environment = environment

    def info(self):
        return self.name+str(self.version)+self.environment

    def compare(self, app):
        return self.info() == app.info()
