class Car:
    def __init__(self, rider="", number=0, driver=""):
        self.rider = rider
        self.number = number
        self.driver = driver

    def walk(self):
       print(self.rider + " is walking")

    def whosriding(self):
        print("the rider is: "+self.rider +" the driver is "+ self.driver)