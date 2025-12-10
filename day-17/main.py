class User:
    # this function is call ever time a new object is created
        # self is the actual object that's being created or being initialized
    def __init__(self, user_id, user_name):
        # print("new user being created...")
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Filipe")
user_2 = User("002", "Ana")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)