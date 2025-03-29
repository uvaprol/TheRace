from Car import Car
from CarComponent import Engine
class CarFabrick():
    _cars = []
    _engine_list = [
        Engine('Ford', 1.5),
        Engine('Ford', 1.8),
        Engine('Ford', 2.0),
    ]
    _engine_dict = {index: value for index, value in enumerate(_engine_list)}
    def _print_engine(self):
        for index, engine in self._engine_dict.items():
            print(index, engine.get_name(), engine.get_power())
    def _pick_engine(self):
        index_engine = input('Введите номер выбранаго мотора')
        return self._engine_dict[int(index_engine)]
    def create_car(self):
        self._print_engine()
        while True:
            maker = input('Введите производителя машины')
            model = input('Введите модель машины')
            year = input('Введите год выпуска машины')
            car = Car(maker, model, year)
            car.add_components_to_car(engine=self._pick_engine())
            self._cars.append(car)
            user_choice = input('Введите выход для выхода из конструктора').strip().lower()
            if user_choice == 'выход':
                break
    def get_cars(self):
        return self._cars