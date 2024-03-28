# Here is my own decorator with two parameters that can be used to make any kind of sandwich :)
from functools import wraps
from typing import Callable


def decorator_sandwich_maker(
        bread_type: str,
        sauce_type: str
        ) -> Callable[[Callable[[str], str]], Callable[[str], str]]:
    """
    Make a sandwich decorator.
    :param bread_type:
    :param sauce_type:
    :return:
    """
    def decorator(func: Callable[[str], str]) -> Callable[[str], str]:
        @wraps(func)
        def wrapper(main_ingredient) -> str:
            print(f'((((( {bread_type.upper()} )))))')
            print(f'~~~ {sauce_type.lower()} ~~~')
            print(f'==={func(main_ingredient.lower())}===')
            print(f'~~~ {sauce_type.lower()} ~~~')
            orig = func(f'((((( {bread_type.upper()} )))))')
            return orig
        return wrapper
    return decorator


@decorator_sandwich_maker(
    bread_type=input('Enter your bread type: '),
    sauce_type=input('Enter your sauce type: ')
)
def make_buter(main_ingredient) -> str:
    """
    Getting a main ingredient.
    :param main_ingredient:
    :return:
    """
    return main_ingredient


print(make_buter(input('Enter your main ingredient: ')))
