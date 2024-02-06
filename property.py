class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return self._celsius +273.15
    

def main():
        #Creating a instance of TempConvert
        temp_convert = TemperatureConverter(10)
        
        #Accessing the property decorators and printing
        print(f"Celsius: {temp_convert.celsius}")
        print(f"Fahrenheit: {temp_convert.fahrenheit}")
        print (f"Kelvin: {temp_convert.kelvin}")


if __name__ == "__main__":
    main()

