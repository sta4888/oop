from cars.car import Car

if __name__ == '__main__':
    car1 = Car(door=3, height=100, width=200, length=100, engine_type="Benzine")

    print(car1.engine_type)
