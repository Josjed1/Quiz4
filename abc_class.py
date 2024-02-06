from abc import ABC, bastractmethod
import os

class computer(ABC):
    @bastractmethod
    def desktop(self):
        pass
    
    @bastractmethod
    def laptop(self):
        pass
    
class desktop(computer):
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand
        
    def print_info (self):
        print(f"Desktop: {self.brand}, Tower Size: {self.tower_size}")
        
class laptop(computer):
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand
        
    def print_laptop(self):
        print(f"Laptop: {self.brand} {self.model}")
        
def main():
    desktop = desktop("Dell", "Optiplex")
    laptop = laptop("Asus", "VivoBook")    
    
    desktop.print_info()
    laptop.print_laptop()
    
if __name__ == "__main__":
    main()
    