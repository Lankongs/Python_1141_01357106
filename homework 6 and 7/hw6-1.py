class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats

class Motorcycle(Vehicle):
    def __init__(self, brand, year, gas):
        super().__init__(brand, year)
        self.gas = gas

class Bicycle(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

def main():
    vehicles = []
    command = input().split()
    
    while command and command[0] != "stop":
        cmd = command[0]
        if (cmd == "Car"):
            car1 = Car(command[1], command[2], command[3])
            vehicles.append(car1)
        elif (cmd == "Motorcycle"):
            motor1 = Motorcycle(command[1], command[2], command[3])
            vehicles.append(motor1)
        elif (cmd == "Bicycle"):
            bike1 = Bicycle(command[1], command[2], command[3])
            vehicles.append(bike1)
        elif (cmd == "print"):
            for v in vehicles:
                if isinstance(v, Car):
                    print(f"Car: {v.brand}, Year: {v.year}, Seat: {v.seats}")
                elif isinstance(v, Motorcycle):
                    print(f"Motorcycle: {v.brand}, Year: {v.year}, cc: {v.gas}")
                elif isinstance(v, Bicycle):
                    print(f"Bicycle: {v.brand}, Year: {v.year}, Model: {v.model}")
        else:
            print("invalid input")

        command = input().split()

if __name__ == '__main__':
    main()
