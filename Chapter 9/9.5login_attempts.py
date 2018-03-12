
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
        
user1 = User('Bob', 'Black', location='Canada', job='worker')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
