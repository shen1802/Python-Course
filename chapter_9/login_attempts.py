class User:
    """A representation of a user"""
    def __init__(self, first_name, last_name, age, sex):
        """Constructor that initialize the attributes to describe a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        """Method that prints the data of a user"""
        print(f"The name of the user is: {self.first_name.title()} {self.last_name.title()}")
        print(f"The age of the user is: {self.age}")
        print(f"The sex of the user is: {self.sex}")

    def greet_user(self):
        """Method that greets the user"""
        print(f"Welcome again, {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


adam = User("adam", "adamou", 40, "male")
adam.increment_login_attempts()
adam.increment_login_attempts()
adam.increment_login_attempts()
print(adam.login_attempts)
adam.reset_login_attempts()
print(adam.login_attempts)

