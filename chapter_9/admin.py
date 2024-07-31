from chapter_9.privileges import Privileges


class User:
    """A representation of a user"""

    def __init__(self, first_name, last_name, age, sex):
        """Constructor that initialize the attributes to describe a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        """Method that prints the data of a user"""
        print(f"The name of the user is: {self.first_name.title()} {self.last_name.title()}")
        print(f"The age of the user is: {self.age}")
        print(f"The sex of the user is: {self.sex}")

    def greet_user(self):
        """Method that greets the user"""
        print(f"Welcome again, {self.first_name.title()}!")


class Admin(User):
    """A representation of admin user"""

    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()


admin = Admin("adam", "adamou", 30, "male")
admin.privileges.show_privileges()
