from copy import deepcopy

class FileSystemObject:

    def __init__(self, name):
        self.__name = name
        self.deleted = False

    @property
    def name(self):
        return self.__name

    def rename(self, new_name):
        print(f"{self.name} перейменовано в {new_name}")
        self.__name = new_name)

    def delete(self):
        self.deleted = True
        print(f"{self.name} видалено")

    def copy(self):
        copied_obj = deepcopy(self)
        print(f"{self.name} скопійовано")
        return copied_obj

    def get_info(self):
        return f"Об'єкт: {self.name}"

class File(FileSystemObject):

    def __init__(self, name, content=""):
        super().init(name)
        self.__content = content

    @property
    def content(self):
        return self.__content

    def get_info(self):
        return f"Файл: {self.name}"

class Folder(FileSystemObject):

    def __init__(self, name):
        super().init(name)
        self.__objects = []

    @property
    def objects(self):
        return self.__objects

    def add_object(self, obj):

        for existing in self.__objects:
            if existing.name == obj.name:
                print("Помилка: об'єкт з такою назвою вже існує")
                return

        self.__objects.append(obj)
        print(f"{obj.name} додано в папку {self.name}")

    def remove_object(self, name):

        for obj in self.__objects:
            if obj.name == name:
                self.__objects.remove(obj)
                print(f"{name} видалено з папки {self.name}")
                return

        print("Помилка: об'єкт не знайдено")

    def show_contents(self):

        print(f"\nВміст папки {self.name}:")

        if not self.__objects:
            print("Папка порожня")
            return

        for obj in self.__objects:
            print("-", obj.get_info())

    def get_info(self):
        return f"Папка: {self.name}"

class FileManager:

    def __init__(self):
        self.root = Folder("root")

    def create_file(self, folder, name, content=""):
        new_file = File(name, content)
        folder.add_object(new_file)

    def create_folder(self, folder, name):
        new_folder = Folder(name)
        folder.add_object(new_folder)

    def delete_object(self, folder, name):
        folder.remove_object(name)

    def rename_object(self, obj, new_name):
        obj.rename(new_name)

    def copy_object(self, obj, destination_folder):

        copied = obj.copy()

        for existing in destination_folder.objects:
            if existing.name == copied.name:
                print("Помилка: копія з такою назвою вже існує")
                return

        destination_folder.add_object(copied)

    def move_object(self, obj_name, source_folder, destination_folder):

        if source_folder == destination_folder:
            print("Помилка: не можна перемістити в ту саму папку")
            return

        for obj in source_folder.objects:

            if obj.name == obj_name:

                for existing in destination_folder.objects:
                    if existing.name == obj.name:
                        print("Помилка: об'єкт з такою назвою вже існує")
                        return

                source_folder.objects.remove(obj)
                destination_folder.add_object(obj)

                print(f"{obj.name} переміщено")
                return

        print("Помилка: об'єкт не знайдено")

manager = FileManager()
manager.create_folder(manager.root, "Documents")
manager.create_folder(manager.root, "Images")

documents = manager.root.objects[0]
images = manager.root.objects[1]

manager.create_file(documents, "notes.txt", "Hello")
manager.create_file(documents, "todo.txt", "Tasks")

documents.show_contents()

file1 = documents.objects[0]
manager.rename_object(file1, "new_notes.txt")

manager.copy_object(file1, images)

manager.move_object("todo.txt", documents, images)

documents.show_contents()
images.show_contents()

manager.delete_object(images, "todo.txt")

images.show_contents()
