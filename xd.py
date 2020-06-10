name = input("Podaj imie: ")

a = ["ala", "ela", "ola"]
if name in a:
    print("Masz dostęp ")
    print("podaj wiek: ")
    wiek = input()

    l = int(wiek)
    if l > 38:
        print("spadaj ")
    if l < 19:
        print("spadaj ")
    else:
        print("gramy dalej ")


else:
    print("zdópcaj ")




