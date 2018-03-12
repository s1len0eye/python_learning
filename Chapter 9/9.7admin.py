class User():
    def __init__(self, first, last, **others):
        self.first_name = first
        self.last_name = last
        self.user_profile = others
        self.login_attempts = 0
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    def describe_user(self):
        print("\nFirst name is: " + self.first_name + ".")
        print("Last name is " + self.last_name + ".")
        for key, value in self.user_profile.items():
            print(key + ": " + str(value))
        
    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello, " + full_name + "!")
        
class Admin(User):
    def __init__(self, first, last, **others):
        super().__init__(first, last, **others)
        self.privileges = ['can add post', 
                        'can delete post',
                        'can ban user']
                        
    def show_privileges(self):
        print("Privileges for admin: ")
        for privilege in self.privileges:
            print("- " + privilege)

admin  = Admin('Bob', 'Black', location='Canada', job='worker')
admin.show_privileges()
