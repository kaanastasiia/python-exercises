class User:
    def __init__(self,first_name, last_name, age, sex):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex.lower()
        self.age=age
        self.login_attempts=0

    def describe_user(self):
        pronoun = "He" if self.sex == "male" else "She"
        describe_output = f"The user's name is {self.first_name} {self.last_name}. {pronoun} is {self.age} years old"
        return describe_output

    def greet_user(self):
        greet_output = f"Hello, {self.first_name} {self.last_name}!"
        return greet_output

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
