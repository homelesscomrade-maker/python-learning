import json
def print_menu():
    print("1. Показать всех пользователей")
    print("2. Добавить пользователя")
    print("3. Изменить возраст пользователя")
    print("4. Удалить пользователя")
    print("0. Выход")
def show_users(users):
    print(users)
def add_user(users):
    while True:
        name = input("Имя: ").lower().strip()
        if name != "":
            found = False
            for user in users:
                if user["name"].lower() == name:
                    found = True
            if found:
                print("Уже существует")
            else:
                name = name.capitalize()
                while True:
                    try:
                        age = int(input("Введите возраст: "))
                        if age >= 0 and age <= 120:
                            break
                        else:
                            print("Некорректно")
                    except ValueError:
                        print("Цифрами")
                new_user = {"name": name, "age": age}
                users.append(new_user)
                break
        else:
            print("Пустое поле")
def change_age(users):
    while True:
        name = input("Имя: ").lower().strip()
        found = False
        if name != "":
            for user in users:
                if user["name"].lower() == name:
                    found = True
                    break
            if found:
                break
            else:
                print("Не существует")
        else:
            print("Пустое поле")
    while True:
        try:
            new_age = int(input("Новый возраст: "))
            if new_age >= 0 and new_age <= 120:
                user["age"] = new_age
                break
            else:
                print("Некорректно")
        except ValueError:
            print("Цифрами")
def delete_user(users):
    while True:
        name = input("Имя: ").lower().strip()
        found = False
        if name != "":
            for user in users:
                if user["name"].lower() == name:
                    found = True
                    break
            if found:
                users.remove(user)
                break
            else:
                print("Не существует")
        else:
            print("Пустое поле")  
carry = True
while carry:
    print_menu()
    while True:
        try:
            act = int(input("Выберите действие: "))
            if act >= 1 and act <= 4:
                break
            elif act == 0:
                print("Завершение")
                carry = False
                break
            else:
                print("Некорректно")
                print_menu()
        except ValueError:
            print("Некорректно")
            print_menu()
    if carry:
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []
            with open("users.json", "w") as file:
                json.dump(users, file)
        if act == 1:
            show_users(users)
        elif act == 2:
            add_user(users)
        elif act == 3:
            change_age(users)
        elif act == 4:
            delete_user(users)
    if carry and act != 1:
        with open("users.json", "w") as file:
            json.dump(users, file)