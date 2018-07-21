def print_models(unprinting_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещатеся в completed_models.
    """
    while unprinting_designs:
        current_design = unprinting_designs.pop()
        # Имитация печати модели на 3D-принтере
        print('Printing models: ' + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)
