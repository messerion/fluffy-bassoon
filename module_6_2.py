class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow']

    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.set_color(color)

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS]
        if new_color.lower() in reg_colours:
            self.__color = new_color.capitalize()
            print(f'Цвет успешно изменен на {self.__color}.')
        else:
            print(f'Нельзя сменить цвет на {new_color}.\n')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Example usage
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Initial properties
vehicle1.print_info()

# Change properties (including calling methods)
vehicle1.set_color('Pink')  # Invalid color
vehicle1.set_color('BLACK')  # Valid color
vehicle1.owner = 'Vasyok'

# Check what has changed
vehicle1.print_info()