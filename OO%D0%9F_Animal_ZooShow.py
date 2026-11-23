# ==========================================
# ООП: Животные, пресмыкающиеся и земноводные
# Дополнительное задание: ZooShow
# ==========================================

# 1. Родительский класс Animal

class Animal:
    def __init__(self, name, species, age, habitat, food):
        self.name = name
        self.species = species
        self.age = age
        self.habitat = habitat
        self.food = food

    # Общий метод 1
    def eat(self):
        print(f"{self.name} питается: {self.food}")

    # Общий метод 2
    def show_info(self):
        print("\n--- Информация о животном ---")
        print(f"Имя: {self.name}")
        print(f"Вид: {self.species}")
        print(f"Возраст: {self.age}")
        print(f"Среда обитания: {self.habitat}")
        print(f"Питание: {self.food}")


# 2. Дочерний класс Пресмыкающиеся

class Reptile(Animal):
    def __init__(self, name, species, age, habitat, food,
                 body_temperature, has_scales):
        super().__init__(name, species, age, habitat, food)
        self.body_temperature = body_temperature
        self.has_scales = has_scales

    # Дополнительный метод 1
    def bask_in_sun(self):
        print(f"{self.name} греется на солнце.")

    # Дополнительный метод 2
    def crawl(self):
        print(f"{self.name} ползёт.")


# 3. Дочерний класс Земноводные

class Amphibian(Animal):
    def __init__(self, name, species, age, habitat, food,
                 skin_type, lives_in_water):
        super().__init__(name, species, age, habitat, food)
        self.skin_type = skin_type
        self.lives_in_water = lives_in_water

    # Дополнительный метод 1
    def jump(self):
        print(f"{self.name} прыгает.")

    # Дополнительный метод 2
    def swim(self):
        print(f"{self.name} плавает в воде.")


# 4. Дополнительный класс ZooShow

class ZooShow:
    def __init__(self):
        self.reptiles = [
            Reptile("Кеша", "Крокодил", 8, "Река", "Рыба",
                    "Переменная", True),
            Reptile("Шурик", "Змея", 4, "Террариум", "Мыши",
                    "Переменная", True)
        ]

        self.amphibians = [
            Amphibian("Кваша", "Лягушка", 2, "Болото", "Насекомые",
                      "Влажная кожа", True),
            Amphibian("Лили", "Саламандра", 3, "Влажный лес", "Черви",
                      "Гладкая кожа", True)
        ]

    def start_show(self):
        print("\n===== ДОБРО ПОЖАЛОВАТЬ В ЗООШОУ! =====")
        print("Выберите вид шоу:")
        print("1. Шоу пресмыкающихся")
        print("2. Шоу земноводных")

        choice = input("Ваш выбор (1 или 2): ")

        if choice == "1":
            animals = self.reptiles
            show_name = "ШОУ ПРЕСМЫКАЮЩИХСЯ"
        elif choice == "2":
            animals = self.amphibians
            show_name = "ШОУ ЗЕМНОВОДНЫХ"
        else:
            print("Неверный выбор. Попробуйте снова.")
            return

        print(f"\n===== {show_name} =====")
        print("Наши участники шоу:")

        for animal in animals:
            animal.show_info()
            animal.eat()

            if isinstance(animal, Reptile):
                animal.bask_in_sun()
                animal.crawl()
            elif isinstance(animal, Amphibian):
                animal.jump()
                animal.swim()

        print("\nВыберите билет:")
        print("1. Обычный билет — 100 сом")
        print("2. VIP билет — 250 сом")

        ticket_choice = input("Ваш выбор (1 или 2): ")

        if ticket_choice == "1":
            ticket_type = "Обычный"
            price = 100
            seat = "Обычное место"
        elif ticket_choice == "2":
            ticket_type = "VIP"
            price = 250
            seat = "VIP-место"
        else:
            print("Неверный выбор билета.")
            return

        print("\n===== ВАШ БИЛЕТ =====")
        print(f"Шоу: {show_name}")
        print(f"Тип билета: {ticket_type}")
        print(f"Место: {seat}")
        print(f"Стоимость: {price} сом")
        print("Спасибо за покупку! Желаем приятного шоу!")


# 5. Запуск программы

zoo = ZooShow()
zoo.start_show()
