from Track import Track
from CarFabrick import CarFabrick

if __name__ == '__main__':
    car_fabric = CarFabrick()
    car_fabric.create_car()
    track = Track(int(input('Введите длину трассы')), car_fabric.get_cars())
    track.ride()
