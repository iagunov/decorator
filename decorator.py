from functools import wraps
from typing import Callable


def decorator_make_buter(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Making of a sandwich depending on the main ingredient.
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(main_ingredient) -> str:
        if main_ingredient == 'колбаса':
            print('((((( ХЛЕБ )))))')
            print('~~~ майонез ~~~')
            print(f'==={func(main_ingredient)}===')
            print('~~~ майонез ~~~')
            orig = func('((((( ХЛЕБ )))))')
            return orig
        print('((((( ХЛЕБ )))))')
        print('~~~ кетчуп ~~~')
        print(f'=== {func(main_ingredient)} ===')
        print('~~~ кетчуп ~~~')
        orig = func('((((( ХЛЕБ )))))')
        return orig
    return wrapper


@decorator_make_buter
def make_buter(main_ingredient: str) -> str:
    """
    Getting a main ingredient.
    :param main_ingredient:
    :return:
    """
    return main_ingredient


print(make_buter(input('Enter your main ingredient: ')))
