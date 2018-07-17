responses = {}

# Установка флага для продолжения опроса.
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Ответ сохраняется в словаре.
    responses[name] = response

    # Проверка продолжения опроса.

    repeat = input("Would you like to let another person respons? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    # Опрос завершен, вывести результаты.
    print("\n--- Poll Result ---")
    for name, response in responses.item():
        print(name + " would like to climb " + response + ".")
