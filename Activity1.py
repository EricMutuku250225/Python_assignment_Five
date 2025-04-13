class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

class Smartphone(Device):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

    def call(self, number):
        print(f"Calling {number} using {self.brand} {self.model}")

phone = Smartphone("Samsung", "S24+", "One UI 6.1")
print(phone.info())  
phone.call("+254751650989") 
