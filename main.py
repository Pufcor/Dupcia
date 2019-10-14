my_friends = ["Daniel", "costa", "myszka"]


def print_all_friends():
    for XD in my_friends:
        print("*******")
        print("My friend to: " + XD)
        print("--------------------")


print_all_friends()

name = input("podaj imię psyjacielu: ")

my_friends.append(name)

print_all_friends()
