class Car:
    def __init__(self, brand, model, speed):
        # Attributes (properties)
        self.brand = brand
        self.model = model
        self.speed = speed
        self.is_engine_on = False 

        # Methods (actions)
    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} engine started")

    def stop_engine(self):
        self.is_engine_on = False
        print(f"{self.brand} {self.model} engine stopped")

    def accelerate(self, increase):
        self.speed += increase
        print(f"Speed increased to {self.speed} km/h")

    def brake(self, decrease):
        self.speed -= decrease
        print(f"Speed decreased to {self.speed} km/h")
        
        
        
car1 = Car("Toyota", "Fortuner", 0)

car1.start_engine()
car1.accelerate(50)
car1.brake(20)
car1.stop_engine()        