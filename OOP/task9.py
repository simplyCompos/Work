from copy import deepcopy

class FileSystemObject:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def rename(self, new_name):
        self._name = new_name

    def get_size(self):
        return 0

    def get_info(self):
        return self.name

class File(FileSystemObject):

    def __init__(self, name, content=""):
        super().init(name)
        self._content = content

    def write(self, text):
        self._content += text

    def read(self):
        return self._content

    def get_size(self):
        return len(self._content)

    def get_info(self):
        return f"Файл: {self.name} | Розмір: {self.get_size()} символів"

class Folder(FileSystemObject):

    def __init__(self, name):
        super().init(name)
        self._objects = []

    @property
    def objects(self):
        return self._objects

    def add_object(self, obj):

        for existing in self._objects:
            if existing.name == obj.name:
                raise Exception("Об'єкт з такою назвою вже існує")

        self._objects.append(obj)

    def remove_object(self, name):

        for obj in self._objects:
            if obj.name == name:
                self._objects.remove(obj)
                return

        raise Exception("Об'єкт не знайдено")

    def find_object(self, name):

        found = []

        for obj in self._objects:

            if name.lower() in obj.name.lower():
                found.append(obj)

            if isinstance(obj, Folder):
                found.extend(obj.find_object(name))

        return found

    def show_contents(self):

        if not self._objects:
            print("Папка порожня")
            return

        for obj in self._objects:
            print(obj.get_info())

    def get_size(self):

        total = 0

        for obj in self._objects:
            total += obj.get_size()

        return total

    def get_info(self):
        return f"Папка: {self.name} | Розмір: {self.get_size()}"

class FileManager:

    def __init__(self):
        self.root = Folder("root")

    def create_file(self, folder, name):

        try:
            folder.add_object(File(name))
            print("Файл створено")

        except Exception as e:
            print("Помилка:", e)

    def create_folder(self, folder, name):

        try:
            folder.add_object(Folder(name))
            print("Папку створено")

        except Exception as e:
            print("Помилка:", e)

    def search(self, folder, name):

        result = folder.find_object(name)

        if result:
            print("\nРезультати пошуку:")

            for obj in result:
                print(obj.get_info())

        else:
            print("Нічого не знайдено")

    def copy_object(self, obj_name, source, destination):

        try:

            for obj in source.objects:

                if obj.name == obj_name:

                    copied = deepcopy(obj)
                    destination.add_object(copied)

                    print("Об'єкт скопійовано")
                    return

            raise Exception("Об'єкт не знайдено")

        except Exception as e:
            print("Помилка:", e)

    def move_object(self, obj_name, source, destination):

        try:

            if source == destination:
                raise Exception("Не можна перемістити в ту саму папку")

            for obj in source.objects:

                if obj.name == obj_name:

                    destination.add_object(obj)
                    source.remove_object(obj_name)

                    print("Об'єкт переміщено")
                    return raise Exception("Об'єкт не знайдено")

        except Exception as e:
            print("Помилка:", e)

manager = FileManager()

current_folder = manager.root

while True:

    print("\n========== ФАЙЛОВИЙ МЕНЕДЖЕР ==========")
    print("1. Створити файл")
    print("2. Створити папку")
    print("3. Переглянути вміст")
    print("4. Пошук")
    print("5. Перейменувати")
    print("6. Видалити")
    print("7. Копіювати")
    print("8. Перемістити")
    print("9. Записати у файл")
    print("10. Прочитати файл")
    print("0. Вихід")

    choice = input("Ваш вибір: ")

    try:

        if choice == "1":

            name = input("Назва файлу: ")
            manager.create_file(current_folder, name)

        elif choice == "2":

            name = input("Назва папки: ")
            manager.create_folder(current_folder, name)

        elif choice == "3":

            current_folder.show_contents()

        elif choice == "4":

            name = input("Введіть назву: ")
            manager.search(current_folder, name)

        elif choice == "5":

            old_name = input("Стара назва: ")
            new_name = input("Нова назва: ")

            found = False

            for obj in current_folder.objects:

                if obj.name == old_name:
                    obj.rename(new_name)
                    print("Перейменовано")
                    found = True

            if not found:
                print("Об'єкт не знайдено")

        elif choice == "6":

            name = input("Назва об'єкта: ")
            current_folder.remove_object(name)

            print("Видалено")

        elif choice == "7":

            name = input("Назва об'єкта: ")
            manager.copy_object(name, current_folder, current_folder)

        elif choice == "8":

            print("Для прикладу створимо нову папку destination")

            destination = Folder("destination")

            name = input("Назва об'єкта: ")

            manager.move_object(name, current_folder, destination)

            print("\nВміст destination:")
            destination.show_contents()

        elif choice == "9":

            file_name = input("Назва файлу: ")
            text = input("Текст: ")

            found = False

            for obj in current_folder.objects:

                if isinstance(obj, File) and obj.name == file_name:

                    obj.write(text)

                    print("Записано")
                    found = True

            if not found:
                print("Файл не знайдено")

        elif choice == "10":

            file_name = input("Назва файлу: ")

            found = False

            for obj in current_folder.objects:

                if isinstance(obj, File) and obj.name == file_name:

                    print("\nВміст файлу:")
                    print(obj.read())

                    found = True

            if not found:
                print("Файл не знайдено")

        elif choice == "0":

            print("Вихід з програми")
            break

        else:
            print("Некоректний вибір")

    except Exception as e:
        print("Помилка:", e)
