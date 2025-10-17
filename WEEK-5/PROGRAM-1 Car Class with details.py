class Car: #Creates a blueprint named Car
    def __init__(self, brand, model, color): #Attributes __init__ runs automatically when you create a new car
        self.brand = brand
        self.model = model #self meant for the specific object we are creating
        self.color = color
        self.mileage = 0

    def start(self): #start is a method a function that belongs to class 
        print(f"{self.brand} {self.model} is starting...")

    def drive(self, km): #drive expects a distance km
        self.mileage += km #adds distance to the car's current mileage 
        print(f"Drove {km} km, Total mileage: {self.mileage} km.")

# create objects from the class
car1 = Car("Toyota", "Camry", "Blue") #calls __init__ with brand="Toyota"......
car2 = Car("Tesla", "Model 3", "White")

car1.start() #methods using the object's methods and attributes that calls the start method for car1 only
car1.drive(50) #Increases car1's mileage by 50
print(car1.color)   #Access the attribute color stored in car1
