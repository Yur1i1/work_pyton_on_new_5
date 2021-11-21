from pprint import pprint
class Person:
    def __init__(self, name, age, address, height):
        self.name, self.age, self.address, self.height = name, age, address, height
        self.key = (name, height)
    def __repr__(self):
        return "Person('%s',%s,'%s', %s)" % (self.name, self.age, self.address, self.height)
        
НАТАША = Person("НАТАША", 18, "Левинский, 56", 180)
Никита = Person("Никита", 27, "Ленина, 61", 190)
Стас = Person("Стас", 20, "Лысьва, 100", 175)
Жора = Person("Жора", 16, "Нью-Вегас", 150)
Бетмен = Person("Бетмен", 82, "Пешера", 200)
people = {
    НАТАША.key: НАТАША,
    Никита.key: Никита,
    Стас.key: Стас,
    Жора.key: Жора,
    Бетмен.key: Бетмен,
}
pprint(people)
pprint(height(190))
#Нудны дополнительные пояснения


