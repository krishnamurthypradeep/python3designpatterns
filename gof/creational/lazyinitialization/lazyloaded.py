class LazyLoadedData:
    def __init__(self) -> None:
        self._data = None
    @property
    #@transactional
    def data(self):
        if self._data is None:
            self._data = self.load_data()
        return self._data
    
    def load_data(self):
        print('Loading Expensive Data')
        return sum(i * i for i in range(100000))
    
def main():
    obj = LazyLoadedData()
    print("Object Created , expensive attribute are not loaded")    
    print("Accessing expensive attribute")
    print(obj.data)
    print("Accessing expensive attribute again")
    print(obj.data)
  
if __name__ == "__main__":
    main()    
    
                