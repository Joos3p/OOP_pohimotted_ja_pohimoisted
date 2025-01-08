"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""
    
    def __init__(self):
        """
        """
        self.firstname = ""
        self.lastname = ""
        self.age = 0
    pass


class Student:
    """Represent student with firstname, lastname and age."""
    
    def __init__(self, firstname="", lastname="", age=0):
        """
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    pass


if __name__ == '__main__':
    # empty usage

    # 3 x person usage

    # 3 x student usage
    pass
