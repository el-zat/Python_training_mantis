from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string("New project", 10), description=random_string("This is new project", 15)) for i in
    range(1)
]
