from abc import ABC, abstractmethod
from datetime import datetime

class FileSystemObject(ABC):

    def __init__(self, name, path, size):
        self.__name = name
        self.__path = path
        self.__created_date = datetime.now()
        self.__size = size

    @property
    def name(self):
        return self.__name

    @property
    def path(self):
        return self.__path

    @property
    def created_date(self):
        return self.__created_date

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value >= 0:
            self.__size = value

    @abstractmethod
    def get_info(self):
        pass

class File(FileSystemObject):

    def __init__(self, name, path, size, extension):
        super().init(name, path, size)
        self.__extension = extension

    @property
    def extension(self):
        return self.__extension

    def get_info(self):
        return (f"Файл: {self.name}, "
                f"Шлях: {self.path}, "
                f"Розмір: {self.size} KB, "
                f"Розширення: {self.extension}")

class TextFile(File):

    def __init__(self, name, path, size, extension, content):
        super().init(name, path, size, extension)
        self.__content = content

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    def get_info(self):
        return (f"Текстовий файл: {self.name}, "
                f"Розмір: {self.size} KB, "
                f"Довжина тексту: {len(self.content)} символів")

class ImageFile(File):

    def __init__(self, name, path, size, extension, width, height):
        super().init(name, path, size, extension)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def get_info(self):
        return (f"Зображення: {self.name}, "
                f"Роздільна здатність: {self.width}x{self.height}, "
                f"Розмір: {self.size} KB")

class Folder(FileSystemObject):

    def __init__(self, name, path):
        super().init(name, path, 0)
        self.__objects = []

    @property
    def objects(self):
        return self.__objects

    def add_object(self, obj):
        self.__objects.append(obj)

    def get_info(self):
        return (f"Папка: {self.name}, "
                f"Кількість об'єктів: {len(self.objects)}")

text_file = TextFile(
    "notes",
    "/documents",
    15,
    ".txt",
    "Привіт! Це текстовий файл."
)

image_file = ImageFile(
    "photo",
    "/images",
    2048,
    ".png",
    1920,
    1080
)

folder = Folder("MyFolder", "/home/user")

folder.add_object(text_file)
folder.add_object(image_file)

objects = [text_file, image_file, folder]

for obj in objects:
    print(obj.get_info())
