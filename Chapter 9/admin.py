from user import User

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 
                        'can delete post',
                        'can ban user']
        
    def show_privileges(self):
        print("Privileges for admin: ")
        for privilege in self.privileges:
            print("- " + privilege)

class Admin(User):
    def __init__(self, first, last, **others):
        super().__init__(first, last, **others)
        self.privileges = Privileges()
