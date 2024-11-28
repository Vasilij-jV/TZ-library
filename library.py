from random import randint
import time


class LibraryOfBooks:
    """Атрибуты и методы привязаны к классу, так как класс предназначен для создания
    файлового хранилища через один экземпляр"""

    id = 0,
    title = '',
    author = '',
    year = '',
    status = '',
    filename = 'library_storage.txt'

    @classmethod
    def add_book(cls):
        """Добавляет в файл library_storage.txt строку с id книги, названием книги, автором книги, годом издания
        книги и предустановленным статусом 'в наличии' """

        cls.title = input('title: ')
        cls.author = input('author: ')
        cls.year = input('year: ')
        cls.id = randint(1000, 9999)
        cls.status = 'в наличии'

        try:
            if cls.year.isdigit():
                with open(cls.filename, 'a', encoding='utf-8') as ls:
                    ls.writelines(f'{cls.id}, {cls.title}, {cls.author}, {cls.year}, {cls.status}' + '\n')
            else:
                raise TypeError('Неправильный тип года издания')
        except TypeError as ter:
            print(f'Исключение типа {type(ter)} с параметром - {ter.args}')

    @classmethod
    def delete_book(cls, id_for_delete):
        """Полностью удаляет запись о книге в файле-хранилище"""

        try:
            if id_for_delete.isdigit():
                with open(cls.filename, 'r', encoding='utf-8') as ls:
                    content = ls.readlines()

                for i, st in enumerate(content):
                    if id_for_delete == st[:4]:
                        break
                    elif (i + 1) == len(content):
                        raise ValueError('Такого id не существует')

                new_content = [st for st in content if st[:4] != id_for_delete]

                with open(cls.filename, 'w', encoding='utf-8') as ls:
                    ls.writelines(new_content)
            else:
                raise TypeError('Неправильный тип id книги')
        except TypeError as ter:
            print(f'Исключение типа {type(ter)} с параметром - {ter.args}')
        except ValueError as ver:
            print(f'Исключение типа {type(ver)} с параметром - {ver.args}')

    @classmethod
    def search_book(cls, data_for_search):
        """Производит поиск и вывод книги в консоль по одному из трёх параметров: название, автор, год издания"""

        try:
            with open(cls.filename, 'r', encoding='utf-8') as ls:
                content = ls.readlines()
            for i, s in enumerate(content):
                if data_for_search in s:
                    print('id: {},\n title: {},\n author: {},\n year: {},\n status: {}'.format(*s.rstrip('\n').split(', ')))
                elif (i + 1) == len(content):
                    raise ValueError('Книги с таким параметром не существует')
        except ValueError as ver:
            print(f'Исключение типа {type(ver)} с параметром - {ver.args}')

    @classmethod
    def display_all_books(cls):
        """Отформатированный вывод списка книг находящихся в хранилище в консоль"""

        with open(cls.filename, 'r', encoding='utf-8') as ls:
            content = ls.readlines()
            for st in content:
                try:
                    print('id: {},\n title: {},\n author: {},\n year: {},\n status: {}'.format(*st.rstrip('\n').split(', ')))
                except IndexError:
                    print('Недостаточно данных для форматирования')

    @classmethod
    def change_book_status(cls, data_for_status):
        """Изменение статуса книги"""

        id, status = data_for_status.split(', ')
        with open(cls.filename, 'r', encoding='utf-8') as ls:
            content = ls.readlines()

        try:
            for i, st in enumerate(content):
                if id == st[:4]:
                    if status != st.rstrip('\n').split(', ')[-1]:
                        break
                    else:
                        raise ValueError('Книга уже имеет такой статус')
                elif (i + 1) == len(content):
                    raise ValueError('Такого id не существует')
        except ValueError as ver:
            print(f'Исключение типа {type(ver)} с параметром - {ver.args}')

        new_content = [', '.join(st.rstrip('\n').split(', ')[:-1] + [status]) if st[:4] == id else st for st in content]

        with open(cls.filename, 'w', encoding='utf-8') as ls:
            ls.writelines(new_content)

    @classmethod
    def user_interaction(cls, user_input):
        """Функция для взаимодействия с пользователем через консоль"""

        if user_input == 'add book':
            cls.add_book()
        elif user_input.startswith('delete book'):
            cls.delete_book(user_input[-4:])
        elif user_input.startswith('search book'):
            cls.search_book(user_input[13:])
        elif user_input == 'display all books':
            cls.display_all_books()
        elif user_input.startswith('change book status'):
            cls.change_book_status(user_input[20:])
        else:
            print('Такой команды нет')


lob = LibraryOfBooks()
# Цикл для бескончных запросов к пользователю с командой прекращения запросов
while True:
    user = input(
        'Enter your query:\n 1. add book\n 2. delete book: xxxx (id)\n 3. search book: title/author/year\n 4. display '
        'all books\n 5. change book status: id, status (в наличии/выдана)\n 6. exit\n input: ')
    if user == 'exit':
        break
    lob.user_interaction(user)
    time.sleep(3)
