users = [
    {"name": "invalid_user", "email": "invalid_user", "password": "qwert1235"},
    {"name": "valid_user", "email": "standard_user", "password": "secret_sauce"},
    {"name": "Admin0", "email": "locked_out_user", "password": "secret_sauce"},
    {"name": "Staff2", "email": "performance_glitch_user", "password": "secret_sauce"},
]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)
