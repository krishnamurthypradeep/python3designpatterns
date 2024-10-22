class Observer:
    def update(self, temprature,humidity,pressure):
        pass

class WeatherStation:
    def __init__(self) -> None:
        self.observers =[]
    
    def add_observer(self,observer):
        self.observers.append(observer)
    
    def remove_observer(self,observer):
        self.observers.remove(observer)
        
    def set_data(self,temprature,humidity,pressure):
           for observer in self.observers:
               observer.update(temprature,humidity,pressure)
          
class DeviceA(Observer):
    def __init__(self,name) -> None:
        self.name = name
    
    def update(self, temprature,humidity,pressure):
        print(f"{self.name} Display")
        print(f"- Temprature: {temprature}C, Humidity {humidity} ,Pressure:{pressure} hpa")    
    
class DeviceB(Observer):
    def __init__(self,name) -> None:
        self.name = name
    
    def update(self, temprature,humidity,pressure):
        print(f"{self.name} Display")
        print(f"- Temprature: {temprature}C, Humidity {humidity} ,Pressure:{pressure} hpa")

def main():
    weather_station = WeatherStation()
    
    display1 = DeviceA("Device A")                
    display2 = DeviceB("Device B")
    
    weather_station.add_observer(display1)
    weather_station.add_observer(display2)
    
    weather_station.set_data(25.5,60,1013.2)
    weather_station.set_data(26.5,58,1012.2)
    weather_station.remove_observer(display1)
    weather_station.set_data(35.5,70,1000.0)
 
if __name__ == "__main__":
    main()    
                       
                
                