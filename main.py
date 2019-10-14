my_friends = ["Daniel", "costa", "myszka"]


def print_all_friends():
    for XD in my_friends:
        print("*******")
        print("My friend to: " + XD)
        print("--------------------")


print_all_friends()
while True:
    friend = input("Którego frienda już nie lubish????? ")
    if friend == "koniec":
        break
    if len(my_friends) == 0:
        print("Nie masz już wrogów")
        break
    else:
        if friend in my_friends:
            my_friends.remove(friend)
            print_all_friends()
        else:
            print("Nie mam takiego ziomka")
