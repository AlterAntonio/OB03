# OB03
 Zoo
1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы
(`make_sound()`, `eat()`) для всех животных.
2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
вызывает метод `make_sound()` для каждого животного.
4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
Должны быть методы для добавления животных и сотрудников в зоопарк.
5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
(например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

### Что тут есть
Я решил также создать базовый класс для персонала ***Humans***.
В классы добавлен метод `__str__()` - теперь при вызове функции print с объектами Animal или Human вывод будет следующим:
- для объектов Animal - название животного и его возраст;
- для объектов Human - имя сотрудника и его должность.

## Классы и методы
- ***Animal(name, sound, age)*** - базовый класс животных. Принимает в качестве аргументов строки с названием и голосом животного, и целое число - возраст животного.

Производные классы: ***Bird, Mammal, Reptile***. Ничем не отличаются, принимают те же аргументы при создании, что и базовый класс. Реализуют метод *.make_sound()*
- ***Human(name, position)*** - принимает в качестве аргументов строки с именем и должностью сотрудника соответственно.

У класса есть производные:

- ***Veterinar(name)*** - ветеринар, добавляет метод *.heal(animal)*, где *animal* - объект класса Animal. При создании объекта требуется только один аргумент - строка с именем работника;
- ***Zookeeper(name)*** - смотритель, добавляет метод *.feed(animal)*, где *animal* - объект класса Animal. При создании объекта требуется только один аргумент - строка с именем работника.

###### Примечательный факт - сотрудники также могут кормить и лечить друг-друга, то есть их методы применимы к объектам как класса Animal, так и к Human.

- ***Zoo()*** - Это зоопарк. В нём есть списки с животными и сотрудниками.
- *Zoo.add_animal(\*args)* - принимает произвольное количество объектов класса Animal;
- *Zoo.add_staff(\*args)* - принимает произвольное количество объектов класса Human;
- *Zoo.all_animals()* - выводит список доступных объектов класса Animal с их характеристиками. Список проиндексирован для удобства; 
- *Zoo.all_staff()* - выводит список доступных объектов класса Human с их характеристиками. Список проиндексирован для удобства;
- *Zoo.animal_sound()* - животные орут;
- *Zoo.feed_animals()* - все животные будут накормлены;
- *Zoo.heal_animals()* - все животные будут подлечены;
- *Zoo.save()* - создаёт текстовые файлы Animals.txt и Staff.txt, и сохраняет доступные объекты классов Animal и Human соответственно;
- *Zoo.restore()* - загружает объекты из файлов Animals.txt и Staff.txt, и добавляет их в списки Zoo.animals и Zoo.staff соответственно.

Фрагмент кода, в котором создаются объекты и сохраняется в файлы закоментирован. Это сделано для проверки остальных функций. При необходимости его можно раскоментировать, предварительно закоментировав следующий участок кода. Как-то так.