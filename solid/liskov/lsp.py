class Bird:
    def fly(self):
        print('Im flying')

class FlyingBird(Bird):
    def fly(self):
        print('Im flying')

class FlightlessBird(Bird):
    def fly(self):
        print('Im walking')  

def make_bird_fly(bird):
    bird.fly()


if __name__ == "__main__":
    generic_bird = Bird()
    eagle = FlyingBird()
    ostrich = FlightlessBird()
    make_bird_fly(generic_bird)
    make_bird_fly(eagle)
    make_bird_fly(ostrich)    
                  
            