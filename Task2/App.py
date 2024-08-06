class App:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def info(self):
        return self.name+str(self.version)

    def compare(self, app):
        return self.info() == app.info()
