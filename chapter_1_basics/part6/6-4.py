python_definitions = {
        'list': 'упорядоченные изменяемые коллекции объектов произвольных типов',
        'slices': 'указанная выборка из списка',
        'tuples': 'неизменяемый список',
        'index': 'номер элемента в списке или кортеже',
        'dict': 'неупорядоченные коллекции произвольных объектов с доступом по ключу',
        'str': 'строка',
        'sort': 'сортировка списка с изменением оригинального списка',
        'reverse': 'вывод в обратном порядке',
        'sorted': 'сортировка без изменения оригинального списка',
        'append': 'добавление элемента в список (по умолчанию в конец списка)',
        }
for term, definitions in python_definitions.items():
    print(term.title() + ' - ' + definitions + '.')