class Privileges:
    """A class representing the privileges"""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can create user", "can update user"]

    def show_privileges(self):
        """Method that shows the privileges the user has"""
        [print(privilege) for privilege in self.privileges]