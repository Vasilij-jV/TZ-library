##### Описание функционала приложения

- Импортирую встроенные библиотеки: randint, time
- Определяю класс LibraryOfBooks
- Класс содержит атрибуты и методы, привязанные к классу
- 6 атрибутов и 6 методов
- После определения класса я создаю единственный экземпляр класса с помощью кторорого я обрабатываю информацию в файле хранилище
- Запускаю бесконечный цикл для пользовательских запросов
- Запускаю каждый метод с помощью команд
- Создаю файл-хранилище в формате .txt
- Для добавления книги использую метод add_book
  - Определяю пять параметров книги
  - Записываю их в файл-хранилище
  - Генерирую исключения, если параметры вводятся неправильные
- Для удаления книги использую метод delete_book
  - Считываю данные из файла-хранилища в виде списка строк
  - Создаю новый список без строки которую нужно удалить
  - Записываю новый список строк в файл хранилище
- Для поиска книги использую метод search_book
  - В зависимости от переданного в метод параметра для поиска нахожу нужные строки и вывожу их на консоль
- Для отображения списка книг использую метод display_all_books
  - Получаю список книг и отформатировав его отображаю в консоли
- Для изменения статуса книги использую метод change_book_status
- Для взаимодействия с пользователем использую метод user_interaction
  - Это метод вызывается в цикле
  - Внутри метода, взависимости от переданного параметра вызывается метод класса
  - От параметра в виде строки берётся срез, чтобы затем преобразовать его в данные