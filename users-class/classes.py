from user import User

class Privileges():
    def __init__(self,privileges):
        self.privileges=privileges
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{privilege}")

class Admin(User):
    def __init__(self,first_name, last_name, age, sex, privileges):
        super().__init__(first_name, last_name, age, sex)
        self.admin_privileges=Privileges(privileges)


#alex=Admin('Alex','Jones',29,'male',["post","delete posts","edit posts","block users","unblock users","change settings"])
#alex.admin_privileges.show_privileges()
#jennifer=User('Jennifer','Lee',31,'female')
