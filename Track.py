class Track():
    def __init__(self, length, cars):
        self._length = length
        self._cars = cars
    def ride(self):
        print('Ride')
        print('Участники: ')
        for car in self._cars:
            print(car.get_name())
        print('Вычисляю результат...')
        print('...')
        result_tab = sorted(self._cars, key=lambda car:self._length/car.get_speed())
        for i in range(len(result_tab)):
            print(f'{i+1} место: {result_tab[i].get_name()}')