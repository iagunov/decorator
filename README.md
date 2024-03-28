# Project Description
This project consists of two decorators in Python for 
creating sandwich recipes.
The first decorator `decorator_make_buter`
is designed to enhance a basic sandwich.
It checks the main ingredient and adds specific toppings
accordingly.
The second decorator `decorator_sandwich_maker` allows
customization of the sandwich by specifying the bread
type and sauce type.

## How to Use
### Decorator `decorator_make_buter`:
This decorator adds sauce to the 
sandwich based on the main ingredient provided.

To use:

```python
@decorator_make_buter
def make_buter(main_ingredient) -> str:
    return main_ingredient
print(make_buter(input('Enter your main ingredient: ')))
```

### Decorator `decorator_sandwich_maker`:
This decorator allows customization of the sandwich by specifying the bread type and sauce type.

To use:
```python
@decorator_sandwich_maker(
    bread_type=input('Enter your bread type: '),
    sauce_type=input('Enter your sauce type: ')
)
def make_buter(main_ingredient) -> str:
    return main_ingredient
print(make_buter(input('Enter your main ingredient: ')))
```

## Note
Feel free to experiment with different ingredients and combinations to create your unique sandwich recipes using these decorators. Enjoy your sandwich-making experience!
