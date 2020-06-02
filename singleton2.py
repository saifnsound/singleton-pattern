class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance


if __name__ == "__main__":
    # lazy initialization
    log1 = Logger()
    print(log1)

    log2 = Logger()
    print(log2)
    print('Are they the same object?', log1 is log2)
