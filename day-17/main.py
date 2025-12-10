class User:
    # this function is call ever time a new object is created
        # self is the actual object that's being created or being initialized
    def __init__(self, user_id, user_name):
        # print("new user being created...")
        self.id = user_id
        self.name = user_name


user_1 = User("001", "Filipe")

print(user_1.name)

# user_2 = User()
# user_2.id = "002"
# user_2.name = "angela"