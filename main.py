from console import print_all_friends
from console import jestes_failem


my_friends = ["Daniel", "costa", "myszka"]

print_all_friends(my_friends)
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
            print_all_friends(my_friends)
        else:
            jestes_failem()
