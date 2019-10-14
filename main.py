my_friends = ["Daniel", "costa", "myszka"]


def print_all_friends():
    for XD in my_friends:
        print("*******")
        print("My friend to: " + XD)
        print("--------------------")


print_all_friends()

imie = input("podaj imię psyjacielu: ")

my_friends.append(imie)

print_all_friends()
