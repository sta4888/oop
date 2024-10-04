class PersianCat:
    breed = 'persian'  # attribute
    age = 12.0


class SiberianCat:
    breed = 'siberian'
    age = .5


class BengalCat:
    breed = 'bengal'
    age = 2.0


tom = PersianCat()
garfield = SiberianCat()
mars = BengalCat()

print(type(tom))
print(type(garfield))
print(type(mars))
print(isinstance(tom, PersianCat))  # проверяет, является ли экземпляром


class A:  # пустой класс
    pass
