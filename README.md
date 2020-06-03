# Singleton Design Pattern

Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

### PROS:
- Ensures that a class has just a single instance.
    - Imagine that you created an object, but after a while decided to create a new one. Instead of receiving a fresh object, you’ll get the one you already created.
- Provide a global access point to that instance.
    - The pattern lets you access some object from anywhere in the program. Additionally, it also protects that instance from being overwritten by other code.

### Use Case:

- logging
- driver objects
- caching and thread pool
- database connections

### Solution
All implementations of the Singleton have these two steps in common:
- Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.
- Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.

If your code has access to the Singleton class, then it’s able to call the Singleton’s static method. So whenever that method is called, the same object is always returned.

![alt text][gfg]

### Implementation

#### Method 1
Code:
```python
class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


# early initialization
s = Singleton()
print s
s = Singleton.getInstance()
print s
```

Output:
```shell
<__main__.Singleton instance at 0x107f6ad88>
<__main__.Singleton instance at 0x107f6ad88>
```

#### Method 2

```python
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
```

Output:
```shell
Creating the object
<__main__.Logger object at 0x10d8b5490>
<__main__.Logger object at 0x10d8b5490>
('Are they the same object?', True)
```

### Resources:

- https://refactoring.guru/design-patterns/singleton
- https://www.geeksforgeeks.org/singleton-design-pattern-introduction/?ref=rp
- https://sourcemaking.com/design_patterns/singleton
- https://python-patterns.guide/gang-of-four/singleton/

[gfg]: https://media.geeksforgeeks.org/wp-content/uploads/SINGLEton.png
