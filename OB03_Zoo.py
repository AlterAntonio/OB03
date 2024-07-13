#Создаём базовый класс животных
class Animal:
    def __init__(self, name, sound, age):
        self.name = name
        self.sound = sound
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} кушает')

    #Меняем вывод объектов при передаче в функцию print()
    def __str__(self): return f'{self.name}, {self.age} лет'

#Создаём производные классы животных
class Bird(Animal):
    def make_sound(self):
        print(f'{self.name}: {self.sound}')

class Mammal(Animal):
    def make_sound(self):
        print(f'{self.name}: {self.sound}')

class Reptile(Animal):
    def make_sound(self):
        print(f'{self.name}: {self.sound}')

#Создаём базовый класс персонала
class Human:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Меняем вывод объектов при передаче в функцию print()
    def __str__(self): return f'{self.name}, {self.position}'

#Создаём производные классы по должностям
class Veterinar(Human):
    def heal(self, animal): print(f'{self.position} {self.name} лечит: {animal}')

class Zookeeper(Human):
    def feed(self, animal): print(f'{self.position} {self.name} кормит: {animal}')

#Создаём класс зоопарка
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, *args):
        for animal in args:
            self.animals.append(animal)
            print(f'Теперь в нашем зоопарке обитает: {animal}')

    def add_staff(self, *args):
        for staff in args:
            self.staff.append(staff)
            print(f'Теперь в нашем зоопарке работает: {staff}')

    def all_animals(self):
        if self.animals:
            print('Животные нашего зоопарка:')
            for animal in self.animals: print(animal)

    def all_staff(self):
        if self.staff:
            print('Персонал нашего зоопарка:')
            for employee in self.staff: print(employee)

    def animal_sound(self):
        for animal in self.animals:
            animal.make_sound()

    def save(self):
        with open('Animals.txt', 'a', encoding='utf-8') as file:
            for animal in self.animals:
                file.write(f'{animal.__class__.__name__}("{animal.name}", "{animal.sound}", {animal.age})' + '\n')

        with open('Staff.txt', 'a', encoding='utf-8') as file:
            for employee in self.staff:
                file.write(f'{employee.__class__.__name__}("{employee.name}", "{employee.position}")' + '\n')

    def restore(self):
        with open('Animals.txt', encoding='utf-8') as file:
            for line in file.readlines():
                self.animals.append(eval(line.rstrip('\n')))

        with open('Staff.txt', encoding='utf-8') as file:
            for line in file.readlines():
                self.staff.append(eval(line.rstrip('\n')))


#Создаём животных
bird = Bird('Попугай', 'Гоша хоррроооший...', 2)
mammal = Mammal('Лев', 'Аррр!', 4)
reptile = Reptile('Змея', 'с-с-с-с', 3)

#Создаём персонал
vet = Veterinar("Анна", "Ветеринар")
keeper = Zookeeper("Николай", "Смотритель")

#Добавляем животных в зоопарк и проверяем их метод .make_sound()
zoo = Zoo()
zoo.add_animal(bird, mammal, reptile, Mammal('Бычара', 'Иди сюда на', 22))
zoo.all_animals()
zoo.animal_sound()

#Добавляем персонал зоопарка
zoo.add_staff(vet, keeper, Human('Василий', 'Охранник'))
zoo.all_staff()

#Проверяем методы персонала
vet.heal(bird)
keeper.feed(mammal)