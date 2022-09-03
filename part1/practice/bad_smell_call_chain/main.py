class Room:
    def get_name(self):
        return 42


class Street(Room):
    def get_room(self) -> Room:
        return Room()


class City(Street):
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country(City):
    def get_city(self) -> City:
        return City()


class Planet(Country):
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self):
        self.planet = Planet()

    def get_person_room(self):
        return self.planet.get_name()

    def get_city_population(self):
        return self.planet.population()


instance = Person()
print(instance.get_person_room())
print(instance.get_city_population())
