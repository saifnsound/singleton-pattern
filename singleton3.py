class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class DBConnection(object):

    def __init__(self):
        """Initialize your database connection here."""
        pass


if __name__ == "__main__":
    c1 = DBConnection()
    c2 = DBConnection.Instance()

    print("Id of c1 : {}".format(str(id(c1))))
    print("Id of c2 : {}".format(str(id(c1))))

    print("c1 is c2 ? " + str(c1 is c2))
