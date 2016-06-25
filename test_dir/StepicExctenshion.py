
class BadName(Exception):
    pass


if __name__ == "__main__":
    print "Class import"

def greet(name):
    if name[0].isupper():
        return "Hello " + name
    else:
        raise BadName(name + " incorrect name")


if __name__ == "__main__":
    print "function import"