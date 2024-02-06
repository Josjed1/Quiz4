from typing import Protocol
import os

class computerProtocol(Protocol):
    def display_info(self) -> None:
        pass

class computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model=model
        
class desktopProtocol(computerProtocol):
    def __init__(self, tower_size: str):
        self.tower_size = tower_size
        
class desktop(computer, desktopProtocol):
    def __init__(self, brand, model, tower_size):
        self.tower_size = tower_size
    
    def display_info(self) -> None:
        print(f"Desktop: {self.brand} {self.model}, Tower Size: {self.tower_size}")
        
class laptopProtocol(computerProtocol):
    def __init__(self, screen_size: float):
        self.screen_size=screen_size
    
class laptop(computer, laptopProtocol):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def display_info(self):
        print (f"Laptop: {self.brand} {self.model}, Screen Size: {self.screen_size}")
        
def main():
    desktop = desktop("Dell", "Optiplex")
    laptop = laptop("Asus", "VivoBook")
    
    desktop.display_info()    
    laptop.display_info()   

if __name__ == "__main__":
    main()