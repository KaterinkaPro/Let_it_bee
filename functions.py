def show_data() -> None:
    """ Выводит информацию из справочника """
    with open("book.txt","r", encoding = "utf-8") as f:
        print(f.read())

def add_data() -> None:
    """ Добавляет информацию в справочник """
    fio = input("Введите ФИО: ")
    tel_number = input("Введите телефон: ")
    with open("book.txt","a", encoding = "utf-8") as f:
        f.write(f'\n{fio} | {tel_number}')

def find_data() -> None:
    """ "Осуществляет поиск по справочнику" """
    data = input("Введите информацию для поиска: ")
    with open("book.txt","r", encoding = "utf-8") as f:
        tel_book = f.read()
    print(search(tel_book, data))

def change_data() -> None:
    """ Изменение записи """
    with open("book.txt","r", encoding = "utf-8") as f:
        tel_book = f.read()
    a = tel_book.split('\n')
    print(a)
    text = input("Введите значение, котрое нужно заменить: ")
    b = (search(tel_book, text))
    a[a.index(b)] = edited(b)
    with open("book.txt","w", encoding = "utf-8") as f:
        f.write('\n'.join(a))    
    
def delete_data() -> None:
    """ Удаление записи """
    with open("book.txt","r", encoding = "utf-8") as f:
        tel_book = f.read()
    a = tel_book.split('\n')
    print(a)
    text = input("Введите значение, котрое нужно удалить: ")
    b = (search(tel_book, text))
    a[a.index(b)] = remove(b, text)
    with open("book.txt","w", encoding = "utf-8") as f:
        f.write('\n'.join(a))

def search(book: str, info: str) -> str:
    """ Находит в строке запись по определенному критерию поиска """
    return '\n'.join([post for post in book.split('\n') if info in post])

def edited(text: str) -> str:
    fio = input("Введите новое фио если нужно изменить его: ")
    num = input("Введите новый номер телефона, если нужно изменить его: ")
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(num) == 0:
        num = text.split(' | ')[1]
    return f'{fio} | {num}'

def remove(text:str, remove_text: str) -> str:
    if remove_text.isalpha():
        num = text.split(' | ')[1]
        return f' | {num}'
    else:
        fio = text.split(' | ')[0]
        return f'{fio} | '
    



# with open("book.txt","w", encoding = "utf-8") as f:
#     f.write('фио | номер телефона')

# with open("book.txt","a", encoding = "utf-8") as f:
#     f.write('\nфио1 | номер телефона1')

# with open("book.txt","r", encoding = "utf-8") as f:
#     print(f.read())