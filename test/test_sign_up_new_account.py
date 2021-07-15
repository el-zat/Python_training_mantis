import string
import random
import time


def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_sign_up_new_account(app):
    username = random_username("user_", 10)
    email = username + "@localhost"
    password = "test"
    print(username, email)
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.session.ensure_logout()
    # assert app.soap.can_login(username, password)
    app.session.login(username, password)