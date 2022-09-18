def my_function():
    print('I am a function.')


# Assign the function to a variable without parenthesis. We don't want to execute the function.

description = my_function

# Accessing the function from the variable I assigned it to.

print(description())


def outer_function():
    """Assign task to student"""

    task = 'Read Python book chapter 3.'

    def inner_function():
        print('I came from the inner function.')
        print(task)

    return inner_function

    # Executing the inner function inside the outer function.
    inner_function()


homework = outer_function()


# A function can be passed to another function as an argument.

def friendly_reminder(func):
    """Reminder for husband"""

    func()
    print('Don\'t forget to bring your wallet!')


def action():
    print('I am going to the store buy you something nice.')


# basic Python decorator:

def my_decorator_func(func):
    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.

    return wrapper_func


@my_decorator_func
def my_func():
    pass


if __name__ == '__main__':
    my_function()
    outer_function()
    homework()
    friendly_reminder(func=action)
